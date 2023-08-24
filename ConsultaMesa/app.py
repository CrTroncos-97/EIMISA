from flask import Flask, request, render_template, jsonify
import json
import pandas as pd

app = Flask(__name__, static_url_path='/static')

# Datos incorporados desde Excel
df = pd.read_csv(r'static\Separación Mesas.csv', encoding='latin', sep=';', index_col=False, header=0)
df = df[df['Nombre Completo'] != "ACOMPAÑANTE"]
df = df.iloc[:, :-4]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obtener_mesa', methods=['POST'])



def obtener_mesa():
    try:
        request_data = request.json
        rut =request_data['rut']
        rut = format_rut(rut)
        print(rut)
        if len(df.index[df['Empleado - RUT'] == rut])>0:
            row_index = df.index[df['Empleado - RUT'] == rut][0]
            mesa = df.loc[row_index, 'Mesa']
            mesa= 'es la '+str(int(mesa))
        else:
            mesa='no fue encontrada, verifique el RUT ingresado.'
        response = {'mesa': mesa}
    except Exception as e:
        response = {'error': str(e)}
    return jsonify(response)

def format_rut(rut):
    rut=rut.lower()
    rut_list = rut.split('-')
    rut_list[0] = rut_list[0].replace('.','')
    rut = rut_list[0][-9:-6]+'.'+rut_list[0][-6:-3]+'.'+rut_list[0][-3:] + '-' + rut_list[1]
    return rut

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/static/script.js')
def serve_js():
    return app.send_static_file('script.js')
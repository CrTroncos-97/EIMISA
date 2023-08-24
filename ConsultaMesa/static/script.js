function consultarMesa() {
    var rut = document.getElementById('rut').value;
    fetch('/obtener_mesa', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'rut': rut })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').textContent = 'Su mesa ' + data.mesa;
    })
    .catch(error => {
        document.getElementById('resultado').textContent = 'Error: ' + error;
    });
}

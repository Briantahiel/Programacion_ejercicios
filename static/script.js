function sum() {
  let num1 = parseFloat(document.getElementById("num1").value);
  let num2 = parseFloat(document.getElementById("num2").value);
  if(num1 && num2){
    let result = num1 + num2;
    document.getElementById("result").textContent = "La suma es: " + result;
  }
}

function temp(){
  let fechaActual = new Date();
  let fechaISO = fechaActual.toISOString(); 
  let fecha = fechaISO.slice(0, 10);
  let hora = fechaActual.toLocaleTimeString("es-AR");
  let temp = parseFloat(document.getElementById('temp').value);
  if(temp){
    document.getElementById("resultado").textContent = "Temp: " + temp + "°C " + fecha + hora;
  }
}



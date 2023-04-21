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

function multiplo(){
  let rango1 = parseFloat(document.getElementById("rango1").value);
  let rango2 = parseFloat(document.getElementById("rango2").value);
  let cantidadMultiplos = 0;
  if (rango1 < rango2) {
    for (let i = rango1; i <= rango2; i++) {
      if (i % 3 === 0) {
        cantidadMultiplos++;
      }
    }
    document.getElementById("multiplos").textContent = "Hay " + cantidadMultiplos + " múltiplos de 3.";
  } else {
    document.getElementById("multiplos").textContent = "Error!";
  }
}


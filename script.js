// function sum() {
//   let num1 = parseFloat(document.getElementById("num1").value);
//   let num2 = parseFloat(document.getElementById("num2").value);
//   if(num1 && num2){
//     let result = num1 + num2;
//     document.getElementById("result").textContent = "La suma es: " + result;
//   }
// }

// let list_temp = [];
// function temp(){
//   let fechaActual = new Date();
//   let fechaISO = fechaActual.toISOString(); 
//   let fecha = fechaISO.slice(0, 10);
//   let hora = fechaActual.toLocaleTimeString("es-AR");
//   let temp = document.getElementById('temp').value
//   if(!isNaN(temp)){
//     list_temp.push(parseFloat(temp))
//   }
//   else{
//     document.getElementById("resultado").textContent = "Ingrese un valor numérico válido.";
//   }
//   if(temp.toLowerCase() == 'parar'){
//     let temp_max = Math.max(...list_temp)
//     document.getElementById("resultado").textContent = "Temp máx: " + temp_max + "°C " + fecha + hora;
//   }
// }



// function multiplo(){
//   let rango1 = parseFloat(document.getElementById("rango1").value);
//   let rango2 = parseFloat(document.getElementById("rango2").value);
//   let cantidadMultiplos = 0;
//   if (rango1 < rango2) {
//     for (let i = rango1; i <= rango2; i++) {
//       if (i % 3 === 0) {
//         cantidadMultiplos++;
//       }
//     }
//     document.getElementById("multiplos").textContent = "Hay " + cantidadMultiplos + " múltiplos de 3.";
//   } else {
//     document.getElementById("multiplos").textContent = "Error!";
//   }
// }


// let provincias = ["Buenos Aires","Córdoba",
// "Santa Fe","Mendoza","Tucumán","Entre Ríos","Salta","Chaco","Corrientes"
// ,"Misiones","San Juan","Jujuy","Río Negro","Neuquén","Formosa","Chubut"
// ,"San Luis","La Rioja", "Santiago del Estero","Catamarca","La Pampa","Santa Cruz","Tierra del Fuego"];
// let elegida = ''
// function eleccion(){
//   let num = document.getElementById("numero").value.trim() - 1;
//   if(!isNaN(num) && num >= 0 && num <= 23){
//     elegida = provincias[num]
//     document.getElementById("provincia").textContent = elegida;
//   }
//   else{
//     document.getElementById("provincia").textContent = "Ingresa un número válido";
//   }
// }
    
let corredores = [];

function carrera(){
  for(let i = 0; i <= 35; i++){
    let nombre = document.getElementById("corredor").value;
    let corredor = "Nombre" + nombre + ( i + 1);
    let puesto = Math.floor(Math.random() * 35) + 1;
    // nombre = "Corredor " + (i + 1);
    // let puesto = Math.floor(Math.random() * 35) + 1;
    // let tiempo = Math.floor(Math.random() * 60) + 60; 
    corredores.push({corredor, puesto});
    
  }
  
}

console.log(corredores)
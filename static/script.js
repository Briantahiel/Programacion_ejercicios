
function sum() {
  let num1 = parseFloat(document.getElementById("num1").value);
  let num2 = parseFloat(document.getElementById("num2").value);
  if(num1 && num2){
    let result = num1 + num2;
    document.getElementById("result").textContent = "La suma es: " + result;
  }
}
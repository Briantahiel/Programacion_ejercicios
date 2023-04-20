
from flask import Flask, render_template, request
import time;
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    mensaje = ''
    respuesta = ''
    count = 0
    localtime = time.asctime(time.localtime(time.time()) )
    if request.method == 'POST':
        if 'num1' in request.form and 'num2' in request.form:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            resultado = num1 + num2
        if 'temp' in request.form:
            temp = int(request.form['temp'])
            mensaje = ("La temperatura es: " + str(temp) + "°C " + "Fecha: " + localtime)
        if 'range1' in request.form and 'range2' in request.form:
            range1 = int(request.form['range1'])
            range2 = int(request.form['range2'])
            for i in range(range1, range2):
                        if(i % 3 == 0):
                            count +=1
            respuesta = ("Hay " + str(count) + " multiplos entre: " + str(range1) + " y " + str(range2))
    return render_template('index.html', resultado=resultado, mensaje=mensaje, respuesta=respuesta)

if __name__ == '__main__':
    app.run()




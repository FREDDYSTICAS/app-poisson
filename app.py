from flask import Flask, render_template, request
from utils.poisson import calcular_poisson, generar_grafica

app = Flask(__name__)

# Página de inicio
@app.route('/')
def inicio():
    return render_template('index.html')

# Página de explicación
@app.route('/explicacion')
def explicacion():
    return render_template('explicacion.html')

# Página de calculadora
@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

# Página de ejemplos reales
@app.route('/ejemplos')
def ejemplos():
    return render_template('ejemplos.html')

# Página de glosario
@app.route('/glosario')
def glosario():
    return render_template('glosario.html')

# Cálculo de probabilidad de Poisson
@app.route('/calcular', methods=['POST'])
def calcular():
    lambda_valor = float(request.form['lambda'])
    k_valor = int(request.form['k'])
    probabilidad = calcular_poisson(lambda_valor, k_valor)
    imagen_grafica = generar_grafica(lambda_valor)
    return render_template('resultado.html',
                           prob=probabilidad,
                           k=k_valor,
                           lam=lambda_valor,
                           grafica=imagen_grafica)

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

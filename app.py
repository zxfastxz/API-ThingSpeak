# app.py
from flask import Flask, render_template
from API_request import requisicao

app = Flask(__name__)

@app.route('/')
def homepage():
    # Chama a função para pegar os dados
    dados = requisicao()
    
    # Passa os dados para o template
    return render_template('chartjs-example.html', 
                           labels=dados.get('labels', []), 
                           temperaturas=dados.get('temperaturas', []), 
                           umidades=dados.get('umidades', []))

if __name__ == '__main__':
    app.run(debug=True)

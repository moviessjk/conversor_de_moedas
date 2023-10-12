from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
c = CurrencyRates()
codes = CurrencyCodes()

@app.route('/', methods=['GET', 'POST'])
def conversor_moeda():
    if request.method == 'POST':
        moeda_de = request.form['moeda_de']
        moeda_para = request.form['moeda_para']
        valor_origem = float(request.form['valor_origem'])
        
        taxa_de_cambio = c.get_rate(moeda_de, moeda_para)  # Obtem a taxa de câmbio em tempo real
        valor_convertido = valor_origem * taxa_de_cambio
        
        return render_template('resultado.html', moeda_de=moeda_de, moeda_para=moeda_para, valor_origem=valor_origem, valor_convertido=valor_convertido)

    # Obter todas as moedas conhecidas
    moedas_conhecidas = codes.get_available_currencies()
    
    return render_template('conversor.html', moedas_conhecidas=moedas_conhecidas)

if __name__ == '__main__':
    app.run(debug=True)

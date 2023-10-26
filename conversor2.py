from flask import Flask, request, render_template
from currency_converter import CurrencyConverter

app = Flask(__name__, template_folder="templates")
c = CurrencyConverter()

# Lista manual de moedas conhecidas
moedas_conhecidas = {
    'BRL': 'Real (BRL)',
    'USD': 'Dólar (USD)',
    'EUR': 'Euro (EUR)',
    'JPY': 'Iene Japonês (JPY)',
    'GBP': 'Libra Esterlina (GBP)',
    # Adicione mais moedas conforme necessário
}

@app.route('/', methods=['GET', 'POST'])
def conversor_moeda():
    if request.method == 'POST':
        moeda_de = request.form['moeda_de']
        moeda_para = request.form['moeda_para']
        valor_origem = float(request.form['valor_origem'])
        taxa_de_cambio = c.convert(1, 'BRL', 'USD')
        valor_convertido = valor_origem * taxa_de_cambio
        # Implemente a conversão de moedas aqui

        return render_template('resultado.html', moeda_de=moeda_de, moeda_para=moeda_para, valor_origem=valor_origem, valor_convertido=valor_convertido)

    return render_template('conversor.html', moedas_conhecidas=moedas_conhecidas)

if __name__ == '__main__':
    app.run(debug=True)

import requests
from datetime import datetime, timedelta

def pegar_cotacao_dolar():
    try:
        url = "https://api.frankfurter.app/latest?from=USD&to=BRL"
        requisicao = requests.get(url)
        dados = requisicao.json()
        valor_atual = dados['rates']['BRL']
        return f"R$ {float(valor_atual):.2f}"
    except Exception as e:
        return "Indisponível"

def pegar_cotacao_bitcoin():
    try:
        url = "https://blockchain.info/ticker"
        requisicao = requests.get(url)
        dados = requisicao.json()
        valor_dolar = float(dados['USD']['last'])
        valor_real = float(dados['BRL']['last'])

        texto_dolar = f"US$ {valor_dolar:,.2f}"
        texto_real = f"R$ {valor_real:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        return f"{texto_dolar} \n{texto_real}"
    except Exception as e:
        return "Indisponível"


def obter_saudacao():

    agora_no_servidor = datetime.now()

    horario_brasil = agora_no_servidor - timedelta(hours=3)

    hora_atual = horario_brasil.hour

    if 5 <= hora_atual < 12:
        return "☀️ Bom dia"
    elif 12 <= hora_atual < 18:
        return "🌤️ Boa tarde"
    else:
        return "🌙 Boa noite"

    url_base = "https://quickchart.io/chart?c="
    return url_base + configuracao_grafico.replace("\n", "").replace(" ", "")
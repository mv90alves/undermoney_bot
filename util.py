import requests
from datetime import datetime, timedelta

# --- ESPECIALISTA EM DÓLAR ---
def pegar_cotacao_dolar():
    try:
        url = "https://api.frankfurter.app/latest?from=USD&to=BRL"
        requisicao = requests.get(url)
        dados = requisicao.json()
        valor_atual = dados['rates']['BRL']
        return f"R$ {float(valor_atual):.2f}"
    except Exception as e:
        return "Indisponível"

# --- ESPECIALISTA EM BITCOIN ---
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

# --- ESPECIALISTA EM GRÁFICOS ---
def gerar_link_grafico():
    # Toda aquela sujeira de texto fica escondida aqui!
    configuracao_grafico = """
    {
        type: 'pie',
        data: {
            labels: ['Bitcoin (70%)', 'Dólar (30%)'],
            datasets: [{
                data: [70, 30],
                backgroundColor: ['orange', 'green']
            }]
        }
    }
    """
# ... (suas funções de dolar, bitcoin e gráfico estão aqui em cima) ...

# --- ESPECIALISTA EM FOTOS ---
def pegar_link_foto():
    return "https://assets.coingecko.com/coins/images/1/large/bitcoin.png"

# --- ESPECIALISTA EM EDUCAÇÃO (SAUDAÇÃO) ---
def obter_saudacao():
    # 1. Pega a hora atual do servidor (Mundo real: UTC)
    agora_no_servidor = datetime.now()

    # 2. Ajusta para o Brasil (Subtrai 3 horas)
    # timedelta é a ferramenta para fazer matemática com tempo
    horario_brasil = agora_no_servidor - timedelta(hours=3)

    # 3. Pega apenas a hora (ex: 14)
    hora_atual = horario_brasil.hour

    # 4. Decide a frase
    if 5 <= hora_atual < 12:
        return "☀️ Bom dia"
    elif 12 <= hora_atual < 18:
        return "🌤️ Boa tarde"
    else:
        return "🌙 Boa noite"

    url_base = "https://quickchart.io/chart?c="
    return url_base + configuracao_grafico.replace("\n", "").replace(" ", "")
import telebot
from telebot import types
import os
from dotenv import load_dotenv

# --- AQUI ESTÁ A MÁGICA ---
import util  # <--- Estamos importando o arquivo que acabamos de criar!

load_dotenv()
CHAVE_API = os.getenv('TOKEN')

bot = telebot.TeleBot(CHAVE_API)

# --- MENU PRINCIPAL ATUALIZADO ---
@bot.message_handler(commands=['start', 'oi'])
def enviar_menu(mensagem):
    bom_dia_tarde_noite = util.obter_saudacao()
    nome_pessoa = mensagem.from_user.first_name

    markup = types.InlineKeyboardMarkup()

    # --- BOTÕES FINANCEIROS (Lado a Lado) ---
    # Note que agora chamei de nomes mais claros, em vez de botao1/botao2
    botao_dolar = types.InlineKeyboardButton("💰 Dólar", callback_data="quer_dolar")
    botao_bitcoin = types.InlineKeyboardButton("₿ Bitcoin", callback_data="quer_bitcoin")

    # Adiciona os dois na MESMA linha
    markup.add(botao_dolar, botao_bitcoin)

    # --- BOTÕES DE CRESCIMENTO ---
    # Lembre de colocar SEUS links reais aqui
    botao_grupo = types.InlineKeyboardButton("📢 Entrar no Grupo", url="https://t.me/rendaextraundermoney")

    texto_pronto = "Olha que irado esse bot de cotações!"
    meu_bot_link = "https://t.me/Undermoney_bot"
    link_viral = f"https://t.me/share/url?url={meu_bot_link}&text={texto_pronto}"

    botao_share = types.InlineKeyboardButton("🚀 Indicar para Amigo", url=link_viral)

    markup.add(botao_grupo)
    markup.add(botao_share)

    texto_final = f"{bom_dia_tarde_noite}, {nome_pessoa}! Bot Undermoney Renda Extra na área! Acompanhe a cotação atual BTC/USD! Entre no grupo com as melhores plataformas de ganhos e indique para amigos!:"

    bot.send_message(mensagem.chat.id, texto_final, reply_markup=markup)

# --- REAÇÕES AOS BOTÕES ---
@bot.callback_query_handler(func=lambda call: True)
def resposta_botao(call):
    # Removemos o "if quer_elogio" pois o botão não existe mais

    if call.data == "quer_dolar":
        preco = util.pegar_cotacao_dolar()
        bot.send_message(call.message.chat.id, f"💵 Dólar: {preco}")

    elif call.data == "quer_bitcoin":
        bot.answer_callback_query(call.id, "Consultando...")
        preco = util.pegar_cotacao_bitcoin()
        bot.send_message(call.message.chat.id, f"₿ Bitcoin:\n{preco}")

# --- COMANDO CARTEIRA (GRÁFICO) ---
@bot.message_handler(commands=['carteira'])
def enviar_grafico(mensagem):
    bot.reply_to(mensagem, "🎨 Gerando gráfico...")

    # Pega só o link limpo do especialista
    link = util.gerar_link_grafico()

    bot.send_photo(mensagem.chat.id, link, caption="Sua carteira ideal!")

# ... (seus outros comandos estão aqui em cima) ...

# --- COMANDO FOTO ---
@bot.message_handler(commands=['foto'])
def enviar_foto(mensagem):
    # O gerente pede o link para o especialista
    link = util.pegar_link_foto()

    bot.send_photo(mensagem.chat.id, link, caption="📸 Aqui está a foto que você pediu!")

print("Bot Organizado rodando...")
bot.polling()
import telebot
from telebot import types
import os
from dotenv import load_dotenv

import util

load_dotenv()
CHAVE_API = os.getenv('TOKEN')

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['start', 'oi'])
def enviar_menu(mensagem):
    bom_dia_tarde_noite = util.obter_saudacao()
    nome_pessoa = mensagem.from_user.first_name

    markup = types.InlineKeyboardMarkup()

    botao_dolar = types.InlineKeyboardButton("💰 Dólar", callback_data="quer_dolar")
    botao_bitcoin = types.InlineKeyboardButton("₿ Bitcoin", callback_data="quer_bitcoin")

    markup.add(botao_dolar, botao_bitcoin)

    botao_grupo = types.InlineKeyboardButton("📢 Entrar no Grupo", url="https://t.me/rendaextraundermoney")

    meu_bot_link = "https://t.me/rendaextra_undermoney_bot"
    texto_pronto = "Encontre as melhores plataformas de ganhos e cotação atualizada BTC/USD aqui!"
    link_viral = f"https://t.me/share/url?url={meu_bot_link}&text={texto_pronto}"

    botao_share = types.InlineKeyboardButton("🚀 Indicar para Amigo", url=link_viral)

    markup.add(botao_grupo)
    markup.add(botao_share)

    texto_final = f"{bom_dia_tarde_noite}, {nome_pessoa}! Bot Renda Extra Undermoney na área! Acompanhe a cotação atual BTC/USD! Entre no grupo com as melhores plataformas de ganhos e indique para amigos!"

    bot.send_message(mensagem.chat.id, texto_final, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def resposta_botao(call):


    if call.data == "quer_dolar":
        preco = util.pegar_cotacao_dolar()
        bot.send_message(call.message.chat.id, f"💵 Dólar: {preco}")

    elif call.data == "quer_bitcoin":
        bot.answer_callback_query(call.id, "Consultando...")
        preco = util.pegar_cotacao_bitcoin()
        bot.send_message(call.message.chat.id, f"₿ Bitcoin:\n{preco}")



print("Bot Organizado rodando...")
bot.polling()
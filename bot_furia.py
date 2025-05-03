# Importações
import os
from dotenv import load_dotenv
import telebot

# Carrega variáveis de ambiente do .env
load_dotenv()

# Pega o token do arquivo .env
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Inicializa o bot com o token
bot = telebot.TeleBot(TOKEN)

# Comando /start ou /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    bot.send_message(msg.chat.id, "Olá! Sou o bot da FURIA, pronto para te ajudar! \n \n"
                                  "Comandos disponíveis:\n"
                                  "/elenco - Ver elenco atual da line de CS\n"
                                  "/jogos - Ver próximos jogos\n"
                                  "/jogosrecentes - Ver resultados de jogos recentes\n"
                                  "/campeonatos - Ver campeonatos que a line está participando ou participará\n"
                                  "/winrate - Ver winrate nos mapas da atual line de CS\n"
                                  "/ranking - Ver ranking atual da FURIA\n")  

# Comando /elenco
@bot.message_handler(commands=['elenco'])
def elenco(msg):
    bot.send_message(msg.chat.id, "Elenco atual da line de CS:\n\n"
                                  "Titulares:\n"
                                  "1. MOLODOY\n"
                                  "2. YEKINDAR\n"
                                  "3. FalleN\n"
                                  "4. KSCERATO\n"
                                  "5. yurrih\n\n"
                                  "Reservas:\n"
                                  "1. skullz\n"
                                  "2. chelo\n\n"
                                  "Coachs:\n"
                                  "1. hepa\n"
                                  "2. sidde\n")

# Comando /jogos
@bot.message_handler(commands=['jogos'])
def jogos(msg):
    bot.send_message(msg.chat.id, "Próximos jogos:\n"
                                  "Nenhum jogo encontrado para os próximos dias.\n")

# Comando /jogosrecentes
@bot.message_handler(commands=['jogosrecentes'])
def jogosrecentes(msg):
    bot.send_message(msg.chat.id, "Resultados de jogos recentes:\n"
                                  "FURIA x The MongolZ - 09/04/2025 às 09:50 - 0 x 2\n"
                                  "FURIA x Virtus.pro - 08/04/2025 às 06:05 - 0 x 2\n"
                                  "FURIA x Complexity - 07/04/2025 às 11:05 - 1 x 2\n"
                                  "FURIA x Apogee - 06/04/2025 às 09:50 - 2 x 0\n")
    
# Comando /campeonatos
@bot.message_handler(commands=['campeonatos'])
def campeonatos(msg):
    bot.send_message(msg.chat.id, "Campeonatos que a line está participando ou participará:\n"
                                  "PGL Astana 2025 - 10/05/2025\n"
                                  "IEM Dallas 2025 - 19/05/2025\n"
                                  "BLAST.tv Austir Major 2025 Stage 2 - 07/06/2025\n")

# Comando /winrate
@bot.message_handler(commands=['winrate'])
def winrate(msg):
    bot.send_message(msg.chat.id, "Winrate dos mapas abaixo:\n"
                                  "Cache - 73.2%\n"
                                  "Cobblestone - 70.6%\n"
                                  "Train - 62.5%\n"
                                  "Vertigo - 61.2%\n"
                                  "Mirage - 60.8%\n"
                                  "Overpass - 60.3%\n"
                                  "Inferno - 59.1%\n"
                                  "Dust2 - 56.8%\n"
                                  "Nuke - 56.1%\n"
                                  "Ancient - 51.5%\n"
                                  "Anubis - 44.4%\n")

# Comando /ranking
@bot.message_handler(commands=['ranking'])
def ranking(msg):
    bot.send_message(msg.chat.id, "Ranking mundial até o momento:\n"
                                  "World Ranking:\n"
                                  "Vitality #1\n"
                                  "Spirit #2\n"
                                  "MOUZ #3\n"
                                  "Natus Vincere #4\n"
                                  "...\n"
                                  "FURIA #17\n\n"
                                  "Observação: O ranking é atualizado semanalmente e pode mudar a qualquer momento, para mais informações, acesse: https://www.hltv.org/\n")

# Rodando o bot
print("Bot está online...")
bot.infinity_polling()
# Projeto: FURIA CS:GO Bot e Landing Page

# Descrição
Este projeto contém dois componentes principais:

Bot de Telegram: Um bot interativo desenvolvido em Python para fornecer informações aos fãs do time de CS:GO da FURIA.

Landing Page: Uma página simples em HTML com informações sobre o time e links para o bot.

# 1. Bot de Telegram - bot.py
Descrição:
O bot de Telegram é um assistente virtual para fãs da FURIA, oferecendo informações como o elenco atual do time, próximos jogos, resultados recentes, winrate dos mapas e ranking mundial.

# Funcionalidades:
O bot responde aos seguintes comandos:

/start ou /help: Inicia a conversa e exibe os comandos disponíveis.

/elenco: Mostra o elenco atual da line de CS:GO da FURIA.

/jogos: Exibe os próximos jogos da FURIA.

/jogosrecentes: Exibe os resultados dos jogos recentes.

/campeonatos: Exibe os campeonatos futuros nos quais a FURIA estará participando.

/winrate: Exibe o winrate dos mapas atuais.

/ranking: Exibe o ranking atual da FURIA.

# 1.1 Como rodar o bot
Instalar dependências:
Antes de rodar o bot, instale as dependências necessárias. Se você não tiver o telebot instalado, basta rodar o seguinte comando:
pip install pyTelegramBotAPI

# 1.2 Rodar o bot:
Para rodar o bot, basta executar o script bot.py:
python bot.py

# 1.3 Interagir com o bot:
Após rodar o bot, você pode interagir com ele no Telegram. Envie os comandos listados e ele responderá com as informações correspondentes.

# 1.4 Estrutura resumida do Código
Observação: os símbolos "--" são para marcar o início e fim.

-- import telebot

# Token do Bot
bot = telebot.TeleBot('SEU_TOKEN')

# Comandos que o bot escuta
@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    bot.send_message(msg.chat.id, "Olá! Sou o bot da FURIA, pronto para te ajudar!")

@bot.message_handler(commands=['elenco'])
def elenco(msg):
    bot.send_message(msg.chat.id, "Elenco atual da line de CS:GO da FURIA: ...")

# Outros comandos seguem a mesma estrutura...

# Bot escutando
bot.infinity_polling() --

# 1.5 Considerações
Certifique-se de substituir 'SEU_TOKEN' pelo token do seu bot, que você pode obter através do BotFather no Telegram.

O bot usa a biblioteca pyTelegramBotAPI, que facilita a comunicação com a API do Telegram.

# 2. Landing Page - index.html
Descrição
A landing page em HTML foi criada para fornecer informações rápidas sobre a FURIA, incluindo links para interagir com o bot e acompanhar o time. A página é simples e responsiva, com foco nas informações chave para os fãs de CS:GO.

# 2.1 Estrutura do Arquivo
O arquivo index.html contém uma estrutura básica de uma página web com um título, subtítulo, links e uma breve descrição do projeto.

Conteúdo do index.html

Observação: os símbolos "--" são para marcar o início e fim.

-- <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FURIA CS:GO Bot</title>
</head>
<body>
    <h1>Bem-vindo ao Bot da FURIA</h1>
    <p>Interaja com o nosso bot de Telegram para saber tudo sobre o time de CS:GO da FURIA!</p>
    <ul>
        <li><a href="https://wa.me/5511993404466" target="_blank">Interagir com o bot no Telegram</a></li>
        <li><a href="https://www.hltv.org/team/5316/furia" target="_blank">Visite o site oficial da FURIA</a></li>
    </ul>
</body>
</html> --

# 2.2 Como Rodar a Landing Page
Abrir no Navegador:

Basta abrir o arquivo index.html diretamente no seu navegador para visualizar a página.

Subir para o GitHub:

Você pode subir o arquivo HTML para o GitHub e utilizar o GitHub Pages para hospedar a página de forma gratuita.

# 2.3 Considerações
A página HTML não possui estilização avançada, mas você pode melhorar o design futuramente com CSS ou JavaScript.

O link do bot do Telegram está configurado para abrir diretamente no Telegram Web (você pode mudar para o link do seu bot específico).




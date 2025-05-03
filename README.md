# FURIA CS Bot 🐆🔥

Este é um bot do Telegram desenvolvido para fãs do time de CS:GO da FURIA. Ele foi criado como parte do **Desafio #1**

# Funcionalidades

- **/elenco**: Exibe o elenco atual da line de CS da FURIA.
- **/jogos**: Mostra os próximos jogos do time.
- **/jogosrecentes**: Exibe os resultados dos jogos mais recentes.
- **/campeonatos**: Lista os campeonatos que a FURIA está participando ou participará.
- **/winrate**: Mostra o winrate da line da FURIA nos mapas de CS:GO.
- **/ranking**: Exibe o ranking atual da FURIA no cenário mundial de CS:GO.

# Como criar um bot
Passo 1: Criar o Bot no Telegram
Abra o Telegram e busque pelo BotFather.

Envie o comando /newbot para o BotFather.

Siga as instruções para criar um nome e um username para o seu bot.

O BotFather fornecerá um token de acesso que será usado para autenticar o bot.

Passo 2: Configuração do Projeto
Instalar Dependências
Para rodar o bot, você precisará do Python e das bibliotecas necessárias. Siga os passos abaixo:

Instale as dependências necessárias:

Use o comando abaixo para instalar as bibliotecas:

pip install pyTelegramBotAPI python-dotenv

Configurar o token do bot:

Crie um arquivo .env na raiz do seu projeto e adicione o token gerado pelo BotFather:

TELEGRAM_BOT_TOKEN=seu-token-aqui

Passo 3: Rodando o Bot
Baixe ou clone o repositório:

Caso ainda não tenha o código localmente, use o comando abaixo para clonar o repositório:

git clone https://github.com/SEU_USUARIO/furia-chatbot.git

Execute o código:

Após garantir que as dependências estão instaladas, execute o bot com o seguinte comando:

python bot.py

Passo 4: Testando o Bot
Abra o Telegram e busque pelo seu bot usando o username que você configurou no BotFather.

Inicie a conversa com o bot enviando o comando /start.

Experimente os comandos: Você pode testar comandos como /elenco, /jogos, /winrate, entre outros, para ver como o bot responde.

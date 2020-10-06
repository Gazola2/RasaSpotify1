# RasaSpotify
Chatbot RASA - Spotify Bot
Descrição:
    O Spotify Bot é um chatbot desenvolvido em  rasa tem como objetivo de facilitar as buscas no spotify

    Funções:
      - Busca por artistas 
      - Playlist(Desenvolvimeto)
      - Sugestao(Desenvolvimento)

### Organização do projeto
Os arquivos e diretórios do projeto estão organizados da seguinte maneira:

    actions.py                  // Arquivos python com ações customizadas voltados para os forms
    data/                       //
        - nlu/                  // Intenções e entidades         
        - stories/              // Histórias e fluxos de conversa
    config.yml                  // Configurações do assistente
    credentials.yml             // Credenciais de acesso às plataformas de chat
    domain.yml                  // Arquivo que instancia as intenções, entidades e ações do assistente
    endpoints.yml               // Endpoints que o bot pode utilizar

## NLU   
    intents:                    //
        - greet                 // Reconhecimento de saudação
        - search_tipo           // Reconhecimento da abertura do formulario
        - out_of_scope          // Reconhecimento de intencoes fora escopo
        - goodbye               // Reconhecimento de despedida 
        - disenteresse          // Reconhecimento de falta de interesse na opcoes 
        - ajuda                 // Reconhecimento de solicitacao de ajuda
        - artista               // Reconhecimento de variados artistas
        - synonym:artista       // sinonimos das plavras que podem reconhcer o tipo de como o formulario sera aberto
        - lookup:artistas.txt   // Tabela de palavras com mais artistas
    entities:                   //
        - tipo                  // Entidade que extrai o tipo de bot que sera aberto

### Instruções de instalação

Para executar o chatbot, antes é necessário seguir esses passos:

1. Instalar o Python (versão 3.6 ou 3.7): [link](https://www.python.org/downloads/);

2. Instalar o RASA: [link](https://rasa.com/docs/rasa/user-guide/installation/);

3. Instalar o RASA-SDK: [link](https://rasa.com/docs/rasa/api/rasa-sdk/#installation);

4. Instalar o Spotipy (biblioteca de conexao do spotify no python) atraves do comando "pip install spotipy --upgrade"

5. Baixar o ngrok [link](https://ngrok.com/download)




### Instruções de execução

Após seguir as instruções de instalação, seguir esses passos para executar a aplicação:

- Clonar  ou baixar os aquivos no repositorio;

- Usar os comandos Rasa train nlu em seguida rasa train;

- Rodar o ngrok na porta 5005 com o comando  (ngrok http 5005);

- Copiar a Url gerada pelo o ngroke substituir no arquivo credentiasl.yml em "webhook_url: "(ngrok nova url)/webhooks/telegram/webhook";

- Execute os comandos a partir do bot principal

- Em um terminal executar o comando rasa run actions;

- Em outro terminal executar o comando rasa run;

- Resumindo, serão 3 serviços rodando em paralelo:

  - Rasa run(para rodar o servidor do rasa)
  
  - Rasa Actions (serviço responsável por fornecer a ação para uma determinada intenção)
  
  - NGROK (serviço responsável por manter a aplicação no ar)
  
- Para testar a aplicação use o telegram "@Spotify_Rasa_bot";



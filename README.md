

# Motion Detection with Telegram Notifications

Este é um programa Python que utiliza a biblioteca OpenCV para detectar movimentos em uma câmera e enviar notificações via Telegram sempre que um movimento significativo é detectado.

## Pré-requisitos

- Python 3.x
- OpenCV
- Biblioteca `requests`
- Conta no Telegram
- Token de um bot do Telegram

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/maryane-castro/motion-detection-telegramBOT.git
    ```

2. Instale as dependências:

    ```bash
    pip install opencv-python requests
    ```

3. Obtenha um token para o seu bot do Telegram seguindo as instruções [aqui](https://core.telegram.org/bots#botfather).

## Utilização

1. Execute o script `bot.py`:

    ```bash
    python motion_detection_telegram.py
    ```

2. O programa usará a câmera padrão do seu dispositivo. Certifique-se de que a câmera esteja configurada corretamente e posicionada para capturar a área desejada.

3. O programa irá detectar movimentos na cena capturada pela câmera. Sempre que um movimento significativo for detectado, uma mensagem será enviada para o seu bot do Telegram com a contagem de movimentos.

4. Você pode ajustar os parâmetros de sensibilidade e área mínima de contorno diretamente no código, conforme necessário.

## Configuração do Telegram

1. Crie um novo bot no Telegram usando o BotFather.

2. Obtenha o token de acesso do seu bot.

3. Encontre o ID do chat para o qual deseja enviar as notificações. Você pode usar métodos como `getUpdates` para encontrar o ID do chat.

4. Substitua o token do bot e o ID do chat no código (`bot_token` e `chat_id`, respectivamente).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar problemas ou solicitações de pull.

## Licença

Este projeto é licenciado sob a licença [MIT](https://opensource.org/licenses/MIT).

---


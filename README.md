# PersonalLoan-DigitalsysTecnologia
Este é um projeto Django que implementa um sistema de empréstimos pessoais. Ele usa o Celery para tarefas assíncronas e o RabbitMQ como broker de mensagens. O projeto é configurado para ser executado em um ambiente Docker.

# Estrutura do Projeto
O projeto é organizado da seguinte forma:

Dockerfile e docker-compose.yaml: Arquivos de configuração do Docker que definem como o aplicativo e seus serviços associados são construídos e executados.

manage.py: O script de linha de comando do Django para tarefas administrativas.

core/: Este diretório contém os arquivos de configuração do projeto Django, incluindo settings.py, urls.py, wsgi.py e asgi.py.

loans/: Este diretório é o aplicativo Django principal. Ele contém modelos (models.py), visualizações (views.py), tarefas do Celery (tasks.py), e outros arquivos relacionados.

requirements.txt: Este arquivo lista as dependências do Python necessárias para o projeto.

wait-for-it.sh: Este script é comumente usado em aplicações Docker para esperar até que um determinado serviço esteja disponível.

# Como Configurar e Executar o Projeto
1 - Clone o repositório para a sua máquina local.

2 - Certifique-se de que você tem o Docker e o Docker Compose instalados em sua máquina. Você pode verificar a instalação executando docker --version e docker-compose --version no terminal. Se você não tem o Docker ou o Docker Compose instalados, você pode baixá-los aqui > https://www.docker.com/products/docker-desktop.

3 - Navegue até o diretório do projeto no terminal.

4 - Execute o comando "docker-compose up --build" para iniciar o aplicativo e todos os serviços associados. A primeira vez que você executar este comando, o Docker irá baixar e construir todas as imagens necessárias, o que pode levar algum tempo, se tudo ocorrer bem, nas demais somente "docker-compose up"

5 - Uma vez que todos os serviços estejam em execução, você pode acessar o aplicativo navegando para http://0.0.0.0:8000 em seu navegador.

6 - credenciais do admin-django: admin/adminpassword

# Como Contribuir

Se você gostaria de contribuir para este projeto, por favor, faça um fork do repositório, faça suas alterações e, em seguida, envie um pull request. Certifique-se de que suas alterações passem em todos os testes antes de enviar o pull request.

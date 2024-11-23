# Projeto_WEB_Django


## Desenvolvimento Web com Python

Este projeto é um site web dinâmico desenvolvido com o framework Django, pensado para ser escalável e seguro, com uma interface intuitiva e funcionalidades robustas de autenticação e gestão de dados. A aplicação é estruturada para oferecer uma experiência fluida aos usuários, permitindo autenticação, manipulação de dados, e interação com formulários seguros. A arquitetura é flexível para suportar novos recursos e extensões, tornando o projeto ideal para expansão futura.

## Funcionalidades

- **Catálogo de Filmes e Séries**: Interface intuitiva para explorar uma ampla seleção de conteúdos organizados por categorias e gêneros.
- **Sistema de Busca**: Pesquisa rápida para encontrar filmes ou séries pelo título.
- **Páginas Detalhadas**: Cada filme ou série tem uma página dedicada com informações, sinopse, classificação e trailer.
- **Perfis de Usuário**: Suporte para múltiplos perfis em uma única conta, permitindo recomendações personalizadas.
- **Lista de Favoritos**: Opção de salvar filmes e séries para assistir mais tarde.
- **Recomendações Baseadas no Histórico**: Sugestões automáticas com base no histórico de visualização.
- **Streaming Simulado**: Reprodutor de vídeo funcional para simular a experiência de streaming (com suporte para legendas).
- **Modo Responsivo**: Totalmente otimizado para dispositivos móveis, tablets e desktops.


## Tecnologias Utilizadas

- **Django 5.1.3**: Framework web para desenvolvimento rápido e seguro.
- **Crispy Forms** com Bootstrap 5: Para melhorar o design dos formulários.
- **Gunicorn**: Servidor WSGI para deploy.
- **Pillow**: Para manipulação de imagens.
- **psycopg2**: Para integração com PostgreSQL.
- **WhiteNoise**: Para servir arquivos estáticos.

## Passo-a-passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
2. Crie e ative um ambiente virtual
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    venv\Scripts\activate     # Para Windows
3. Instale as dependências do projeto
    ```bash
    pip install -r requirements.txt

Configure o banco de dados no arquivo .env (ou diretamente no settings.py, se aplicável)
Exemplo de configuração:
DATABASE_URL=postgres://usuario:senha@localhost:5432/nome_do_banco

4. Realize as migrações do banco de dados
    ```bash
    python manage.py migrate
5. Inicie o servidor de desenvolvimento
    ```bash   
    python manage.py runserver
6. Acesse o projeto em: http://127.0.0.1:8000

## Deploy e eonfiguração para Produção
Este projeto pode ser facilmente implantado em plataformas como Heroku ou Render. Certifique-se de configurar as variáveis de ambiente e o banco de dados na plataforma escolhida.
Use gunicorn e whitenoise para servir o projeto em produção.


### Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

### Como Contribuir

Contribuições serão bem-vindas! Para contribuir, faça um fork do projeto, crie uma nova branch, faça suas alterações e envie um pull request.

### Contatos

- **E-mail**: marcio.asriel@gmail.com
- **LinkedIn**: [Marcio Luiz](https://www.linkedin.com/in/marcioluiz-multicloud/)
- **WhatsApp**: +47 99926-1250

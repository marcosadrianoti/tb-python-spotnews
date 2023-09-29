# Projeto Python Spotnews! :newspaper:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Desenvolver uma aplicação que faz consultas em notícias sobre tecnologia usando raspagem de dados no [_blog da Trybe_](https://blog.betrybe.com).
  * Verificar se sou capaz de:
    * Escrever aplicações usando Django e Django Rest Framework.
    * Desenvolver uma aplicação que usa a arquitetura Model-View-Template.
    * Trabalhar com banco de dados MYSQL.
</details>
<details>
<summary><strong> Requisitos do projeto:</strong></summary>

  * Criar a migrate e o model `Categories`.
  * Criar a migrate e o model `Users`.
  * Criar a migrate e o model `News`.
  * Criar a página Inicial.
  * Criar a página de detalhes de uma Notícia.
  * Criar a página de Formulário de uma nova Categoria.
  * Criar a página de Formulário de uma nova Notícia.
  * Criar a rota `/api/categories/` com o DRF.
  * Criar a rota `/api/users/` com o DRF.
  * Requisito Bônus:
    * Criar a rota `/api/news/` com o DRF.
</details>
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone git@github.com:marcosadrianoti/tb-python-traduzo.git
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-python-traduzo
```

crie o ambiente virtual:
```bash
python3 -m venv .venv
```

Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

Instale as dependências no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt
```

Suba o projeto pelo docker:
```bash
docker compose up translate
```

Rode a aplicação e acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/):
```bash
python3 src/app.py
```

Execute testes com:
```bash
python3 -m pytest
```

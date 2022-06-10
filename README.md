<div align="center">
  <img width="180" src="public/images/logo.svg" alt="Logo">
  <h1>Adote um Pet</h1>
</div>
<p align="center">
  <a href="LICENCE"><img alt="licence" src="https://img.shields.io/github/license/ShadowsS01/Adopt-a-Pet-Backend-Python?color=%23AE0FEA"></a>
  <img src="https://img.shields.io/github/languages/top/ShadowsS01/Adopt-a-Pet-Backend-Python?color=%23AE0FEA" alt="Main project language">
</p>
<br/>

## Sobre

> Um projeto de adoção de animais. Desenvolvido junto ao Workshop [Multi-Stack 3](https://lp.treinaweb.com.br/multi-stack/aula1) da [TreinaWeb](https://www.treinaweb.com.br/).
>
> Este projeto é um multi-repo. Este repositório contem o Backend do projeto e no repositório [Adopt-a-Pet-Frontend](https://github.com/ShadowsS01/Adopt-a-Pet-Frontend) contem o Frontend, feito em [React](https://reactjs.org/) e [Next.Js](https://nextjs.org/).

## Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)

## Como executar o projeto

Para executar o projeto você precisa ter o [Python](https://www.python.org/) e o [Git](https://git-scm.com) instalados na sua maquina. Você também precisará de um editor de código, eu utilizei o [VSCode](https://code.visualstudio.com).

### 1. Clone esse repositório

```bash
git clone https://github.com/ShadowsS01/Adopt-a-Pet-Backend-Python.git
```

### 2. Acesse a pasta do projeto

```bash
cd Adopt-a-Pet-Backend-Python
```

### 3. Ambiente Virtual

```bash
# Criar
  # Linux
      python3 -m venv venv
  # Windows
      python -m venv venv
    
# Ativar
  # Linux
      source venv/bin/activate
  # Windows
      venv/Scripts/Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

 Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente

Copie o arquivo `.env.example` neste diretório para `.env` (que será ignorado pelo Git):

```bash
cp .env.example .env
```

- Se der errado o `cp` crie o arquivo `.env` nesta pasta.

Em seguida, defina cada variável em `.env` com a URL do seu Backend:

```text
SECRET_KEY=Digite_Uma_Senha_Secreta_aqui
DEBUG=True
```

Também será necessária as variáveis de Email, mas elas são opcionais:

```text
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

- Caso não queira utilizar o envio de email é só entrar no `adote_um_pet/settings.py`, no final do arquivo e deletar ou comentar as linhas após o comentário `# EMAIL`
- Também será necessário entrar no `adocao/views.py` e deletar ou comentar as linhas 7 e 19 do arquivo.

### 6. Migações no Banco Dados

Agora precisamos fazer as migrações para o banco de dados, só rodar no terminal:

```bash
python manage.py migrate
```

### 7. Execute a aplicação em modo de desenvolvimento

```bash
python manage.py runserver
```

- A aplicação inciará localmente - acesse: (<http://127.0.0.1:8000/>)

- Na URL depois do `8000/` dígite `api/pets` para ver os pets cadastrados ou `api/adocoes` para ver as adoções feitas.

## Deploy

Deploy do Backend foi feito no [Heroku](https://devcenter.heroku.com/).

Se você for fazer deploy do Backend para usar no Front, recomendo utilizar o [Heroku](https://devcenter.heroku.com/) por já estar tudo pronto só setar as variáveis lá no seu App e fazer as migrações e pronto.

## Licença

Este projeto esta sobe a licença [MIT](/LICENSE).

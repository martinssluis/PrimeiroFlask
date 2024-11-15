# Projeto de Login em Flask

Este projeto tem como objetivo dar os primeiros passos com Flask, criando uma aplicação simples de login utilizando o framework Flask. O foco principal é ser um guia para quem está começando, ser um direcionador de onde começar e o que fazer.

## Passos para a criação do ambiente e configuração do projeto

### 1. Criando o ambiente virtual

Para criar um ambiente virtual, utilize o comando:

```bash
python -m venv env_Flask
```
### 2. Ativando o ambiente virtual
Dentro do diretório do projeto, entre na pasta do ambiente virtual e ative-o:
```
cd env_Flask
cd Scripts
activate.bat
```
Agora o ambiente virtual está ativado e você pode instalar as dependências do projeto de forma isolada.

### 3. Instalando o Flask
Com o ambiente virtual ativado, instale o Flask:
```
pip install flask
```

### 4. Criando o arquivo principal (main.py)
Crie o arquivo main.py para definir as rotas da aplicação Flask:
```
touch main.py
```
Dentro do arquivo main.py, adicione o código do servidor Flask:

```
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'chave_secreta'

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return f'Bem-vindo {username}'
    return f'Bem-vindo ao Flask! <a href="login">Faça login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

### 5. Criando a pasta templates e o arquivo HTML
Dentro do diretório do projeto, crie a pasta templates para armazenar os arquivos HTML e dentro da pasta templates, crie o arquivo login.html:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="{{ url_for('login') }}" method="post">
        <label for="username">Nome do usuário</label>
        <input type="text" id="username" name="username" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### 6. Executando a aplicação
Verifique se você está no ambiente virtual env_Flask (caso contrário, entre novamente com o comando cd). Em seguida, execute o servidor Flask:
 ```
python main.py
 ```
 A aplicação será executada no endereço http://127.0.0.1:5000/. Ao acessar essa URL no navegador, você verá a página de boas-vindas com um link para a página de login.

### 7. Testando a aplicação
Quando você acessar a rota /login, poderá inserir o nome de usuário.
Após enviar o formulário, você será redirecionado para a página inicial com uma mensagem de boas-vindas, incluindo o nome do usuário.
Caso deseje sair, basta clicar no link de logout, que irá redirecionar para a página inicial.
Estrutura do Pr
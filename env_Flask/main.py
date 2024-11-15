from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key =  'chave_secreta'

@app.route('/') # pagina inicial 
def home():
    if 'username' in session:
        username = session['username']
        return f'Bem vindo {username}'
    return f'Bem vindo ao Flask! <a href="login">Faça login</a>'

@app.route('/login', methods=['GET','POST']) # rota para login (boas praticas pedem nome simples e coesoes '/login')
def login():
    if request.method == 'POST':
        username = request.form['username'] # sincronizando a variavel com o formulario html
        session['username'] = username # entrando na sessao do username 
        return redirect(url_for('home')) # redirecionar para a home
    return render_template('login.html') 

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__': # obrigatorio para o codigo rodar 
    app.run(debug=True)
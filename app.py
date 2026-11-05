from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "goulb007"

ADMIN_EMAIL = "'igorgouveiajumbos@gmail.com'"
ADMIN_SENHA = "123456"

@app.route("/") # Isso é a url (dominio/rota) // Home-page página inicial 
def index():
    if "login" not in session:
        return redirect("/login")
    # Usuario logado
    return render_template("index.html")
#-------------------------------------------------------------------------------------------------
# ROTAS PARA LOGIN
@app.route("/login", methods=['GET', 'POST'])
def login():
    if "login" in session:
        return redirect("/") # Serve para barrar a entrada pagina inicial login
    
    if request.method == 'GET':
        return render_template("login.html")
    #averiguar post
    email = request.form.get("email") # pegando o email que estava no forms 
    senha = request.form.get("senha") # essa informação está no atributo name

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session["login"] = True
        return redirect("/") # Redireciona para a rota inicial
    else:
        return render_template("login.html", msgerro = "E-mail ou senha estão incorretos!")

#-------------------------------------------------------------------------------------------------
# ROTAS PARA LOGOUT
@app.route("/logout")
def logout():
    session.clear() # Apaga a lista sessão 
    return redirect("/login")

#-------------------------------------------------------------------------------------------------
# tratamento de erro - código 404
@app.errorhandler(404)
def not_found(erro):
    return render_template("/erro404.html")








































if __name__ == "__main__":
    app.run(debug=True, port=5000)
from flask import Flask, render_template, request, session, redirect
from database import consultar_tarefas
app = Flask(__name__)
app.secret_key = "igor"

# Dados de acesso do ADMIN
ADMIN_EMAIL = "igor.escudeiro@gmail.com"
ADMIN_SENHA = "123456"

@app.route("/") # HomePage- Página Inicial
def home():
    if "login" not in session:
        return redirect("/login")

    # Usuário logado
    tarefas = consultar_tarefas() # Essa variavel serve para realizar todas as consultas 
    return render_template("index.html", tarefas=tarefas) # A letra T passa a ter o mesmo valor de (TAREFAS)

# --------------------------------------------------------------------------------------------------------------------------------
# Rota de Login
@app.route("/login", methods=["GET","POST"])
def login():
    if "login" in session:
        return redirect("/")

    if request.method == "GET":
        return render_template("login.html")
   
    # POST
    email = request.form.get("email") # Pegando o email que estava no form HTML
    senha = request.form.get("senha") # Essa informação está no atributo name

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session["login"] = True # Cria a sessão login
        return redirect("/") # Redireciona para a rota inicial
    else:
        return render_template("login.html", msgerro = "E-mail ou senha estão incorretos!")

# --------------------------------------------------------------------------------------------------------------------------------
# Rota Logout
@app.route("/logout")
def logout():
    session.clear() # Apaga a lista sessão
    return redirect("/login")
# --------------------------------------------------------------------------------------------------------------------------------
# Tratamento de erro - Código 404
@app.errorhandler(404)
def not_found(erro):
    return render_template("erro404.html")







































if __name__ == "__main__":
    app.run(debug=True, port=5000)
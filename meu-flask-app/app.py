from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    usuario = None
    tarefas = []
    mostrar_boas_vindas = False

    if request.method == "POST":
        usuario = request.form.get("nome")
        tarefas = ["Estudar Flask", "Fazer exercício", "Ler livro"]
        mostrar_boas_vindas = True
    return render_template("home.html", usuario=usuario, tarefas=tarefas, mostrar=mostrar_boas_vindas)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

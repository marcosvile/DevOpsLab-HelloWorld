from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/explorar.html")
def explorar():
    return render_template('explorar.html')

@app.route("/contato.html")
def contato():
    return render_template('contato.html')

@app.route("/github.html")
def github():
    return render_template('github.html')

@app.route("/roadmap.html")
def roadmap():
    return render_template('roadmap.html')

if __name__ == '__main__':
    app.run(debug=True)
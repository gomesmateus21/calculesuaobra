from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    calculos = ["Pisos", "Tijolos", "Contrapiso", "Tinta"]
    return render_template("index.html", calculos=calculos)


if __name__ == "__main__":
    app.run()

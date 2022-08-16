from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    calculos = ["pisos", "tijolos", "contrapiso", "tinta"]
    return render_template("index.html", calculos=calculos)


if __name__ == "__main__":
    app.run()

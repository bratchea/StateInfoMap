from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    with open("static/images/us.svg") as um:
        us_map = um.read()

    return render_template("index.j2", us_map=us_map)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

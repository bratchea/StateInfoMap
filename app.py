from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    with open("static/images/us.svg") as um:
        us_map = um.read()

    return render_template("index.j2", us_map=us_map)


@app.route("/state/<state>")
def state(state):
    q_args = request.args

    # make call to state info micro service here

    info = {
        "state": state,
        "capital": f"Capital of {state}",
        "largest_metro": f"Largest Metro in {state}",
        "governor": f"Governor of {state}",
        "admitted": f"Year {state} was admitted",
        "area": f"area of {state}"
    }
    return render_template("state_info.j2", info=info)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

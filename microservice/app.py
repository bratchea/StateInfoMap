from flask import Flask


app = Flask(__name__)

@app.route("/<state>")
def get_state_info(state):
    return f"State Info Requested: {state}"


if __name__ == "__main__":
    app.run(host="localhost", port=50000, debug=True)

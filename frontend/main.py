import requests
import random

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    with open("static/images/us.svg") as um:
        us_map = um.read()

    return render_template("index.j2", us_map=us_map)


@app.route("/list")
def list_view():
    return render_template("list_view.j2")


@app.route("/state/<state>")
def state(state):
    # make call to state info micro service here
    resp = requests.get(url=f"https://backend-api-dot-state-info-proj.uk.r.appspot.com/states/{state}")
    assert resp.status_code == 200, resp.text

    image = requests.get(url=f"http://20.121.0.200/?keyword={state}")
    assert image.status_code == 200, image.text

    # grab the image links that is a .jpg
    image_links = [img for img in image.json() if img.endswith(".jpg")]
    if len(image_links) > 0:
        # pick a random image from the list of .jpg
        image_link = image_links[random.randrange(0, len(image_links))]
    else:
        image_link = "static/images/NotFound.jpg"

    return render_template("state_info.j2", info=resp.json(), image=image_link)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

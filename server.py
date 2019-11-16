from flask import Flask
from src.cliptool import getClip, setClip

app = Flask(__name__)

@app.route("/set/<string:clipdata>")
def clipSet(clipdata):
  return setClip(clipdata)

@app.route("/get")
def clipGet():
  return getClip()


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4665)

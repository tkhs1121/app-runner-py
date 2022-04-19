from random import randint
from flask import Flask, Response

PORT = 8080
app = Flask(__name__)

@app.route("/")
def hello():
    r = randint(0, 2)
    if r == 0:
        return Response(status=200)
    if r == 1:
        return Response(status=400)
    if r == 2:
        return Response(status=500)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
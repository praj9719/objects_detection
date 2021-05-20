from flask import Flask, jsonify, request
from yolo import get_predictions

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify("Object Detection")


@app.route("/detect", methods=["GET", "POST"])
def detect():
    if request.method == 'POST':
        predictions = get_predictions(request)
        return jsonify(predictions)
    else:
        return jsonify("Use POST method")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False)

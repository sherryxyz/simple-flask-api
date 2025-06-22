from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("features", [])

    if not isinstance(features, list):
        return jsonify({"error": "features must be a list"}), 400

    if sum(features) > 10:
        result = "class_B"
    else:
        result = "class_A"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
from flask import Flask, request, jsonify
import torch
from torchvision import models, transforms
from torchvision.models import ResNet50_Weights
from PIL import Image
import io

app = Flask(__name__)

# Load a pretrained ResNet model
weights = ResNet50_Weights.DEFAULT
model = models.resnet50(weights=weights)
model.eval()

# Define image preprocessing
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']

    try:
        img = Image.open(io.BytesIO(file.read())).convert("RGB")
        img_tensor = preprocess(img).unsqueeze(0)  # Add batch dimension

        with torch.no_grad():
            outputs = model(img_tensor)
            predicted_idx = outputs.argmax(1).item()

        # Use ImageNet labels
        from torchvision.models import ResNet50_Weights
        labels = ResNet50_Weights.DEFAULT.meta["categories"]
        predicted_label = labels[predicted_idx]

        # Simple dog/cat/unknown classification
        lower = predicted_label.lower()
        if "cat" in lower:
            result = "cat"
        elif "dog" in lower or "retriever" in lower:
            result = "dog"
        else:
            result = "unknown"

        return jsonify({
            "prediction": result,
            "imagenet_label": predicted_label
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

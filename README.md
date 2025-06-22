# 🐱🐶 🐾 Cat vs Dog Classifier API

This is a lightweight Flask API that uses a pretrained **ResNet50** model from PyTorch to classify uploaded images as **cat**, **dog**, or **unknown**.

---

## 🔧 Features

- Built with Flask
- Accepts image upload via POST request
- Uses `ResNet50` pretrained on ImageNet
- Returns prediction result as JSON

---

## 🚀 Setup

### 1. Create virtual environment (optional)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install flask torch torchvision pillow
```
or use requirements.txt

### 3. Run the app
python app.py

The API will be available at your local computer:
📍 http://127.0.0.1:5000


### 📤 Endpoint
POST /predict
Uploads an image and returns the classification result.

🔧 Example using curl:
```bash
curl -X POST -F "file=@/path/to/your/image.jpg" http://127.0.0.1:5000/predict
```
Replace /path/to/your/image.jpg with your actual image path.
Replace the url if you host your app on a cloud platform.
The current URL can only be used locally


📌 Notes
The model is a pretrained ResNet50 (ResNet50_Weights.DEFAULT) from PyTorch.

It maps ImageNet predictions to 3 labels: "cat", "dog", or "unknown" using keyword matching.

You can easily modify the logic or add more label mappings based on your use case.


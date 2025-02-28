from flask import Flask, request, jsonify, render_template
from keras.models import load_model

import numpy as np

# Load the trained model
model_path = 'modelnew.h5'
model = load_model(model_path)


app = Flask(__name__)

# Define class labels
labels = ["Cardboard", "Metal", "Plastic", "Glass", "Trash"]

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    # Placeholder for prediction logic
    # result = predict(file)
    return 'File uploaded successfully', 200

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input features
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        
        # Make prediction
        prediction = model.predict(final_features)
        output = labels[int(prediction[0])]  # Convert numeric output to label

        return render_template('index.html', prediction_text=f'Prediction: {output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)

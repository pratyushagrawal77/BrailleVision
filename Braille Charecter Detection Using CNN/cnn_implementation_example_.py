# -*- coding: utf-8 -*-
"""CNN Implementation Example .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a68AfBU4Sf_A6zWVK2u_6a9aSPJt7EsL

![pppp.png](data:image/png;base64,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)
"""

# Define class labels for Braille characters (assuming A-Z)
class_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to load the model, preprocess the image, and predict the Braille character
def predict_braille_character(image_path, model_path):
    # Load the model
    model = joblib.load(model_path)

    # Load and prepare the image
    img = load_img(image_path, target_size=(28, 28), color_mode='grayscale')
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img.astype('float32') / 255.0  # Normalize to [0, 1]

    # Predict the class
    prediction = model.predict(img)
    predicted_class_idx = np.argmax(prediction, axis=1)[0]

    # Get the corresponding Braille character label
    predicted_character = class_labels[predicted_class_idx]
    return predicted_character

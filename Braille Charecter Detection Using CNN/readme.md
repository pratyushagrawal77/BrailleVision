# Braille Character Prediction

This project provides an implementation to predict Braille characters using a Convolutional Neural Network (CNN) model. The model identifies Braille characters in grayscale images and outputs the predicted alphabet.

## Requirements

To run the code, ensure you have the following libraries installed:

```python
import joblib
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
```

## Function Description

The core function, `predict_braille_character`, processes an input image to predict the corresponding Braille character as follows:

- **Load Model**: The pre-trained CNN model is loaded using the Joblib library.
- **Preprocess Image**: The function loads and preprocesses the input image by resizing it to the required dimensions and normalizing pixel values.
- **Predict Character**: After processing, the model outputs a predicted index, which is then mapped to the corresponding character in the English alphabet (A-Z).

## Example Usage

To run the function with a specified image and model, use the following code:

```python
# Example usage:
image_path = "/content/sss.png"
model_path = "/content/CNNmodel_joblib.pkl"
predicted_character = predict_braille_character(image_path, model_path)
print(f"Predicted Braille character: {predicted_character}")
```

This code will:

- Load the specified CNN model from the given path.
- Process the input Braille character image.
- Output the predicted alphabet character (e.g., "A", "B", "C", etc.).

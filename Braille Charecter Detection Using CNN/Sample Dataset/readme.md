# Dataset Description for Braille Character Prediction

This dataset is designed for predicting Braille characters using a Convolutional Neural Network (CNN). The dataset contains images of Braille characters that are made on our own, each representing a letter from 'a' to 'z'. The dataset has been augmented using various techniques to increase its size and robustness for model training.

## Dataset Structure

- The dataset is organized into 26 subfolders, each named after a letter of the alphabet (from 'a' to 'z').
- Each subfolder contains 108 images of the corresponding Braille character. The images are generated using custom-made Braille sheets.
- Each image starts with the letter it represents (e.g., images in the "a" folder represent the Braille character for the letter 'a').

## Augmentation Techniques

To enhance the dataset and improve model performance, various augmentation techniques have been applied to the images, including:

- **Blurring**: Introduced to simulate noise and imperfections in real-world images.
- **Hue and Contrast Adjustment**: To provide variation in color and brightness for better generalization.
- **Zooming**: Random zooming applied to the images to simulate different perspectives.
- **Brightness Adjustment**: To simulate different lighting conditions.

These augmentations were implemented using Python libraries to generate synthetic variations of the images, effectively expanding the dataset size and helping the model learn more generalized features.

## Labeling Logic

The labeling of images follows a simple structure:

- Each folder name corresponds to the Braille character it represents (e.g., images in the 'a' folder are labeled as 'a').
- The images are labeled according to the folder they are located in, allowing for clear identification of the character each image signifies.

This dataset provides a solid foundation for training a model to predict Braille characters and can be extended for other applications in assistive technologies.

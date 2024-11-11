# Page Detection Dataset

This dataset contains images used for training a YOLO-based model to detect pages in various conditions. The images are captured from different real-life settings and include variations in background, lighting, and perspective to ensure model robustness. Additionally, the dataset includes non-page images, allowing the model to learn what should **not** be classified as a page.

## Dataset Details

- **Total Images**: ~3,000 images
- **Contents**: 
  - **Page Images**: Images of different pages captured under diverse conditions.
  - **Non-Page Images**: Random images to help the model differentiate between page and non-page content.
- **Annotations**: Labeled in YOLOv8 format, with separate folders for `images` and `labels`.

## Usage

This dataset can be used to train object detection models to accurately identify page regions within an image, while ignoring irrelevant content.

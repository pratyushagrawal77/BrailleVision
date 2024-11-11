# Page Extraction and Background Removal

This project provides an implementation to extract a specific region (page) from an image, remove its background, and resize the result. The extracted region is identified using a YOLO model trained on page detection.

## Requirements

Install the necessary libraries with the following command:

```bash
!pip install ultralytics opencv-python
```

### Import Libraries

After installing the required packages, import the following libraries:

```python
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
from IPython.display import display
```

## Function Description

The core function, `extract_and_display`, processes an image as follows:

1. **Extract Page**: Detects and extracts the region of interest (ROI) representing a page from the image using a pre-trained YOLO model.
2. **Remove Background**: Applies a grayscale and binary threshold mask to remove the background from the detected page.
3. **Resize**: Resizes the extracted page to a standard size of 750x750 pixels.

### Function: `extract_and_display`

This function takes the following inputs:

- `image_path`: Path to the input image.
- `model_path`: Path to the YOLO model file (`best.pt`).

The function outputs:

- The extracted and background-removed image.
- Displays the resized image along with the detected class and confidence score.

## Example Usage

Run the code with your specified image and model paths as follows:

```python
image_path = '/content/x.jpg'
model_path = '/content/best.pt'
extract_and_display(image_path, model_path)
```

This command will:

- Extract the region containing the page.
- Remove the background.
- Resize and display the final result with class and confidence score.

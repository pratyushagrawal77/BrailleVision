# Hand Index Finger Detection using MediaPipe

## Installation

First, install the required packages:

```bash
!pip install opencv-python mediapipe matplotlib
```bash
## Import Libraries

After installing the required packages, import the following libraries:

```python
import cv2
from matplotlib import pyplot as plt
import mediapipe as mp

## Function Description

The core function, `detect_and_display_hand_with_index_finger`, processes an input image to detect the hand and places a green dot on the index finger tip:

- **Detect Hand**: The function uses MediaPipe to detect hand landmarks in the image.
- **Highlight Index Finger**: It locates the index finger and draws a green dot on the finger tip.
- **Display Result**: The image with the green dot on the index finger is displayed.

### Function: `detect_and_display_hand_with_index_finger`

This function takes the following input:

- `image_path`: Path to the input image file.

The function outputs:

- An image with the hand landmarks and a green dot on the index finger tip.

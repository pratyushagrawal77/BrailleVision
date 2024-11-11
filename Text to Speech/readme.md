# Text-to-Speech Conversion Project

This project converts user-input text to speech, plays the audio, and cleans up temporary files afterward. It’s designed to use Google Text-to-Speech (gTTS) and pydub for efficient audio playback and is compatible with platforms supporting `ffmpeg`.

## Requirements

1. **Python Packages**:
   - `gTTS`: For converting text to speech.
   - `pydub`: For handling audio playback.

2. **System Requirements**:
   - `ffmpeg`: Needed by pydub for audio file handling. Install it using the command below in your terminal or Colab notebook.

## Installation

Install the required packages and dependencies by running the following commands:

```bash
# Install Python packages
!pip install gtts pydub

# Install ffmpeg
!apt-get install -y ffmpeg
```

## Library Imports

To use the text-to-speech function, ensure you import the following libraries:

```python
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
```
## Example Usage

The following example prompts the user to enter text, which will then be converted to speech and played:

```python
# Example usage:
text = input("Enter the text you want to convert to speech: ")
text_to_speech(text)
```

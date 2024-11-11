# Speech Recognition Script using Python's SpeechRecognition Library

This project leverages Python's `speech_recognition` library to capture audio input from a microphone and convert it into text using Google's Speech Recognition API. It's designed to listen to spoken input from the user and transcribe it accurately in real-time.

## Features
- **Real-time Speech Recognition**: Listens to the user's spoken input and provides an instant transcription.
- **Language Customization**: By default, the language is set to English (India), but it can be adjusted as needed.
- **Error Handling**: Includes error handling for unrecognized audio or connection issues with Google’s API.

## Requirements
To use this script, ensure the following library is installed:
```bash
pip install SpeechRecognition
```
## Usage

### Running the Script

1. **Listening for Audio Input**:
   - The script initiates listening for audio input from the microphone as soon as it is run.

2. **Transcribing Audio**:
   - After capturing the audio, the script uses Google’s Speech Recognition API to transcribe it into text.

3. **Output**:
   - If the transcription is successful, the script outputs the recognized text.
   - If there is an error (e.g., if the audio is unclear or there’s a connection issue), an error message will be displayed.
## Example Output

```plaintext
Listening, please say something:
Recognized text: Hello, how are you doing?
```
## Customization

- **Language Adjustment**: The language for transcription can be customized by modifying the `language` parameter in the code. You can set it to any supported language code, such as `"en-US"` for English (United States) or `"hi-IN"` for Hindi (India).

## Notes

- **Internet Connection**: An active internet connection is necessary to use Google’s Speech Recognition API for transcription.
- **Applications**: This tool is ideal for applications requiring voice-to-text functionality, including virtual assistants, transcription services, and hands-free interfaces.


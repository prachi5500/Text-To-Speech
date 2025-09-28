# Text-to-Speech (Indian English Accent) Python Project

## Overview
This project is a **Text-to-Speech (TTS) generator** built using Python.  
It converts any input text into **natural-sounding speech** in **Indian English accent** and saves it as an audio file (`.mp3`).  
The generated audio can also be played automatically on Windows.

This is useful for:
- Audiobooks
- Educational content
- Accessibility for visually impaired users
- Voice notifications

---

## Features
- Converts text input to speech using **gTTS**.
- Supports **Indian English accent** (`tld='co.in'`).
- Automatically saves audio as an MP3 file.
- Plays the audio automatically on Windows.
- Easy to modify input text and output file location.

---

## Requirements
- Python 3.x
- Internet connection (gTTS requires online access)

### Python Libraries
Install required libraries using pip:
```bash
pip install gTTS

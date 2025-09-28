from gtts import gTTS

from playsound import playsound
import os


INPUT_TEXT = """ Engineering is the application of science, technology, and mathematics to solve real-world problems and create useful systems, structures, and machines. It plays a vital role in improving the quality of life and advancing human civilization. Engineers design, build, and maintain bridges, buildings, vehicles, software, electrical systems, and countless other technologies that people rely on every day.Engineering requires creativity, critical thinking, and problem-solving skills. Engineers must also consider safety, efficiency, and environmental impact while developing new solutions. Modern engineering is increasingly interdisciplinary, combining knowledge from multiple fields to address complex challenges like renewable energy, artificial intelligence, and sustainable infrastructure.
"""


tts = gTTS(text=INPUT_TEXT, lang='en', tld='co.in', slow=False)
 
OUTPUT_FILENAME = "audio_output.mp3"
tts.save(OUTPUT_FILENAME)


print("Audio is playing...")
playsound(OUTPUT_FILENAME)
print(f"File successfully saved: {os.system(f'start {OUTPUT_FILENAME}')}")

# 🎙️ Emotion Voice AI

An AI-powered multilingual emotion analysis and voice synthesis system that combines Speech-to-Text, Emotion Detection, Translation, AI Response Generation, and Text-to-Speech into a single interactive application.

## 🚀 Features

### 🎤 Speech Recognition

* Microphone input support
* Multilingual speech recognition
* Powered by Faster-Whisper
* Supports English, Tamil, Hindi, Telugu, and Malayalam

### 😊 Emotion Detection

* Transformer-based emotion classification
* Detects:

  * Joy
  * Sadness
  * Anger
  * Fear
  * Surprise
  * Neutral
  * Disgust

### 🤖 AI Response Generation

* Generates contextual responses based on detected emotions
* Emotion-aware interaction

### 🌍 Multilingual Support

* English
* Tamil
* Hindi
* Telugu
* Malayalam

### 🔊 Voice Synthesis

* Edge-TTS Neural Voices
* Male Voice
* Female Voice
* Child Voice
* Robot Voice

### 📊 Analytics Dashboard

* Emotion Distribution Graph
* Emotion History
* Statistics Dashboard
* Insights Dashboard

---

## 🏗️ System Architecture

User Speech/Text
↓
Speech-to-Text (Faster Whisper)
↓
Translation to English
↓
Emotion Detection (Transformer Model)
↓
AI Response Generation
↓
Translation to Selected Language
↓
Voice Synthesis (Edge-TTS)
↓
Dashboard Visualization

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI / NLP

* Transformers
* Faster-Whisper
* Deep Translator

### Voice Processing

* Edge-TTS
* FFmpeg

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib

---

## 📂 Project Structure

EmotionVoiceAI/

├── app.py

├── emotion_detector.py

├── speech_ui.py

├── voice_generator.py

├── translator.py

├── chatbot.py

├── tone_analyzer.py

├── graph_generator.py

├── history_manager.py

├── statistics_manager.py

├── insights_manager.py

├── outputs/

├── requirements.txt

└── README.md

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aadhithya10112004/EmotionVoiceAI.git
cd EmotionVoiceAI
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---


## 🎯 Learning Outcomes

* Natural Language Processing
* Speech Recognition
* Transformer Models
* Emotion Analysis
* Translation Systems
* Text-to-Speech Synthesis
* Streamlit Development
* AI Application Deployment

---

## 👨‍💻 Author

Aadhithya S

Artificial Intelligence & Data Science Student

Passionate about AI, NLP, Machine Learning, Full Stack Development, and Problem Solving.

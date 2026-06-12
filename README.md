# 🎙️ Emotion-Based Voice Synthesis and Tone Analysis System

## Overview

The Emotion-Based Voice Synthesis and Tone Analysis System is an AI-powered application that analyzes user text, detects the underlying emotion, performs tone analysis, and generates speech output with emotion-aware characteristics.

The system combines Natural Language Processing (NLP), emotion classification, data visualization, speech synthesis, and an interactive dashboard to provide a complete end-to-end AI solution.

---

## Features

### Emotion Detection

* Detects emotions from user-entered text.
* Uses a Transformer-based NLP model from Hugging Face.
* Supports:

  * Joy
  * Sadness
  * Anger
  * Fear
  * Surprise
  * Neutral
  * Disgust

### Confidence Analysis

* Displays confidence scores for emotion predictions.
* Shows the most probable emotion along with prediction confidence.

### Multi-Emotion Distribution

* Displays probability scores for all detected emotions.
* Helps understand how the AI model interprets the input text.

### Tone Analysis

Maps detected emotions to speech characteristics:

| Emotion  | Pitch  | Speed  | Energy    |
| -------- | ------ | ------ | --------- |
| Joy      | High   | Fast   | High      |
| Sadness  | Low    | Slow   | Low       |
| Anger    | High   | Fast   | Very High |
| Fear     | Medium | Fast   | Medium    |
| Surprise | High   | Medium | High      |
| Neutral  | Normal | Normal | Normal    |
| Disgust  | Low    | Normal | Medium    |

### Emotion Visualization

* Generates emotion distribution charts.
* Displays confidence levels using graphical visualizations.

### Voice Generation

* Converts text into speech.
* Adjusts speech rate based on detected emotion.

### Emotion History

* Stores previous analyses.
* Displays historical emotion predictions inside the dashboard.

### Interactive Dashboard

* Built using Streamlit.
* Provides a user-friendly interface for emotion analysis and visualization.

---

## System Architecture

User Text Input
↓
Emotion Detection Model
↓
Confidence Analysis
↓
Tone Analyzer
↓
Voice Generator
↓
Dashboard Visualization
↓
Emotion History Storage

---

## Technologies Used

### Frontend

* Streamlit

### Artificial Intelligence / NLP

* Hugging Face Transformers
* PyTorch

### Data Processing

* Pandas

### Visualization

* Matplotlib

### Speech Synthesis

* pyttsx3

### Storage

* CSV File Storage

---

## Project Structure

EmotionVoiceAI/

├── app.py

├── emotion_detector.py

├── tone_analyzer.py

├── graph_generator.py

├── voice_generator.py

├── history_manager.py

├── history.csv

├── requirements.txt

├── outputs/

│   └── emotion_chart.png

└── README.md

---

## Installation

### Clone Repository

git clone <repository-url>

cd EmotionVoiceAI

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## Run the Application

streamlit run app.py

---

## Sample Input

I got selected for my dream company today!

### Sample Output

Detected Emotion: JOY

Confidence: 93.31%

Tone Analysis:

* Pitch: High
* Speed: Fast
* Energy: High

Voice Output Generated

Emotion Distribution Chart Displayed

---

## Future Enhancements

* Multi-language support
* Real-time speech emotion detection
* Voice personality selection
* Emotion-aware audio generation
* Download generated audio
* AI avatar integration
* Cloud deployment

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Natural Language Processing (NLP)
* Transformer Models
* Emotion Classification
* Text-to-Speech Systems
* Data Visualization
* Streamlit Application Development
* AI System Integration
* End-to-End Machine Learning Applications

---

## Author

Aadhithya S

Artificial Intelligence and Data Science Student

Passionate about AI, Machine Learning, Full-Stack Development, and Software Engineering.

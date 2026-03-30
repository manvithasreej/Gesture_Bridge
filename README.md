# 🖐️🎙️ Gesture Bridge

### A Bi-Directional Sign Language Communication System

Gesture Bridge is an application that enables **two-way communication** between **hearing-impaired** and **hearing users** by converting:

- ✋ **Sign Language → Text**
- 🎙️ **Voice → Sign Language (GIFs & Letter Visuals)**

The system bridges the communication gap using **Computer Vision**, **Speech Recognition**, and **Deep Learning**.

---

## 📌 Project Overview

Gesture Bridge integrates **real-time hand gesture recognition** with **voice-to-sign visualization** to create an inclusive communication platform.

- Uses a camera to detect hand landmarks and recognize gestures.
- Converts recognized gestures into readable text.
- Converts spoken words into **sign language GIFs** or **letter-by-letter visual actions**.
- Designed with a **simple GUI** for easy interaction.

---

## 🎯 Key Features

### ✋ Sign to Text (Visual → Text)

- Real-time hand gesture detection using **MediaPipe**.
- ASL/ISL gesture classification using a **Deep Learning model**.
- Displays detected gesture labels on-screen.
- Supports dataset creation and model retraining.

### 🎙️ Voice to Sign (Speech → Visual)

- Converts live voice input into text using **Speech Recognition**.
- If detected text matches predefined dictionary phrases:

  - Displays the **corresponding Sign Language GIF**.

- If not:

  - Breaks the word into letters.
  - Displays **letter-by-letter sign images** sequentially.

- Automatically exits when the user says **“goodbye”**.

### 🖥️ User Interface

- Simple and interactive GUI using **EasyGUI**.
- Central menu with two modes:

  - Sign to Text
  - Voice to Sign

---

## 🧭 Application Flow

### Main Menu

```
Gesture Bridge
│
├── Sign to Text
│   └── Camera → Hand Detection → Gesture Classification → Text Output
│
├── Voice to Sign
│   └── Speech → Text
│       ├── If phrase in dictionary → Display GIF
│       ├── Else → Display letter visuals sequentially
│       └── If “goodbye” → Exit
│
└── Exit
```

---

## 🛠️ Technologies Used

- **Python 3.10**
- **OpenCV** – Camera handling & visualization
- **MediaPipe** – Hand landmark detection
- **TensorFlow** – Gesture classification model
- **SpeechRecognition** – Voice input processing
- **EasyGUI** – GUI menu and dialogs
- **Pillow** – Image & GIF handling
- **NumPy, Pandas, Scikit-learn**
- **Matplotlib, Seaborn** – Visualization & debugging

---

## 📦 Requirements

Create a virtual environment and install dependencies using:

```txt
numpy==1.26.4
opencv-contrib-python==4.8.1.78
mediapipe==0.10.9
tensorflow-intel==2.16.1
protobuf==3.20.3

Pillow
pandas
scikit-learn
matplotlib
seaborn
easygui
SpeechRecognition
```

> ⚠️ **Note:** > `tkinter` comes pre-installed with Python on Windows and should NOT be added to `requirements.txt`.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bhavya0420/Gesture_Bridge.git
cd Gesture_Bridge
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

---

## 🎮 Usage Instructions

### ▶️ Sign to Text

- Select **Sign to Text** from the main menu.
- Show hand gestures in front of the camera.
- Detected gestures will be classified and displayed as text.
- Press **ESC** to exit.

### ▶️ Voice to Sign

- Select **Voice to Sign**.
- Choose **Live Voice**.
- Speak clearly into the microphone.
- Output:

  - Phrase GIF (if predefined).
  - Letter-by-letter sign images (if not).

- Say **“goodbye”** to exit automatically.

---

## 📁 Project Structure

```
Gesture_Bridge/
│
├── app.py
├── sign_to_text.py
├── voice_to_sign.py
│
├── assets/
│   ├── logo.png
│   ├── voicetosign.png
│   ├── letters/
│   └── ISL_Gifs/
│
├── model/
│   ├── dataset/
│   └── keypoint_classifier/
│
├── utils/
│   └── cvfpscalc.py
│
├── requirements.txt
└── README.md
```

---

## 🧠 Model Training (Optional)

You can retrain the gesture classifier using your own dataset:

- Capture hand landmarks using:

  - **`k`** → Manual logging mode
  - **`d`** → Dataset-based logging mode

- Data stored in:

  ```
  model/keypoint_classifier/keypoint.csv
  ```

- Train using the provided Jupyter Notebook.

---

## 🚀 Future Enhancements

- Support for **full sentence sign animation**
- Multilingual speech input
- Mobile & web-based deployment
- Enhanced dataset for more gestures
- Real-time text-to-sign avatar

---

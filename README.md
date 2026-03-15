# Smart Traffic Rules Violation Detection System 🚦

A real-time **Computer Vision system** that detects traffic rule violations such as **helmet absence and speed violations** using **Python and OpenCV**. The system processes video frames, identifies violations, and automatically generates visual evidence for enforcement.

---

## 📌 Overview

Monitoring traffic violations manually is difficult due to the increasing number of vehicles on roads. This project demonstrates how **computer vision techniques** can automate traffic rule enforcement by detecting violations from video streams.

The system analyzes frames from a video or camera feed and detects:

* Helmet violations by two-wheeler riders
* Speed violations
* Vehicles involved in rule violations
* Evidence frames for violation records

This helps improve **road safety and automated traffic monitoring**.

---

## ⚙️ Technologies Used

* **Python**
* **OpenCV**
* **NumPy**
* **Computer Vision Techniques**
* **Image Processing**

---

## 🧠 Features

* Real-time traffic rule violation detection
* Helmet detection for riders
* Speed violation monitoring
* Automatic violation evidence generation
* Frame-by-frame video processing
* Lightweight and easy to run

---

## 🏗 System Workflow

1. Capture video input from a camera or video file
2. Extract frames from the video stream
3. Detect vehicles in the frame
4. Identify violations such as helmet absence or overspeeding
5. Highlight violations and generate evidence frames

---

## 📂 Project Structure

```
Smart-Traffic-Rules-Violation-Detection-System
│
├── images/
├── videos/
├── detection.py
├── violation_detection.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```
git clone https://github.com/lakshminagasai/Smart-Traffic-Rules-Violation-Detection-System.git
```

### 2. Navigate to the project directory

```
cd Smart-Traffic-Rules-Violation-Detection-System
```

### 3. Install required dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the main detection script:

```
python detection.py
```

or

```
python violation_detection.py
```

The system will process video frames and highlight detected traffic violations.

---

## 📊 Output

The system will:

* Detect vehicles and riders
* Identify rule violations
* Draw bounding boxes around violations
* Save violation evidence images

---

## 🔮 Future Improvements

* License plate recognition system
* Automatic challan generation
* Deep learning models such as YOLO for improved detection
* Real-time CCTV integration
* Traffic analytics dashboard

---

## 👩‍💻 Author

**Samatham Lakshmi Naga Sai**

GitHub: https://github.com/lakshminagasai


---

## ⭐ Support

If you found this project helpful, please give this repository a **star ⭐ on GitHub**.

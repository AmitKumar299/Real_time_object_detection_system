# ✨ Real-Time Object Detection System


## 📌 Overview
The Real-Time Object Detection System is a web-based computer vision application that performs live object detection using a webcam.  
It is built using **Flask, OpenCV, and YOLOv8 (Ultralytics)** to detect and display objects in real-time through a web interface.

The system also provides **voice-based announcements** for detected objects, making it interactive and user-friendly.

---

## 🎯 Objectives
- To implement real-time object detection using YOLOv8.
- To integrate deep learning with a web-based interface.
- To capture live webcam feed using OpenCV.
- To dynamically display detected objects.
- To provide speech feedback for detected objects.

---

## 🛠️ Technologies Used

- **Python** – Backend programming  
- **Flask** – Web framework  
- **OpenCV** – Video capture & frame processing  
- **YOLOv8 (Ultralytics)** – Object detection model  
- **HTML, CSS, JavaScript** – Frontend development  
- **pyttsx3 – Text-to-Speech conversion  

---

## 🧠 Working Principle

1. The webcam captures live video frames.
2. Each frame is processed using the YOLOv8 model.
3. Detected objects are identified with confidence filtering.
4. Annotated frames are streamed to the browser.
5. Object names are displayed dynamically.
6. Voice alerts are triggered when new objects are detected.

---

## 🚀 Features

- Live webcam streaming  
- Real-time object detection  
- Confidence-based filtering  
- Dynamic object name display  
- Voice-based object announcements  
- Start/Stop stream control  
- Responsive web interface  

---

## 📂 Project Structure

Real_time_object_detection_system/
│
├── main.py
├── requirements.txt
├── README.md
│
└── templates/
└── index.html


### 3️⃣ Download YOLOv8 Model
Download `yolov8n.pt` from the official Ultralytics repository and place it in the project folder.

### 4️⃣ Run the Application
python main.py


### 5️⃣ Open in Browser
http://127.0.0.1:5000


---

## 📊 Applications

- Smart surveillance systems  
- Assistive technology for visually impaired users  
- Educational demonstrations of computer vision  
- Automated monitoring systems  

---

## 🔮 Future Enhancements

- Multi-camera support  
- Object tracking  
- Detection history logging  
- Cloud deployment  
- Performance optimization using GPU  

---

## 👨‍💻 Author
**Amit Kumar**  
Real-Time Object Detection using Flask 

---

## 📜 License
This project is licensed under the MIT License.

## 📸 Project Screenshot

. ![img](https://github.com/user-attachments/assets/bdd5801d-2fed-4df7-a639-1632f6ac6b01)

..  <img width="1873" height="907" alt="Screenshot 2025-07-18 031525" src="https://github.com/user-attachments/assets/56880dcd-646e-45a0-9a8b-3012d766db2e" />

...  <img width="1830" height="863" alt="Screenshot 2025-07-18 031552" src="https://github.com/user-attachments/assets/f6a56fe7-2739-4ef8-8f48-191db5bc293c" />


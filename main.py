from flask import Flask, render_template, Response, jsonify
import cv2
from ultralytics import YOLO
import threading

app = Flask(__name__)

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

streaming = False
current_objects = []
lock = threading.Lock()

def generate_frames():
    global streaming, current_objects
    while streaming:
        success, frame = cap.read()
        if not success:
            break

        results = model.predict(frame, conf=0.5)

        names = set()
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                name = model.names[cls_id]
                names.add(name)

        with lock:
            current_objects = list(names)

        annotated_frame = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start_stream', methods=['POST'])
def start_stream():
    global streaming
    streaming = True
    return '', 204

@app.route('/stop_stream', methods=['POST'])
def stop_stream():
    global streaming
    streaming = False
    return '', 204

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_objects')
def get_objects():
    with lock:
        return jsonify(current_objects)

if __name__ == "__main__":
    app.run(debug=False)

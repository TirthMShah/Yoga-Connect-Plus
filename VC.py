from app import app, render_template,request,Response
import cv2

def generate_frames():
    camera = cv2.VideoCapture(0)  # Use 0 for the default camera
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/vc')
def vc():
    return render_template('VC.html',trainer_username=request.args.get("trainer_username"),username=request.args.get("username"))

@app.route('/VideoC')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/view')
def view():
    return render_template('')
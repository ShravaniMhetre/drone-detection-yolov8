import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as tb 
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO
import time

# Load YOLO model
model = YOLO("models/best.pt")

# Global variables
cap = None
stop_camera = False
confidence_threshold = 0.25  # fixed threshold

# Function: detect from file (image)
def predict_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.png *.jpeg")]
    )
    if not file_path:
        return

    results = model.predict(file_path, conf=confidence_threshold)
    im_array = results[0].plot()
    show_image(im_array)


# Function: start webcam live detection
def start_camera():
    global cap, stop_camera
    stop_camera = False
    cap = cv2.VideoCapture(0)

    def update_frame():
        global stop_camera
        if stop_camera:
            return

        ret, frame = cap.read()
        if ret:
            start_time = time.time()
            results = model.predict(frame, conf=confidence_threshold, verbose=False)
            im_array = results[0].plot()

            # FPS
            fps = 1 / (time.time() - start_time + 1e-6)
            cv2.putText(im_array, f"FPS: {fps:.1f}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            show_image(im_array)

        panel.after(20, update_frame)

    update_frame()


# Function: open video file and run detection
def open_video():
    global cap, stop_camera
    stop_camera = False
    file_path = filedialog.askopenfilename(
        title="Select a Video",
        filetypes=[("Video files", "*.mp4 *.avi *.mov")]
    )
    if not file_path:
        return

    cap = cv2.VideoCapture(file_path)

    def update_frame():
        global stop_camera
        if stop_camera:
            return

        ret, frame = cap.read()
        if ret:
            start_time = time.time()
            results = model.predict(frame, conf=confidence_threshold, verbose=False)
            im_array = results[0].plot()

            # FPS
            fps = 1 / (time.time() - start_time + 1e-6)
            cv2.putText(im_array, f"FPS: {fps:.1f}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            show_image(im_array)
            panel.after(20, update_frame)
        else:
            stop_camera_feed()

    update_frame()


# Function: stop webcam/video
def stop_camera_feed():
    global cap, stop_camera
    stop_camera = True
    if cap:
        cap.release()


# Function: capture current webcam frame & run detection
def capture_photo():
    global cap
    if cap:
        ret, frame = cap.read()
        if ret:
            results = model.predict(frame, conf=confidence_threshold)
            im_array = results[0].plot()
            show_image(im_array)


# Function: save snapshot
def save_snapshot():
    global panel
    if hasattr(panel, "image"):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
        )
        if file_path:
            panel.image._PhotoImage__photo.write(file_path)
            messagebox.showinfo("Saved", f"Snapshot saved to {file_path}")


# Helper function: show image in panel
def show_image(im_array):
    im_rgb = cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(im_rgb)
    im_tk = ImageTk.PhotoImage(im_pil)

    panel.config(image=im_tk)
    panel.image = im_tk


# Tkinter GUI 
root = tb.Window(themename="darkly")
root.title("🚁 Drone Detection with YOLOv8")
root.geometry("900x700")

# Frame: Buttons
btn_frame = tb.Frame(root)
btn_frame.pack(side="top", pady=10)

btn1 = tb.Button(btn_frame, text="📁 Select Image", bootstyle="info", command=predict_image)
btn1.grid(row=0, column=0, padx=5)

btn2 = tb.Button(btn_frame, text="🎥 Start Camera", bootstyle="success", command=start_camera)
btn2.grid(row=0, column=1, padx=5)

btn3 = tb.Button(btn_frame, text="🎬 Open Video", bootstyle="primary", command=open_video)
btn3.grid(row=0, column=2, padx=5)

btn4 = tb.Button(btn_frame, text="📸 Capture Photo", bootstyle="warning", command=capture_photo)
btn4.grid(row=0, column=3, padx=5)

btn5 = tb.Button(btn_frame, text="🛑 Stop", bootstyle="danger", command=stop_camera_feed)
btn5.grid(row=0, column=4, padx=5)

btn6 = tb.Button(btn_frame, text="💾 Save Snapshot", bootstyle="secondary", command=save_snapshot)
btn6.grid(row=0, column=5, padx=5)

# Panel for image/video
panel = tk.Label(root, bg="black")
panel.pack(fill="both", expand=True, padx=10, pady=10)

# Status bar
status = tb.Label(root, text="✅ Model Loaded", anchor="w")
status.pack(side="bottom", fill="x")

root.mainloop()

# Clean up
if cap:
    cap.release()
cv2.destroyAllWindows()

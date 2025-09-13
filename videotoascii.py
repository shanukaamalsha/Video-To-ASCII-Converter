import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import cv2
import os
import time

ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(frame, width=100):
    height, old_width = frame.shape
    aspect_ratio = old_width / height
    new_height = int(width / aspect_ratio / 2)
    resized = cv2.resize(frame, (width, new_height))
    ascii_frame = ""
    for row in resized:
        for pixel in row:
            ascii_frame += ASCII_CHARS[int(pixel / 256 * len(ASCII_CHARS))]
        ascii_frame += "\n"
    return ascii_frame

class AsciiVideoPlayer(tk.Toplevel):
    def __init__(self, master, video_path, width=100):
        super().__init__(master)
        self.title("Video to Ascii Convertor")
        self.geometry("900x600")
        self.configure(bg="#181818")
        self.resizable(True, True)

        self.text = tk.Text(self, font=("Consolas", 7, "bold"), bg="#181818", fg="#f8f8f2", wrap=tk.NONE)
        self.text.pack(expand=True, fill=tk.BOTH)
        self.text.config(state=tk.DISABLED)

        self.stop_playback = False
        self.play_thread = threading.Thread(target=self.play_ascii_video, args=(video_path, width), daemon=True)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.play_thread.start()

    def play_ascii_video(self, video_path, width=100):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            messagebox.showerror("Error", "Error opening video file.")
            self.destroy()
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = 1 / fps if fps > 0 else 0.04

        try:
            while not self.stop_playback:
                ret, frame = cap.read()
                if not ret:
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                ascii_art = frame_to_ascii(gray, width)
                self.text.config(state=tk.NORMAL)
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, ascii_art)
                self.text.config(state=tk.DISABLED)
                self.update_idletasks()
                time.sleep(delay)
        except Exception:
            pass
        finally:
            cap.release()

    def on_close(self):
        self.stop_playback = True
        self.destroy()

class VideoToAsciiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video to ASCII Converter")
        self.geometry("500x300")
        self.configure(bg="#222831")
        self.resizable(False, False)
        self.file_path = None

        self.label = tk.Label(self, text="Click below to select your video file", bg="#222831",
                              fg="#ffd369", font=("Arial", 14))
        self.label.pack(pady=30)

        self.select_btn = tk.Button(self, text="Select Video File", font=("Arial", 12, "bold"),
                                    bg="#393e46", fg="#eeeeee", command=self.browse_file)
        self.select_btn.pack(pady=10)

        self.file_label = tk.Label(self, text="No file selected", bg="#222831", fg="#eeeeee", font=("Arial", 12))
        self.file_label.pack(pady=10)

        self.convert_btn = tk.Button(self, text="Convert", state=tk.DISABLED, font=("Arial", 12, "bold"),
                                     bg="#ffd369", fg="#222831", command=self.convert_video)
        self.convert_btn.pack(pady=20)

    def browse_file(self):
        ftypes = [("Video files", "*.mp4 *.avi *.mov *.mkv *.webm"), ("All files", "*.*")]
        file = filedialog.askopenfilename(title="Select Video File", filetypes=ftypes)
        if file:
            self.set_file_path(file)

    def set_file_path(self, path):
        self.file_path = path
        self.file_label.config(text=os.path.basename(path))
        self.convert_btn.config(state=tk.NORMAL)

    def convert_video(self):
        if not self.file_path:
            messagebox.showwarning("No File", "Please select a video file first!")
            return
        player = AsciiVideoPlayer(self, self.file_path)
        player.grab_set()

if __name__ == "__main__":
    app = VideoToAsciiApp()
    app.mainloop()
# 🎥 Video to ASCII Converter  

A simple yet fun Python application that converts and plays videos as ASCII art in real-time.  
This project uses **OpenCV** for video processing and **Tkinter** for the GUI interface.  

---

## ✨ Features  
- Select any video file (`.mp4`, `.avi`, `.mov`, `.mkv`, `.webm`, etc.).  
- Converts video frames into ASCII characters dynamically.  
- Adjustable ASCII resolution (default width = 100).  
- Real-time playback in a Tkinter window.  
- User-friendly GUI with file selection and playback controls.  

---

## 🖼️ Demo  
Watch a demo on how the Video is converted into ASCII (example representation):  

🌐 Youtube: https://youtube.com/shorts/THoSEthWGWU?si=Ffk1YIlVu9QELg9o

---

## ⚙️ Requirements  
Make sure you have Python **3.7+** installed, then install the dependencies:  

```bash
pip install opencv-python
```

*(Tkinter comes pre-installed with most Python distributions.)*  

---

## 🚀 How to Run  

1. Clone this repository:  
   ```bash
   git clone https://github.com/shanukaamalsha/Video-To-ASCII-Converter.git
   cd video-to-ascii
   ```

2. Run the script:  
   ```bash
   python videotoascii.py
   ```

3. Use the GUI to:  
   - Select a video file.  
   - Click **Convert**.  
   - Watch your video play in ASCII!  

---

## 🛠️ How It Works  
- **Step 1:** The app loads the selected video using OpenCV.  
- **Step 2:** Each frame is resized and converted to grayscale.  
- **Step 3:** Pixel intensities are mapped to ASCII characters (`@%#*+=-:. `).  
- **Step 4:** Frames are displayed as ASCII in a Tkinter text widget.  

---

## 📂 Project Structure  

```
video-to-ascii/
│
├── videotoascii.py   # Main script
├── README.md                                 # Project documentation
```

---


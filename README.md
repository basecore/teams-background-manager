<p align="center">
  <img src="image/readme-banner.png" alt="Teams Animated Background Manager Banner" width="100%">
</p>

# Teams Animated Background Manager 🎥✨

[![Python 3.x](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Made with AI](https://img.shields.io/badge/AI_Generated-Perplexity_%26_Gemini-blue?style=for-the-badge&logo=google)](https://github.com/basecore)

A powerful, local Python GUI application to customize, manage, and optimize animated video backgrounds for Microsoft Teams. Inject your own MP4s, fix aspect ratios, and compress massive video files with a single click to save bandwidth during your meetings.

<p align="center">
  <img src="image/screenshot1.png" alt="App UI Screenshot" width="45%">
  &nbsp;&nbsp;&nbsp;
  <img src="image/screenshot2.png" alt="Video Editor Screenshot" width="45%">
</p>

## ✨ Features (v12.0.0)

- 🎥 **Inline Video Preview:** No extra pop-ups! Click any active background thumbnail to instantly play the video animation directly inside the app. Click again to stop.
- ⚡ **Smart Auto-Optimization (Auto-Opt):** 1-click downscaling to 480p and 15 fps. Compresses massive 17 MB+ videos down to <2 MB to save network traffic during calls. Safely aborts and reverts if the output would become larger.
- 🛠️ **Advanced OpenCV Video Editor:** Got a video with the wrong format? The built-in editor fixes it instantly:
  - **Crop / Zoom:** Fills the screen and cuts off edges.
  - **Zoom In:** Extra 25% zoom to remove hardcoded black bars from downloaded videos.
  - **Pad:** Adds cinematic black borders to fit the entire original video into a 16:9 frame.
  - **Stretch:** Distorts the image to perfectly fill 16:9.
- 🛡️ **Auto-Backup & 1-Click Restore:** The app silently backs up original files. Hit “Delete / Reset” and Teams will automatically restore its default video.
- ⚠️ **Size Analysis & Traffic Warnings:** Automatically reads video metadata (resolution + MB). Warns visually if a file is heavy (>5 MB 🟠) or critical (>10 MB 🔴).
- 📦 **Zero-Config Dependencies:** Just run the script! If modules like `customtkinter`, `opencv-python` or `pillow` are missing, the script auto-installs them via `pip` and restarts itself.
- 🌍 **Bilingual UI:** Switch seamlessly between 🇩🇪 German and 🇬🇧 English.
- 🚀 **Fast Teams Restart:** Built-in button to kill and relaunch the Teams process immediately to apply injected backgrounds.

---

## 💻 System Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10 / 11 |
| **Python** | Python 3.x (check “Add Python to PATH” during install) |
| **Teams** | New Microsoft Teams Client |
| **Tested with** | Teams Version `26093.415.4620.1935` (May 2026) |

---

## 🚀 How to Use

### 1. Installation

Clone this repository or simply download `Teams_Manager_v12_0_Komplett.py`:

```bash
git clone https://github.com/basecore/teams-background-manager.git
cd teams-background-manager
python Teams_Manager_v12_0_Komplett.py
```

> On the very first launch, the console will briefly appear to auto-install `customtkinter`, `opencv-python`, `pillow`, `psutil` and `numpy` via pip.

### 2. Workflow

1. The app automatically scans your hidden Teams `Backgrounds` folder.
2. Find a background you want to replace (e.g. “Animated feeling dreamy”) and click **Ersetzen / Replace**.
3. Select your custom `.mp4` file.
4. **Check the file size!** If a warning appears (⚠️), click **⚡ Auto-Opt** to compress it automatically, or use the **🎥 Editor** to fix aspect ratio issues (black borders, wrong crop).
5. Click the thumbnail to **preview the animation inline** — directly in the app, no pop-up needed.
6. Click **🚀 Teams Neustart** on the sidebar to restart Teams and apply the change.
7. In Teams, open your camera effects and select the original-looking preview image — your custom video will now play!

> 💡 **Note:** Microsoft Teams caches static preview thumbnails. The thumbnail in the Teams UI won’t change visually, but your custom video will play correctly when you select it.

---

## 💡 Ideas & Future Features

- [ ] Drag & Drop support for video files
- [ ] GIF to MP4 auto-conversion
- [ ] Batch optimization of all videos at once
- [ ] Video trimming (set custom start/end point)
- [ ] Preview of frame-accurate thumbnail at any timecode
- [ ] Auto-detect and warn about videos with burned-in black bars
- [ ] Export optimized video back to a chosen folder

---

## 🛠 Technical Details

Built in pure **Python**. The UI uses **CustomTkinter** for a modern, dark-mode compatible interface.
Video processing (frame extraction, resolution scaling, padding, cropping, inline player) is powered by **OpenCV (`cv2`)** and **NumPy**.
Image caching and base64 thumbnail decoding is handled by **Pillow (PIL)**.

The app maps internal base64-encoded preview images to the cryptic alphanumeric filenames Microsoft uses in:
```
%LOCALAPPDATA%\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams\Backgrounds
```

---

## 🤖 Credits

- **Developer:** [basecore](https://github.com/basecore)
- **AI Assistance:** Logic, OpenCV video processing, UI layout, auto-install routines and inline video player were engineered with **Perplexity AI** and **Gemini 3.1 Pro**.

---

> **Disclaimer:** This project is not affiliated with or endorsed by Microsoft. It is a local file-management tool for personal use only. Modifying app cache files is done at your own risk.

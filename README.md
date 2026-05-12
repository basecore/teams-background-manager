<p align="center">
  <img src="image/readme-banner.png" alt="Teams Animated Background Manager Banner" width="100%">
</p>

<h1 align="center">Teams Animated Background Manager 🎥✨</h1>

<p align="center">
  A local Windows utility to replace, preview, optimize, and manage animated Microsoft Teams backgrounds.
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x">
  </a>
  <a href="https://opencv.org/">
    <img src="https://img.shields.io/badge/OpenCV-Video_Processing-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  </a>
  <a href="https://github.com/basecore">
    <img src="https://img.shields.io/badge/AI_Assisted-Perplexity_%26_Gemini-blue?style=for-the-badge&logo=google" alt="AI Assisted">
  </a>
</p>

<p align="center">
  <img src="image/screenshot1.png" alt="Main App Screenshot" width="46%">
  &nbsp;
  <img src="image/screenshot2.png" alt="Video Editor Screenshot" width="46%">
</p>

---

## Contents

- [What this app is](#what-this-app-is)
- [Why it exists](#why-it-exists)
- [Features](#features)
- [Tested environment](#tested-environment)
- [Installation & Execution](#installation--execution)
- [How to use](#how-to-use)
- [How it works](#how-it-works)
- [Security and transparency](#security-and-transparency)
- [Known limitations](#known-limitations)
- [Credits](#credits)
- [Disclaimer](#disclaimer)

---

## What this app is

**Teams Animated Background Manager** is a local desktop utility for Windows that helps users replace built-in animated Microsoft Teams background videos with custom MP4 files.

It is designed to make this process easier, safer, and more transparent than manually browsing hidden cache folders inside Windows.

---

## Why it exists

Microsoft Teams includes built-in animated backgrounds, but there is currently no simple official workflow for assigning your own custom MP4 animated backgrounds in the same way.

This tool uses a **local replacement approach**:
- it identifies the Teams animated background cache files,
- lets you replace selected built-in MP4 files with your own video,
- and helps keep those files small and practical for meetings.

> **Important:** The static preview thumbnail shown inside Microsoft Teams usually stays the same. Teams still shows the original built-in image even when the underlying video file has been replaced.

---

## Features

- 🎬 **Inline preview player:** Click the thumbnail of the Current Video inside the app to play or stop the animation directly in place.
- ⚡ **Auto optimization:** Large videos can be reduced automatically by lowering resolution and/or frame rate.
- 🛠 **Built-in video editor:** Includes Crop/Zoom, Zoom In, Pad (Add Black Borders), and Stretch.
- 🛡 **Reset and restore:** Revert custom replacements so Teams falls back to its original default animation.
- ⚠ **File size warnings:** Visual indicators for videos that may be too large (>5MB / >10MB).
- 🌍 **Bilingual UI:** Fully supports English and German.
- 🚀 **Teams restart:** Stop and restart Teams instantly to apply the new background.

---

## Tested environment

| Item | Value |
|---|---|
| Operating System | Windows 10 / 11 |
| Microsoft Teams | New Microsoft Teams |
| Tested version | `26093.415.4620.1935` |
| Verification date | May 12, 2026 |

Because Microsoft may change internal paths and file handling in future releases, compatibility with later versions cannot be guaranteed.

---

## Installation & Execution

This application runs purely as a Python script. This ensures 100% transparency of the source code and bypasses strict corporate AppLocker policies that usually block unknown `.exe` files.

### Requirements
Ensure **Python 3.x** is installed on your system.

### Standard Execution (Terminal)
Clone the repository or download the source code, open a terminal in the folder, and run:
```bash
python Teams_Manager_v12_0_Komplett.py
```
*(On the very first launch, the script will automatically install required dependencies like `customtkinter`, `opencv-python`, and `pillow` via pip).*

### Enterprise Execution (The `.bat` Workaround)
If you don't want to use the terminal every time, you can create a simple Windows Batch file to launch the app like a normal desktop application:

1. Place `Teams_Manager_v12_0_Komplett.py` in your preferred folder.
2. Right-click inside the folder -> **New** -> **Text Document**.
3. Name it `Start_TeamsManager.bat` (ensure the `.txt` extension is removed).
4. Open the file in Notepad and paste the following line:
   ```cmd
   pythonw Teams_Manager_v12_0_Komplett.py
   ```
5. Save and close. Double-click the `.bat` file to launch the GUI application silently without keeping a black console window open.

---

## How to use

1. Start the application.
2. Let it scan the local Teams animated background folder.
3. Select one of the built-in animated background slots.
4. Click **Replace** and choose your custom MP4 file.
5. If the video is too large, use **Auto-Opt.** or open the **Editor**.
6. Click the **Current Video** thumbnail to preview the animation inline.
7. Click **Teams Restart** to reload the Teams client.
8. In Microsoft Teams, select the original built-in animated thumbnail that corresponds to the replaced slot.

---

## How it works

The app operates locally on the user machine.

### Main local folder used
```text
%LOCALAPPDATA%\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams\Backgrounds
```

### Local backup/reset folder
```text
%USERPROFILE%\Teams_Background_Backups
```

---

## Security and transparency

This project is designed as a **local-only utility**. It is intended to be transparent and auditable, especially for use on work computers where trust matters.

### What the app does
- Reads and writes local MP4 files in the Teams background cache folder.
- Processes local video files with OpenCV.
- Can terminate and restart the local Teams process to apply changes.
- Stores local backup copies in the user profile.

### What the app does **not** do
- No custom cloud backend communication.
- No user tracking, telemetry, or analytics.
- No credential collection.
- No persistence mechanisms or autorun installation.

Because it runs directly from the `.py` source code, internal IT or endpoint protection tools can review the exact operations being performed at any time. 

---

## Known limitations

- The preview thumbnail inside Microsoft Teams itself cannot reliably be changed.
- The tool depends on internal Teams cache behavior, which Microsoft may change in future versions.
- Some video optimizations trade quality for a smaller file size.

---

## Credits

- **Developer:** [basecore](https://github.com/basecore)
- **AI Assistance:** Perplexity AI and Gemini 3.1 Pro

---

## Disclaimer

This project is **not affiliated with or endorsed by Microsoft**.

It modifies local Microsoft Teams cache files on the user’s machine. Use it only if this is permitted by your company policy and internal IT/security rules. Use at your own risk.

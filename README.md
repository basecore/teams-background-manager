<p align="center">
  <img src="image/readme-banner.png" alt="Teams Animated Background Manager Banner" width="100%">
</p>

<h1 align="center">Teams Animated Background Manager 🎥✨</h1>

<p align="center">
  A local Windows desktop app to replace, preview, optimize, and manage animated Microsoft Teams backgrounds.
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x">
  </a>
  <a href="https://opencv.org/">
    <img src="https://img.shields.io/badge/OpenCV-Video_Processing-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  </a>
  <a href="https://www.pyinstaller.org/">
    <img src="https://img.shields.io/badge/Built_with-PyInstaller-5A3E85?style=for-the-badge" alt="PyInstaller">
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
- [Installation](#installation)
- [How to use](#how-to-use)
- [How it works](#how-it-works)
- [Security and transparency](#security-and-transparency)
- [Python modules used](#python-modules-used)
- [Building the EXE](#building-the-exe)
- [VirusTotal verification](#virustotal-verification)
- [Known limitations](#known-limitations)
- [Roadmap ideas](#roadmap-ideas)
- [Credits](#credits)
- [Disclaimer](#disclaimer)

---

## What this app is

**Teams Animated Background Manager** is a local desktop utility for Windows that helps users replace built-in animated Microsoft Teams background videos with custom MP4 files.

It is designed to make this process easier, safer, and more transparent than manually browsing hidden cache folders inside Windows.

The app can:
- detect the Teams animated background folder,
- show previews of current and original backgrounds,
- replace built-in animated background videos,
- optimize large video files,
- preview animations inline,
- and restore/reset changes.

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

### 🎬 Inline preview player
Click the thumbnail of the **Current Video** inside the app to play or stop the animation directly in place.

### ⚡ Auto optimization
Large videos can be reduced automatically by lowering resolution and/or frame rate.  
If the optimized result would become larger than the original, the app aborts the save and keeps the original file.

### 🛠 Built-in video editor
The integrated editor includes:
- **Crop / Zoom** — fills the frame and removes outer edges
- **Zoom In** — extra zoom to remove hardcoded black bars
- **Pad / Add Black Borders** — fits the entire video into 16:9 with borders
- **Stretch** — stretches the image to match 16:9 exactly

### 🛡 Reset and restore behavior
The app supports resetting custom replacements so Teams can fall back to its original default/cached animation again.

### ⚠ File size warnings
The interface highlights videos that may be too large for practical use:
- medium warning for larger files,
- critical warning for very large files.

### 🌍 Bilingual UI
The interface supports:
- German
- English

### 🚀 Teams restart
The app can stop and restart Teams so the new background file is picked up faster.

---

## Tested environment

| Item | Value |
|---|---|
| Operating System | Windows 10 / 11 |
| Microsoft Teams | New Microsoft Teams |
| Tested version | `26093.415.4620.1935` |
| Verification date | May 11, 2026 |

Because Microsoft may change internal paths and file handling in future releases, compatibility with later versions cannot be guaranteed.

---

## Installation

### Option A — Run from Python source

Clone the repository and run the script directly:

```bash
git clone https://github.com/basecore/teams-background-manager.git
cd teams-background-manager
python Teams_Manager_v12_0_Komplett.py
```

> On some development builds, the script may auto-install required dependencies if they are missing. For enterprise deployment, a prebuilt EXE is usually the better option.

### Option B — Use the packaged EXE

Download the EXE from the project release section and run it directly on Windows.

For enterprise/work PCs, a reviewed internal build is recommended.

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

> **Note:** The image shown in Teams may still look like the original Microsoft preview, even though the underlying animated video is now your custom file.

---

## How it works

The app operates locally on the user machine.

### Main workflow
1. Detect the Teams background cache path.
2. Identify known animated background filenames.
3. Show both:
   - the currently active local file,
   - and the original preview reference.
4. Replace the selected Teams MP4 with a custom MP4.
5. Optionally optimize that file with OpenCV.
6. Restart Teams so the replacement becomes active more quickly.

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

This section is intentionally detailed, because the app may be used on work computers and should be easy to review.

### What the app does
- Reads files from the local Teams animated background folder.
- Writes and replaces local MP4 files in that folder.
- Reads video metadata such as file size, resolution, and frames.
- Processes local video files with OpenCV.
- Can terminate and restart the local Teams process.
- Stores local backup/reset data in the user profile.

### What the app does **not** do
- No custom cloud backend communication.
- No user tracking or analytics.
- No telemetry.
- No ads.
- No credential collection.
- No keystroke logging.
- No browser data extraction.
- No scheduled tasks.
- No persistence mechanism.
- No autorun installation.
- No hidden service.

### Is this a security risk?
The app is **not intended as malware**, but it does have capabilities that security software may inspect carefully:
- modifying files in `%LOCALAPPDATA%`,
- replacing cached application media,
- terminating/restarting a user application,
- bundling Python and dependencies into an EXE.

That does **not** automatically make it dangerous, but it does mean the binary may require explanation, review, or whitelisting in enterprise environments.

### Honest risk assessment
Potential concern areas to review in source code:
- file write/delete operations,
- process management,
- runtime dependency installation in developer builds,
- packaging behavior of PyInstaller,
- false positives from unsigned EXEs.

### Recommendation for company use
For internal/company deployment, the most trustworthy workflow is:
- review the Python source code,
- build the EXE internally,
- publish SHA256 hashes,
- check the EXE in VirusTotal,
- optionally sign the EXE,
- optionally have internal IT/security whitelist the release.

---

## Python modules used

| Module | Purpose |
|---|---|
| `customtkinter` | Modern GUI on top of Tkinter |
| `Pillow` | Image loading, resizing, thumbnail rendering |
| `opencv-python` (`cv2`) | Video reading, frame extraction, scaling, crop, pad, stretch, preview |
| `numpy` | Array processing for frames and image data |
| `psutil` | Teams process detection, stop, restart |
| `pathlib` | Safer Windows path handling |
| `shutil` | Copy, replace, delete files |
| `threading` | Background tasks without freezing the UI |
| `base64`, `io` | Embedded preview image handling |
| `datetime`, `time`, `os`, `sys` | Standard runtime and file/process helpers |

### Why these modules are needed
- **OpenCV** is required for video processing and frame-based editing.
- **Pillow** is used for image handling and thumbnails.
- **psutil** is used to restart Teams reliably.
- **customtkinter** provides the modern desktop interface.
- **numpy** supports efficient frame manipulation for OpenCV.

---

## Building the EXE

This project can be packaged into a Windows executable using **PyInstaller**, which bundles Python together with the required libraries [page:1].

### Recommended build for work environments

For enterprise or office PCs, `--onedir` is usually preferable because single-file packaging can trigger antivirus heuristics more often [page:2].

```bash
pip install -U pyinstaller
pyinstaller --clean --noconfirm --windowed --onedir --name "TeamsBackgroundManager" --icon app.ico Teams_Manager_v12_0_Komplett.py
```

### Single-file build

```bash
pip install -U pyinstaller
pyinstaller --clean --noconfirm --onefile --windowed --name "TeamsBackgroundManager" --icon app.ico Teams_Manager_v12_0_Komplett.py
```

### Meaning of the build flags
- `--clean` removes old build cache before packaging [page:1]
- `--noconfirm` overwrites previous build folders without asking [page:1]
- `--windowed` creates a GUI app without a console window [page:1]
- `--onedir` creates a folder-based build [page:1]
- `--onefile` creates a single EXE file [page:1]
- `--icon` assigns a custom Windows executable icon [page:1]

### Enterprise note
Unsigned PyInstaller binaries can trigger SmartScreen or antivirus false positives, especially in `--onefile` mode, because the packaging/extraction behavior can look suspicious heuristically [page:2]. For company rollout, signed builds and internal whitelisting are recommended [page:2].

---

## VirusTotal verification

To improve trust, every public EXE release should be checked manually with VirusTotal before distribution.

### Release scan record

Fill this section in after uploading your EXE:

| Field | Value |
|---|---|
| Version | `v12.0.0` |
| Build type | `PyInstaller onedir` / `PyInstaller onefile` |
| SHA256 | `PASTE_HASH_HERE` |
| VirusTotal URL | `PASTE_LINK_HERE` |
| Detection ratio | `PASTE_RESULT_HERE` |
| Scan date | `PASTE_DATE_HERE` |

### Suggested interpretation
- `0/x` is the ideal result.
- A few heuristic detections can happen with packaged Python applications and do not automatically prove malicious behavior [page:2].
- Any detection should still be reviewed carefully before deployment.

---

## Known limitations

- The preview thumbnail inside Microsoft Teams itself cannot reliably be changed.
- The tool depends on internal Teams cache behavior, which Microsoft may change in future versions.
- Some optimizations trade video quality for smaller file size.
- Some enterprise endpoint security tools may still warn about unsigned EXEs.
- Developer builds that auto-install dependencies may be less suitable for locked-down workstations.

---

## Roadmap ideas

- Drag & Drop support
- GIF to MP4 conversion
- Batch optimization for all backgrounds
- Trim start/end of video
- Better black-bar detection
- Export optimized video to separate folder
- Signed enterprise release workflow
- Published checksum file for every release

---

## Credits

- **Developer:** [basecore](https://github.com/basecore)
- **AI Assistance:** Perplexity AI and Gemini 3.1 Pro
- **Packaging:** PyInstaller [page:1]

---

## Disclaimer

This project is **not affiliated with or endorsed by Microsoft**.

It modifies local Microsoft Teams cache files on the user’s machine.  
Use it only if this is permitted by your company policy and internal IT/security rules.

Use at your own risk.

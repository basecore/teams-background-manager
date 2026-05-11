import os
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import time
import base64
import io
import threading
import math

def install_requirements():
    try:
        import customtkinter as ctk
        from PIL import Image, ImageTk, ImageDraw
        import psutil
        import cv2
        import numpy as np
    except ImportError:
        print("Installiere benoetigte Module...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "pillow", "psutil", "opencv-python", "numpy"])
        os.execv(sys.executable, ['python'] + sys.argv)

install_requirements()

import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image, ImageDraw
import psutil
import cv2
import numpy as np

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

IMAGE_B64 = {
    "thumb_dreamy2.jpg": "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",
    "thumb_dreamy4.jpg": "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",
    "thumb_dreamy5.jpg": "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",
    "thumb_dreamy7.jpg": "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",
    "thumb_lights.jpg": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA0JCgsKCA0LCgsODg0PEyAVExISEyccHhcgLikxMC4pLSwzOko+MzZGNywtQFdBRkxOUlNSMj5aYVpQYEpRUk//2wBDAQ4ODhMREyYVFSZPNS01T09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0//wAARCABsAMADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDziS7nltkt5ZpHij+4hY7V9cCoSCADxzRgkZAOBxmkoQ277hTjnYOQR/L/ADikUFmAHf8ACpJVzmRVfZnBLc849aA6EX4UED1p4UeWx2knggg8Ae9NBAIJAI9D3oCw6HmQLgHccckD9T0+tIcxsynGeh6GnEoAQhLZUZ3ADB9qZjNAEjEtbpkIFDEZBG78qYCy8g4yOx7dKCAuMMGyO3agqUYrIrAjIx0INAPUbSkgn7uOvShlACkMDkZwO1KF3OqxgszHAXGefT3oEEbsjAqxHPatO7trf+zo7mJ41LYBjD5Oe5xWWR0yKkm5kCqu0YHG7POB3qZK7RtCfLFpotxzWYsJInjLTHlH6Y9aosdwHAwOOKkkt5Ip2hbbvXOcMMcdeajZXifDBlYfgaIpIVSbla62EA56496OuB3pWDKAD0YZ4OaFbbnjORjpVGQ2jtTt2RnIBHAAGMijcxUJ2BJHH+fSgAXg9T07U3pxV3Tp5LHUFeJUldWwFK5DduhqvcI6SsZF2sScjGMVN9bF8vu3O38FeLNM0XRpbW7hfzd5YMq538cA1xN3IJ7mWZECI7kqo6D2qGlAyQOn1pRpqLbXUTldWNLVtOfTbhWjY7G5jYcEf/XqslvG1hJOZCHVgAuOuf8AJplzPPLgTSlxjIBbOKi3/JtJOOO9EVLlV3qaSlDmdloLCnmSKm9U3EDLHAFLcIIpmjDI23jKHINMBGDkc44waSrMrqw9VBXBBDMRtycDFMIxTsHb14POKbxQIkhCFiHBIxnhgP5+2ab8oPAyMd6QYKnnBH60Cgd9BRgqRj5s5znFK8sjoqMxIQYUegzmmAkHIODRQFye3tp55BFChZnHA9abNBJA5SVWVx1BHSrun3159sg8tgzouxN2OBUeqXc89232gASplGxis05c1uhtKEPZ8yepTUglQ7ELnnAzj8KbSjGeelO8uQw+ZsPlg43Y4z9a0MLjTn72c5PrzTnZ5CC+WZu5703JVuD0PBFB68DFA7iqpdtqgljwAB1pCMdsZ6VJG0fkyIynccFSMHGM8f5P50kLiKRZCqvg52nNAWCFo0kVpI/MUdVzjP41s6fqWl2/hy9tLiw8y+mYGKbd93/9XP1zWWk4MshfKJLncEH44/PFV+OeM+lJ+8rMrSOqL2k3UNnfJPNGZAhBA6Vd8TavBq9wksFsIggwx9f881hjPalJycnvU+zjzc3Ur2r5OQSnEL5YIzuzg8ce3P50hBAGe9GTjFWZEk0LW80kUoAkjOCM5GRUagswA70rsXYsxJY9SaEZkbcpIPrSK0v5Fi7tDbSPEShaPhirghvpVcKWIA61r6bc6ZDpN6t9aPNcyKBbyBsBD/k1Utrm3VD5sSs4Tavy8ck8n1PNSpNdDVwjJ72KwGQiN8gJ++c9P8Bjt71ERg1LOAkrKsgdRxlc4P51GATwB0qzGSs7CquSQQeAc84xTaUAk9CfpSt1OFx2oAbTgjldwU7fXHFNrUt9Xnh0K501Eh8qZlZiU+bj0NJtrYaV9ygZW+zogk4ViQoHI6c/59KbGpdiflO0bjuYDI/HvSxRiRiu7Bxxx1PpTNuG2n5TnBz2qrW1Jv0E78VIZXEIiEh2H5ivYGmAZOKTHeluFhQcHI7etadjPp8WkXqXNqZbp9ohk3Y2Gss075icDuAMDvSlG5UZWLemu0cztHKkZ8thlxkHjpVVxglcDIJ5B60kbmNicA8EYI9qfukSHbkbJMHsTxn8u9FtblcycUmad3b6dFoFs4nkfUC2GjJBVU5PHp/9c1kAZycgAetKSNuBz05PUUnGOAc0oq24ptSegA4NPgVZJkSR9iE8tjOB64pqKznCKWOCcAZ4AyTSDAPIP51RK0dySZUjmkSJhIgOFfGMj1pgO1gdoODnB71Z064hguo2uYRLCHBdeMkDtntUmsXNndanPNZWxt7dj+7j3Z2/55qU3exTStcpBsAAjIBzj1qaSRZ1VRGFKjC7e/1qvWkl/apoT2P2FDctLvFzn5lHpRIIvRorSweXC6yvtnhcq0RXp+P17VCkckpbYpYquTgdAO9NDFWBGM+4zSsrIcMCpIzz3FUS9dgOS3zH0560oCu4yVjB4J5wPekQncoUZ54HXJ+lX5bW3Gjxzi7Qzbj+5xyPU/ypN2HGLeqJNBazh1ONr35oxg5HQVY8R3GnNfLJpa7cHJ9M/SsUDKtJuUEEfL0Jz6UPIWZiBtVjnaDxWbp3nz3NFVtT5bCtIAGWMYVsZzgmlSZlt5IgSFkIJHY4zSDyfs7Z3+duGP7uO9SLcKtm0HkRlmYN5hHzD2+laGa13IAM9KOMY6+9KjtGcoxU+o60AFtoGM9B2pkkkEqxK+5Msy4U+lIZAkweFcAYOHwwJ+mMEe1MYfM2TgjtQyFVUkr8wyMEH/8AVSsU5O1hFALDJwO59Kkt0aWZYo8b2YBWJxioqfGrM+FwCATycU3sKO5veIvDv9j2Fldm7jmN0udqjG04/wA81hQgtNGgZVywwX+6Pc+1SSSSSwgyysQpxgn247//AKqr1EE0tWVNrm0DvirUlvdWPlyTwNH5qbk8xfvKR1Gf51WAJBIBwOtTXV3Nd+X5zlvLQIoJJwBVO4la1yCl4OOo9aSnKNxwCB9TTJNCw0W81F5VtowPKi81g7AHbjqKzmGDgEH3p6TOgYAn5hg80zrk/iaSvfUqXL0Ep2w7A3GCcdefy/Gm05ACwGDye1MkGAXGDmlVlZwZtxAHY800bdrZzntRxg5J9uKB3FK4CkMDkZOM8f5/rTaUsxAyScDAz2pVG9gGYLx1agBzx7UVmKncOApHH1pgzjPagc9SB9afMiIyhX3AqCTjoSOlILX1Q3IIAxwOtIzFjk+mKVsFjzx7CkA6+1MBcA52nIAyc8U5XT5t4J4OMY6+5qMAk4FOQMx2rnLcYHegEKoj8xQ7HZxuKjJ/KmnqQOR9KsXVlc2LR/aIzGZFDpnuPWoUZtwxyV5AxkUKzG01oxGILFlUKD2HQfnRFI0UiyIcMpyKVVDbsn5uwx1pu35iAQcfhQLbUdIzSOZH6sck4plSSNvAwFRQBhQSeeAT9TjNMDEIVHQkE0A9x3HzEZBzwOvHv+lNJBJIGPapI5GQsivtWQbWJ54yDUR60A7CkYPXNCoWJx2GetJ0PFOd2d2ZiSWOSTQARsFfcd3HI2nBB7VLbQz3Uwgtwzu/AUHt1qOKTyn3BQTjHOaIpDE4dCQwpO/QI2vqEXllsS5xg42+uOKGfcirtHygjIHXmmCimF9A7e9OBX5s9xxxnvSAkYI49DUkaJJMqtLtU4yxHSgEgSNG3EybQFyMjqfSmyFckJ90HgkcmgthCg2kEg5xzTc7WBQkEYIPTBoB7WEpRuwduenOPSm07J+9nmgRNZW32u7jtxIke843OcAUXEZtpZIRKGIYqxQ5Vsdwe9QAkcinEFQDkfMM8H8KWtyrq3mNp0btFIskbFWU5BHUGm04kFe+BgDJ6UxInvLqe7kHnTvOV+VScniq+cdD9aFYqwIJBByCKCRzgcZ4yeRQkktAbbd2GTx6irNjb/bb+K3aeOLznCmWQ8LnuTUESK7EM4QAE5Pc46U04GME579sUmGxNe24tLya3EqS+W5XfGcq2O4PpUcZQOPNBKdwDg01WKnIx+IzSU0F+ooJGQDjI596CS3JJPbmgEqcj6UpTAQ7l+YZ+nOOaBE8VvKbN7jylaENgsT0OPz7iq1WI4x5BkkkAXPCZwX55x/iaijTe4VeSSAB60kXJbDCScZPSlBwTxmlYAMRgjnjnpTSSTk9aZAvIHTg80lLk4Azx6UsQDSKp6EgUDAuzKqFiVXO0Z4GaBlRnsfapr+JIbySOMYUYwPwqvQDVnYlR4hDKrxbpGxscNjb68d81GFJBIxgdeaCcnJx0xwMUlAgzzxxSUUueKAFHzHkgcUDGeckUmaSgB+8hCnGCc9Bn86Nq7chuccgj+VNp8oAfAGBtB/SgY3OQB6UAZOKlaNRaJLzuZ2U+mAB/jSnNtNG8RIbYGyeeoprViegzBXKCRcHnrweKSSQuADjA/2QD0H+FMNFJrUdwqa2RZZgksojQ9WbJAwOKhooBOz1HOSTyxOOB9KTvxzSrwTwDSKSDwcUIH3EHv0pc/KBgcEnNJQTkk0CClJp20eUW7hsVHQB/9k=",
    "thumb_sparkles.jpg": "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"
}

LANG = {
    "DE": {
        "title": "Teams Animated Background Manager",
        "logo": "Teams Video\nManager",
        "refresh": "🔄 Liste aktualisieren",
        "open_folder": "📂 Teams-Ordner öffnen",
        "restart_teams": "🚀 Teams Neustart",
        "lang_switch": "🇬🇧 Switch to English",
        "status_ready": "Status: Bereit",
        "status_refreshed": "Liste aktualisiert",
        "status_folder_not_found": "Ordner nicht gefunden!",
        "status_saved": "Original gesichert!",
        "status_already_saved": "Original existiert bereits.",
        "status_save_failed": "Backup fehlgeschlagen",
        "status_replaced": "Video erfolgreich ersetzt!",
        "status_replaced_missing": "Video erfolgreich ersetzt!",
        "status_replace_failed": "Fehler beim Ersetzen",
        "status_restored": "Original wiederhergestellt!",
        "status_deleted": "Eigenes Video gelöscht (Teams stellt Original wieder her)",
        "status_restore_failed": "Fehler beim Wiederherstellen/Löschen",
        "status_restarting": "Teams wird neugestartet...",
        "status_started": "Teams gestartet",
        "status_restart_manual": "Neustart manuell nötig",
        "status_optimizing": "Optimiere Video... (bitte warten)",
        "status_optimized": "Video erfolgreich optimiert!",
        "status_opt_aborted": "Optimierung bringt nichts (bereits optimal)",
        "contact": "Kontakt",
        "date": "Datum",
        "created_with": "Erstellt mit Gemini 3.1 Pro",
        "explanation": "Hinweis: Das Vorschaubild direkt in Teams ändert sich nicht, das neue Video wird aber dennoch abgespielt!\nOrientieren Sie sich an der 'Original Vorschau', um das richtige Bild in Teams auszuwählen.",
        "main_label": "Vorhandene und fehlende Teams Hintergründe",
        "file": "Datei",
        "size": "Größe",
        "warning_large": "⚠️ (Zu groß!)",
        "warning_medium": "⚠️ (Warnung)",
        "current_preview": "Aktuelles Video:",
        "original_preview": "Original Vorschau:",
        "no_original": "(Kein Original)",
        "unknown_bg": "Unbekannter Hintergrund",
        "btn_replace": "Ersetzen",
        "btn_restore": "Löschen / Reset",
        "btn_editor": "🎬 Editor",
        "btn_auto_opt": "⚡ Auto-Opt.",
        "dialog_title": "Neues Video auswählen",
        "dialog_video": "Video",
        "dialog_all": "Alle",
        "editor_title": "Video Check & Optimierung",
        "editor_info": "Größe: {size:.1f} MB | Auflösung: {w}x{h}\nIst das Video zu groß oder nicht im 16:9 Format, kann es in Teams stören.\nHier kannst du es bei Bedarf optimieren:",
        "editor_zoom": "Zuschneiden / Zoom (Ränder ab, volles Bild)",
        "editor_zoom_in": "Heranzoomen (Entfernt fest einkodierte Ränder)",
        "editor_pad": "Schwarze Ränder (Ganzes Original einpassen)",
        "editor_stretch": "Strecken (Bild verzerren auf 16:9)",
        "editor_btn_opt": "Optimierung starten",
        "editor_btn_restore": "Import-Original laden",
        "editor_btn_cancel": "Schließen",
        "editor_processing": "Video wird optimiert ({percent}%)... Bitte warten."
    },
    "EN": {
        "title": "Teams Animated Background Manager",
        "logo": "Teams Video\nManager",
        "refresh": "🔄 Refresh List",
        "open_folder": "📂 Open Teams Folder",
        "restart_teams": "🚀 Restart Teams",
        "lang_switch": "🇩🇪 Auf Deutsch wechseln",
        "status_ready": "Status: Ready",
        "status_refreshed": "List refreshed",
        "status_folder_not_found": "Folder not found!",
        "status_saved": "Original saved!",
        "status_already_saved": "Original already exists.",
        "status_save_failed": "Backup failed",
        "status_replaced": "Video replaced successfully!",
        "status_replaced_missing": "Video replaced successfully!",
        "status_replace_failed": "Error during replacement",
        "status_restored": "Original restored!",
        "status_deleted": "Custom video deleted (Teams will auto-restore)",
        "status_restore_failed": "Error during restore/delete",
        "status_restarting": "Restarting Teams...",
        "status_started": "Teams started",
        "status_restart_manual": "Manual restart required",
        "status_optimizing": "Optimizing video... (please wait)",
        "status_optimized": "Video optimized successfully!",
        "status_opt_aborted": "Optimization brings no benefit (already optimal)",
        "contact": "Contact",
        "date": "Date",
        "created_with": "Created with Gemini 3.1 Pro",
        "explanation": "Note: The preview image inside Teams will not change, but your new video will still play!\nUse the 'Original Preview' as a guide to know which image you need to select in Teams.",
        "main_label": "Existing and missing Teams backgrounds",
        "file": "File",
        "size": "Size",
        "warning_large": "⚠️ (Too large!)",
        "warning_medium": "⚠️ (Warning)",
        "current_preview": "Current Video:",
        "original_preview": "Original Preview:",
        "no_original": "(No Original)",
        "unknown_bg": "Unknown background",
        "btn_replace": "Replace",
        "btn_restore": "Delete / Reset",
        "btn_editor": "🎬 Editor",
        "btn_auto_opt": "⚡ Auto-Opt.",
        "dialog_title": "Select new video",
        "dialog_video": "Video",
        "dialog_all": "All",
        "editor_title": "Video Check & Optimization",
        "editor_info": "Size: {size:.1f} MB | Resolution: {w}x{h}\nIf the video is too large or not 16:9, it might cause issues in Teams.\nYou can optimize it here:",
        "editor_zoom": "Crop / Zoom (Fill screen, cut borders)",
        "editor_zoom_in": "Zoom In (Removes hardcoded black bars)",
        "editor_pad": "Add black borders (Fit entire original)",
        "editor_stretch": "Stretch (Distort to 16:9 format)",
        "editor_btn_opt": "Start Optimization",
        "editor_btn_restore": "Load imported original",
        "editor_btn_cancel": "Close",
        "editor_processing": "Optimizing video ({percent}%)... Please wait."
    }
}

def create_editor_icon(mode):
    img = Image.new('RGB', (64, 36), color='#2b2b2b')
    d = ImageDraw.Draw(img)
    if mode == "pad":
        d.rectangle([16, 0, 47, 35], fill='#3498DB') 
    elif mode == "zoom":
        d.rectangle([0, -6, 63, 41], fill='#E74C3C') 
    elif mode == "zoom_in":
        d.rectangle([8, 6, 55, 29], fill='#E67E22') 
    elif mode == "stretch":
        d.rectangle([0, 0, 63, 35], fill='#9B59B6') 
        for i in range(5, 64, 10):
            d.line([(i, 0), (i, 35)], fill='#8E44AD', width=1)
    return ctk.CTkImage(light_image=img, dark_image=img, size=(64, 36))

class VideoEditorDialog(ctk.CTkToplevel):
    def __init__(self, parent, file_path, w, h, size_mb):
        super().__init__(parent)
        self.parent = parent
        self.file_path = file_path
        self.unopt_path = parent.backup_dir / f"unopt_{file_path.name}"

        l = LANG[parent.current_lang]
        self.title(l["editor_title"])
        self.geometry("600x520")
        self.resizable(False, False)
        self.grab_set() 

        info_text = l["editor_info"].format(size=size_mb, w=w, h=h)
        ctk.CTkLabel(self, text=info_text, justify="center", font=ctk.CTkFont(size=13)).pack(pady=15, padx=20)

        self.mode_var = ctk.StringVar(value="zoom")

        opts_frame = ctk.CTkFrame(self, fg_color="transparent")
        opts_frame.pack(fill="x", padx=40, pady=5)

        f_zoom = ctk.CTkFrame(opts_frame)
        f_zoom.pack(fill="x", pady=5)
        ctk.CTkRadioButton(f_zoom, text=l["editor_zoom"], variable=self.mode_var, value="zoom").pack(side="left", padx=15, pady=10)
        ctk.CTkLabel(f_zoom, image=create_editor_icon("zoom"), text="").pack(side="right", padx=15)

        f_zoom_in = ctk.CTkFrame(opts_frame)
        f_zoom_in.pack(fill="x", pady=5)
        ctk.CTkRadioButton(f_zoom_in, text=l["editor_zoom_in"], variable=self.mode_var, value="zoom_in").pack(side="left", padx=15, pady=10)
        ctk.CTkLabel(f_zoom_in, image=create_editor_icon("zoom_in"), text="").pack(side="right", padx=15)

        f_pad = ctk.CTkFrame(opts_frame)
        f_pad.pack(fill="x", pady=5)
        ctk.CTkRadioButton(f_pad, text=l["editor_pad"], variable=self.mode_var, value="pad").pack(side="left", padx=15, pady=10)
        ctk.CTkLabel(f_pad, image=create_editor_icon("pad"), text="").pack(side="right", padx=15)

        f_stretch = ctk.CTkFrame(opts_frame)
        f_stretch.pack(fill="x", pady=5)
        ctk.CTkRadioButton(f_stretch, text=l["editor_stretch"], variable=self.mode_var, value="stretch").pack(side="left", padx=15, pady=10)
        ctk.CTkLabel(f_stretch, image=create_editor_icon("stretch"), text="").pack(side="right", padx=15)

        self.progress_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(weight="bold"), text_color="#27AE60")
        self.progress_label.pack(pady=5)

        self.progress_bar = ctk.CTkProgressBar(self, width=450)
        self.progress_bar.set(0)

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=10)

        self.btn_opt = ctk.CTkButton(self.btn_frame, text=l["editor_btn_opt"], fg_color="#27AE60", hover_color="#1E8449", command=self.start_optimization)
        self.btn_opt.grid(row=0, column=0, padx=10)

        self.btn_restore = ctk.CTkButton(self.btn_frame, text=l["editor_btn_restore"], fg_color="#E67E22", hover_color="#D35400", command=self.restore_original)
        self.btn_restore.grid(row=0, column=1, padx=10)

        if not self.unopt_path.exists():
            self.btn_restore.configure(state="disabled", fg_color="gray")

        self.btn_cancel = ctk.CTkButton(self.btn_frame, text=l["editor_btn_cancel"], fg_color="gray", command=self.destroy)
        self.btn_cancel.grid(row=0, column=2, padx=10)

    def restore_original(self):
        if self.unopt_path.exists():
            shutil.copy2(self.unopt_path, self.file_path)
            if str(self.file_path) in self.parent.thumbnail_cache:
                del self.parent.thumbnail_cache[str(self.file_path)]
            self.parent.load_backgrounds()
            self.destroy()

    def start_optimization(self):
        self.btn_opt.configure(state="disabled")
        self.btn_restore.configure(state="disabled")
        self.btn_cancel.configure(state="disabled")
        self.progress_bar.pack(pady=5)
        self.progress_label.configure(text=LANG[self.parent.current_lang]["editor_processing"].format(percent=0))

        if not self.unopt_path.exists():
            shutil.copy2(self.file_path, self.unopt_path)

        mode = self.mode_var.get()
        threading.Thread(target=self.process_video, args=(mode,), daemon=True).start()

    def process_video(self, mode):
        temp_out = os.path.join(os.path.dirname(self.file_path), "temp_optimized.mp4")
        cap = cv2.VideoCapture(str(self.file_path))
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps == 0 or fps != fps: fps = 25.0
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(temp_out, fourcc, fps, (1920, 1080))

        # mode is passed via args
        count = 0

        while True:
            ret, frame = cap.read()
            if not ret: break

            h, w = frame.shape[:2]
            if mode == "zoom":
                scale = max(1920/w, 1080/h)
                new_w, new_h = int(w*scale), int(h*scale)
                resized = cv2.resize(frame, (new_w, new_h))
                start_x = max(0, (new_w - 1920) // 2)
                start_y = max(0, (new_h - 1080) // 2)
                final_frame = resized[start_y:start_y+1080, start_x:start_x+1920]
                if final_frame.shape[:2] != (1080, 1920):
                    final_frame = cv2.resize(final_frame, (1920, 1080))
            elif mode == "zoom_in":
                scale = max(1920/w, 1080/h) * 1.25
                new_w, new_h = int(w*scale), int(h*scale)
                resized = cv2.resize(frame, (new_w, new_h))
                start_x = max(0, (new_w - 1920) // 2)
                start_y = max(0, (new_h - 1080) // 2)
                final_frame = resized[start_y:start_y+1080, start_x:start_x+1920]
                if final_frame.shape[:2] != (1080, 1920):
                    final_frame = cv2.resize(final_frame, (1920, 1080))
            elif mode == "pad":
                scale = min(1920/w, 1080/h)
                new_w, new_h = int(w*scale), int(h*scale)
                resized = cv2.resize(frame, (new_w, new_h))
                final_frame = np.zeros((1080, 1920, 3), dtype=np.uint8)
                x = (1920 - new_w) // 2
                y = (1080 - new_h) // 2
                final_frame[y:y+new_h, x:x+new_w] = resized
            else: # stretch
                final_frame = cv2.resize(frame, (1920, 1080))

            out.write(final_frame)
            count += 1
            if count % max(1, int(total_frames/100)) == 0 and total_frames > 0:
                pct = int((count / total_frames) * 100)
                self.parent.after(0, self.update_progress, pct)

        cap.release()
        out.release()

        self.parent.after(0, self.finish_optimization, temp_out)

    def update_progress(self, pct):
        self.progress_bar.set(pct / 100.0)
        self.progress_label.configure(text=LANG[self.parent.current_lang]["editor_processing"].format(percent=pct))

    def finish_optimization(self, temp_out):
        orig_size = os.path.getsize(self.unopt_path)
        new_size = os.path.getsize(temp_out)

        if new_size > orig_size:
            # Re-compress with lower bitrate to ensure it's smaller, or just abort
            # We will abort the optimization and keep original if it grows
            self.parent.status_label.configure(text=LANG[self.parent.current_lang]["status_opt_aborted"], text_color="#E74C3C")
            try: os.remove(temp_out)
            except: pass
            shutil.copy2(self.unopt_path, self.file_path)
        else:
            shutil.copy2(temp_out, self.file_path)
            try: os.remove(temp_out)
            except: pass

        if str(self.file_path) in self.parent.thumbnail_cache:
            del self.parent.thumbnail_cache[str(self.file_path)]

        self.parent.load_backgrounds()
        self.destroy()




class InlineVideoPlayer(ctk.CTkLabel):
    def __init__(self, master, video_path, static_image, size=(192, 108), **kwargs):
        super().__init__(master, image=static_image, text="", cursor="hand2", **kwargs)
        self.video_path = video_path
        self.static_image = static_image
        self.size = size
        self.playing = False
        self.cap = None
        self.delay = 30
        self.after_id = None
        self.bind("<Button-1>", self.toggle_play)

    def toggle_play(self, event=None):
        if self.playing:
            self.stop()
        else:
            self.start()

    def start(self):
        self.playing = True
        self.cap = cv2.VideoCapture(str(self.video_path))
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.delay = int(1000 / fps) if fps and fps > 0 else 30
        self.update_frame()

    def stop(self):
        self.playing = False
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
        if self.cap:
            self.cap.release()
            self.cap = None
        self.configure(image=self.static_image)

    def update_frame(self):
        if not self.playing:
            return
        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resized = cv2.resize(frame_rgb, self.size)
            img = Image.fromarray(frame_resized)
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=self.size)
            self.configure(image=ctk_img)
            self.after_id = self.after(self.delay, self.update_frame)

    def destroy(self):
        self.stop()
        super().destroy()

class TeamsBackgroundManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.teams_bg_path = self.get_teams_background_path()
        self.thumbnail_cache = {}
        self.version = "v12.0.0"
        self.current_lang = "DE" 

        self.bg_metadata = {
            "feelingDreamy2Animated_v=0.1.mp4": ("Animated feeling dreamy 2", "thumb_dreamy2.jpg"),      
            "feelingDreamy4Animated_v=0.1.mp4": ("Animated feeling dreamy 4", "thumb_dreamy4.jpg"),     
            "feelingDreamy5Animated_v=0.2.mp4": ("Animated feeling dreamy 5", "thumb_dreamy5.jpg"),      
            "feelingDreamy7Animated_v=0.1.mp4": ("Animated feeling dreamy 7", "thumb_dreamy7.jpg"),     
            "holidayLightsAnimated_v=0.1.mp4": ("Animated holiday lights", "thumb_lights.jpg"),         
            "blueSparklesHolidayAnimated_v=0.1.mp4": ("Animated holiday blue sparkles", "thumb_sparkles.jpg") 
        }

        self.title(LANG[self.current_lang]["title"])
        self.geometry("1100x800") 
        self.minsize(1100, 650)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text=LANG[self.current_lang]["logo"], font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.refresh_btn = ctk.CTkButton(self.sidebar_frame, text=LANG[self.current_lang]["refresh"], command=self.load_backgrounds)
        self.refresh_btn.grid(row=1, column=0, padx=20, pady=10)

        self.open_folder_btn = ctk.CTkButton(self.sidebar_frame, text=LANG[self.current_lang]["open_folder"], command=self.open_teams_folder, fg_color="#2E86C1", hover_color="#1B4F72")
        self.open_folder_btn.grid(row=2, column=0, padx=20, pady=10)

        self.restart_teams_btn = ctk.CTkButton(self.sidebar_frame, text=LANG[self.current_lang]["restart_teams"], command=self.restart_teams, fg_color="#C21807", hover_color="#8A0303")
        self.restart_teams_btn.grid(row=3, column=0, padx=20, pady=10)

        self.lang_btn = ctk.CTkButton(self.sidebar_frame, text=LANG[self.current_lang]["lang_switch"], command=self.toggle_language, fg_color="#5B2C6F", hover_color="#4A235A")
        self.lang_btn.grid(row=4, column=0, padx=20, pady=30)

        self.status_label = ctk.CTkLabel(self.sidebar_frame, text=LANG[self.current_lang]["status_ready"], text_color="green", width=180, wraplength=180)
        self.status_label.grid(row=5, column=0, padx=20, pady=20, sticky="s")
        self.status_label.grid_propagate(False)

        self.info_label = ctk.CTkLabel(self.sidebar_frame, text="", font=ctk.CTkFont(size=11), text_color="gray", justify="left")
        self.info_label.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.explanation_label = ctk.CTkLabel(self, text=LANG[self.current_lang]["explanation"], font=ctk.CTkFont(size=14, weight="bold"), text_color="#E67E22", justify="left")
        self.explanation_label.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="ew")
        self.explanation_label.configure(wraplength=850, justify="center")

        self.main_frame = ctk.CTkScrollableFrame(self, label_text=LANG[self.current_lang]["main_label"])
        self.main_frame.grid(row=1, column=1, padx=20, pady=(10, 20), sticky="nsew")

        self.setup_backup_dir()
        self.update_ui_texts()
        self.load_backgrounds()

    def toggle_language(self):
        self.current_lang = "EN" if self.current_lang == "DE" else "DE"
        self.update_ui_texts()
        self.load_backgrounds()

    def update_ui_texts(self):
        l = LANG[self.current_lang]
        self.title(l["title"])
        self.logo_label.configure(text=l["logo"])
        self.refresh_btn.configure(text=l["refresh"])
        self.open_folder_btn.configure(text=l["open_folder"])
        self.restart_teams_btn.configure(text=l["restart_teams"])
        self.lang_btn.configure(text=l["lang_switch"])

        info_text = f"Version: {self.version}\n{l['created_with']}\n{l['contact']}: basecore@gmx.de\n{l['date']}: {datetime.now().strftime('%d.%m.%Y')}"
        self.info_label.configure(text=info_text)
        self.main_frame.configure(label_text=l["main_label"])
        self.status_label.configure(text=l["status_ready"])
        self.explanation_label.configure(text=l["explanation"])

    def setup_backup_dir(self):
        self.backup_dir = Path.home() / "Teams_Background_Backups"
        self.backup_dir.mkdir(exist_ok=True)

    def get_teams_background_path(self):
        local_app_data = os.environ.get('LOCALAPPDATA', '')
        new_teams_path = Path(local_app_data) / "Packages" / "MSTeams_8wekyb3d8bbwe" / "LocalCache" / "Microsoft" / "MSTeams" / "Backgrounds"
        if new_teams_path.exists() or Path(local_app_data).exists():
            return new_teams_path
        return Path(os.environ.get('APPDATA', '')) / "Microsoft" / "Teams" / "Backgrounds"

    def open_teams_folder(self):
        if self.teams_bg_path.exists():
            os.startfile(self.teams_bg_path)
        else:
            self.status_label.configure(text=LANG[self.current_lang]["status_folder_not_found"], text_color="red")

    def extract_first_frame(self, video_path, size=(192, 108), force_refresh=False): 
        if force_refresh and str(video_path) in self.thumbnail_cache:
            del self.thumbnail_cache[str(video_path)]

        if str(video_path) in self.thumbnail_cache:
            return self.thumbnail_cache[str(video_path)]

        try:
            cap = cv2.VideoCapture(str(video_path))
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

            if fps > 0 and total_frames > 0:
                target_frame = int(fps * 1.5)
                if target_frame >= total_frames:
                    target_frame = int(total_frames / 2)
                cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)

            ret, frame = cap.read()
            cap.release()

            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_resized = cv2.resize(frame_rgb, size)
                pil_image = Image.fromarray(frame_resized)
                ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=size)
                self.thumbnail_cache[str(video_path)] = ctk_image
                return ctk_image
        except Exception:
            pass
        return None

    def get_static_original_thumbnail(self, exact_filename, size=(192, 108)): 
        if exact_filename in self.bg_metadata:
            thumb_filename = self.bg_metadata[exact_filename][1]
            if thumb_filename in IMAGE_B64:
                try:
                    image_data = base64.b64decode(IMAGE_B64[thumb_filename])
                    pil_image = Image.open(io.BytesIO(image_data))
                    pil_image = pil_image.resize(size, Image.Resampling.LANCZOS)
                    return ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=size)
                except Exception:
                    pass
        empty = Image.new('RGB', size, color='#444444')
        return ctk.CTkImage(light_image=empty, dark_image=empty, size=size)

    def load_backgrounds(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if not self.teams_bg_path.exists():
            self.teams_bg_path.mkdir(parents=True, exist_ok=True)

        for exact_filename, data in self.bg_metadata.items():
            video_path = self.teams_bg_path / exact_filename
            self.create_list_item(video_path, exact_filename)

        known_files = self.bg_metadata.keys()
        mp4_files = list(self.teams_bg_path.glob("*.mp4"))
        unknown_files = [f for f in mp4_files if f.name not in known_files]

        for file_path in unknown_files:
            self.create_list_item(file_path, None)

        self.status_label.configure(text=LANG[self.current_lang]["status_refreshed"], text_color="green")

    def create_list_item(self, file_path, exact_filename):
        l = LANG[self.current_lang]
        frame = ctk.CTkFrame(self.main_frame)
        frame.pack(fill="x", padx=10, pady=8)

        video_exists = file_path.exists()
        w, h, size_mb = 0, 0, 0
        file_size_str = "0.00 MB"

        if video_exists:
            current_thumb = self.extract_first_frame(str(file_path), force_refresh=True)
            if not current_thumb:
                empty = Image.new('RGB', (192, 108), color='gray')
                current_thumb = ctk.CTkImage(light_image=empty, dark_image=empty, size=(192, 108))

            try:
                size_mb = file_path.stat().st_size / (1024*1024)
                cap = cv2.VideoCapture(str(file_path))
                w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                cap.release()
                file_size_str = f"{size_mb:.2f} MB | {w}x{h}"
            except:
                file_size_str = "Lesefehler"
        else:
            current_thumb = self.get_static_original_thumbnail(exact_filename)

        current_indicator_frame = ctk.CTkFrame(frame, fg_color="transparent")
        current_indicator_frame.grid(row=0, column=0, padx=15, pady=5, sticky="n")
        ctk.CTkLabel(current_indicator_frame, text=l["current_preview"], font=ctk.CTkFont(size=11, weight="bold")).pack(side="top")

        if video_exists:
            thumb_label = InlineVideoPlayer(current_indicator_frame, file_path, current_thumb, size=(192, 108))
        else:
            thumb_label = ctk.CTkLabel(current_indicator_frame, image=current_thumb, text="", cursor="arrow")
        thumb_label.pack(side="top", pady=5)

        if video_exists:
            btn_box = ctk.CTkFrame(current_indicator_frame, fg_color="transparent")
            btn_box.pack(side="top", pady=5)

            btn_auto = ctk.CTkButton(btn_box, text=l["btn_auto_opt"], width=80, height=24, fg_color="#F39C12", hover_color="#D68910", command=lambda p=file_path: self.auto_optimize_size(p, w, h))
            btn_auto.pack(side="left", padx=2)

            btn_edit = ctk.CTkButton(btn_box, text=l["btn_editor"], width=80, height=24, fg_color="#3498DB", hover_color="#2980B9", command=lambda p=file_path: VideoEditorDialog(self, p, w, h, size_mb))
            btn_edit.pack(side="left", padx=2)

        if exact_filename:
            friendly_name = self.bg_metadata[exact_filename][0]
        else:
            friendly_name = l["unknown_bg"]

        orig_indicator_frame = ctk.CTkFrame(frame, fg_color="transparent")
        orig_indicator_frame.grid(row=0, column=1, padx=5, pady=5, sticky="n")

        info_frame = ctk.CTkFrame(frame, fg_color="transparent")
        info_frame.grid(row=0, column=2, sticky="nw", padx=(15, 10), pady=10)

        ctk.CTkLabel(info_frame, text=f"{friendly_name}", font=ctk.CTkFont(size=14, weight="bold"), wraplength=250, justify="left").grid(row=0, column=0, sticky="w", pady=(5,0))
        ctk.CTkLabel(info_frame, text=f"{l['file']}:\n{file_path.name}", font=ctk.CTkFont(size=11, slant="italic"), text_color="gray", wraplength=250, justify="left").grid(row=1, column=0, sticky="w", pady=2)

        if size_mb > 10.0:
            ctk.CTkLabel(info_frame, text=f"{l['size']}: {size_mb:.2f} MB {l['warning_large']}", text_color="#E74C3C", font=ctk.CTkFont(size=12, weight="bold")).grid(row=2, column=0, sticky="w")
        elif size_mb > 5.0:
            ctk.CTkLabel(info_frame, text=f"{l['size']}: {size_mb:.2f} MB {l['warning_medium']}", text_color="#F39C12", font=ctk.CTkFont(size=12, weight="bold")).grid(row=2, column=0, sticky="w")
        else:
            ctk.CTkLabel(info_frame, text=f"{l['size']}: {file_size_str}", font=ctk.CTkFont(size=12)).grid(row=2, column=0, sticky="w")

        frame.grid_columnconfigure(2, weight=1)
        ctk.CTkLabel(orig_indicator_frame, text=l["original_preview"], font=ctk.CTkFont(size=11, weight="bold")).pack(side="top")

        if exact_filename:
            orig_thumb = self.get_static_original_thumbnail(exact_filename)
            ctk.CTkLabel(orig_indicator_frame, image=orig_thumb, text="").pack(side="top", pady=5)
        else:
            ctk.CTkLabel(orig_indicator_frame, text=l["no_original"], text_color="gray").pack(side="top", pady=20)

        btn_box_orig = ctk.CTkFrame(orig_indicator_frame, fg_color="transparent")
        btn_box_orig.pack(side="top", pady=5)

        btn_replace = ctk.CTkButton(btn_box_orig, text=l["btn_replace"], width=80, height=24, fg_color="#27AE60", hover_color="#1E8449", command=lambda p=file_path: self.replace_background(p, video_exists))
        btn_replace.pack(side="left", padx=2)

        btn_restore = ctk.CTkButton(btn_box_orig, text=l["btn_restore"], width=80, height=24, fg_color="#E67E22", hover_color="#D35400", command=lambda p=file_path: self.restore_original_teams(p, video_exists))
        btn_restore.pack(side="left", padx=2)

        if not video_exists:
            btn_restore.configure(state="disabled", fg_color="gray")

    def auto_optimize_size(self, file_path, w, h):
        self.status_label.configure(text=LANG[self.current_lang]["status_optimizing"], text_color="#E67E22")
        threading.Thread(target=self._run_auto_optimize, args=(file_path, w, h), daemon=True).start()

    def _run_auto_optimize(self, file_path, w, h):
        unopt_path = self.backup_dir / f"unopt_{file_path.name}"
        if not unopt_path.exists():
            shutil.copy2(file_path, unopt_path)

        temp_out = os.path.join(os.path.dirname(file_path), "temp_auto_opt.mp4")
        cap = cv2.VideoCapture(str(file_path))
        fps = cap.get(cv2.CAP_PROP_FPS)
        target_fps = min(fps, 15.0) if fps and fps > 0 else 15.0

        scale = min(854/w, 480/h) if w > 0 and h > 0 else 1.0
        if scale < 1.0:
            new_w, new_h = int(w * scale), int(h * scale)
        else:
            new_w, new_h = w, h

        new_w = new_w if new_w % 2 == 0 else new_w + 1
        new_h = new_h if new_h % 2 == 0 else new_h + 1

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(temp_out, fourcc, target_fps, (new_w, new_h))

        frame_interval = fps / target_fps if target_fps > 0 else 1
        frame_idx = 0
        written_frames = 0

        while True:
            ret, frame = cap.read()
            if not ret: break

            if int(frame_idx) == int(written_frames * frame_interval):
                resized = cv2.resize(frame, (new_w, new_h))
                out.write(resized)
                written_frames += 1
            frame_idx += 1

        cap.release()
        out.release()
        self.after(0, self._finish_auto_optimize, file_path, temp_out)

    def _finish_auto_optimize(self, file_path, temp_out):
        orig_size = os.path.getsize(file_path)
        new_size = os.path.getsize(temp_out)

        if new_size >= orig_size:
            try: os.remove(temp_out)
            except: pass
            self.status_label.configure(text=LANG[self.current_lang]["status_opt_aborted"], text_color="#E74C3C")
            self.load_backgrounds()
            return

        shutil.copy2(temp_out, file_path)
        try: os.remove(temp_out)
        except: pass

        if str(file_path) in self.thumbnail_cache:
            del self.thumbnail_cache[str(file_path)]

        self.status_label.configure(text=LANG[self.current_lang]["status_optimized"], text_color="green")
        self.load_backgrounds()

    def backup_file(self, file_path, silent=False):
        l = LANG[self.current_lang]
        try:
            dest = self.backup_dir / f"backup_{file_path.name}"
            if not dest.exists():
                shutil.copy2(file_path, dest)
                if not silent:
                    self.status_label.configure(text=l["status_saved"], text_color="green")
        except Exception:
            pass

    def replace_background(self, target_path, video_exists):
        l = LANG[self.current_lang]
        new_file = filedialog.askopenfilename(title=l["dialog_title"], filetypes=[(l["dialog_video"], "*.mp4 *.gif"), (l["dialog_all"], "*.*")])
        if new_file:
            try:
                if video_exists:
                    self.backup_file(target_path, silent=True)

                unopt_path = self.backup_dir / f"unopt_{target_path.name}"
                if unopt_path.exists():
                    os.remove(unopt_path)

                shutil.copy2(new_file, target_path)
                if str(target_path) in self.thumbnail_cache:
                    del self.thumbnail_cache[str(target_path)]

                self.status_label.configure(text=l["status_replaced"], text_color="green")
                self.load_backgrounds()
            except Exception as e:
                self.status_label.configure(text=l["status_replace_failed"], text_color="red")

    def restore_original_teams(self, target_path, video_exists):
        l = LANG[self.current_lang]
        backup_path = self.backup_dir / f"backup_{target_path.name}"
        try:
            if target_path.exists():
                os.remove(target_path)
            if str(target_path) in self.thumbnail_cache:
                del self.thumbnail_cache[str(target_path)]

            self.status_label.configure(text=l["status_deleted"], text_color="orange")
            self.load_backgrounds()
        except Exception:
            self.status_label.configure(text=l["status_restore_failed"], text_color="red")

    def restart_teams(self):
        l = LANG[self.current_lang]
        self.status_label.configure(text=l["status_restarting"], text_color="#E67E22")
        self.update()
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] and ('ms-teams' in proc.info['name'].lower() or 'teams.exe' in proc.info['name'].lower()):
                    proc.kill()
            except:
                pass
        time.sleep(2)
        try:
            os.system('explorer.exe shell:appsFolder\\MSTeams_8wekyb3d8bbwe!MSTeams')
            self.status_label.configure(text=l["status_started"], text_color="green")
        except:
            self.status_label.configure(text=l["status_restart_manual"], text_color="red")

if __name__ == "__main__":
    app = TeamsBackgroundManager()
    app.mainloop()

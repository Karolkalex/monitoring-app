import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self, root, heart_rate_callback):
        self.root = root
        self.heart_rate_callback = heart_rate_callback
        self.heart_rate_label = tk.Label(root, text="Heart Rate: --", font=('Helvetica', 16))
        self.heart_rate_label.pack(pady=20)

        # Start button to fetch real-time data
        start_button = tk.Button(root, text="Start Monitoring", command=self.start_monitoring)
        start_button.pack(pady=10)

    def start_monitoring(self):
        # Continuously update heart rate in the GUI
        self.update_heart_rate()

    def update_heart_rate(self):
        heart_rate = self.heart_rate_callback()
        self.heart_rate_label.config(text=f"Heart Rate: {heart_rate}")
        if heart_rate < 40 or heart_rate > 120:
            self.show_alert(f"Abnormal Heart Rate Detected: {heart_rate}")
        self.root.after(1000, self.update_heart_rate)

    def show_alert(self, message):
        messagebox.showwarning("Warning", message)
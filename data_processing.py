import numpy as np

# Thresholds for normal heart rate
LOW_THRESHOLD = 40
HIGH_THRESHOLD = 120

def process_heart_rate(raw_data):
    heart_rate = int(raw_data)
    return heart_rate

def detect_anomaly(heart_rate):
    if heart_rate < LOW_THRESHOLD or heart_rate > HIGH_THRESHOLD:
        return True
    return False
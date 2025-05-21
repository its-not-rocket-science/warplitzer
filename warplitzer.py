import librosa 
import numpy as np 
import soundfile as sf 
from scipy.signal import correlate 
 
"# Load the two recordings" 
y_33, sr = librosa.load("vinyl_33rpm.wav", sr=None) 
y_45, _ = librosa.load("vinyl_45rpm.wav", sr=None) 
 
"# Resample 45rpm to match 33rpm speed" 
speed_ratio = 33 / 45 
y_45_resampled = librosa.resample(y_45, orig_sr=sr, target_sr=int(sr * speed_ratio)) 
 
"# Trim to equal length" 
min_len = min(len(y_33), len(y_45_resampled)) 
y_33 = y_33[:min_len] 
y_45_resampled = y_45_resampled[:min_len] 
 
"# Align using cross-correlation" 
corr = correlate(y_33, y_45_resampled, mode='full') 
offset = np.argmax(corr) - min_len 
if offset 
    y_33 = y_33[offset:] 
    y_45_resampled = y_45_resampled[:len(y_33)] 
else: 
    y_45_resampled = y_45_resampled[-offset:] 
    y_33 = y_33[:len(y_45_resampled)] 
 
"# Combine the two" 
sf.write("vinyl_cleaned.wav", y_combined, sr) 

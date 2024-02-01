#Version 1 of the audio analyzer. This gets close but not quite there for accuracy on sonic analysis. Refinement of the find cutoff frequency method is needed.

#Smoothing may be turned on using the command --smooth
#Recommended for live audio, but not for electronic music. 
 
#Example command 
# python audio_analysis.py path_to_your_audio_file.mp3 --smooth

import numpy as np
import matplotlib.pyplot as plt
import librosa
import argparse

def smooth_spectrum(magnitude, window_size=5):
    """ Smooth the magnitude spectrum """
    return np.convolve(magnitude, np.ones(window_size)/window_size, mode='same')

def find_cutoff_frequency(freqs, magnitudes, start_freq=10000, smooth=False):
    """Find the cutoff frequency by looking for a sustained decrease in magnitude."""
    # Optionally smooth the magnitude spectrum
    if smooth:
        magnitudes = smooth_spectrum(magnitudes)

    # Convert magnitudes to decibels
    magnitudes_db = 10 * np.log10(magnitudes)

    # Look for the point where the magnitude decreases by a significant amount over a range
    # Define the drop in dB that we consider significant
    significant_drop_db = 3

    # Initialize cutoff frequency at the highest frequency (i.e., no cutoff found)
    cutoff_freq = freqs[-1]
    
    # Start at the high frequency end and move towards the start frequency
    for i in reversed(range(np.where(freqs >= start_freq)[0][0], len(freqs))):
        # Look for a significant drop over a range of 1000 indices (~214 Hz range)
        if i-1000 > 0 and np.mean(magnitudes_db[i-1000:i]) - np.mean(magnitudes_db[i:i+1000]) >= significant_drop_db:
            cutoff_freq = freqs[i]
            break

    return cutoff_freq



def plot_spectrum(freqs, magnitudes, cutoff_freq):
    """Plot the spectrum and the cutoff frequency."""
    plt.figure(figsize=(12, 6))
    plt.semilogx(freqs, 20 * np.log10(magnitudes))  # Plot on a logarithmic scale
    plt.axvline(x=cutoff_freq, color='r', linestyle='--', label=f'Cutoff Frequency: {cutoff_freq} Hz')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.title('Frequency Spectrum with Cutoff Frequency')
    plt.legend()
    plt.xlim([20, 22050])  # Limit x-axis to human hearing range (20 Hz to 22.05 kHz)
    plt.ylim([np.min(20 * np.log10(magnitudes)), np.max(20 * np.log10(magnitudes))])  # Limit y-axis to magnitude range
    plt.grid(True, which="both", ls="--")
    plt.show()

# Parse command line arguments
parser = argparse.ArgumentParser(description='Analyze audio file for cutoff frequency.')
parser.add_argument('filepath', type=str, help='Path to the audio file.')
parser.add_argument('-sm', '--smooth', action='store_true', help='Apply smoothing to the frequency spectrum.')
args = parser.parse_args()

# Load audio file
y, sr = librosa.load(args.filepath, sr=None)

# Compute FFT
N = len(y)
y_fft = np.fft.rfft(y)
y_fft_mag = np.abs(y_fft)
freqs = np.fft.rfftfreq(N, 1 / sr)

# Find cutoff frequency with optional smoothing
cutoff_freq = find_cutoff_frequency(freqs, y_fft_mag, smooth=args.smooth)

# Print and plot
print(f"Cutoff Frequency: {cutoff_freq} Hz")
plot_spectrum(freqs, y_fft_mag, cutoff_freq)

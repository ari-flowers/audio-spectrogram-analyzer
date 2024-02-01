#WIP v2 of the analysis algorithmic process using a threshold-based approach. Challenges include calculating the average cutoff frequency that could be seen easily with the human eye, omitting any irrelevent peaks

#Example output: Frame 5 has the largest differential with min: 8.434305527771357e-06, max: 306.9082946777344

import numpy as np
import librosa

def frame_with_largest_differential(fft_frames):
    """
    Find the frame with the largest differential between max and min magnitudes.
    
    Parameters:
    fft_frames (np.ndarray): 2D array of FFT frames (shape: [num_frames, fft_size/2+1])
    
    Returns:
    int: Index of the frame with the largest differential
    float: Minimum magnitude in the identified frame
    float: Maximum magnitude in the identified frame
    """
    # Initialize variables to store the max differential and the index of the frame
    max_diff = 0
    frame_index = 0
    
    # Convert FFT frames to magnitude
    magnitude_frames = np.abs(fft_frames)
    
    # Iterate over each frame to find the differential
    for i, frame in enumerate(magnitude_frames):
        frame_max = np.max(frame)
        frame_min = np.min(frame)
        diff = frame_max - frame_min
        
        # Update max_diff and frame_index if current differential is greater
        if diff > max_diff:
            max_diff = diff
            frame_index = i
    
    # Get the min and max magnitude of the frame with the largest differential
    frame_max_magnitude = np.max(magnitude_frames[frame_index])
    frame_min_magnitude = np.min(magnitude_frames[frame_index])
    
    return frame_index, frame_min_magnitude, frame_max_magnitude

# Example usage:
# Load an audio file
y, sr = librosa.load('command.wav')

# Calculate the Short-Time Fourier Transform (STFT) of the audio
stft_frames = librosa.stft(y)

# Find the frame with the largest differential
index, min_mag, max_mag = frame_with_largest_differential(stft_frames)

print(f"Frame {index} has the largest differential with min: {min_mag}, max: {max_mag}")

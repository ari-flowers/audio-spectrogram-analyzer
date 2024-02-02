#Audio Analysis Toolkit

##Description

This project provides tools for in-depth audio analysis, focusing on two key aspects:

1. Cutoff Frequency Detection: Determines the cutoff frequency in audio files, which is particularly useful for understanding the frequency range effectively used in an audio track.
2. (WIP) Bit Depth Determination: Identifies the bit depth of audio files from their metadata, giving insights into the resolution and dynamic range of the audio.

The toolkit is designed to handle various audio file formats and applies signal processing techniques to extract meaningful information from audio samples.

## Features
- **Cutoff Frequency Analysis**:
- Identifies the frequency at which the audio signal's energy drops significantly.
- Useful for analyzing the effective frequency range of music tracks, especially compressed formats like MP3.

- **Bit Depth Analysis**: (WIP)
-Reads audio file metadata to determine the bit depth (e.g., 16-bit, 24-bit).
-Helps in assessing the resolution and potential dynamic range of the audio.

##Installation

This project requires Python 3.x and several dependencies, including numpy, matplotlib, and librosa. To set up the project:

1. Clone the repository:

git clone https://github.com/ari-flowers/audio-spectrogram-analyzer

2. Navigate to the project directory:

cd audio-spectrogram-analyzer

3. Install required dependencies:

pip install -r requirements.txt

## Usage

### Cutoff Frequency Analysis

Run the audio_analysis.py script with the path to the audio file:

python audio_analysis.py path_to_your_audio_file.wav

### Optional arguments:

-sm or --smooth: Apply smoothing to the frequency spectrum for analysis. Recommended to leave off for electronic music.

### Bit Depth Analysis
WIP 

import numpy as np
import soundfile as sf

# Frequency and duration pairs (i, j) where i is frequency in Hz and j is duration in ms
note_pairs = [
    (185, 200), (196, 200), (220, 400), (220, 400), (247, 400), 
    (247, 400), (220, 600), (196, 200), (185, 400), (185, 200), 
    (196, 200), (220, 400), (220, 400), (247, 400), (247, 400), 
    (220, 600), (196, 200), (185, 400), (185, 200), (196, 200), 
    (220, 400), (220, 400), (247, 400), (277, 400), (294, 800), 
    (294, 400), (330, 400), (277, 400), (277, 400), (247, 400), 
    (277, 200), (247, 400), (220, 800)
]

# Parameters
amplitude = 1.0
sampling_rate = 10000  # in Hz

# Initialize an empty list to hold the audio samples
song = []

# Generate sinusoids for each (frequency, duration) pair
for frequency, duration_ms in note_pairs:
    duration_seconds = duration_ms / 1000  # Convert ms to seconds
    t = np.linspace(0, duration_seconds, int(sampling_rate * duration_seconds), endpoint=False)
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    song.extend(sine_wave)  # Append the generated wave to the song list

# Convert the list to a NumPy array
song = np.array(song)

# Save the concatenated sine wave to a .wav file
sf.write('songA.wav', song, sampling_rate)

print("Concatenated sine wave audio file saved as 'songA.wav'")

import numpy as np
import soundfile as sf

# Frequency and duration pairs (i, j) where i is frequency in Hz and j is duration in ms
note_pairs = [
    (262, 200), (294, 200), (294, 200), (330, 1000), (294, 200), 
    (262, 200), (294, 400), (392, 800), (349.23, 200), (330, 200), 
    (262, 800), (220, 800), (196, 1200),
    (262, 200), (294, 200), (294, 200), (330, 1000), (294, 200), 
    (262, 200), (294, 400), (392, 800), (330, 200), (392, 200), 
    (440, 800), (392, 800), (294, 1600),
    (262, 600), (262, 200), (262, 400), (262, 400), (247, 400), 
    (262, 800), (262, 400), (247, 400), (262, 800), (294, 400), 
    (330, 800), (294, 800), (262, 600), (262, 200), (262, 400), 
    (262, 400), (247, 400), (262, 800), (262, 400), (196, 3200),
    (262, 1600), (294, 1200), (196, 400), (392, 800), (349.23, 400), 
    (330, 400), (294, 800), (330, 400), (349.23, 400), (330, 1200), 
    (294, 200), (262, 200), (247, 400), (262, 800), (247, 400), 
    (220, 1600), (196, 1600)
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
sf.write('songB.wav', song, sampling_rate)

print("Concatenated sine wave audio file saved as 'songB.wav'")

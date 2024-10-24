import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Parameters
frequency = 220  # Frequency in Hz
sampling_rate = 44100  # Sampling rate in samples per second
duration = 5  # Duration in seconds

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sine wave
amplitude = 1  # Amplitude (values should range between -1 and 1)
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Save the generated sine wave to a .wav file
sf.write('sine_wave_200Hz.wav', sine_wave, sampling_rate)

# Plot only the first 0.05 seconds (50 ms) of the sine wave for clarity
samples_to_plot = int(0.05 * sampling_rate)  # 50 ms worth of samples

plt.figure(figsize=(8, 4))
plt.plot(t[:samples_to_plot], sine_wave[:samples_to_plot])
plt.title(f'Sine Wave - Frequency: {frequency} Hz (First 50 ms)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()

print("Sine wave audio file saved as 'sine_wave_200Hz.wav'")

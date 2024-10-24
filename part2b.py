import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Parameters for the sinusoids (Rhythm)
fundamental_frequency = 220  # Fundamental Frequency in Hz
harmonic_count = 10  # Number of harmonics to include
frequencies = [fundamental_frequency * i for i in range(1, harmonic_count + 1)]  # Frequencies in Hz

# Amplitudes for a nice musical output (decreasing amplitudes)
amplitudes = [1.0 / i for i in range(1, harmonic_count + 1)]  # Amplitudes decreasing
phases = [0, np.pi/4, -np.pi/4, np.pi/2, np.pi] + [0] * (harmonic_count - 5)  # Phases in radians
sampling_rate = 44100  # Increased sampling rate for smoother output
duration = 10  # Duration in seconds

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration))

# Initialize the superposed wave to zero
superposed_wave = np.zeros_like(t)

# Generate the superposed wave
for i in range(len(frequencies)):
    sine_wave = amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t + phases[i])
    superposed_wave += sine_wave

# Plot the superposed sine wave
plt.figure(figsize=(10, 6))
plt.plot(t[:int(0.02 * sampling_rate)], superposed_wave[:int(0.02 * sampling_rate)], color='black', linewidth=2)
plt.title('Superposed Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')  # Add a horizontal line at y=0
plt.legend()
plt.xlim(0, 0.02)  # Set x-axis limits to show the first 0.02 seconds

# Dynamically set y-axis limits based on the superposed wave
plt.ylim(np.min(superposed_wave[:int(0.02 * sampling_rate)]) * 1.1, np.max(superposed_wave[:int(0.02 * sampling_rate)]) * 1.1)

plt.grid(True)
plt.show()

# Save the superposed wave to a .wav file
sf.write('superposed_sine_waves_richer.wav', superposed_wave, sampling_rate)

print("Superposed sine wave audio file saved as 'superposed_sine_waves_richer.wav'")

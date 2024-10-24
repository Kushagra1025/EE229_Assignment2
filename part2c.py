import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Parameters for the sinusoids (Rhythm)
fundamental_frequency = 220  # Fundamental Frequency in Hz
harmonic_count = 10  # Total harmonics (including fundamental)
frequencies = [fundamental_frequency * i for i in range(1, harmonic_count + 1)]  # Frequencies in Hz

# Amplitudes for a richer musical output (decreasing)
amplitudes = [1.0 / (i + 1) for i in range(len(frequencies))]  # Amplitudes decreasing
phases = [0, np.pi/4, -np.pi/4, np.pi/2] + [0] * (len(frequencies) - 4)  # Phases in radians
sampling_rate = 44100  # Sampling rate in samples per second
duration = 10  # Duration in seconds

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Initialize the superposed wave to zero
superposed_wave = np.zeros_like(t)

# Generate individual sine waves and add to the superposed wave
for i in range(len(frequencies)):
    sine_wave = amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t + phases[i])
    superposed_wave += sine_wave

# Function to compute magnitude spectrum
def compute_magnitude_spectrum(signal, sampling_rate):
    N = len(signal)
    freq = np.fft.fftfreq(N, 1/sampling_rate)
    fft_signal = np.fft.fft(signal)

    # Normalize the magnitude by the number of samples
    magnitude = np.abs(fft_signal)[:N // 2] * (2 / N)  # Magnitude spectrum normalized
    freq = freq[:N // 2]  # Only positive frequencies
    return freq, magnitude

# Compute magnitude spectrum for the superposed wave
freq, magnitude = compute_magnitude_spectrum(superposed_wave, sampling_rate)

# Plot the magnitude spectrum of the superposed wave
plt.figure(figsize=(10, 6))
plt.stem(freq, magnitude, linefmt='k-', basefmt='k-', markerfmt='ko')  # Set color to black
plt.title('Magnitude Spectrum of Superposed Wave')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.xlim(0, 2400)  # Limit x-axis to 2400 Hz

# Set x-ticks for frequencies from 220 Hz to 2200 Hz (10th harmonic)
plt.xticks(frequencies)

# Set y-ticks to include amplitude levels and specific magnitudes for harmonics
magnitude_ticks = [np.max(magnitude) * (amplitudes[i] / max(amplitudes)) for i in range(len(amplitudes))]  # Calculate magnitudes for each frequency
y_ticks = np.linspace(0, np.max(magnitude), 6)  # Increased ticks from 0 to max magnitude
plt.yticks(np.unique(np.concatenate((y_ticks, magnitude_ticks, [1]))))  # Combine and set y-ticks including 1

# Increase the spacing of the y-axis ticks
plt.gca().set_yticks(plt.yticks()[0][::2])  # Reduce the number of y-ticks for spacing

plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

# Save the superposed wave to a .wav file
sf.write('superposed_sine_waves.wav', superposed_wave, sampling_rate)

print("Superposed sine wave audio file saved as 'superposed_sine_waves.wav'")

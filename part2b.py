import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sinusoids (Rhythm)
fundamental_frequency = 220  # Fundamental Frequency in Hz
frequencies = [fundamental_frequency, 
               2 * fundamental_frequency, 
               3 * fundamental_frequency, 
               4 * fundamental_frequency, 
               5 * fundamental_frequency]  # Frequencies in Hz
amplitudes = [1.0, 0.8, 0.6, 0.4, 0.2]  # Amplitudes
phases = [0, np.pi/4, -np.pi/4, np.pi/2, np.pi]  # Phases in radians
sampling_rate = 44100  # Sampling rate in samples per second
duration = 10  # Duration in seconds

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Initialize the superposed wave to zero
superposed_wave = np.zeros_like(t)

# Prepare arrays to store individual sine waves for plotting
sinusoids = []

# Generate individual sine waves and add to the superposed wave
for i in range(len(frequencies)):
    sine_wave = amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t + phases[i])
    sinusoids.append(sine_wave)
    superposed_wave += sine_wave

# Function to compute magnitude spectrum
def compute_magnitude_spectrum(signal, sampling_rate):
    N = len(signal)
    freq = np.fft.fftfreq(N, 1/sampling_rate)
    fft_signal = np.fft.fft(signal)
    
    magnitude = np.abs(fft_signal)[:N // 2] * 2 / N  # Magnitude spectrum
    freq = freq[:N // 2]  # Only positive frequencies
    return freq, magnitude

# Plot magnitude spectrum for each sinusoid
fig, axs = plt.subplots(len(frequencies) + 1, 1, figsize=(10, 12))

for i in range(len(frequencies)):
    freq, magnitude = compute_magnitude_spectrum(sinusoids[i], sampling_rate)
    
    # Plot magnitude spectrum
    axs[i].plot(freq, magnitude)
    axs[i].set_title(f'Magnitude Spectrum of {frequencies[i]} Hz')
    axs[i].set_ylabel('Magnitude')
    axs[i].set_xlim(0, 1500)
    
    # Default x-ticks with additional frequencies where the amplitude is non-zero
    xticks = list(np.arange(0, 1500, 200)) + [frequencies[i]]
    axs[i].set_xticks(xticks)
    
    axs[i].set_yticks(np.arange(0, max(magnitude) + 0.1, 0.2))
    axs[i].grid(True)

# Plot magnitude spectrum for the superposed wave
freq, magnitude = compute_magnitude_spectrum(superposed_wave, sampling_rate)

# Magnitude spectrum of superposed wave
axs[-1].plot(freq, magnitude, color='black')
axs[-1].set_title('Magnitude Spectrum of Superposed Wave')
axs[-1].set_xlabel('Frequency [Hz]')
axs[-1].set_ylabel('Magnitude')
axs[-1].set_xlim(0, 1500)

# Default x-ticks with additional frequencies where the amplitude is non-zero (all frequencies used)
xticks = list(np.arange(0, 1500, 200)) + frequencies
axs[-1].set_xticks(xticks)

axs[-1].set_yticks(np.arange(0, max(magnitude) + 0.1, 0.2))
axs[-1].grid(True)

# Adjust layout to prevent overlap
plt.subplots_adjust(top=0.97, right=0.998, left=0.04, bottom=0.06, hspace=0.7)
plt.show()

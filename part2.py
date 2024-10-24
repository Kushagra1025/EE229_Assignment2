import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Parameters for the sinusoids (Rhythm)
fundamental_frequency = 220  # Fundamental Frequency in Hz
frequencies = [fundamental_frequency, 
               2 * fundamental_frequency, 
               3 * fundamental_frequency, 
               4 * fundamental_frequency, 
               5 * fundamental_frequency]  # Frequencies in Hz

# Amplitudes for a nice musical output
amplitudes = [1.0, 0.8, 0.6, 0.4, 0.2]  # Amplitudes
phases = [0, np.pi/4, -np.pi/4, np.pi/2, np.pi]  # Phases in radians
sampling_rate = 44100  # Sampling rate in samples per second
duration = 5  # Duration in seconds

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration))

# Initialize the superposed wave to zero
superposed_wave = np.zeros_like(t)

# Create subplots
fig, axs = plt.subplots(len(frequencies) + 1, 1, figsize=(10, 12), sharex=True)

# Generate and plot individual sinusoids
for i in range(len(frequencies)):
    # Generate individual sine wave
    sine_wave = amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t + phases[i])
    
    # Add the sine wave to the superposed wave
    superposed_wave += sine_wave
    
    # Plot the individual sine wave
    axs[i].plot(t[:int(0.05 * sampling_rate)], sine_wave[:int(0.05 * sampling_rate)], label=f'{frequencies[i]} Hz')
    axs[i].set_title(f'Sine Wave - {frequencies[i]} Hz')
    axs[i].set_ylabel('Amplitude')
    axs[i].legend(loc='upper right')
    
    # Set dynamic y-limits based on the amplitude
    axs[i].set_ylim(-amplitudes[i], amplitudes[i])  # Set limits to 1.5 times the amplitude
    # Set custom y-ticks to display only -amplitude, 0, +amplitude
    axs[i].set_yticks([-amplitudes[i], 0, amplitudes[i]])

# Plot the superposed sine wave
axs[-1].plot(t[:int(0.05 * sampling_rate)], superposed_wave[:int(0.05 * sampling_rate)], color='black', linewidth=2, label='Superposed Wave')
axs[-1].set_title('Superposed Sine Wave')
axs[-1].set_xlabel('Time [s]')  # Set the x-axis label
axs[-1].set_ylabel('Amplitude')
axs[-1].legend(loc='upper right')
# Set custom y-ticks to display only -amplitude, 0, +amplitude
axs[-1].set_yticks([-1.8356306788674575, 0, 1.8356306788674575])

# Set x-axis limits for all subplots
for ax in axs:
    ax.set_xlim(0, 0.05)  # Set x-axis limits up to 0.05 seconds

# Manually set margins
plt.subplots_adjust(top=0.97, right=0.997, left=0.05, bottom=0.06,hspace=0.4)  # Set margins as specified

plt.show()

# Save the superposed wave to a .wav file
sf.write('superposed_sine_waves.wav', superposed_wave, sampling_rate)

print("Superposed sine wave audio file saved as 'superposed_sine_waves.wav'")

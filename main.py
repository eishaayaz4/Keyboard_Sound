import pygame
import keyboard
import numpy as np

# Initialize pygame mixer for sound
pygame.mixer.init()

# Dictionary to map keys to frequencies (Hz)
key_tones = {
    'a': 261.63,  # Middle C
    's': 293.66,  # D
    'd': 329.63,  # E
    'f': 349.23,  # F
    'g': 392.00,  # G
    'h': 440.00,  # A
    'j': 493.88,  # B
    'k': 523.25,  # High C
    'l': 554.37  # C#
}


# Function to generate a stereo sound wave for a given frequency and duration
def generate_sound(frequency, duration=0.5):
    sample_rate = 44100  # samples per second
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Generate a mono sine wave
    mono_wave = np.sin(2 * np.pi * frequency * t) * 32767  # Generate a sine wave
    mono_wave = mono_wave.astype(np.int16)  # Convert to 16-bit  format

    # Create a stereo sound by duplicating the mono wave for both left and right channels
    stereo_wave = np.vstack((mono_wave, mono_wave)).T  # Stack mono_wave into two channels (stereo)
    stereo_wave = stereo_wave.astype(np.int16)  # Convert to 16-bit PCM format

    # Ensure the array is C-contiguous
    stereo_wave = np.ascontiguousarray(stereo_wave)

    # Return the stereo sound
    return pygame.sndarray.make_sound(stereo_wave)


# Main loop to check for key presses
while True:
    for key, frequency in key_tones.items():
        if keyboard.is_pressed(key):  # If the key is pressed
            sound = generate_sound(frequency)  # Generate the sound for the key
            sound.play()  # Play the sound
            pygame.time.delay(300)  # Delay to avoid multiple rapid sounds for one press

    if keyboard.is_pressed('esc'):  # Stop the program when ESC key is pressed
        break

pygame.quit()  # Clean up and close pygame


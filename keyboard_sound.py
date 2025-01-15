import pygame
import keyboard
# Initialize pygame mixer for sound
pygame.mixer.init()

# Dictionary to map keys to frequencies (Hz)
key_tones = {
    'a': './sounds/scream.mp3',
    's': './sounds/baby.mp3',
    'd': './sounds/exp.mp3',
    'f': './sounds/fear.mp3',
    'g': './sounds/explosion.mp3',
    'h': './sounds/guitarar.mp3',
    'j': './sounds/baby-cry.mp3',
}

# Main loop to check for key presses
while True:
    for key, sound_path in key_tones.items():
        if keyboard.is_pressed(key):  # If the key is pressed
            sound = pygame.mixer.Sound(sound_path)
            sound.play()  # Play the sound
            pygame.time.delay(300)  # Delay to avoid multiple rapid sounds for one press

    if keyboard.is_pressed('esc'):  # Stop the program when ESC key is pressed
        break

pygame.quit()  # Clean up and close pygame

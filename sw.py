import random
import time
import os
import pygame

pygame.mixer.init()

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(2)

def show_animation(frames, delay=0.5):
    for frame in frames:
        print(frame)
        time.sleep(delay)

def show_scary_window():
    window_frames = [
        "============================",
        "|                          |",
        "|        RUSSIAN          |",
        "|        ROULETTE         |",
        "|                          |",
        "|        Beware of        |",
        "|        the BANG!        |",
        "|                          |",
        "|                         |",
        "|                           |",
        "|      Let the games      |",
        "|        Begin...            |",
        "|                          |",
        "============================"
    ]

    show_animation(window_frames)

def show_game_over():
    window_frames = [
        "============================",
        "|                          |",
        "|       GAME OVER!          |",
        "|                          |",
        "|       You didn't           |",
        "|       survive...         |",
        "|                         |",
        "|                          |",
        "|   Better luck next time.. |",
        "|                          |",
        "|                          |",
        "|                         |",
        "|                          |",
        "============================"
    ]

    show_animation(window_frames)
    

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    show_scary_window()

def display_animation(frames):
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.6)

def russian_roulette():
    rounds = 6
    revolver_frames = ["kekeke. . ."]

    print("Welcome to Russian Roulette!")
    show_menu()

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")

        chambers = [0] * 5 + [1]  
        random.shuffle(chambers)

        print("Spinning the chamber...")
        show_animation(["...", "..", "."], delay=1)  
        play_sound('Revspin.mp3')
        time.sleep(1.5)  

        input("Press Enter to pull the trigger...")

        outcome = chambers.pop()

        if outcome == 1:
            play_sound('Revshot.mp3')
            display_animation(["+=__--", "   _  __,_____", " / __.==--'  POW!", "/#(-'", "`. . . .'"])
            time.sleep(7)

            show_game_over()
            show_animation(revolver_frames)
            break
        else:
            play_sound('Revclick.mp3')
            print("Click... Nothing Happens... ")
            time.sleep(1)


if __name__ == "__main__":
    
    russian_roulette()

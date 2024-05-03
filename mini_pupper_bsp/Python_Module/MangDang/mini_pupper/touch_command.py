from UDPComms import Publisher
import pygame
import netifaces as ni
from PIL import Image, ImageDraw, ImageFont
from enum import Enum
from MangDang.LCD.ST7789 import ST7789
import sounddevice as sd
import soundfile as sf
import time
import os
from display import Display
from helper_movement import *
import time
import RPi.GPIO as GPIO


def touch_init():
    # There are 4 areas for touch actions
    # Each GPIO to each touch area
    touchPin_Front = 6
    touchPin_Left  = 3
    touchPin_Right = 16
    touchPin_Back  = 2

    # Use GPIO number but not PIN number
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO numbers to input
    GPIO.setup(touchPin_Front, GPIO.IN)
    GPIO.setup(touchPin_Left,  GPIO.IN)
    GPIO.setup(touchPin_Right, GPIO.IN)
    GPIO.setup(touchPin_Back,  GPIO.IN)

def pygame_stuff():
    pygame.init()
    pygame.display.init()
    MESSAGE_RATE = 20
    win = pygame.display.set_mode((500, 250))
    
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)
    text_surface = font.render("Click to enable.", False, (220, 0, 0))
    win.fill((255, 255, 255))
    win.blit(text_surface, (40, 100))

def play_audio(filename):
    fs = 48000  # 48KHz, Audio sampling rate
    duration = 5  # Recording duration in seconds
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')
    print("Mini Pupper 2 audio playback start...")
    sd.play(data, fs)
    sd.wait()

if __name__ == "__main__":


    touchPin_Front = 6
    touchPin_Left  = 3
    touchPin_Right = 16
    touchPin_Back  = 2

    # Use GPIO number but not PIN number
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO numbers to input
    GPIO.setup(touchPin_Front, GPIO.IN)
    GPIO.setup(touchPin_Left,  GPIO.IN)
    GPIO.setup(touchPin_Right, GPIO.IN)
    GPIO.setup(touchPin_Back,  GPIO.IN)





    pub = Publisher(8830)
    pygame_stuff()
    disp = Display()
    pygame.event.pump()
    wait_time = 500
    MESSAGE_RATE = 20
    counter_a = 0
    counter_m = 0
    rx_ = 0.0
    ry_ = 0.0
    lx_ = 0.0
    ly_ = 0.0
    os.system("amixer -c 0 sset 'Headphone' 100%")
    #disp.show_image('moonphases/moon11.png')

    msg = reset()
    pub_msg(msg , wait_time)

    msg,counter_a = toggle_activation(counter_a)
    pub_msg(msg, wait_time)

    #msg,counter_m = toggle_movement(counter_m)
    #pub_msg(msg,wait_time)

    # msg = movement_rx_ry(0.3,0.3)
    # pub_msg(msg,wait_time)

    # msg = movement_rx_ry(0.3,0.3)
    # pub_msg(msg,wait_time)

    # msg = movement_rx_ry(0.3,0.3)
    # pub_msg(msg,wait_time)

    # msg = movement_rx_ry(0.3,0.3)
    # pub_msg(msg,wait_time)

    # msg = movement_rx_ry(0.3,0.3)
    # pub_msg(msg,wait_time)

    # msg = movement_rx_ry(0.3,0.3)
    # pub_msg(msg,wait_time)

    # msg,counter_m = toggle_movement(counter_m)
    # pub_msg(msg,wait_time)

    # audio_file = 'audio_files/gettysburg.wav'
    # play_audio(audio_file)

    count = 1   #first image for display
    image_path = f'moonphases/moon{count}.png'
    disp.show_image(image_path)  #default set to the full moon image

    while True:
        touchValue_Front = GPIO.input(touchPin_Front)
        touchValue_Back  = GPIO.input(touchPin_Back)
        touchValue_Left  = GPIO.input(touchPin_Left)
        touchValue_Right = GPIO.input(touchPin_Right)
        display_sting = ''

        if not touchValue_Front:
            display_sting += ' Front'
            disp.show_image('cropped.jpg')
            play_audio('meme_out.wav')

        if not touchValue_Back:
            display_sting += ' Back'
            break

        if not touchValue_Right:
            count += 1  # increment counter
            if count > 25:
                count = 1
            display_sting += ' Right'
            msg = movement_rx_ry(0.3, 0.3)
            image_path = f'moonphases/moon{count}.png'
            disp.show_image(image_path)
            pub_msg(msg, wait_time)

        if not touchValue_Left:
            count -= 1
            if count < 1:
                count = 25
            display_sting += ' Left'
            msg = movement_rx_ry(-0.3,-0.3)
            image_path = f'moonphases/moon{count}.png'
            disp.show_image(image_path)
            pub_msg(msg,wait_time)

        if display_sting == '':
            display_sting = 'No button touched'
        print(display_sting)
        time.sleep(0.5)

    msg = {
            "ly": 0,
            "lx": 0,
            "rx": 0,
            "ry": 0,
            "L2": 0,
            "R2": 0,
            "R1": 0,
            "L1": 0,
            "dpady": 0,
            "dpadx": 0,
            "x": 0,
            "square": 0,
            "circle": 0,
            "triangle": 0,
            "message_rate": 20,
        }
    pub.send(msg)
    #pygame.display.flip()
    pygame.time.wait(int(1000/20))

    msg = {
            "ly": 0,
            "lx": 0,
            "rx": 0,
            "ry": 0,
            "L2": 0,
            "R2": 0,
            "R1": 0,
            "L1": 1,
            "dpady": 0,
            "dpadx": 0,
            "x": 0,
            "square": 0,
            "circle": 0,
            "triangle": 0,
            "message_rate": 20,
        }
    pub.send(msg)
    #pygame.display.flip()
    pygame.time.wait(int(1000/20))










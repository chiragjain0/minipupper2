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

if __name__ == "__main__":
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

    disp.show_image('moonphases/moon11.png')

    msg = reset()
    pub_msg(msg , wait_time)

    msg,counter_a = toggle_activation(counter_a)
    pub_msg(msg, wait_time)

    msg,counter_m = toggle_movement(counter_m)
    pub_msg(msg,wait_time)

    msg,counter_a = toggle_activation(counter_a)
    pub_msg(msg, wait_time)

    msg,counter_m = toggle_movement(counter_m)
    pub_msg(msg,wait_time)








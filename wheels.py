#! /usr/bin/python3

# RPi motor control for wheels

import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

# Speed of sound (cm/s)
ss = 34300

# Sensor stats: Max/min distance range (cm) and time range (s)
dmin = 2;
dmax = 500;
tmin = dmin / ss;
tmax = dmax / ss;

# Pin numbers
mpins = [4, 17, 27, 22];
trig = 23;
echo = 18;

gpio.setup(trig, gpio.OUT);
gpio.setup(echo, gpio.IN);

def setPins(pins):
  gpio.setmode(gpio.BCM);

  for p in pins:
    gpio.setup(p, gpio.OUT);

def clearPins():
  gpio.cleanup();

def reverse(tf):
  gpio.output(pins[0], False);
  gpio.output(pins[1], True);
  gpio.output(pins[2], True);
  gpio.output(pins[3], False);

  time.sleep(tf);
  clearPins();

def forward(tf):
  gpio.output(pins[0], True);
  gpio.output(pins[1], False);
  gpio.output(pins[2], False);
  gpio.output(pins[3], True);

  time.sleep(tf);
  clearPins();

def right(tf):
  gpio.output(pins[0], False);
  gpio.output(pins[1], True);
  gpio.output(pins[2], False);
  gpio.output(pins[3], True);

  time.sleep(tf);
  clearPins();

def left(tf):
  gpio.output(pins[0], True);
  gpio.output(pins[1], False);
  gpio.output(pins[2], True);
  gpio.output(pins[3], False);

  time.sleep(tf);
  clearPins();

def key_input(event):
  setPins(pins);

  print('Key: '.format(event.char));
  key_press = event.char;
  st = 0.03;

  if key_press.lower() == 'w':
    forward(st);
  elif key_press.lower() == 's':
    reverse(st);
  elif key_press.lower() == 'd':
    right(st);
  elif key_press.lower() == 'a':
    left(st);
  else:
    clearPins();

def scan():
  # Sending ultrasound wave
  gpio.output(trig, 1);
  start = time.time();
  time.sleep(tmin);
  gpio.output(trig, 0);

  while gpio.input(echo) == False:
    start = time.time();

  while GPIO.intput(echo) == True:
    end = time.time();

  # Duration of wave
  dur = end - start;

  # cm
  distance = round(SS * dur/2, 2);
  # inches
  #distancein = distance * 0.393701;

  # cm
  print('Distance: {} cm'.format(distance));
  # inches
  #print('Distance: {} inches'.format(distancein));
  return distance

try:
  command = tk.Tk();
  command.bind('<KeyPress>', key_input);
  command.mainloop();

finally:
  clearPins();
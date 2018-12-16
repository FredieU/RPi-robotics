#! /usr/bin/python3

# RPi proximity sensor

import RPi.GPIO as GPIO
import time

# Speed of sound (cm/s)
SS = 34300;

# Sensor stats: Max/min distance range (cm) and time range (s)
dmin = 2;
dmax = 500;
tmin = dmin/SS;
tmax = dmax/SS;

# GPIO pin values
TRIG = 4;
ECHO = 18;
BEEP = 21;

# Setting GPIO pins to BCM naming convention
GPIO.setmode(GPIO.BCM);

# Setting pin types
GPIO.setup(TRIG, GPIO.OUT);
GPIO.setup(ECHO, GPIO.IN);
GPIO.setup(BEEP, GPIO.OUT);
GPIO.output(BEEP, 0);

def beep(interval):
  GPIO.output(BEEP, 1);
  time.sleep(interval);
  GPIO.output(BEEP, 0);

def shoot():
  # Sending ultrasound wave through TRIG
  GPIO.output(TRIG, 1);
  start = time.time();
  time.sleep(tmin);
  GPIO.output(TRIG, 0);

  while GPIO.input(ECHO) == False:
    start = time.time();

  while GPIO.input(ECHO) == True:
    end = time.time();

  # Duration of wave
  dur = end - start;

  # cm
  distance = round(SS * dur/2, 2);
  # inches
  #distancein = distance * 0.393701;

if distance < 150:
  beep(0.125);

  # cm
  print('Distance: {} cm'.format(distance));
  # inches
  #print('Distance: {} inches'.format(distancein));
  return distance

try:
  while True:
    distance = shoot();
    time.sleep(0.5);

finally:
  # Clear all pins
  GPIO.cleanup();

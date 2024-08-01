# Python Setup for DobotMagician using Dobot's API
## Required Equipment and Setup:
Dobot Magician('s) that are already set up with suction, gripper, and/or conveyer belt

Helpful github page that gives instructions of how to set up Dobot plus how to download control software: https://github.com/SERLatBTH/StarterGuide-DobotMagician?tab=readme-ov-file

Helpful vid to connect Dobot to conveyer belt: https://www.youtube.com/watch?v=1Gh26EeiiGM

Helpful vid to connect Dobot to gripper: https://www.youtube.com/watch?v=UfoEkJWgask

A working webcam setup is required to use opencv (I am using an intel webcam)

## What will be covered:
- How to control one Dobot
- How to control multiple Dobots
- How to control conveyer belt
- How to use opencv adjacent to dobots 

## Packages Needed
install V2 dobot files and unzip them: https://www.dobot.us/download/dobot-demo-v2-0/ 

install driver suitable for your computer: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads
## Helpful pages
describes many important features of the dobot api: https://github.com/SERLatBTH/StarterGuide-Dobot-Magician-with-Python
giv
### Resourses to try pydobot, a peer grown library to control dobots
https://github.com/sammydick22/pydobotplus: improved pydobot library

https://github.com/luismesas/pydobot: original pydobot

## Setup Code Instructions

download Dobot Demo (DOBOT Magician) v2.3 · Aug 23, 2021 off of https://www.dobot-robots.com/service/download-center?keyword=&products%5B%5D=316

download latest 32 bit python version suitable for your computer: https://www.python.org/downloads/release/python-3120/

I AM USING Python 3.12 32 bit version for Windows

install VS studio code: https://code.visualstudio.com/docs/setup/setup-overview

create virtual envirnoment on VS studio code with latest python 32 bit version as interpreter: https://code.visualstudio.com/docs/python/environments

open the DobotDemoForPython folder from the v2 files in virtual envirnoment

in the DobotDemoForPython folder read DobotD11Type.py and DobotControl.py to understand documentation and usage 

pip install cv2 and pySerial



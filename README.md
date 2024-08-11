# Python Setup for DobotMagician using Dobot's API + Dobot's API with OpenCV and pySerial
## Required Equipment and Setup:
Dobot Magician('s) that are already set up with suction, gripper, and/or conveyer belt

Helpful github page that gives instructions of how to set up Dobot: https://github.com/SERLatBTH/StarterGuide-DobotMagician?tab=readme-ov-file

Helpful vid to connect Dobot to conveyer belt: https://www.youtube.com/watch?v=1Gh26EeiiGM

Helpful vid to connect Dobot to gripper: https://www.youtube.com/watch?v=UfoEkJWgask

A working webcam setup is required to use opencv (I am using an intel webcam)

## What will be covered:
- How to control one Dobot: stackingblockscode: https://drive.google.com/file/d/1sZoxOxZeYifQYNI0_VIuU0d6AWnhdggi/view?usp=sharing
  
- How to control multiple Dobots: multipledobotspythondemo and anotherwaymultipledobots:
  https://drive.google.com/file/d/14JNtAFIdmHSAzK3MoNBoFvdx_u9PJEej/view?usp=sharing
  
- How to control conveyer belt: multipledobotspythondemo, anotherwaymultipledobots, and finalprojectopencv
  
- How to use opencv adjacent to dobots (detecting the largest areas of yellow and green and capturing the center of that object)(though the center is captured, it is not being used in the project, only the color detection part is): finalprojectopencv and opencvmethods
    - find_yellow_block and find_green_block methods work well to approx center for any shape other than triangles
    - The find_center_yellow_block and find_center_green_block methods work to approximate the center of all shapes, including triangles, as they use the centroid method to do it. However, they are very average at approximating the center compared to the find_yellow_block and find_green_block methods
    - https://drive.google.com/file/d/1OY45W_8M9R6e-G6WpFJ8hmwcoQd__hUc/view?usp=drive_link
    - https://drive.google.com/file/d/17xvwIs8j7ahAPq5-MYAatMkjl3f_uB1n/view?usp=sharing

## How to improve this project:
 - detect all shapes and then find the center of that object WITHOUT sorting by color (can do this with yolo)
 - convert dobot coordinates to the camera coordinate's center of the object, so that pick and place is not hardcoded (very useful, can use the centers from my opencv methdos)
 - instead of one object by one object, capture multiple objects on the conveyer belt and calculate center points of each object

## Packages Needed
install V2 dobot files and unzip them: https://www.dobot.us/download/dobot-demo-v2-0/ 

install driver suitable for your computer: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads
## Helpful pages
describes many important features of the dobot api: https://github.com/SERLatBTH/StarterGuide-Dobot-Magician-with-Python

youtube tutorials on OpenCV: https://www.youtube.com/playlist?list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn

Tech by Tim's github page on OpenCV: https://github.com/techwithtim/OpenCV-Tutorials/blob/main/README.md
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

copy and paste my opencvmethods code into a new file in your virtual workspace and name the file opencvmethods.py if you want to use my finalprojectopencv file



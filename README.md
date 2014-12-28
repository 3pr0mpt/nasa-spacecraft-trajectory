nasa-spacecraft-trajectory
==========================

## Description

This python2.7 script makes videos from still images captured on http://space.jpl.nasa.gov/ for multiple outer space missions: Juno, Cassini, New Horizons, Voyager I and Voyager II.

## Features

The main objective of this project is to see spacecraft trajectory in motion. Unfortunately NASA's website doesn't provide any video of spacecraft trajectory in http://space.jpl.nasa.gov/.
With this script, you'll be able to download still images of each day for each mission:
* Juno Mission (to Jupiter)
* Cassini Mission (to Saturn)
* New Horizons (to Pluto and further)
* Voyager I (Study of Solar System)
* Voyager II (Study of Solar System)

This script only downloads the images till "today" and never to the future. Once images are on disk, you can re-run the program in order to get ONLY the new images, downloading only the missing days.

## Screenshots
![Downloading images](http://i.imgur.com/3BAg0Tc.png)
![A 800x450 video is generated at the end](http://i.imgur.com/JwxiMjf.png)


### Requirements

Linux system. This script was successfully developed and tested on Ubuntu 14.10 (utopic) with the following packages:
* python2.7
* libav-tools (provides avconv)
* urllib2 (python module for downloading images)
* progress_bar (python module for showing a "non-intuitive" but useful status bar while downloading the files)
 
### Installing the script

Clone this repo to your Linux box (you must git installed before: ```sudo apt-get install git```)
* ```git clone git://github.com/3pr0mpt/nasa-spacecraft-trajectory.git```
* ```cd nasa-spacecraft-trajectory```
 
Install python 2.7, pip2 and avconv on Ubuntu (should also work with Debian)
* ```sudo apt-get install python2.7 python-pip libav-tools```

Install progress_bar
* ```sudo pip2 install progress_bar```

### Usage

Open a new terminal, and run:
* ```python2.7 ./nasa-spacecraft.py```

### About me

Nothing to say, just a simple sys admin with my head in the stars :)

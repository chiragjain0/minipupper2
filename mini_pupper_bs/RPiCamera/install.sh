#!/bin/bash
#
# This script configures a Raspberry Pi for use with a camera module.
# Version: 1.1
# Date: 2023-04-10

# Exit the script immediately if a command exits with a non-zero status
# set -x
set -e


# Get the directory where this script is located
BASEDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Update and upgrade the system
sudo apt update
sudo apt upgrade -y

# Install v4l2, a video capture utility
sudo apt install -y v4l-utils

# Edit the /boot/firmware/config.txt file to enable camera support
sudo sed -i 's/^camera_auto_detect=1/# camera_auto_detect=1/g' /boot/firmware/config.txt
echo "gpu_mem=128" | sudo tee -a /boot/firmware/config.txt
echo "start_x=1" | sudo tee -a /boot/firmware/config.txt

# Add the user to the video group to grant access to video devices
sudo usermod -aG video $USER

# Install xauth for PC(Ubuntu22.04) GUI Display
sudo apt install -y xauth

# Compile the dt-blob file to support the camera
cd $BASEDIR/dts
sudo dtc -I dts -O dtb -o /boot/firmware/dt-blob.bin dt-blob-cam1.dts
# For more details about the dts file, please refer to [https://datasheets.raspberrypi.org](https://datasheets.raspberrypi.org)

# Print successful information
echo "Camera settings successful, changes will be applied after the next reboot."

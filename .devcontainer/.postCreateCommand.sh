# !/bin/bash
sudo apt-get update && sudo apt-get -y upgrade

# Install FUSE
sudo apt-get install -y fuse

# Install required packages
pip install -r requirements.txt
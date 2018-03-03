#!/bin/bash
sudo docker build -t mynode .
clear
sudo docker run -it mynode node src/view/interface.js $1

#!/bin/bash
#!/usr/bin/bash
sudo docker build --no-cache -t mynode .
clear
sudo docker run -it mynode startGrid $1

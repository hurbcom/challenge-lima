#!/bin/bash
#!/usr/bin/bash
sudo docker build -t mynode .
clear
sudo docker run mynode npm test
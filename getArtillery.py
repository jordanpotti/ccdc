#!/bin/sh
 
wget https://github.com/JordanPotti/artillery/archive/master.zip
 
unzip master.zip
 
cd artillery-master
 
python setup.py
 
python /var/artillery/restart_server.py

#!/bin/sh
 
wget https://github.com/JordanPotti/artillery/archive/master.zip
 
unzip master.zip
 
cd artillery-master
 
/usr/local/bin/python2.7 setup.py
 
/usr/local/bin/python2.7 /var/artillery/restart_server.py

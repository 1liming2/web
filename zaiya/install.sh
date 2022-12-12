#!/bin/bash

sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y lib32gcc1
sudo apt-get install -y libcurl4-gnutls-dev:i386
sudo apt-get install -y screen

mkdir steamcmd
cd steamcmd

wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
tar -xvzf steamcmd_linux.tar.gz
./steamcmd.sh +login anonymous +force_install_dir ~/dst +app_update 343050 validate +quit

cp steamcmd/linux32/libstdc++.so.6 dst/bin/lib32/

mkdir -p .klei/DoNotStarveTogether/MyDediServer




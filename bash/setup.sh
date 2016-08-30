!/bin/bash

#A shell script to make your life easy,by installing commonly used software
#Suitable for a fresh installation of fedora 24
#Author: Aditya Konarde
#Date: 26 Aug 2016

#First, Update all packages to their latest available versions
echo 'Updating your system';
dnf update -y;
echo 'System Updated successfully';

#Install some essentials
echo 'Installing some good stuff';

#Install RPMFusion Repos
echo 'Installing RPMFusion Repos';
su -c 'dnf install -y http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm vlc gnome-tweak-tool';

#Install Fedy
echo 'Installing Fedy';
bash -c 'su -c "curl http://folkswithhats.org/fedy-installer -o fedy-installer && chmod +x fedy-installer && ./fedy-installer"'

#Install Tuned Utility
echo 'Installing Tuned';
dnf install tuned -y;
systemctl enable tuned;

#Install Redshift-Gtk, Because your eyes are precious
echo 'Installing Redshift'
dnf install redshift-gtk -y;
echo 'Installed Redshift';

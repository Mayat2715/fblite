#!usr/bin/bash
pkg install python -y
pkg install cowsay -y
pip install requests==2.22.0
pip install mechanize==0.4.2
cd '/data/data/com.termux/files/usr/lib/python3.7/site-packages/'
if [ -r mechanize ]; then
	echo ''
else
	cp -rf '/data/data/com.termux/files/usr/lib/python2.7/site-packages/mechanize' .
fi
if [ -r request ]; then
	echo ''
else
	cp -rf '/data/data/com.termux/files/usr/lib/python2.7/site-packages/requests' .
fi

#!usr/bin/bash
pat='/data/data/com.termux/files/usr/lib/python3.7/site-packages'
put='/data/data/com.termux/files/usr/lib/python2.7/site-packages'
pkg install python -y
pkg install cowsay -y
pip install requests==2.22.0
pip install mechanize==0.4.2
cd $pat
if [ -r mechanize ]; then
	echo ''
else
	cp -rf "$put/mechanize*" $pat
fi
if [ -r request ]; then
	echo ''
else
	cp -rf "$put/requests*" $pat
fi

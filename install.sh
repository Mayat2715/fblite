#!usr/bin/bash
if [ $(uname -o) = 'Android' ];then
	pat='/data/data/com.termux/files/usr/lib/python3.7/site-packages'
	put='/data/data/com.termux/files/usr/lib/python2.7/site-packages'
	pkg install python cowsay -y
	pip install requests==2.22.0 mechanize==0.4.2
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
elif [ $(uname -o) = 'GNU/Linux' ]; then
	pkg install python cowsay -y
	pip install requests==2.22.0 mechanize==0.4.2
else
	echo -e "gagal :( \n Silahkan hubungi saya"
fi

import requests,re,os,urllib
'''Jangan direcode ya
nanti scriptnya gak bisa dipake kalo direcode'''
down = urllib.request.urlretrieve
link = "https://github.com/Mayat2715/fblite/raw/master/"
try:
    ls = requests.get("https://github.com/Mayat2715/fblite/raw/master/README.md")
    sl = ls.text
    q = re.search(r"versi: (.*?)\n",sl).group().replace("\n","")
    ch = os.listdir()
    if '.versi.txt' in ch:
        pass
    else:
        open(".versi.txt","w").write("")
    check = open(".versi.txt","r").read()
    if q == check:
        print("Tidak ada pembaharuan!")
    else:
        print("Ada pembaharuan\nMenginstall...")
        down(link+"main.py","./main.py")
        down(link+"install.sh","./install.sh")
        down(link+"update.py","./update.py")
        open(".versi.txt","w").write(q)
        print("Selesai")
except Exception as eeq:
    print(eeq)

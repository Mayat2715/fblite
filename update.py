import requests,re,os,urllib
'''Jangan direcode ya
nanti scriptnya gak bisa dipake kalo direcode'''

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
        urllib.request.urlretrieve("https://github.com/Mayat2715/fblite/raw/master/main.py","/data/data/com.termux/files/home/fblite/main.py")
        open(".versi.txt","w").write(q)
        print("Selesai")
except Exception as eeq:
    print(eeq)

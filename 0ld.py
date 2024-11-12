#coding=utf-8
# Github : https://github.com/HUNTER
# Whatsapp : +92351830318
# More About : https://bio.link/HUNTER
import os, sys, platform
print('\033[0;97m [√]\033[92m join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/GjKY8C8AMhNJLwhKzCBQtr')
os.system('clear')
print('\033[0;97m [√] \033[92mChecking For Updates...')
os.system('git pull --quiet 2>/dev/null')
os.system("pip install fake_useragent")
bit = platform.architecture()[0]
if bit == '64bit':
    import old
elif bit == '32bit':
    print("\033[1;90m [\033[1;91m Sorry Baby 32 Bit Not Supported! 🥺💔 \033[1;90m]");exit()
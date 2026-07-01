import os
import time
import sys

# Color codes
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m"   # White
]
reset = "\033[0m"

# Password check
os.system('clear')
print(colors[3] + "Script run korte password din:" + reset)
password = input("Password: ")

if password != "ramesh":
    print(colors[0] + "\n[ Wrong password! Access denied ]" + reset)
    sys.exit()

# ASCII Banner frames
banner_frames = [
    r"""
     
  
     /$$$$$$   /$$$$$$  /$$$$$$$                                  
 /$$__  $$ /$$__  $$| $$__  $$                                 
| $$  \__/| $$  \__/| $$  \ $$                                 
| $$      |  $$$$$$ | $$$$$$$                                  
| $$       \____  $$| $$__  $$                                 
| $$    $$ /$$  \ $$| $$  \ $$                                 
|  $$$$$$/|  $$$$$$/| $$$$$$$/                                 
 \______/  \______/ |_______/                                  
                                                               
                                                               
                                                               
 /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$  /$$$$$$  /$$   /$$
| $$__  $$ /$$__  $$| $$$    /$$$| $$_____/ /$$__  $$| $$  | $$
| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$      | $$  \__/| $$  | $$
| $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$$$$   |  $$$$$$ | $$$$$$$$
| $$__  $$| $$__  $$| $$  $$$| $$| $$__/    \____  $$| $$__  $$
| $$  \ $$| $$  | $$| $$\  $ | $$| $$       /$$  \ $$| $$  | $$
| $$  | $$| $$  | $$| $$ \/  | $$| $$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|__/  |__/|__/     |__/|________/ \______/ |__/  |__/
                            
                                                                                 
    """,
    r"""
     
  
/$$$$$$   /$$$$$$  /$$$$$$$                                  
 /$$__  $$ /$$__  $$| $$__  $$                                 
| $$  \__/| $$  \__/| $$  \ $$                                 
| $$      |  $$$$$$ | $$$$$$$                                  
| $$       \____  $$| $$__  $$                                 
| $$    $$ /$$  \ $$| $$  \ $$                                 
|  $$$$$$/|  $$$$$$/| $$$$$$$/                                 
 \______/  \______/ |_______/                                  
                                                               
                                                               
                                                               
 /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$  /$$$$$$  /$$   /$$
| $$__  $$ /$$__  $$| $$$    /$$$| $$_____/ /$$__  $$| $$  | $$
| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$      | $$  \__/| $$  | $$
| $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$$$$   |  $$$$$$ | $$$$$$$$
| $$__  $$| $$__  $$| $$  $$$| $$| $$__/    \____  $$| $$__  $$
| $$  \ $$| $$  | $$| $$\  $ | $$| $$       /$$  \ $$| $$  | $$
| $$  | $$| $$  | $$| $$ \/  | $$| $$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|__/  |__/|__/     |__/|________/ \______/ |__/  |__/
                            
                                                      
    """
]

# Show banner as animation
os.system('clear')
for i in range(6):
    os.system('clear')
    print(colors[i % len(colors)] + banner_frames[i % len(banner_frames)] + reset)
    time.sleep(0.3)

# Banglish message
print(colors[2] + "\nPriyo user,\nEi tool ta use kore apni notun ekta experience pete cholen.\nDoya kore responsibly use korun. Thank you!" + reset)

# Social media
print(colors[4] + "\nMy Facebook ID name: RAMESH")
print("My Telegram ID name: @Ramesh152" + reset)

# Final message
print(colors[1] + "\n\n=========================================================")
print("Assalamu Alaikum RAMESH VAI")
print("Ami RAMESH, apnar script ta edit sompurno bhabe korte perechi.")
print("=========================================================" + reset)
import logging, os, platform
from os import system
try:
    import psutil
except:
    system("python -m pip install psutil")
    import psutil

total_memory = psutil.virtual_memory().total / (1024 ** 3)
gpu = GPUtil.getGPUs()
print(gpu)
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='[%(levelname)s] %(message)s')

logging.info(f"CPU Name: {platform.processor()}.")
logging.info(f"CPU Cores: {psutil.cpu_count(logical=False)}.")
logging.info(f"CPU Threads: {os.cpu_count()}.")
for i in psutil.cpu_freq(percpu=True):
    logging.info(f"CPU Frequency: {i.current / 1000}GHz.")

logging.info(f"Total RAM: {round(total_memory)}GB.")
if platform.system() == "Windows":
    logging.info(f"Operating System: {platform.system()} {platform.win32_ver()[1]}.")
else:
    logging.info(f"Operating System  {platform.system()}.")
    logging.info(f"Operating System Version: {platform.release()}")

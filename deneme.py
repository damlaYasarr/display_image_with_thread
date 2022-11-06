import threading
from PIL import Image

from time import sleep
local_path = '/home/damlayasarr/threadExample/images/bisi.png'
def load_img(local_path):
    img=Image.open(local_path)
    img.show()



img_thread = threading.Thread(target=load_img, args=(local_path,))
img_thread.start()
while img_thread.is_alive():
    print(img_thread)
    print (f"doing some other stuff while the thread does its thing")
    sleep(1)
img_thread.join()
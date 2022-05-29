import asyncio
from itertools import count
import threading
from time import monotonic, monotonic_ns
from pynput.keyboard import Listener, Key
from pynput.mouse import Listener as lt

prev_time = 0
curr_time = 0
cnt = 0
arr = [0] * 4
def on_release(key):
    if(key == Key.backspace): 
        listener.stop()
    print("\n\nKey pressred")
    global prev_time
    global cnt
    curr_time = monotonic_ns()
    diff = (curr_time - prev_time+1)/1000000000
    prev_time = curr_time
    print("Diff : ", diff)
    cnt += 1
    print(cnt)
    arr[cnt%4] = diff
    print("arr : ", arr[0], arr[1], arr[2], arr[3])
    print("Sum arr : ", sum(arr)/4)
    print("APM", (60 / (sum(arr)/4)))
# with Listener as listener:
#     listener.join()

def on_click(x,y):
    print("bla")
    print(monotonic_ns())



def apm():
    _thread = threading.Thread(target=asyncio.run, args=(Listener(on_release=on_release, on_click=on_click)))
    _thread.start()
    

apm()
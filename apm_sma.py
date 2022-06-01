import time
from pynput.keyboard import Listener, Key
from pynput.mouse import Listener as MouseListener


def handle_click():
        global running, input_list, list_lengh, previous_press, number_of_total_button_presses, correction_factor
        current_press = time.perf_counter_ns()
        time_since_last_press = (current_press - previous_press) / (10**9)
        input_list[number_of_total_button_presses %
                list_lengh] = time_since_last_press
        number_of_total_button_presses += 1
        previous_press = current_press
        correction_factor = 1
        # print(f'{key} was pressed. After {time_since_last_press:.3f} idle time.\nNumber of Presses = {number_of_total_button_presses}')
        # print(str(input_list))
        print("APM = ", 60/(sum(input_list)/list_lengh), end='\r')


def on_release(key):
    global listener
    if(key == Key.backspace):
        listener.stop()
        print(f"You clicked a total of {number_of_total_button_presses} times")
    handle_click()


def on_click(x, y, button, pressed):
    if(pressed):
        # print("clicked mouse key " )
        handle_click()


running = True
delay = 0.25
list_lengh = 10
input_list = [0] * list_lengh

number_of_total_button_presses = 0
previous_press = time.process_time_ns()

mouseListener = MouseListener(on_click=on_click)
listener = Listener(on_release=on_release)
mouseListener.start()
listener.start()
correction_factor = 1



while(listener.running):
    time.sleep(.25)
    print(listener.running)
    last_press = (time.perf_counter_ns() - previous_press) / (10**9)

    if(last_press > 1):
        # print("hi ", last_press)
        previous_press = time.perf_counter_ns()
        input_list[number_of_total_button_presses %
                list_lengh] = 10 * correction_factor
        # print(input_list[number_of_total_button_presses % list_lengh])
        correction_factor *= 1.5
        number_of_total_button_presses += 1
        # print(str(input_list), end='\r')
        print("APM = ", 60/(sum(input_list)/list_lengh), end='\r')
        # if label:
        #     label.update()

print("Finished!")



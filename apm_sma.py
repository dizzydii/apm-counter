import time
from pynput.keyboard import Listener, Key
from pynput.mouse import Listener as MouseListener


def handle_click(idle=None, last_press=None, apm_sma=None):
        if not apm_sma:
            return "No Object was given"

        if not idle:
            apm_sma.current_press = time.perf_counter_ns()
            apm_sma.time_since_last_press = (apm_sma.current_press - apm_sma.previous_press) / (10**9)
            apm_sma.time_diff_tracked_inputs_list[apm_sma.number_of_tracked_events %
                    apm_sma.number_of_tracked_inputs] = apm_sma.time_since_last_press
            
            apm_sma.number_of_total_button_presses +=1
            apm_sma.number_of_tracked_events += 1
            apm_sma.previous_press = apm_sma.current_press
            apm_sma.correction_factor = 1
        else:
            apm_sma.previous_press = time.perf_counter_ns()
            apm_sma.time_diff_tracked_inputs_list[apm_sma.number_of_tracked_events %
                    apm_sma.number_of_tracked_inputs] = 3 * apm_sma.correction_factor
            apm_sma.correction_factor *= 1.5
            apm_sma.number_of_tracked_events += 1
            print(str(apm_sma.time_diff_tracked_inputs_list))
        return (60/(sum(apm_sma.time_diff_tracked_inputs_list)/apm_sma.number_of_tracked_inputs))    
        print("APM = ", 60/(sum(apm_sma.time_diff_tracked_inputs_list)/apm_sma.number_of_tracked_inputs), end='\r')


class apm_sma():
    def on_press(self, key):
        if key in self.COMBINATION:
            print(key)
            self.current.add(key)
            if all(k in self.current for k in self.COMBINATION):
                #print('All modifiers active!')
                self.listener.stop() # terminate listener and program


    def on_release(self, key):
        self.apm = handle_click(apm_sma=self)
        try:
            self.current.remove(key)
        except KeyError:
            pass
           

    def on_click(self, x, y, button, pressed):
        if(pressed):
            #print("clicked mouse key " )
            return
        self.apm = handle_click(apm_sma=self)

    
    def idle(self):
        last_press = (time.perf_counter_ns() - self.previous_press) / (10**9)
        if(last_press > 1):
            if(self.apm > 10):
                self.apm = handle_click(True, last_press, apm_sma=self)
            else:
                self.apm = 0
              

    def __init__(self, number_of_tracked_inputs=12, apm_label=None) -> None:        
        self.COMBINATION = {Key.backspace, Key.ctrl_l}
        self.current = set()

        self.number_of_tracked_inputs = number_of_tracked_inputs
        self.time_diff_tracked_inputs_list = [0] * number_of_tracked_inputs

        self.number_of_total_button_presses = 0
        self.number_of_tracked_events = 0
        
        self.previous_press = time.process_time_ns()            
        self.correction_factor = 1                              # correction_factor to increase the apm_penalty for being idle each cycle 

        self.listener = Listener(on_release=self.on_release, on_press=self.on_press)
        self.mouseListener = MouseListener(on_click=self.on_click)
        self.mouseListener.start()
        self.listener.start()
        
        
        self.label = apm_label

        self.apm = 0

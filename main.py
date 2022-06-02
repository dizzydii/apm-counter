import PySimpleGUI as sg

from apm_sma import apm_sma

sg.theme('SystemDefault')
layout =    [
    #[sg.Push(), sg.Button("Exit", button_color = ("#AAAA00", "#00AAAA"), key = "-EXIT-")],
    [sg.VPush()],
    [sg.Text("0 APM", key = "-APM-", font=("Helvetica", 25))],
    [sg.VPush()]]

window = sg.Window('APM Display', 
        layout,
        size = (300,80),
        no_titlebar = False,
        element_justification = 'right')

apm_object = apm_sma()

while True:
    event, values = window.read(timeout_key="-TIMEOUT_KEY-", timeout=1000)
    window['-APM-'].update(value=str(round(apm_object.apm))+ " APM")
    
    if event == "-TIMEOUT_KEY-":
        apm_object.idle()
        window['-APM-'].update(value=str(round(apm_object.apm))+ " APM")

    if((event == "-EXIT-") | (not apm_object.listener.running) | (event == sg.WIN_CLOSED)):
        break

window.close()
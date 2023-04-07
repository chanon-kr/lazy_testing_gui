# Core
import PySimpleGUI as sg
# Tabs
from tab.port import port_tab, test_port
from tab.socket import socket_tab, test_socket

# Create the Tab Layout
tab_group_layout = [[port_tab(), socket_tab()]]
# tab_group_layout = [[]]

# Put Tab into the Layout
layout = [[sg.Text('Lazy Testing', size=(10, 1), font='Helvetica 14'), ],
          [sg.TabGroup(tab_group_layout,enable_events=True,key='-TABGROUP-')],
          [sg.Text('version 1.00',key = 'Version', justification='right')]]

# Create Window
window = sg.Window('Py Topping Testing GUI' , layout , finalize=True, resizable=True) 

# Event Loop 
while True:
    # Get Value
    event, values = window.read()
    print(values)
    # Port TEST
    if event == '-PORT-TEST-' : 
       window.start_thread(lambda : test_port(values, window), '-PORT-SEND-END-')
    # Socket TEST
    if event == '-SOCKET-TEST-' :
        window.start_thread(lambda : test_socket(values, window), '-SOCKET-SEND-END-')
    # When close window or press Close
    if event in (sg.WIN_CLOSED, 'Close'): break

# Close window
window.close()
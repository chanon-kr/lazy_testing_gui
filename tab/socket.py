# Core
import PySimpleGUI as sg

# Design Layout
def socket_tab() :
    tab_layout = [  
                    [sg.Combo(['SEND','RECEIVE'], size = (10,2) , enable_events=False, key='-SOCKET-LIST-')] ,
                    [sg.Text('IP or Hostname', size=15)         , sg.InputText(key='-SOCKET-IP-')],
                    [sg.Text('Port', size=15)                   , sg.InputText(key='-SOCKET-PORT-')],
                    [sg.Text('Sending Message', size=15)        , sg.InputText(key='-SOCKET-MESSAGE-')],
                    [sg.Checkbox('Loop listening', key= '-SOCKET-LOOP-')],
                    [sg.Button('TEST', key='-SOCKET-TEST-', size=(10, 1)), sg.Button('STOP', key='-SOCKET-STOP-', size=(10, 1))],
                    [sg.Text(key='-SOCKET-RESULT-')]
                 ]
    return sg.Tab('TCP/IP', tab_layout, font='Courier 15', key='-SOCKET-')

# Test Socket Function
def test_socket(values, window) :
    from py_topping.data_connection.socket import lazy_TCP
    try :
        # Create Based Socket
        socket_base = lazy_TCP(host= values['-SOCKET-IP-'], port= int(values['-SOCKET-PORT-']))
        # Receving Test
        if values['-SOCKET-LIST-'] == 'RECEIVE' :
            window['-SOCKET-RESULT-'].update('Listening...')
            receive_message = socket_base.listen()
            out = receive_message
            window['-SOCKET-RESULT-'].update(out)
        # Sending Test
        else : 
            window['-SOCKET-RESULT-'].update('Sending...')
            socket_base.send(send_message= values['-SOCKET-MESSAGE-'], wait_return= False)
            out = '-SOCKET- Send OK'
    except Exception as e:
        # Store error if needed
        out = str(e)
    finally :
        # Update Result
        window['-SOCKET-RESULT-'].update(out)
# Core
import PySimpleGUI as sg

# Design Layout
def port_tab() :
    tab_layout = [ 
                    [sg.Text('IP or Hostname', size=15) ,sg.InputText(key='-PORT-IP-')],
                    [sg.Text('Port', size=15)           ,sg.InputText(key='-PORT-PORT-')],
                    [sg.Button('TEST', key='-PORT-TEST-', size=(10, 1))],
                    [sg.Text(key='-PORT-RESULT-')]
                 ]
    return sg.Tab('PORT', tab_layout, font='Courier 15', key='-PORT-')

# Test Port Function
def test_port(values, window) :
    from py_topping.general_use import check_port
    window['-PORT-RESULT-'].update('Sending...')
    try :
        # Create Based Socket
        result = check_port(values['-PORT-IP-'], values['-PORT-PORT-'])
        if result : out = '-PORT- OPEN'
        else : out = '-PORT- CLOSE'
    except Exception as e:
        # Store error if needed
        out = str(e)
    finally :
        # Update Result
        window['-PORT-RESULT-'].update(out)
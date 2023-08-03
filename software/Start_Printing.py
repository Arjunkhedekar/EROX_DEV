import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import webbrowser
import pywinauto
def start_printing(file_path):
    progmam_path = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
    # file_path = r'C:\Users\A\Desktop\Atharva\erox\software\trail1.pdf'

    app = Application().start(r'{} "{}"'.format(progmam_path, file_path))

    time.sleep(3)

    send_keys('^a^P')

    time.sleep(4)

    w_hanlde = pywinauto.findwindows.find_windows(title=u'Print')[0]
    window = app.window(handle=w_hanlde)
    window.wait('ready', timeout=10)


    window[u'Pri&nter:comboBox'].select(0)
    # window[u'&Properties'].click()
    # time.sleep(8)

    # w_hanlde_1 = pywinauto.findwindows.find_windows(best_match=u'Properties')[0]
    # window1= app.window(handle=w_hanlde_1)
    # window1.wait('ready', timeout=10)

    # window1[u'Job Type:comboBox'].select('Sample Set')
    # window1[u'2-sided Printing:comboBox'].select('1-sided Print')
    # window1.selectPaper.click_input()
    # send_keys("{VK_DOWN}")
    # send_keys("{RIGHT}")
    # send_keys("{RIGHT}")
    # send_keys("{VK_DOWN}")
    # send_keys("{ENTER}")

    # window1.selectPaper.click_input()
    # send_keys("{VK_DOWN}")
    # send_keys("{VK_DOWN}")
    # send_keys("{VK_DOWN}")
    # send_keys("{VK_DOWN}")
    # send_keys("{RIGHT}")
    # send_keys("{VK_DOWN}")
    # send_keys("{ENTER}")

    window[u'Print in gra&yscale(black and white)'].click()
    time.sleep(2)

    # copies_dropdown = window.child_window(title='&Copies', control_type='ComboBox')
    # copies_dropdown.select('2')
    window[u'Shrink oversized pages'].click()
    time.sleep(2)

    window[u'Auto'].click()
    time.sleep(2)

    window.Print.click()
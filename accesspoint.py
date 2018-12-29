from pywinauto.application import Application
from pywinauto.keyboard import SendKeys, KeySequenceError
import pywinauto
import pyperclip

delete_files = ['config.txt', 'capwap-saved-config', 'capwap-saved-config-bak', 'private-multiple-fs']
app = Application().connect(process = 11864)

dlg = app.window(title = "COM1 - PuTTY", class_name="PuTTY")

for file in delete_files:
	dlg.type_keys('delete flash:' + file + '{ENTER}')
	dlg.type_keys('y{ENTER}')

dlg.type_keys('reset')
dlg.type_keys('en')
dlg.type_keys('Cisco')


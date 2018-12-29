from pywinauto.application import Application
from pywinauto.keyboard import SendKeys, KeySequenceError
import pyperclip
import time

delete_files = ['config.txt', 'capwap-saved-config', 'capwap-saved-config-bak', 'private-multiple-fs']
app = Application().connect(process = 11864)

dlg = app.window(title = "COM1 - PuTTY", class_name="PuTTY")

for file in delete_files:
	dlg.type_keys('delete flash:' + file + '{ENTER}')
	sleeptime(5)
	dlg.type_keys('y{ENTER}')
	sleeptime(10)

dlg.type_keys('reset')
sleeptime(120) #estimate amount of time for the AP to reset.
login()

#script one
pyperclip.copy('debug capwap console cli\ndebug capwap client no-reload\nlwapp ap ip address 172.28.128.6 255.255.255.0\nlwapp ap ip default-gateway 172.28.128.7\nconfig t\nno ip domain-lookup\nexit\narchive download-sw /overwrite /reload tftp://172.28.128.7/c1140-k9w7-tar.124-25d.JA2.tar')
dlg.type_keys('+{INS}')

sleeptime(120) #estimate amount of time for new software to install
dlg.type_keys('delete /force /recursive flash:c1140-k9w8-mx.153-3.JC5')
sleeptime(10)
dlg.type_keys('delete /force /recursive flash:c1140-k9w8-mx.153-3.JC6')
sleeptime(10)
dlg.type_keys('reload')
dlg.type_keys('n')
sleeptime(60)
login()

#script two
pyperclip.copy('version 12.4\nno service pad\nservice timestamps debug datetime msec\nservice timestamps log datetime msec\nservice password-encryption\n!\nhostname ap.nhscisco.com\n!\nlogging rate-limit console 9\nenable secret 5 $1$SM3A$xV9VkrtdBVPvnsTI0HZeS1\n!\nno aaa new-model\n!\n!\ndot11 syslog\ndot11 vlan-name wifivlan vlan 1\n!\ndot11 ssid school\n   vlan 1\n   authentication open\n   authentication key-management wpa version 2\n   guest-mode\n   wpa-psk ascii 7 003716070C5A1C0D1C701E1D\n!\ndot11 arp-cache\n!\n!\nusername Cisco password 7 00271A150754\nusername rotary privilege 15 secret 5 $1$UVUC$ttarizYxT3ju462T4FP0k1\n!\n!\nbridge irb\n!\n!\ninterface Dot11Radio0\n no ip address\n no ip route-cache\nno shutdown\n !\n encryption vlan 1 mode ciphers aes-ccm\n !\n ssid school\n !\n antenna gain 0\n station-role root\n!\ninterface Dot11Radio0.1\n encapsulation dot1Q 1 native\n no ip route-cache\n bridge-group 1\n bridge-group 1 subscriber-loop-control\n bridge-group 1 block-unknown-source\n no bridge-group 1 source-learning\n no bridge-group 1 unicast-flooding\n bridge-group 1 spanning-disabled\n!\ninterface Dot11Radio1\n no ip address\n no ip route-cache\nno shutdown\n !\n encryption vlan 1 mode ciphers aes-ccm\n !\n ssid school\n !\n antenna gain 0\n dfs band 3 block\n channel dfs\n station-role root\n!\ninterface Dot11Radio1.1\n encapsulation dot1Q 1 native\n no ip route-cache\n bridge-group 1\n bridge-group 1 subscriber-loop-control\n bridge-group 1 block-unknown-source\n no bridge-group 1 source-learning\n no bridge-group 1 unicast-flooding\n bridge-group 1 spanning-disabled\n!\ninterface GigabitEthernet0\n no ip address\n no ip route-cache\n duplex auto\n speed auto\n no keepalive\n!\ninterface GigabitEthernet0.1\n encapsulation dot1Q 1 native\n no ip route-cache\n bridge-group 1\n no bridge-group 1 source-learning\n bridge-group 1 spanning-disabled\n!\ninterface BVI1\n ip address dhcp\n no ip route-cache\nno shutdown\n!\nip http server\nno ip http secure-server\nip http help-path http://www.cisco.com/warp/public/779/smbiz/prodconfig/help/eag\nbridge 1 route ip\n!\n!\n!\nline con 0\nline vty 0 4\n login local\n!\nend\n\ncopy run start')
dlg.type_keys('+{INS}')

func sleeptime(n):
	time.sleep(n)

func login():
	dlg.type_keys('en')
	sleeptime(5)
	dlg.type_keys('Cisco')
	sleeptime(5)

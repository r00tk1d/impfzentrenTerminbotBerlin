#setup: download and install Chromedriver + pip install Selenium
#run: python3 huimpf.py


from selenium import webdriver
import time 
import os

url = 'https://zeh2.zeh.hu-berlin.de/angebote/aktueller_zeitraum/_Impfangebot_fuer_HU_Mitarbeitende.html'
while True:
	browser = webdriver.Chrome()
	browser.get(url)
	time.sleep(3)

	while not browser.find_elements_by_class_name('bs_btn_buchen'):
		print('no buchen button found')
		time.sleep(3)
		browser.refresh()
	print('website changed')
	browser.switch_to.window(browser.current_window_handle)
	os.system('play -nq -t alsa synth {} sine {}'.format(1, 440))
	time.sleep(9999999)
	

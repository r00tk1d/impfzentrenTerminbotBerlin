# start the bash script impfbot.sh for running this script for all Impfzentren in Berlin

# If you want just specific Impfzenttren, start the script in the terminal with 0, 1, 2, 3, 4 or 5 for each Impfzentrum (for example for Arena Berlin type: python3 impfbot2.py 0)

# If the time is already booked, please restart the bash script

from selenium import webdriver
import time 
import os
import sys

impfzentrum = int(sys.argv[1])
names = ['Arena Berlin', 
'Messe Berlin', 
'Erika-Heß-Eisstadion', 
'Velodrom Berlin', 
'Flughafen Tegel', 
'Flughafen Tegel (Moderna)']
urls = ['https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158431',
'https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158434', 
'https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158437', 
'https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158435', 
'https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158436', 
'https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-191612']

while True:
	browser = webdriver.Chrome()
	browser.maximize_window()
	browser.get(urls[impfzentrum])
	time.sleep(3)
	
	# or not browser.find_elements_by_xpath("//*[contains(text(), 'Juni 2021')]")
	while not browser.find_elements_by_class_name('availabilities-message'):
		print('searching at ', names[impfzentrum])
		browser.refresh()
		time.sleep(1)
	browser.find_element_by_css_selector('button.Tappable-inactive.dl-button-small-primary.dl-button.dl-button-size-normal').click()
	print('NEW DATE FOUND at ', names[impfzentrum], '. Go to your Browser to check specific dates.')
	browser.switch_to.window(browser.current_window_handle)
	os.system('play -nq -t alsa synth {} sine {}'.format(0.1, 440))
	time.sleep(999999)




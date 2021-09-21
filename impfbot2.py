# this bot tries to book your two appointments. Its experimental and doesn't work always but can be run in background without the need of a fast user. However after the two appointments are booked, the user need to put further informations into the form to really get the appointments.

#start the script for all Impfzentren with the bash script impfbot2.sh

# or start the script in the terminal with 0, 1, 2, 3, 4 or 5 for specific Impfzentrum (for example for Arena Berlin type: python3 impfbot2.py 0)

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
	time.sleep(2)
	
	# currently only searching for appointments in "Juni 2021"
	#not browser.find_elements_by_class_name('availabilities-message') or
	while not browser.find_elements_by_xpath("//*[contains(text(), 'Juni 2021')]"):
		print('searching at ', names[impfzentrum])
		browser.refresh()
		time.sleep(1)
	print('NEW DATE FOUND at ', names[impfzentrum])
	browser.switch_to.window(browser.current_window_handle)
	os.system('play -nq -t alsa synth {} sine {}'.format(0.1, 440))
	try:
		# select date
		browser.find_element_by_css_selector('button.Tappable-inactive.dl-button-small-primary.dl-button.dl-button-size-normal').click()
		time.sleep(1)
		# select first time
		available_first_times = browser.find_elements_by_css_selector('div.Tappable-inactive.availabilities-slot')
		for impf_time in available_first_times:
			impf_time.click()
		time.sleep(2)
		# select second time
		available_second_times = browser.find_elements_by_css_selector('div.Tappable-inactive.availabilities-slot')
		for impf_time in available_second_times:
			impf_time.click()
		os.system('play -nq -t alsa synth {} sine {}'.format(4, 440))
		print('Possible Impftermine found. Please go into the browser to fill your informations.')
		time.sleep(999999)
	except:
		print("date at", names[impfzentrum], "no longer available. I'll try to be faster next time")
		pass


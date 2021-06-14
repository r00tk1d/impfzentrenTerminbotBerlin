
# Impfterminbot Berlin Impfzentren

This is a bot for getting an Impftermin in an Impfzentrum in Berlin via doctolib.


## Installation 

You need Python, Selenium and the Chromedriver for this bot

Install Selenium:

```bash 
  pip install Selenium
```

Install Chromedriver:
Download from https://chromedriver.chromium.org/downloads and unzip it. Then:

```bash 
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```
## Usage

There are two scripts:

Semiautomatic: impfbot.py and impfbot.sh:

This script just search for new available dates
 and notifies you with a sound and opens the browser so 
 you can choose the exact date and time. The bash script runs the script for 
 all six Impfzentren in Berlin.

Automatic: impfbot2.opy and impfbot2.sh:

This script additionally tries to book the two appointments, because this is first 
come, first serve. It is experimental. After finishing, you got two appointments and 
don't need to be fast. You just have to fill your information in the browser soon, to finish 
the process and getting the two appointments. The bash script runs the script for 
 all six Impfzentren in Berlin.

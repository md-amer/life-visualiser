# Life visualizer
# By Amer

from datetime import datetime, timedelta
from time import sleep
from mpmath import mpf, mp

mp.dps = 10

current = datetime.now()

def update_current_time():
    global current
    current = datetime.now()

#Take user's birthday as input
birth_year = 2000
birth_month = 1
birth_day = 1
birth_time = 0

birth = datetime(birth_year, birth_month, birth_day, birth_time)

#Take user's gender as input
gender = 'male'

#Calculate how much time has passed
def time_passed_func():
    global current
    global birth
    global time_passed
    time_passed = current - birth

time_passed_func()  
  
time_passed_sec = time_passed.total_seconds()

def update_time_passed():
    global time_passed
    global time_passed_sec
    global current
    global birth
    time_passed = current - birth
    time_passed_sec = time_passed.total_seconds()
    
#Calculate total life span
if gender == 'male':
    total_life_date = birth + timedelta(days=25258)
if gender == 'female':
    total_life_date = birth + timedelta(days=26207)

total_life = total_life_date - birth 

total_life_sec = total_life.total_seconds()

#Ratio function
percent_passed = mpf(time_passed_sec) / mpf(total_life_sec) * 100

def update_percent_passed():
    global percent_passed
    percent_passed = mpf(time_passed_sec) / mpf(total_life_sec) * 100

def run():
    while True:
        output=percent_passed
        update_current_time()
        update_time_passed()
        update_percent_passed()
        print(output)
        sleep(0.2)
  
run()






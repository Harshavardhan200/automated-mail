##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib as sm
import random
import datetime as dt
# 1. Update the birthdays.csv
letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
data = pd.read_csv('birthdays.csv')
dict = data.to_dict(orient='records')
# 2. Check if today matches a birthday in the birthdays.csv
date = dt.datetime.now().day
month = dt.datetime.now().month
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for i in dict:
    if date == i['day'] and month == i['month']:
        letter = random.choice(letters)
        with open(str(letter)) as let:
            old = let.read()
            new = old.replace('[NAME]', i['name'])
            new1 = old.replace('Angela', 'harsha')
            age_update = new1.replace('[AGE]', str(dt.datetime.now().year - i['year']))
            with sm.SMTP_SSL('smtp.gmail.com') as connection:
                mail = 'sanalakshmiprasanna79@gmail.com'
                password = 'harsha13062002@'
                connection.login(user=mail, password=password)
                connection.sendmail(from_addr=mail, to_addrs=i['email'], msg=age_update)




import pandas as pd
import random
import datetime as dt
import dotenv
import os

dotenv.load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# reading data from csv file
df = pd.read_csv("Day-032/birthdays.csv", index_col=False)
birthday_month = list(df["month"])
birthday_day = list(df["day"])
birthday_name = list(df["name"])
email = list(df["email"])




# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

if (month in birthday_month) and (day in birthday_day):
    index_month = birthday_month.index(month)
    birthday_person = birthday_name[index_month]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





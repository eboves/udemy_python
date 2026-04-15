import smtplib
import os
import dotenv
import datetime as dt
import pandas as pd
import random

# # "smtp.mail.yahoo.com"
# print("Connecting to Gmail...")
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="marcolino_perez@yahoo.com", 
#         msg="Subject:Hello\n\n klk manin como tu ta"
#         )

# import datetime as dt

# now = dt.datetime.now()
# today_is = now.weekday()
# year = now.year()
# print(today_is)


# Load environment variables
dotenv.load_dotenv()

# Get email and password
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

now = dt.datetime.now()
today = now.weekday()
# print(today)

######################################### THIS IS THE WAY I DID IT ##############################################

# df = pd.read_csv("/Users/elvisboves/Desktop/projects/python/Angela_Yu/udemy_python/Day-032/quotes.txt", sep=",")
# data = df.to_dict()

# quotes = list(data.values())
# dict_quotes = quotes[0]
# # print(type(dict_quotes))
# quotes = []
# for key, value in dict_quotes.items():
#     quotes.append(value)
# quote = random.choice(quotes)

# if today == 1:
#     print("Connecting to Gmail...")
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email, to_addrs="marcolino_perez@yahoo.com",
#             msg=f"Subject:Quote\n\n {quote}"
#             )


######################################### THIS IS ANGELA's WAY  ##############################################

if today == 1:
    with open("/Users/elvisboves/Desktop/projects/python/Angela_Yu/udemy_python/Day-032/quotes.txt") as quote_files:
        all_quotes = quote_files.readlines()
        quote = random.choice(all_quotes)
    print("Connecting to Gmail...")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs="marcolino_perez@yahoo.com",
            msg=f"Subject:Quote\n\n {quote}"
            )






# import smtplib
# import os
# import dotenv
# # Load environment variables
# dotenv.load_dotenv()

# # Get email and password
# my_email = os.getenv("EMAIL")
# password = os.getenv("PASSWORD")

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


import datetime as dt

now = dt.datetime.now()
today_is = now.weekday()
year = now.year()
print(today_is)
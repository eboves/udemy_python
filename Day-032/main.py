import smtplib
import os
import dotenv
# Load environment variables
dotenv.load_dotenv()

# Get email and password
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(my_email)

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()

# "smtp.mail.yahoo.com"
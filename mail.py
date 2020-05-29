import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("sssolanki724@gmail.com", "*********")


    # message
message = "Your accuracy is less than 90% .Try again"


    # sending the mail
s.sendmail("sssolanki724@gmail.com", "sssolanki@gmail.com", message)


    # terminating the session
s.quit()

import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("sssolanki724@gmail.com", "**********")


    # message
message_success = "Achieved your desired accuracy without tweeking . Congrats "


    # sending the mail
s.sendmail("sssolanki724@gmail.com", "sssolanki724@gmail.com", message_success)


    # terminating the session
s.quit()

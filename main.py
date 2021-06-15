import smtplib
gmailaddress = "spanc8800@gmail.com"
gmailpassword = "mincraft8800"
mailto = "boryasokolov@gmail.com"
msg = "lol"
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)

try:
 mailServer.starttls()
 mailServer.login(gmailaddress , gmailpassword)
 mailServer.sendmail(gmailaddress, mailto , msg)
 print(" \n Sent!")
 mailServer.quit()

except:
 print("Ошибка ПОЧТЫ : неверный логин или пароль и включите вход для ненадёжных приложений")

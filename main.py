import smtplib


#написать сообщение на почту 
def WriteToEMAIL(text): 
 
  addr_from = "spidermanlove69@mail.ru" # Адресат 
  addr_to = "boryasokolov@gmail.com" # Получатель 
  password = "hero2233" # Пароль 

 
  msg = MIMEMultipart() # Создаем сообщение 
  msg['From'] = addr_from # Адресат 
  msg['To'] = addr_to # Получатель 
  msg['Subject'] = '' # Тема сообщения 
 
  body = text 
  msg.attach(MIMEText(body, 'plain')) # Добавляем в сообщение текст 
 
 
  server = smtplib.SMTP_SSL('smtp.mail.ru', 465) # Создаем объект SMTP 
 
  try: 
  server.login(addr_from, password) # Получаем доступ 
 
  server.send_message(msg) # Отправляем сообщение 
  server.quit() # Выходим 
 
  print("письмо отправленно") 
  except: 
  print("Ошибка ПОЧТЫ : неверный логин или пароль") 
 
  
print("lol")
 
 

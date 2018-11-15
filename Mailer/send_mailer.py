import poplib
import smtplib
print("Compose your message.")
content =input() #please compose a msg
mail= smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
print("please enter sender email")
sender_mail=input() #please enter a mail
print("please enter sender email password")
sender_password=input() #please give your password
print("please enter receiver email")
receiver_emailID=input() 
mail.login(sender_mail,sender_password)
mail.sendmail(sender_mail,receiver_emailID,content)
mail.close()
mailServer = 'pop.gmail.com'


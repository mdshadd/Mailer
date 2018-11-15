import poplib
import smtplib
mailServer = 'pop.gmail.com'
myemailconnection=poplib.POP3_SSL(mailServer)
print(myemailconnection.getwelcome())
print("please enter receiver email")
receiver_emailID=input() 
print("please enter receiver email password")
receiver_emailpassword=input() 
myemailconnection.user(receiver_emailID)
myemailconnection.pass_(receiver_emailpass)
emailinformation=myemailconnection.stat()
print('number of new emails:%s(%s bytes)'%emailinformation)
print('\n \n===\nRead message\n===\n\n')
numberofmails=emailinformation[0]
for i in range(numberofmails):
    for email in myemailconnection.retr(i+1)[1]:
      print (email)
from sys import*
import time
import smtplib
import urllib

def is_connected():
 try:
  urllib2.urlopen('http://216.58.192.142',timeout=1)
  return True
 except urllib2.URLError as err:
  return False

 def MailSeander(gmail_user,gamil_password):
    sent_from = gmail_user 
    to = ['mahaleavinash99@ymail.com']

    email_text = "Welcome to ..."

    try:
     sever = smtplib.SMTP_SSL('smtp.gmail.com',465)
     sever.ehlo()
     sever.login(gmail_user,gamil_password)
     sever.sendmail(sent_from,to,email_text)
     sever.close()

     print("mail sent successfully...")

    except Exception as E:
     print ("Unable to send mail.",E)
    
def main():
     print("----AVINASH MAHALE-----")

     print("Application name :" +argv[0])

    try:
     gmail_user = avinashmahale96@gmail.com'
     gamil_password = '----------------'
       
     connected = is_connected()

     if connected:
         startTime = time.time()
         mailsender(gmail_user,gamil_password)
         endTime = time.time()

         print('took %s seconds to evalute'%(endTime-startTime))
     else:
         print("There is no internet connection")

    except Exception as E:
        print("Error:invalid input",E)

if __name__=="__main__":
main()    





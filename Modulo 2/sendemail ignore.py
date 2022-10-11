import smtplib 
try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.mail.yahoo.com', 465) 

   #Use TLS to add security 
    smtp.starttls() 

    #User Authentication 
    smtp.login("fsociety405@yahoo.com","Mrrobot#22")

    #Defining The Message 
    message = "Message_you_need_to_send" 

    #Sending the Email
    smtp.sendmail("fsociety405@yahoo.com", "joasantonio109@gmail.com",message) 

    #Terminating the session 
    smtp.quit() 
    print ("Email sent successfully!") 

except Exception as ex: 
    print("Something went wrong....",ex)

from django.core.mail import send_mail

from .models import ReadUser
from .defReadDB import *


#----------------------------------------------------------------
def sendSignMail(q):
    # q - добавленный объект в BlogPost
    #print('sendSignMail')

    # список email адресов подписанных пользователей
    listmail = []

    # подписанные пользователи
    (error, qset) = readSignUser(q.user)

    if error == 0:
        for s in qset: 
            email = s.signuser.email
            if  email != '' and  email != ' ' and  email !=None:
                listmail.append(email)

        #print(listmail)

        if len(listmail) > 0:
            subject = "User: " + q.user 
            message =  q.header + "\n\n" + q.content
            sendfrom = 'from@gmail.com'
            
            try:
                send_mail(subject, message, sendfrom, listmail, fail_silently=False)             
            except Exception as inst:
                error = 8
                print(error,type(inst)) 
                print(inst)             

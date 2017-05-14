
from .models import *


#========================================================================================================
# 
def getReadUser(user, signuser):
    #print("getReadUser")            
    error = 0
    q ={}
    try:
        q = ReadUser.objects.get(user=user, signuser=signuser)
    except ReadUser.DoesNotExist:
        error = 1
    except ReadUser.MultipleObjectsReturned:
        error = 2
    except Exception as inst:
        error = 3
        print(error,type(inst))    # the exception instance
        print(inst) 
     
    #print(error,"\n---------------")
    return (error, q)

#----------------------------------------------------------------------
def getPost(idn):
    #print("getPost")            
    error = 0
    q ={}
    try:
        q = BlogPost.objects.get(pk=idn)
    except BlogPost.DoesNotExist:
        error = 1
    except BlogPost.MultipleObjectsReturned:
        error = 2
    except Exception as inst:
        error = 3
        print(error,type(inst))    # the exception instance
        print(inst) 
     
    #print(error,"\n---------------")
    return (error, q)

#----------------------------------------------------------------------
def getReadPost(user, qpost):
    #print("getReadPost")            
    error = 0
    q ={}
    try:
        q = ReadPost.objects.get(user=user, post=qpost)
    except ReadPost.DoesNotExist:
        error = 1
    except ReadPost.MultipleObjectsReturned:
        error = 2
    except Exception as inst:
        error = 3
        print(error,type(inst))    # the exception instance
        print(inst) 
     
    #print(error,"\n---------------")
    return (error, q)


#---------------------------------------------------------
def readUserPost(user):
    #print("readUserPost")            
    error = 0
    qset = {}
    try:
        qset = BlogPost.objects.filter(user=user).order_by('-qdate')
    except Exception as inst:
        error = 5
        print(error,type(inst)) 
        print(inst) 
    else:
        pass

    if (len(qset)  == 0):
        error = 99

    #print(len(qset))
    #print(error,"\n---------------")
    return (error, qset)


#---------------------------------------------------------
def receiveSignPost(user):
    #print("receiveSignPost")  
    error = 0
    qlist = []

    (error, list_signuser) = readListSignUser(user)

    if error == 0:        
        (error, qset) = readSignPost(list_signuser)
        if error == 0:
            for q in qset:
                s = []
                s.append(q)

                (error_rp, q) = getReadPost(user, q)

                if error_rp == 0:
                    s.append(True)
                else:
                    s.append(False)

                qlist.append(s)
                    
    
    #print(error,"\n---------------")
    return (error, qlist)



#---------------------------------------------------------
def readListSignUser(user):
    #print("readListSignUser")            
    error = 0
    qset = []
    try:
        qset = ReadUser.objects.filter(
            user=user).values_list('signuser__username', flat=True)
    except Exception as inst:
        error = 5
        print(error,type(inst)) 
        print(inst) 
    else:
        pass

    if (len(qset)  == 0):
        error = 99

    #print(error,"\n---------------")
    return (error, qset)


#---------------------------------------------------------
def readSignPost(signusers):
    #print("readSignPost")            
    error = 0
    qset = {}
    try:
        qset = BlogPost.objects.filter(
            user__in=list(signusers)).order_by('-qdate')
    
    except Exception as inst:
        error = 5
        print(error,type(inst)) 
        print(inst) 
    else:
        pass

    if (len(qset)  == 0):
        error = 99

    #print(len(qset))
    #print(error,"\n---------------")
    return (error, qset)


#---------------------------------------------------------
def writeReadPost(user, idn):
    #print("writeReadPost")

    (error, qpost) = getPost(idn)

    if error == 0:

        (err, q) = getReadPost(user, qpost)

        if err == 1:
            record = ReadPost(user=user, post=qpost)
            record.save()

    return(error)


#---------------------------------------------------------
def readSignUser(user):
    #print("readSignUser")            
    error = 0
    qset = []
    try:
        qset = ReadUser.objects.filter(user=user)
    except Exception as inst:
        error = 5
        print(error,type(inst)) 
        print(inst) 
    else:
        pass

    if (len(qset)  == 0):
        error = 99

    #print(error,"\n---------------")
    return (error, qset)






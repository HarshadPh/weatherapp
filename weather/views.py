from django.shortcuts import render,HttpResponse
import requests
import json 
from django.core.mail import send_mail
from .models import subscriber
from email.message import EmailMessage
import smtplib



# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['cityname']
        
        dict=fun(city,"current")
       
        
        return render(request,'index.html',dict)

    return render(request,"index.html",)



def fun(city,status):
    apistr = "http://api.weatherapi.com/v1/"+status+".json?key=e785b4096e04488aa9f25638232010&q="+city
    val = requests.get(apistr)
    val = val.text
    val = json.loads(val)

    return val

def forecast(request):
    if request.method == "POST":
        city = request.POST['cityname']
        dict = fun(city,"forecast")
        # print(dict)
        return render(request,'forecast.html',{'forecast':dict['forecast']['forecastday'][0]["hour"]})

    
    return render(request,'forecast.html')

def subscribe(request):
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        city = request.POST['city']
        selected = request.POST['selected']
        
        sub = subscriber(name=name,email=email,mobile_no=mobile,sub=selected,city=city)
        sub.save()
        return HttpResponse("Subscription Successful")

    return render(request,"sub.html")


def sendmail(request):
    cust = subscriber.objects.all()
    

    for sub in cust:
        sender = "harshalphadatare@outlook.com"
        recipient = sub.email
        message = "Hello"
        details = fun(sub.city,"current")
        print(details)
        message = f"""
                     weather Report for your city {details['location']['name']}
                        Temerature is {details['current']['temp_c']} °C
                        Pressure is {details['current']['pressure_in']} mm
                        wind Speed is {details['current']['wind_kph']} km/h

                     """


        email = EmailMessage()
        email["From"] = sender
        email["To"] = recipient
        email["Subject"] = "Test Email in django"
        email.set_content(message)

        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, "Harshal#2002")
        smtp.sendmail(sender, recipient, email.as_string())
        smtp.quit()




    
    return render(request,"mail.html")


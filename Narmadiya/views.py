from django.shortcuts import render,redirect
from .models import News,Patrika,Advertisement,ContactUs,Dharmik,Matrimony,BloodDonor,DanDakshina,Sampark
from . models import sanstha as san
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as lgin
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404
import datetime
# Create your views here.
def index(request):
    news=News.objects.all()
    dict={'News':news}
    return render(request,'home.html',dict)
def news(request):
    news=News.objects.all()
    patrika=Patrika.objects.all()
    dict={'News':news,'Patrika':patrika}
    return render(request,'patrika.html',dict)
def aboutsociety(request):
    return render(request,'samajvistar.html')
def religious(request):
    dharmik=Dharmik.objects.all()
    dict={'dharmik':dharmik}
    return render(request,'RELIGIOUS.html',dict)
def contactus(request):
    if request.method=="POST":
        firstname=request.POST['name']
        LastName=request.POST['surname']
        e_mail=request.POST['email']
        phon=request.POST['phone']
        messag=request.POST['message']
        print(firstname)
        ContactUs(fname=firstname,lname=LastName,email=e_mail,phone=phon,message=messag).save()
    return render(request,'contactus.html')
def login(request):
    return render(request,'login.html')
def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            lgin(request,user)
            msg="Welcome "+str(user.first_name)+" "+str(user.last_name)
            messages.success(request,msg)
            return redirect('/') 
        else:
            messages.error(request,"Invalid Credentials,Please try again later")
            return redirect('/')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password1']
        password1=request.POST['password2']
        if not username.isalnum():
            messages.error(request,'Username must have only Numbers and Letters')
        elif len(password)<8:
            messages.error(request,'Password should have minimum 8 characters')
        elif password!=password1:
            messages.error(request,'The Passwords do not match')
        elif password==password1:
            myuser=User.objects.create_user(username,email,password)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,'User Created Successfully')
    return render(request,'register.html')
def matrimonyform(request):
    if request.method=='POST':
        bywhom=request.POST['Profile']
        fullname=request.POST['fullname']
        fathername=request.POST['fathername']
        mothername=request.POST['mothername']
        gender=request.POST['gender']
        filename=request.FILES['filename']
        dateofb=request.POST['dateofb']
        placeofb=request.POST['placeofb']
        Marital=request.POST['Marital']
        height=request.POST['height']
        bhaibahankisankya=request.POST['bhaibahankisankya']
        mamaname=request.POST['mamaname']
        mamaGautra=request.POST['mamaGautra']
        MTongue=request.POST['MTongue']
        mobno=request.POST['mobno']
        altmob=request.POST['altmob']
        fmob=request.POST['fmob']
        email=request.POST['email']
        qualification=request.POST['qualification']
        job=request.POST['job']
        star=request.POST['star']
        raasi=request.POST['raasi']
        gautra=request.POST['gautra']
        dosh=request.POST['dosh']
        patrika=request.POST['patrika']
        Road=request.POST['Road']
        post=request.POST['post']
        tehsil=request.POST['tehsil']
        Jila=request.POST['Jila']
        pincode=request.POST['pincode']
        rajya=request.POST['rajya']
        Matrimony(madeby=bywhom,Name=fullname,fName=fathername,mName=mothername,gender=gender,photo=filename,dob=dateofb,placeofbirth=placeofb,marital=Marital,noOfBroSis=bhaibahankisankya,mama=mamaname,mamagautra=mamaGautra,height=height,mothertongue=MTongue,mobileno=mobno,altmobileno=altmob,fmobileno=fmob,email=email,qualification=qualification,job=job,nakshatra=star,rashi=raasi,gautra=gautra,dosh=dosh,patrikamilan=patrika,road=Road,post=post,tehsil=tehsil,jila=Jila,pincode=pincode,rajya=rajya).save()
    return render(request,'matrimonyform.html')
def matrimony(request):
    if request.method=='POST':
        fil=request.POST['filter']
        print(fil)
        if fil=='कुआंरे लड़के':
             matrimony=Matrimony.objects.filter(gender='पुरूष',marital='अविवाहित')
             dict={'matrimoni':matrimony}
             return render(request,'matrimony.html',dict)
        if fil=='कुंआरी लड़किया':
             matrimony=Matrimony.objects.filter(gender='महिला',marital='अविवाहित')
             dict={'matrimoni':matrimony}
             if not matrimony:
                raise Http404("No MyModel matches the given query.")
             return render(request,'matrimony.html',dict)
        if fil=='All':
            matrimony=Matrimony.objects.all()
            dict={'matrimoni':matrimony}
            return render(request,'matrimony.html',dict)
        if fil=='तलाकशुदा':
            matrimony=Matrimony.objects.filter(marital='तलाकशुदा')
            dict={'matrimoni':matrimony}
            if not matrimony:
                raise Http404("No MyModel matches the given query.")
            return render(request,'matrimony.html',dict)
        if fil=='विधवा/विदुर':
            matrimony=Matrimony.objects.filter(marital='विधवा/विदुर')
            dict={'matrimoni':matrimony}
            if not matrimony:
                raise Http404("No MyModel matches the given query.")
            return render(request,'matrimony.html',dict)
        

    else:
        matrimony=Matrimony.objects.all()
        dict={'matrimoni':matrimony}
        return render(request,'matrimony.html',dict)
def sampark(request):
    sam=Sampark.objects.all()
    return render(request,'sampark.html',{'sampark':sam})
def pratibha(request):
    return render(request,'pratibha.html')
def sanstha(request):
    Sanstha=san.objects.all()
    return render(request,'sanstha.html',{'sans':Sanstha})
def samajvistar(request):
    return render(request,'samajvistar.html')
def bloodbank(request):
    blooddonor=BloodDonor.objects.all()
    return render(request,'bloodbank.html',{'blooddonor':blooddonor})
def donation(request):
    dona=DanDakshina.objects.all()
    return render(request,'donation.html',{'donation':dona})
def add(request):
    if request.method=="POST":
        firstname=request.POST['name']
        LastName=request.POST['surname']
        e_mail=request.POST['email']
        phon=request.POST['phone']
        messag=request.POST['message']
        filee=request.FILES['Files']
        print(firstname)
        Advertisement(fname=firstname,lname=LastName,email=e_mail,phone=phon,description=messag,content=filee).save()
        messages.success(request,'Request Submitted Successfully') 
    return render(request,'add.html')
def feedback(request):
    return render(request,'contactus.html')
def forgotpass(request):
    return render(request,'forgotpass.html')
def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully Logged out')
    return redirect('/')
def profile(request,myid):
    profile=Matrimony.objects.filter(id=myid)
    dobc=profile[0]
    doba=dobc.dob
    cur=datetime.datetime.now()
    birthdate=cur.year-int(doba.year)
    return render(request,'profile.html',{'profile':profile[0],'age':birthdate})
from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class News(models.Model):
    heading=models.CharField('Heading',max_length=100,default='')
    news=models.CharField('News',max_length=5000,default='')
    images=models.ImageField('Image',upload_to='News/Images',default='')
    photo=models.ImageField('Image',upload_to='News/Images',default='')
    photo2=models.ImageField('Image',upload_to='News/Images',default='',blank=True)
    video=models.FileField('Video',upload_to='News/Video',default="")
    def __str__(self):
        return self.heading
class Patrika(models.Model):
    photo=models.ImageField('Image',upload_to='Patrika/Images')
    name=models.CharField('Name of Patrika',max_length=100,default='')
    description=models.CharField('Description of Patrika',max_length=500,default='')
    pdf=models.FileField('File',upload_to='Patrika/pdf',default='')
    def __str__(self):
        return self.name
class Advertisement(models.Model):
    fname=models.CharField('First Name',max_length=20,default='')
    lname=models.CharField('Last Name',max_length=20,default='')
    email=models.EmailField('E-mail')
    phone=models.BigIntegerField('Phone Number')
    description=models.CharField('Description of the Advertisement',max_length=500,default='')
    content=models.FileField('File',upload_to='Adv/Images',default='')
    def __str__(self):
        return "Advertisement Request From "+self.fname+' '+self.lname
class ContactUs(models.Model):
    fname=models.CharField('First Name',max_length=20,default='')
    lname=models.CharField('Last Name',max_length=20,default='')
    email=models.EmailField('E-mail')
    phone=models.BigIntegerField('Phone Number')
    message=models.CharField('Message',max_length=500,default='')
    def __str__(self):
        return self.fname+' '+self.lname
class Dharmik(models.Model):
    title=models.CharField('Title',max_length=50,default='')
    description=models.CharField('Description',max_length=500000)
    def __str__(self):
        return self.title
class Matrimony(models.Model):
    madeby=models.CharField('Made By',max_length=50,default='')
    Name=models.CharField('Full Name',max_length=50,default='')
    fName=models.CharField('''Father's  Name''',max_length=50,default='')
    mName=models.CharField('''Mother's  Name''',max_length=50,default='')
    gender=models.CharField('Gender',max_length=30,default='')
    photo=models.FileField('Photo',upload_to='Matrimony/Images',max_length=30,default='')
    dob=models.DateField('Date of Birth')
    placeofbirth=models.CharField('Place of Birth',max_length=30,default='')
    marital=models.CharField('Marital Status',max_length=30,default='')
    noOfBroSis=models.IntegerField('Number of Brothers and Sisters',default=0)
    mama=models.CharField('Name of Maternal Uncle',max_length=30,default='')
    mamagautra=models.CharField('Maternal Uncle Gautra',max_length=30,default='')
    height=models.CharField('Height',max_length=30,default='')
    mothertongue=models.CharField('Mother Tongue',max_length=50,default='')
    mobileno=models.BigIntegerField('Mobile Number',default='')
    altmobileno=models.BigIntegerField(' Alternate Mobile Number',default=0)
    fmobileno=models.BigIntegerField('''Father's Mobile Number''',default='')
    email=models.EmailField('Email',default='')
    qualification=models.CharField('Qualifications',max_length=50,default='')
    job=models.CharField('Job Type',max_length=50,default='')
    nakshatra=models.CharField('Nakshatra',max_length=50,default='')
    rashi=models.CharField('Rashi',max_length=50,default='')
    gautra=models.CharField('Gautra',max_length=50,default='')
    dosh=models.CharField('Dosh',max_length=50,default='')
    patrikamilan=models.CharField('Patrika Milan',max_length=20,default='')
    road=models.CharField('Road',max_length=150,default='')
    post=models.CharField('Post',max_length=30,default='')
    tehsil=models.CharField('Tehsil',max_length=50,default='')
    jila=models.CharField('Jila',max_length=50,default='')
    pincode=models.CharField('Pin Code',max_length=30,default='')
    rajya=models.CharField('Rajya',max_length=30,default='')
    def __str__(self):
        return self.Name
    def age (self):
        doba=self.dob
        cur=datetime.datetime.now()
        return cur.year-int(doba.year)
class BloodDonor(models.Model):
    name=models.CharField('Full Name',max_length=30,default='')
    address=models.CharField('Address',max_length=30,default='')
    mob=models.BigIntegerField('Mobile Number',default=0)
    def __str__(self):
        return self.name
class Sampark(models.Model):
    name=models.CharField('Full Name',max_length=30,default='')
    address=models.CharField('Address',max_length=30,default='')
    mob=models.BigIntegerField('Mobile Number',default=0)
    def __str__(self):
        return self.name
class DanDakshina(models.Model):
    name=models.CharField('Full Name',max_length=30,default='')
    address=models.CharField('Address',max_length=30,default='')
    mob=models.BigIntegerField('Mobile Number',default=0)
    def __str__(self):
        return self.name
class sanstha(models.Model):
    img=models.ImageField('Image',upload_to='Sanstha/img')
    name=models.CharField('Name of Sanstha',max_length=100,default='')
    description=models.CharField('Description of Sanstha',max_length=500,default='')
    gmap=models.CharField('Map',max_length=500,default='')
    def __str__(self):
        return self.name




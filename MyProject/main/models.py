from django.db import models

class ForLogo(models.Model):
    img=models.ImageField(upload_to='home',null=True)

class HeaderTitle(models.Model):
    title=models.CharField('title',max_length=100)
    subtitle=models.TextField(verbose_name='subtitle')
    img=models.ImageField(upload_to='home',null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Header Title'
        verbose_name_plural = 'Header Titles'

class Services(models.Model):
    title=models.CharField('title',max_length=100)
    subtitl=models.TextField(verbose_name='subtitle')

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'

class Prmision(models.Model):
    icon=models.CharField('icon',max_length=100)
    title=models.CharField('title',max_length=100)
    text=models.TextField('text')



class WhatWeDo(models.Model):
    title=models.CharField('title',max_length=100)
    text=models.TextField('text')
    img=models.ImageField(verbose_name='home')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='What We Do'
        verbose_name_plural='What We Do'

class Problems(models.Model):
    title=models.CharField('title',max_length=100)
    text=models.TextField('text')

    class Meta:
        verbose_name='Problem'
        verbose_name_plural='Problems'

    def __str__(self):
        return self.title
    
class TheCleantSay(models.Model):
    title=models.CharField('title',max_length=100)
    text=models.TextField('text')
    img=models.ImageField(upload_to='home',null=True)

    class Meta:
        verbose_name='The Cleant Say'
        verbose_name_plural='The Cleant Says'

    def __str__(self):
        return self.title
    
class About(models.Model):
    name=models.CharField('name',max_length=100)
    text=models.TextField('text')
    profession=models.CharField('profession',max_length=100)
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return self.name
    
class SubAbout(models.Model):
    aboutt=models.OneToOneField(About,on_delete=models.CASCADE,related_name='about_r')
    img=models.ImageField(verbose_name='staffs image',upload_to='staffs')
    description=models.TextField('description')

    def __str__(self):
        return f'{self.aboutt}'
    
class Getting(models.Model):
    title=models.CharField('title',max_length=100)
    text=models.TextField('text')
    img=models.ImageField(upload_to='home')

    def __str__(self):
        return self.title

class Tickets(models.Model):
    price=models.IntegerField(verbose_name='price')
    img=models.ImageField(verbose_name='image',upload_to='ticket')
    name=models.CharField('name',max_length=100)
    storage=models.IntegerField(verbose_name='storage')
    status=models.CharField(max_length=2,choices=[('GB','GB'),('TB','TB')],default='TB')
    LTS=models.BooleanField(verbose_name='Life-time Support', default=True)
    PAO=models.BooleanField(verbose_name='Premium Add-Ons', default=True)
    FN=models.BooleanField(verbose_name='Fastest Network', default=True)
    MO=models.BooleanField(verbose_name='More Options', default=True)

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    emile=models.EmailField(verbose_name='emile')

    def __str__(self):
        return self.emile
    
class ContactUs(models.Model):
    address=models.CharField(max_length=100,verbose_name='address')
    phone=models.CharField('phone',max_length=50)
    email=models.EmailField('email')

    def __str__(self):
        return self.address



   



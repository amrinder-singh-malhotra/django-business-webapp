from django.db import models
# Create your models here.

class Slidebar(models.Model):
    title=models.CharField(max_length=100, blank=True)
    description=models.CharField(max_length=100, blank=True)
    image=models.ImageField(upload_to='slidebar/') 
    
    def __str__(self):
            return self.title

#Cards
class HomeServiceCards(models.Model):
    # Card 1 Fields
    card1_image = models.ImageField(upload_to='cards/')
    card1_p = models.CharField(max_length=500, blank=True, default="Service 1 description text")
    card1_anchor = models.CharField(max_length=100, default="Go Documents Checklist")

    # Card 2 Fields
    card2_image = models.ImageField(upload_to='cards/')
    card2_p = models.CharField(max_length=500, blank=True, default="Service 2 description text")
    card2_anchor = models.CharField(max_length=100, default="Go Documents Checklist")

    # Card 3 Fields
    card3_image = models.ImageField(upload_to='cards/')
    card3_p = models.CharField(max_length=500, blank=True, default="Service 3 description text")
    card3_anchor = models.CharField(max_length=100, default="Go Documents Checklist")

    # Card 4 Fields
    card4_image = models.ImageField(upload_to='cards/')
    card4_p = models.CharField(max_length=500, blank=True, default="Service 4 description text")
    card4_anchor = models.CharField(max_length=100, default="Go Documents Checklist")

    # Card 5 Fields
    card5_image = models.ImageField(upload_to='cards/')
    card5_p = models.CharField(max_length=500, blank=True, default="Service 5 description text")
    card5_anchor = models.CharField(max_length=100, default="Go Documents Checklist")

    # Card 6 Fields
    card6_image = models.ImageField(upload_to='cards/')
    card6_p = models.CharField(max_length=500, blank=True, default="Service 6 description text")
    card6_anchor = models.CharField(max_length=100, default="Go Documents Checklist")

    def __str__(self):
        return "Homepage Services Cards"
 
 #Documents Checklist
class About(models.Model):
    paragraph=models.TextField()
    paragraph_2=models.TextField(default="Why Choose Us?")
    
    def __str__(self):
        return "About Page"

class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField()
    email=models.EmailField(unique=True)
    service=models.CharField()
    description=models.TextField()
    
    def __str__(self):
            return "Contact Page"
    

from django.db import models
from django.forms import ModelForm
# Create your models here.
transaction_type_choices=(
    ('buy','Buy'),
    ('rent','Rent'),
    ('sell', 'Sell')
)
area_choices=(
    ('Bandra E', 'Bandra East'),
    ('Bandra W', 'Bandra West'),
    ('Khar E', 'Khar East'),
    ('Khar W', 'Khar West'),
    ('Santacruz E', 'Santacruz East'),
    ('Santacruz W', 'Santacruz West'),
    ('Parle E', 'Vile-Parle East'),
    ('Parle W', 'Vile-Parle West'),
    ('Andheri E', 'Andheri East'),
    ('Andheri W', 'Andheri West'),
)
property_choices=(
    ('apartment','Apartment'),
    ('house/villa','House/Villa'),
    ('plot','Plot')
)
purpose_choices=(
    ('residential','Residential'),
    ('commercial','Commercial')
)
furnished_choices=(
    ('fully-furnished','Fully Furnished'),
    ('semi-furnished','Semi Furnished'),
    ('non-furnished','Non Furnished')
)
class Booking(models.Model):
    transaction_type=models.CharField(max_length=10, choices=transaction_type_choices, default='buy')
    name=models.CharField(max_length=50, null=False, blank=False)
    message_id=models.AutoField(primary_key=True)
    property_type=models.CharField(max_length=20, blank=False, null=False, default='apartment', choices=property_choices)
    bedrooms=models.IntegerField(null=True, blank=True)
    purpose=models.CharField(max_length=20, choices=purpose_choices, default='residential')
    square_feet=models.CharField(max_length=20, blank=True, null=True)
    
    furniture=models.CharField(max_length=20, choices=furnished_choices, default='fully-furnished')
    area=models.CharField(max_length=50, choices=area_choices, blank=True, null=True)
    landmark=models.CharField(max_length=20,null=True, blank=True)
    budget=models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField(null=False, blank=False)
    phone=models.CharField(max_length=20,blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    additional_message=models.TextField(max_length=250,null=True, blank=True)
    def __str__(self):
        return self.name
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, null=False, blank=False)
    message=models.TextField(max_length=250, null=False, blank=False)
    email=models.EmailField(blank=False, null=False)
    phone=models.CharField(max_length=20,blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name

class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        labels={
            "transaction_type":"You want to?",
            "budget":"Price (In Rupees)"
        }

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class PropertyType(models.Model):
    type_name=models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
        return self.type_name
    
class Listing(models.Model):
    
    property_name=models.CharField(max_length=100, null=False, blank=False)
    property_rate=models.CharField(max_length=20, null=False, blank=True)
    property_size=models.CharField(max_length=20, blank=True, null=True)
    property_attributes=models.CharField(max_length=30, null=False, blank=False)
    property_type=models.ForeignKey(PropertyType,blank=False, null= False, on_delete=models.CASCADE)
    property_transaction_type=models.CharField(max_length=10, choices=transaction_type_choices, default='buy')
    property_intro=models.CharField(max_length=50, null=False, blank=False)
    property_rooms=models.IntegerField(blank=True, null=True)
    property_bathrooms=models.IntegerField(blank=True, null=True)
    property_landmark=models.CharField(max_length=20, null=False)
    property_address=models.TextField(blank=False, null=False)
    property_description=models.TextField(null=False, blank=False)
    property_thumbnail=models.ImageField(null=False, blank=True, upload_to='uploads')
    property_image1=models.ImageField(blank=True, null=True, upload_to='uploads')
    property_image2=models.ImageField(blank=True, null=True, upload_to='uploads')
    property_image3=models.ImageField(blank=True, null=True, upload_to='uploads')
    property_image4=models.ImageField(blank=True, null=True, upload_to='uploads')
    property_image5=models.ImageField(blank=True, null=True, upload_to='uploads')

    
    def __str__(self):
        return self.property_name


class Customers(models.Model):
    customer_name=models.CharField(max_length=20, null=False, blank=False)
    customer_phone=models.IntegerField(null=False, blank=False)
    customer_email=models.EmailField(null=True, blank=True)
    property_reference=models.ForeignKey(Listing, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.customer_name

class CustomerForm(ModelForm):
    class Meta:
        model=Customers
        fields='__all__'

    



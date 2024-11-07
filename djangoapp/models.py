from django.db import models

# Create your models here.
class usermodel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=200)
    user_age=models.IntegerField()
    date=models.DateField()

class user(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13)



class emp(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)

class product(models.Model):
    name=models.CharField(max_length=100)
    discription=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.name

class pross(models.Model):
    pro_id=models.IntegerField(primary_key=True)
    pro_name=models.CharField(max_length=100)
    use1=models.ForeignKey(product,on_delete=models.CASCADE)

class crud(models.Model):
    first_name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True)

class admn(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class publish(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self) :
        return self.name

class model(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=10)
    pub = models.ForeignKey(publish,on_delete=models.CASCADE)

class cours(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100,unique=True)
    

class students(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    stdns= models.ForeignKey(cours,on_delete=models.CASCADE)  

    def __str__(self):
        return self.first_name 


class hotel(models.Model):
    name = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    rate = models.FloatField()
    decsription = models.TextField()
    def _str_(self):
        return self.name
    
class gust(models.Model):
    gust_name = models.CharField(max_length=15)
    check_in = models.DateField()
    hotels = models.ForeignKey(hotel,on_delete=models.CASCADE)
    def _str_(self):
        return self.gust_name
    

class userm(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)    

class userprofile(models.Model):
    user_name = models.CharField(max_length=100)
    date_of_birth=models.DateField()
    location = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)


class blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    confirm_pass=models.CharField(max_length=10)


class uss(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    image=models.ImageField(upload_to='image/')




class imga(models.Model):
    title=models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/')
    date = models.DateField(auto_now_add=True)




    

    



    










































































































from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import *

# Create your views here.
def fun(request):
    return HttpResponse("hi")
def fun1(request):
    return render(request,"a.html",{"name":'an'})
def fun3(request):
    context = {
       'fruits' :['Apple','banana','cherry'],
    }
    
    return render(request,"fruit.html",context)
def fun4(request):
    items =[
        {'name':'laptop','price':200,'quantity':10},
        {'name':'phone','price':200,'quantity':5},
        {'name':'tv','price':200,'quantity':10},
    ]
    return render(request,"item.html",{'item':items})
def fun5(request):
    li = [
        {'name':'laptop','price':'$999','status':True},
        {'name':'smartphone','price':'$299.99','status':False},
        {'name':'tablet','price':'$149.99','status':True},


    ]
    return render(request,"product list.html",{'item':li})
def fun6(request):
    data=usermodel.objects.all()
    return render(request,"all.html",{'data1':data})
def delete_user(request,id):
    user=usermodel.objects.get(user_id=id)
    user.delete()
    return redirect('hi')
def update_user(request,id):
    user=usermodel.objects.filter(user_id=id)
    if request.method =='POST':
        ID=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        date=request.POST.get('date')
        user_obj=usermodel()
        user_obj.user_id=ID
        user_obj.user_name=name
        user_obj.user_age=age
        user_obj.date=date
        user_obj.save()
        return redirect('hi')
    return render(request,"update.html",{'user1':user})






def add_user(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        date=request.POST.get('date')
        user_obj=usermodel()
        user_obj.user_id=id
        user_obj.user_name=name
        user_obj.user_age=age
        user_obj.date=date
        user_obj.save()
        return redirect('hi')
    return render(request,"add_user.html")

def user_(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        title=request.POST.get('title')
        author=request.POST.get('author')
        p_date=request.POST.get('publishedate')
        isbn=request.POST.get('isbn')
        user_obj=user()
        user_obj.book_id=id
        user_obj.title=title
        user_obj.author=author
        user_obj.published_date=p_date
        user_obj.isbn=isbn
        user_obj.save()
    return render(request,"mook.html")
def fun7(request):
    
    data=user.objects.all()
    return render(request,"display.html",{'display':data})

def users(request):
    if request.method == 'POST':
        id=request.POST.get('emp_id')
        name=request.POST.get('emp_name')
        phone=request.POST.get('phone')
        address=request.POST.get("address")
        em=emp()
        em.emp_id=id
        em.emp_name=name
        em.phone=phone
        em.address=address
        em.save()
        return redirect('my')
    return render(request,'emp.html')

def fun8(request):
    data=emp.objects.all()
    return render(request,'dis.html',{"disp":data})

def pro(req):
    if req.method == 'POST':
        name=req.POST.get('name')
        disc=req.POST.get('discription')
        price=req.POST.get("price")
        stock=req.POST.get('stock_quantity')
        created=req.POST.get("createdate")
        pro=product()
        pro.name=name
        pro.discription=disc
        pro.price=price
        pro.stock_quantity=stock
        pro.created_at=created
        pro.save()
        return redirect('k')
    return render(req,'product.html')

def fun9(req):
    dat=product.objects.all()
    return render(req,'pro.html',{"data":dat})

def funn10(request):
    if request.method == 'POST':
        first_Name=request.POST.get("fname")
        last_Name=request.POST.get("lname")
        Email=request.POST.get("email")
        Phone_number=request.POST.get("pnumber")
        Addres=request.POST.get("address")
        Date_of_birth=request.POST.get("dbirth")
        u=crud()
        u.first_name=first_Name
        u.lastname=last_Name
        u.email=Email
        u.phone_number=Phone_number
        u.address=Addres
        u.date_of_birth=Date_of_birth
        u.save()
        return redirect('c')
    return render(request,"funn10.html")

def funn11(req):
    data=crud.objects.all()
    return render(req,"funn11.html",{"data":data})

def deleee(req,id):
    dele=crud.objects.get(id=id)
    dele.delete()
    return redirect('c')

def updat(req,id):
    user=crud.objects.get(id=id)
    if req.method=='POST':
        name=req.POST.get('fname')
        lastname=req.POST.get('lname')
        email=req.POST.get('email')
        pnumber=req.POST.get('pnum')
        addre=req.POST.get('address')
        date=req.POST.get('date')

        user.first_name=name
        user.lastname=lastname
        user.email=email
        user.phone_number=pnumber
        user.address=addre
        user.date_of_birth=date
        user.save()
        return redirect('c')
    return render(req,'upd.html',{'data':user})

def userr(req):
    if req.method == 'POST':
        titl=req.POST.get('Title')
        con=req.POST.get('Content')
        auth=req.POST.get('author')
        cdate=req.POST.get('createdat')
        udate=req.POST.get('udate')
        u=admn()
        u.title=titl
        u.content=con
        u.author=auth
        u.created_at=cdate
        u.updated_at=udate
        u.save()
        return redirect('mo')
    return render(req,'usr1.html')

def usertbl(request):
    data=admn.objects.all()
    return render(request,'usrtable.html',{"data":data})

def userup(req,id):
    u=admn.objects.get(id=id)
    if req.method == 'POST':
        titl=req.POST.get('Title')
        con=req.POST.get('Content')
        auth=req.POST.get('author')
        cdate=req.POST.get('createdat')
        udate=req.POST.get('udate') 

        u.title=titl
        u.content=con
        u.author=auth
        u.created_at=cdate
        u.updated_at=udate
        u.save()
        return redirect('mo')
    return render(req,'userudate.html',{"up":u}) 

def produ(request):
    prs=pross.objects.all()
    return render(request,'usedis.html',{"data":prs})

def adduser(request):
    data = product.objects.all()
    if request.method == 'POST':
        proid = request.POST.get('proidd')
        proname = request.POST.get('pronamme')

        obj = pross()

        obj.pro_id = proid
        obj.pro_name = proname
        obj.use1=product.objects.get(emp_id=request.POST.get('user_id'))

        obj.save()
        return redirect('ww')
    return render(request,'ad.html',{"data":data})


def publi(req):
    data = model.objects.all()
    return render(req,'publish.html',{"data":data})

def modeldis(request):
    data=publish.objects.all()
    if request.method == 'POST':
        Title = request.POST.get('title')
        pub_date = request.POST.get('pbdate')
        ISBN =request.POST.get('isbn')
        obj = model()
        obj.title = Title
        obj.publication_date = pub_date
        obj.isbn = ISBN
        obj.pub=publish.objects.get(id=request.POST.get('id'))
        obj.save()
        return redirect("ww")
    return render(request,'form.html',{"data":data})




def delbook(request,id):
    dele = model.objects.get(id=id)
    dele.delete()
    return redirect("ww")

def upbook(request,id):
    value = model.objects.get(id=id)
    value2 = publish.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        update=request.POST.get('pbdate')
        isbn=request.POST.get('isbn')
        value.title=title
        value.publication_date=update
        value.isbn=isbn
        value.pub=publish.objects.get(id=request.POST.get('id'))
        value.save()
        return redirect('ww')
    return render(request,'updbook.html',{"data":value,'data1':value2})


def course(request):
    data=students.objects.all()
    return render(request,'courtabl.html',{'data1':data})

def stddeatials(request):
    data = cours.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        phn = request.POST.get('phone')
        # course = request.POST.get('crs')
        ob=students()
        ob.first_name=firstname
        ob.last_name=lastname
        ob.email=email
        ob.phone= phn
        # ob.course=course
        ob.stdns = cours.objects.get(id=request.POST.get('id'))
        ob.save()
        return redirect('tbl')
    return render(request,'stdform.html',{'value':data})

def upstudent(request,id):
    value = students.objects.get(id=id)
    data = cours.objects.all()
    if request.method == "POST":
        fname =request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        value.first_name=fname
        value.last_name=lname
        value.email=email
        value.phone=phone
        
        value.stdns=cours.objects.get(id=request.POST.get('id'))
        value.save()
        return redirect('tbl')
    return render(request,'updtstd.html',{'data':value,'data1':data})





def view_gust(req):
    data = gust.objects.all()
    return render(req,'viewgust.html',{'value':data})

def add_gust(req):
    data1 = hotel.objects.all()
    if req.method =='POST':
        name = req.POST.get('name')
        date =  req.POST.get('date')

        add = gust()
        add.gust_name = name
        add.check_in = date
        add.hotels= hotel.objects.get(id=req.POST.get('id'))
        add.save()
        return redirect('d')
    return render(req,'addgust.html',{'value1':data1})

def dlt_gust(req,id):
    dlt = gust.objects.get(id=id)
    dlt.delete()
    return redirect('d')

def uptd_gust(req,id):
        data2 = hotel.objects.all()
        data3 = gust.objects.get(id=id)
        if req.method == 'POST':
            name = req.POST.get('name')
            date =  req.POST.get('date')

            data3.gust_name = name
            data3.check_in = date
            data3.hotels = hotel.objects.get(id=req.POST.get('id'))
            data3.save()
            return redirect('d')
        return render(req,'uptdgust.html',{'value3':data2,'val':data3})



from .forms import userform
def userfor(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('vw')
    else:
        form=userform()
    return render(request,"userforms.html",{'form':form})




from .forms import userprofiles
def profileform(request):
    if request.method == 'POST':
        form = userprofiles(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vw')
    else:
        form=userprofiles
    return render(request,'profileform.html',{"forms":form})


def usertable(request):
    data = userprofile.objects.all()
    return render(request,"profileview.html",{"data":data})

def profileupdate(request,id):
    data = userprofile.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('user_name') 
        dfb = request.POST.get('date_of_birth')
        location = request.POST.get('location')
        bio = request.POST.get('bio')
        data.user_name = username
        data.date_of_birth = dfb
        data.location = location
        data.bio = bio
        data.save()
        return redirect('vw')
    return render(request,"uprofile.html",{'value':data})   


def log(request):
    return render(request,"login.html")


from .forms import blogform
def blog(request):
    if request.method =='POST':
        form=blogform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bt')
    else:
        form=blogform()
    return render(request,"blogform.html",{'form':form})  

def blogtable(request):
    data = blog.objects.all()
    return render(request,'bltable.html',{'data':data})  



from.forms import regi
def regis(request):
    if request.method == 'POST':
        form = regi(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rg')
    else:
        regi()
    return render(request,'regi_form.html',{'form':form})


def regi_table(request):
    data = register.objects.all() 
    return render(request,'regi_table.hmtl',{"data":data})
def usi(request):
    data=uss.objects.all()
    return render(request,"usim.html",{'data':data})
        
def dis_im(request):
    data=imga.objects.all()
    m=data.values()
    
    return render(request,"utim.html",{'data':data})


def image(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        imgi = request.FILES.get('image')

        m_obj=imga()
        m_obj.title=title
        m_obj.image=imgi
        m_obj.save()
        return redirect('im')
    return render(request,'ui.html')



def home(request):
    return render(request,'base.html')

def homepage(request):
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')





    




    







        






















from django.shortcuts import render,HttpResponseRedirect
from .models import register,add_pets,add_food,cart_tb,payment_tb,paymenttoshop_tb,review_tb,vetenery_tb
import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from .forms import imgForm
from django.contrib.auth import logout
import os
from django.db.models import Q


# Create your views here.
################################################################################################################
#####################################---ADMIN---################################################################
################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_login(request):
	if request.method=="POST":
		email=request.POST['username']
		password=request.POST['password']
		b =register.objects.all().filter(email=email,password=password,type='admin')
		if b.exists():
			for x in b:
				request.session["myid"]=x.id
				return render(request,'admin/admin_home.html')

		else:
				return render(request,'admin/admin_login.html',{'message':'Invalid credentials'})
	else:
		 return render(request,'admin/admin_login.html')

################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_home(request):
	return render(request,'admin/admin_home.html')

#################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def add_pet(request):
	if request.method=="POST":
		ii=request.session['myid']
		Category=request.POST['type']
		name=request.POST['name']
		Breed=request.POST['breed']
		Age=request.POST['age']
		Colour=request.POST['colour']
		size=request.POST['size']
		Vaccination=request.POST['vacci']
		Description=request.POST['desc']
		Price=request.POST['price']
		availableqty=request.POST['aqty']
		var=register.objects.get(id=ii)
		check=add_pets.objects.all().filter(pid=var,Category=Category,name=name,Breed=Breed,Age=Age,Colour=Colour,size=size,Vaccination=Vaccination,Description=Description,Price=Price,status="available",type="admin")
		if check:
			return render(request,'admin/admin_add_pets.html',{'msg':'Already inserted'})
		img=imgForm(request.POST,request.FILES)
		if img.is_valid():
			image1=img.cleaned_data['image']
			toReg=add_pets(pid=var,Category=Category,name=name,Breed=Breed,Age=Age,Colour=Colour,size=size,Image=image1,Vaccination=Vaccination,Description=Description,Price=Price,status="available",type="admin",availableqty=availableqty )
			toReg.save()
			img=imgForm()
			return render(request,'admin/admin_add_pets.html',{'msg':'successfully Inserted'})
		else:
			img=imgForm()
			print("upload failed")
			return render(request,'admin/admin_add_pets.html',{'msg':'Image upload failed'})
	else:
		img=imgForm()
		print("process failed")
		return render(request,'admin/admin_add_pets.html')

#########################################################################################################################
	
@cache_control(no_cache=True, must_revalidate=True,no_store=True)	
def view_pets(request):
	upd=add_pets.objects.all().filter(type='admin',status='available')
	spd=add_pets.objects.all().filter(type='shop',status='available')
	return render(request,"admin/admin_view_pets.html",{'admin':upd,'shop':spd})
	

@cache_control(no_cache=True, must_revalidate=True,no_store=True)	
def view_foods(request):
	spd=add_food.objects.all().filter(status='available')
	return render(request,"admin/admin_view_foods.html",{'food':spd})
	
##################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_reject_pets(request):
	id1=request.GET['id']
	print(id1,"+++++++++++++++++++++++++++++++++++++++++")
	add_pets.objects.all().filter(id=id1).update(status="rejected")
	print("========================================================")
	up=add_pets.objects.all().filter(status="available")	
	return render(request,'admin/admin_view_pets.html',{'db':up})

##################################################################################################################3#

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_reject_pets(request):
	fromReg=add_pets.objects.all().filter(status='rejected')
	return render(request,'admin/view_reject_pets.html',{'db':fromReg})

########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_update_pet(request):
	print('inside getData')
	if request.method=='GET':
		id2=request.GET['id']
		fromReg=add_pets.objects.all().filter(id=id2)
		print(fromReg)
		if fromReg.exists():
			print('get record')
			return render(request,'admin/admin_update_pets.html',{'b':fromReg})
		else:
			print("failed")
			return render(request,"admin/admin_update_pets.html")

###########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_update_pet(request):
	if request.method=="POST":
		print("----------update inside post-----------")
		up=request.GET['id']
		name=request.POST['name']
		Breed=request.POST['breed']
		Category=request.POST['type']
		Age=request.POST['age']
		Colour=request.POST['colour']
		size=request.POST['size']
		Vaccination=request.POST['vacci']
		Description=request.POST['desc']
		Price=request.POST['price']
		ii=request.session['myid']
		imgup=request.POST['imgupdate']
		if imgup=='Yes':
			image1=request.FILES['image']
			oldrec=add_pets.objects.all().filter(id=up)
			updrec=add_pets.objects.get(id=up)
			for x in oldrec:
				imgurl=x.Image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.Image=image1
			updrec.save()
		add_pets.objects.filter(id=up).update(Category=Category,name=name,Breed=Breed,Age=Age,Colour=Colour,size=size,Vaccination=Vaccination,Description=Description,Price=Price)
		upd=add_pets.objects.all().filter(type='admin')
		spd=add_pets.objects.all().filter(type='shop')
		return render(request,"admin/admin_view_pets.html",{'admin':upd,'shop':spd})
	elif request.method=="GET":
		print("-----------------get update------------")
		id1=request.GET['id']
		up=add_pets.objects.all().filter(id=up)
		print("-----------------render page--------------")
		return render(request,'admin/admin_view_pets.html',{'db':up})

# # ########################################################################################################################
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def view_shop(request):
	upd=register.objects.all().filter(type="shop",status1="pending")
	upd1=register.objects.all().filter(type="shop",status1="approved")
	upd2=register.objects.all().filter(type="shop",status1="rejected")
	print("-------------------------",upd)
	return render(request,"admin/admin_view_shop.html",{'db':upd,'db1':upd1,'db2':upd2})

#########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_approve_shop(request):
	id1=request.GET['id']
	register.objects.all().filter(id=id1).update(status1="approved")
	upd=register.objects.all().filter(type="shop",status1="pending")
	upd1=register.objects.all().filter(type="shop",status1="approved")
	upd2=register.objects.all().filter(type="shop",status1="rejected")
	return render(request,"admin/admin_view_shop.html",{'db':upd,'db1':upd1,'db2':upd2})

##########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_reject_shop(request):
	id1=request.GET['id']
	register.objects.all().filter(id=id1).update(status1="rejected")
	upd=register.objects.all().filter(type="shop",status1="pending")
	upd1=register.objects.all().filter(type="shop",status1="approved")
	upd2=register.objects.all().filter(type="shop",status1="rejected")
	return render(request,"admin/admin_view_shop.html",{'db':upd,'db1':upd1,'db2':upd2})

##########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_reject_shop(request):
	fromReg=register.objects.all().filter(type="shop",status1='rejected')
	return render(request,'admin/view_reject_shop.html',{'db':fromReg})

#######################################################################################################################	

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_approved_shop(request):
	fromReg=register.objects.all().filter(status1='approved')
	return render(request,'admin/view_reject_shop.html',{'db':fromReg})

########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def view_user(request):
	vie=register.objects.all().filter(status1="active")
	if vie.exists():
		return render(request,'admin/admin_view_user.html',{'db':vie})
	else:
		return render(request,'admin/admin_view_user.html')

##########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_reject_user(request):
	id1=request.GET['id']
	print(id1,"+++++++++++++++++++++++++++++++++++++++++")
	register.objects.all().filter(id=id1).update(status1="rejected")
	print("========================================================")
	up=register.objects.all().filter(status1="active")	
	return render(request,'admin/admin_view_user.html',{'db':up})

##########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_reject_user(request):
	fromReg=register.objects.all().filter(status1='rejected',type='user')
	return render(request,'admin/view_reject_user.html',{'db':fromReg})

#######################################################################################################################		

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def view_orders(request):
	id1=request.session['myid']
	pets=cart_tb.objects.all().filter(Q(status="Paid")|Q(status="Processing")|Q(status="Shipping")|Q(status="Delivered"),item='pet')
	foods=cart_tb.objects.all().filter(Q(status="Paid")|Q(status="Processing")|Q(status="Shipping")|Q(status="Delivered"),item='food')
	print(pets)
	return render(request,'admin/admin_view_order.html',{'uv':pets,'xy':foods})


#########################################################################################################################

# def Suggestions():
# 	return render(request,'admin/Suggestions.html')

########################################################################################################################

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def admin_booking_approve(request):
	ii=request.GET["id"]
	fromform=booking_details.objects.all().filter(id=ii,owner="admin").update(status="approved")
	up=booking_details.objects.all().filter(owner="admin",status="pending")
	return render(request,'admin/booking_approvel.html',{'db':up})

############################################################################################################################

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def admin_booking_reject(request):
	ii=request.GET["id"]
	fromform=booking_details.objects.all().filter(id=ii,owner="admin").update(status="rejected")
	up=booking_details.objects.all().filter(owner="admin",status="pending")
	return render(request,'admin/booking_approvel.html',{'db':up})

#################################################################################################################################
	
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def admin_view_rejectedbooking(request):
	ii=request.session["myid"]
	fromform=booking_details.objects.all().filter(owner="admin",status="rejected")
	return render(request,'admin/rejected_bookings.html',{'db':fromform})

#############################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_user_payment(request):
	ab=payment_tb.objects.all()
	return render(request,'admin/admin_view_user_payment.html',{'db':ab})

##############################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_change_password(request):
	if request.method=="POST":
		print("----------update inside post-----------")
		oldpassword=request.POST['oldpassword']
		newpassword=request.POST['newpassword']
		cpassword=request.POST['cpassword']
		uid=request.session['myid']
		oldcheck=register.objects.all().filter(id=uid)
		if oldcheck:
			for x in oldcheck:
				oldpwd=x.password
		if (oldpassword==oldpwd) and (newpassword==cpassword):
			register.objects.filter(id=uid).update(password=newpassword)
			up=register.objects.all()
			print("-----------------render page--------------")
			return render(request,'admin/admin_change_password.html',{'db':up,"success":'success password is changed'})
		else:
			return render(request,'admin/admin_change_password.html',{"error":'error password not matched'})
	else:
		print("-----------------get update------------")
		uid=request.session['myid']
		up=register.objects.all().filter(id=uid)
		print("-----------------render page--------------")
		return render(request,'admin/admin_change_password.html',{'db':up})

################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_orders(request):
	id1=request.session['myid']
	print(id1)
	pets=cart_tb.objects.all().filter(shopid=id1,status='Paid',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Paid',item='food')
	print(pets)
	return render(request,'admin/admin_view_myorder.html',{'uv':pets,'xy':foods})

################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_processing(request):
	id1=request.session['myid']
	pets=cart_tb.objects.all().filter(shopid=id1,status='Processing',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Processing',item='food')
	return render(request,'admin/admin_view_myorder.html',{'uv':pets,'xy':foods})

################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_shipped(request):
	id1=request.session['myid']
	pets=cart_tb.objects.all().filter(shopid=id1,status='Shipped',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Shipped',item='food')
	print(pets)
	return render(request,'admin/admin_view_myorder.html',{'uv':pets,'xy':foods})

################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_view_completed(request):
	id1=request.session['myid']
	pets=cart_tb.objects.all().filter(shopid=id1,status='Delivered',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Delivered',item='food')
	print(pets)
	return render(request,'admin/admin_view_myorder.html',{'uv':pets,'xy':foods})

################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_processing(request):
	id1=request.session['myid']
	cid=request.GET['id']
	cart_tb.objects.all().filter(id=cid).update(status='Processing')
	pets=cart_tb.objects.all().filter(shopid=id1,status='Processing',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Processing',item='food')
	print(pets)
	return render(request,'admin/admin_view_myorder.html',{'uv':pets,'xy':foods})

################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_shipping(request):
	id1=request.session['myid']
	cid=request.GET['id']
	cart_tb.objects.all().filter(id=cid).update(status='Shipping')
	pets=cart_tb.objects.all().filter(shopid=id1,status='Shipping',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Shipping',item='food')
	print(pets)
	return render(request,'admin/admin_view_myorder.html',{'uv':pets,'xy':foods})

################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_delivered(request):
	id1=request.session['myid']
	cid=request.GET['id']
	cart_tb.objects.all().filter(id=cid).update(status='Delivered')
	pets=cart_tb.objects.all().filter(shopid=id1,status='Delivered',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Delivered',item='food')
	print(pets)
	return render(request,'admin/admin_view_myorder.html',{'uv':pets,'xy':foods})

################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def admin_makepayment(request):
	if request.session['myid']:
		ids=request.session['myid']
		if request.method=='POST':
			amount=request.POST['amount']
			sid=request.POST['shop']
			cart=request.POST['cart']
			x = datetime.datetime.now()
			id1=register.objects.get(id=sid)
			cart1=cart_tb.objects.get(id=cart)
			topay=paymenttoshop_tb(shopid=id1,amount=amount,date=x,cartid=cart1)
			topay.save()
			cart_tb.objects.all().filter(id=cart).update(shoppay='Paid')
			cart_tb.objects.all().filter(userid=ids,status='pending').update(status='Paid',date=x)
			pets=cart_tb.objects.all().filter(Q(status="Paid")|Q(status="Processing")|Q(status="Shipping")|Q(status="Delivered"),item='pet')
			foods=cart_tb.objects.all().filter(Q(status="Paid")|Q(status="Processing")|Q(status="Shipping")|Q(status="Delivered"),item='food')
			return render(request,'admin/admin_view_order.html',{'uv':pets,'xy':foods})
		else:
			return render(request,'user/cart.html')
	else:
		return render(request,'user/login-register.html')
#######################################################################################################

def admin_cancelpayment(request):
	if request.session['myid']:
		pets=cart_tb.objects.all().filter(Q(status="Paid")|Q(status="Processing")|Q(status="Shipping")|Q(status="Delivered"),item='pet')
		foods=cart_tb.objects.all().filter(Q(status="Paid")|Q(status="Processing")|Q(status="Shipping")|Q(status="Delivered"),item='food')
		return render(request,'admin/admin_view_order.html',{'uv':pets,'xy':foods})
	else:
		return render(request,'admin/login-register.html')

#############################################################################################################

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def paytoshop(request):
	if request.session.has_key('myid'):
		if request.method=='POST':
			gt=request.POST['amount']
			pid=request.GET['shop']
			cart=request.POST['cart']
			return render(request,'admin/payment_to_shop.html',{'amount':gt,'shop':pid,'cart':cart})

	else:
		return render(request,'user/login-register.html')




def view_vetenery(request):
	upd=vetenery_tb.objects.all().filter(status="pending")
	upd1=vetenery_tb.objects.all().filter(status="approved")
	upd2=vetenery_tb.objects.all().filter(status="rejected")
	print("-------------------------",upd)
	return render(request,"admin/admin_view_vetenarians.html",{'db':upd,'db1':upd1,'db2':upd2})


def admin_view_approved_vetenery(request):
	if request.method=='POST':
		print('==================')
		id1=request.GET['id']
		print(id1)
		register.objects.all().filter(id=id1).update(status1="approved")

		vetenery_tb.objects.all().filter(regid=id1).update(status="approved")
	upd1= vetenery_tb.objects.all().filter(status="approved")
	return render(request,"admin/admin_view_vetenarians.html",{'db1':upd1})

def admin_view_reject_vetenery(request):
	if request.method=='POST':
		print('==================')
		id1=request.GET['id']
		register.objects.all().filter(id=id1).update(status1="rejected")
		vetenery_tb.objects.all().filter(regid=id1).update(status="rejected")
	upd2= vetenery_tb.objects.all().filter(status="rejected")
	return render(request,"admin/admin_view_vetenarians.html",{'db2':upd2})


###############################################################################################################################
#############################################---PET SHOP---####################################################################
###############################################################################################################################




@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_login_register(request):
	return render(request,'pet-shop/shop_login_register.html')

################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_registrations(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		mobile=request.POST['number']
		address=request.POST['address']
		image=request.FILES['image']
		check=register.objects.all().filter(email=email)
		if check:
			return render(request,'pet-shop/shop_login_register.html',{'msg':"Email already exists"})
		add=register(name=name,email=email,password=password,phone=mobile,address=address,type="shop",status1="pending",Image=image)
		add.save()
		fname=register.objects.all()
		return render(request,'pet-shop/shop_login_register.html',{'db':fname,'msg':'success'})
	else:
		fname=register.objects.all()
		return render(request,'pet-shop/shop_login_register.html',{'msg':"error",'db':fname})

####################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_login(request):
	if request.method=="POST":
		username=request.POST['name']
		password1=request.POST['password']
		log=register.objects.all().filter(email=username,password=password1,type="shop",status1='approved')
		print(log)
		if log:
			for x in log:
				request.session["myid"]=x.id
				return render(request,'pet-shop/shop_home.html',{'db':log})
		else:
			return render(request,'pet-shop/shop_login_register.html',{'msg':'invalid credential or not approved'})
	else:
		return render(request,'pet-shop/shop_login_register.html')


#################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_home(request):
	return render(request,'pet-shop/shop_home.html')

#######################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_profile(request):
	myid=request.session['myid']
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		address=request.POST['address']
		number=request.POST['number']
		imgup=request.POST['imgupdate']
		if imgup=='Yes':
			image1=request.FILES['image']
			oldrec=register.objects.all().filter(id=myid)
			updrec=register.objects.get(id=myid)
			for x in oldrec:
				imgurl=x.Image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.Image=image1
			updrec.save()
		
		register.objects.filter(id=myid).update(name=name,email=email,address=address,phone=number)
		data=register.objects.all().filter(id=myid)
		return render(request,'pet-shop/shop_profile.html',{'data':data,'msg':'Successfully Updated'})
	else:
		data=register.objects.all().filter(id=myid)
		return render(request,'pet-shop/shop_profile.html',{'data':data})

########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_add_pets(request):
	if request.method=="POST":
		ii=request.session['myid']
		Category=request.POST['type']
		name=request.POST['name']
		Breed=request.POST['breed']
		Age=request.POST['age']
		Colour=request.POST['colour']
		size=request.POST['size']
		Vaccination=request.POST['vacci']
		Description=request.POST['desc']
		Price=request.POST['price']
		var=register.objects.get(id=ii)
		image1=request.FILES['image']
		availableqty=request.POST['aqty']
		toReg=add_pets(pid=var,Category=Category,name=name,Breed=Breed,Age=Age,Colour=Colour,size=size,Image=image1,Vaccination=Vaccination,Description=Description,Price=Price,status="available",type="shop",availableqty=availableqty)
		toReg.save()
		img=imgForm()
		return HttpResponseRedirect('/shop_view_pets/')
	else:
		return render(request,'pet-shop/shop_add_pets.html')

#####################################################################################################################
	
@cache_control(no_cache=True, must_revalidate=True,no_store=True)	
def shop_view_pets(request):
	ii=request.session["myid"]
	upd=add_pets.objects.all().filter(pid=ii,status='available')
	if upd.exists():
		return render(request,"pet-shop/shop_view_pets.html",{'db':upd})
	else:
		return render(request,'pet-shop/shop_view_pets.html')

##################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_reject_pets(request):
	id1=request.GET['id']
	add_pets.objects.all().filter(id=id1).update(status="rejected")
	up=add_pets.objects.all().filter(status="available",type='shop',pid=id1)	
	return render(request,'pet-shop/shop_view_pets.html',{'db':up})


##################################################################################################################3#

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_rejected_pets(request):
	ii=request.session["myid"]
	fromReg=add_pets.objects.all().filter(status='rejected',pid=ii)
	return render(request,'pet-shop/shop_view_reject_pets.html',{'db':fromReg})

#######################################################################################################################	

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_add_food(request):
	if request.method=="POST":
		ii=request.session['myid']
		Type=request.POST['name']
		Category=request.POST['Category']
		Description=request.POST['Description']
		quantity=request.POST['quantity']
		Price=request.POST['price']
		var=register.objects.get(id=ii)
		image1=request.FILES['image']
		availableqty=request.POST['aqty']
		toReg=add_food(fid=var,name=Type,Category=Category,quantity=quantity,Description=Description,Image=image1,Price=Price,status="available",availableqty=availableqty)
		toReg.save()
		db=add_food.objects.all().filter(fid=ii,status='available')
		return render(request,'pet-shop/shop_view_food.html',{'db':db})
	else:
		return render(request,'pet-shop/shop_add_food.html')

#####################################################################################################################
	
@cache_control(no_cache=True, must_revalidate=True,no_store=True)	
def shop_view_food(request):
	ii=request.session['myid']
	upd=add_food.objects.all().filter(status='available',fid=ii)
	if upd.exists():
		return render(request,"pet-shop/shop_view_food.html",{'db':upd})
	else:
		return render(request,'pet-shop/shop_view_food.html')

##################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_reject_food(request):
	uid=request.session['myid']
	id1=request.GET['id']
	add_food.objects.all().filter(id=id1).update(status="rejected")
	up=add_food.objects.all().filter(status="available",fid=uid)	
	return render(request,'pet-shop/shop_view_food.html',{'db':up})

##################################################################################################################3#

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_rejected_food(request):
	ii=request.session["myid"]
	fromReg=add_food.objects.all().filter(status='rejected',fid=ii)
	return render(request,'pet-shop/shop_view_reject_food.html',{'db':fromReg})

########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_user(request):
	vie=register.objects.all().filter(type="user")
	if vie.exists():
		return render(request,'pet-shop/shop_view_user.html',{'db':vie})
	else:
		return render(request,'pet-shop/shop_view_user.html')

##########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_rejected_user(request):
	fromReg=register.objects.all().filter(status1='rejected')
	return render(request,'pet-shop/shop_view_rejected_user.html',{'db':fromReg})

#######################################################################################################################		

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_applied_user(request):
	id1=request.GET['id']
	log=register.objects.all()
	ab=user_order_pets.objects.all().filter(id=id1)
	return render(request,'pet-shop/shop_view_users.html',{'db':ab,'abc':log})

##############################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_orders(request):
	id1=request.session['myid']
	print(id1)
	pets=cart_tb.objects.all().filter(shopid=id1,status='Paid',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Paid',item='food')
	print(pets)
	return render(request,'pet-shop/shop_view_order.html',{'uv':pets,'xy':foods})

#####################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_processing(request):
	id1=request.session['myid']
	pets=cart_tb.objects.all().filter(shopid=id1,status='Processing',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Processing',item='food')
	return render(request,'pet-shop/shop_view_order.html',{'uv':pets,'xy':foods})

#####################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_shipped(request):
	id1=request.session['myid']
	pets=cart_tb.objects.all().filter(shopid=id1,status='Shipped',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Shipped',item='food')
	print(pets)
	return render(request,'pet-shop/shop_view_order.html',{'uv':pets,'xy':foods})

#####################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_completed(request):
	id1=request.session['myid']
	pets=cart_tb.objects.all().filter(shopid=id1,status='Delivered',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Delivered',item='food')
	print(pets)
	return render(request,'pet-shop/shop_view_order.html',{'uv':pets,'xy':foods})

#####################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_processing(request):
	id1=request.session['myid']
	cid=request.GET['id']
	cart_tb.objects.all().filter(id=cid).update(status='Processing')
	pets=cart_tb.objects.all().filter(shopid=id1,status='Processing',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Processing',item='food')
	print(pets)
	return render(request,'pet-shop/shop_view_order.html',{'uv':pets,'xy':foods})

#####################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_shipping(request):
	id1=request.session['myid']
	cid=request.GET['id']
	cart_tb.objects.all().filter(id=cid).update(status='Shipping')
	pets=cart_tb.objects.all().filter(shopid=id1,status='Shipping',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Shipping',item='food')
	print(pets)
	return render(request,'pet-shop/shop_view_order.html',{'uv':pets,'xy':foods})

#####################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_delivered(request):
	id1=request.session['myid']
	cid=request.GET['id']
	cart_tb.objects.all().filter(id=cid).update(status='Delivered')
	pets=cart_tb.objects.all().filter(shopid=id1,status='Delivered',item='pet')
	foods=cart_tb.objects.all().filter(shopid=id1,status='Delivered',item='food')
	print(pets)
	return render(request,'pet-shop/shop_view_order.html',{'uv':pets,'xy':foods})

#####################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_mypayments(request):
	id1=request.session['myid']
	payments=paymenttoshop_tb.objects.all().filter(shopid=id1)
	return render(request,'pet-shop/shop_mypayments.html',{'pay':payments})

#######################################################################################################

########################################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_user_payment(request):
	ab=user_apply_laundry_tb.objects.all()
	return render(request,'shop_view_user_payment.html',{'db':ab})

##########################################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_userorder_completed(request):
	id1=request.GET['id']
	id2=request.session['myid']
	oldcheck=user_apply__tb.objects.all().filter(id=id1)
	if oldcheck:
			for x in oldcheck:
				oldpwd=x.amount
				if (oldpwd!="pending"):			
					user_apply__tb.objects.all().filter(id=id1).update(status="compleated")
					up=user_apply__tb.objects.all().filter(shopsid=id2,status="pending")	
					upd=user_apply__tb.objects.all().filter(shopsid=id2,status="approved")
					abc=_shop_tb.objects.all().filter(id=id2)
					print(up,'.....................................')
					return render(request,'shop_view_oder.html',{'db':up,'dbd':upd,'abc':abc})
				else:
					id1=request.GET['id']
					id2=request.session['myid']
					abc=_shop_tb.objects.all().filter(id=id2)
					up=user_apply__tb.objects.all().filter(id=id1)
					print("-----------------render page--------------")
					return render(request,'_amount.html',{'db':up,'abc':abc,'msg':"Enter amount"})
	else:
		id2=request.session['myid']
		abc=_shop_tb.objects.all().filter(id=id2)
		return render(request,'_amount.html',{'abc':abc})

#############################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_previous_order(request):
	id1=request.session['myid']
	print(id1,"..........................")
	log=_shop_tb.objects.all().filter(id=id1)
	up=user_apply__tb.objects.all().filter(shopsid=id1,status="compleated")
	return render(request,"shop_view_previousoder.html",{'db':up,'abc':log})

##########################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_update_pet(request):
	print('inside getData')
	if request.method=='GET':
		id2=request.GET['id']
		fromReg=add_pets.objects.all().filter(id=id2)
		print(fromReg)
		if fromReg.exists():
			print('get record')
			return render(request,'pet-shop/shop_update_pets.html',{'b':fromReg})
		else:
			print("failed")
			return render(request,"pet-shop/shop_update_pets.html")

###########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_update_pet(request):
	if request.method=="POST":
		print("----------update inside post-----------")
		up=request.GET['id']
		name=request.POST['name']
		Breed=request.POST['breed']
		Category=request.POST['cat']
		Age=request.POST['age']
		Colour=request.POST['colour']
		size=request.POST['size']
		Vaccination=request.POST['vacci']
		Description=request.POST['desc']
		Price=request.POST['price']
		ii=request.session['myid']
		imgup=request.POST['imgupdate']
		if imgup=='Yes':
			image1=request.FILES['image']
			oldrec=add_pets.objects.all().filter(id=up)
			updrec=add_pets.objects.get(id=up)
			for x in oldrec:
				imgurl=x.Image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.Image=image1
			updrec.save()
		
		add_pets.objects.filter(id=up).update(Category=Category,name=name,Breed=Breed,Age=Age,Colour=Colour,size=size,Vaccination=Vaccination,Description=Description,Price=Price,status="available" )
		up=add_pets.objects.all().filter(pid=ii,status='available')
		print("-----------------render page--------------")
		return render(request,'pet-shop/shop_view_pets.html',{'db':up})
	elif request.method=="GET":
		print("-----------------get update------------")
		id1=request.GET['id']
		up=add_pets.objects.all().filter(id=up)
		print("-----------------render page--------------")
		return render(request,'pet-shop/shop_view_pets.html',{'db':up})

##########################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_update_food(request):
	print('inside getData')
	if request.method=='GET':
		id2=request.GET['id']
		fromReg=add_food.objects.all().filter(id=id2)
		print(fromReg)
		if fromReg.exists():
			print('get record')
			return render(request,'pet-shop/shop_update_food.html',{'b':fromReg})
		else:
			print("failed")
			return render(request,"pet-shop/shop_update_food.html")

###########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_view_update_food(request):
	if request.method=="POST":
		print("----------update inside post-----------")
		up=request.GET['id']
		Type=request.POST['name']
		Category=request.POST['Category']
		quantity=request.POST['quantity']
		Price=request.POST['price']
		imgup=request.POST['imgupdate']
		if imgup=='Yes':
			image1=request.FILES['image']
			oldrec=add_food.objects.all().filter(id=up)
			updrec=add_food.objects.get(id=up)
			for x in oldrec:
				imgurl=x.Image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):		
					os.remove(pathtoimage)
					print('Successfully deleted')

			updrec.Image=image1
			updrec.save()
		add_food.objects.filter(id=up).update(name=Type,Category=Category,quantity=quantity,Price=Price,status="available" )
		uid=request.session['myid']
		up=add_food.objects.all().filter(fid=uid,status="available")
		print("-----------------render page--------------")
		return render(request,'pet-shop/shop_view_food.html',{'db':up})
	elif request.method=="GET":
		print("-----------------get update------------")
		id1=request.GET['id']
		up=add_food.objects.all().filter(id=up)
		print("-----------------render page--------------")
		return render(request,'pet-shop/shop_view_food.html',{'db':up})


#######################################################################################################################		
##############################################--USER--###################################################################
#######################################################################################################################		

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_home(request):
	food=add_food.objects.all().filter(status="available")
	pets=add_pets.objects.all().filter(status="available")
	shop=register.objects.all().filter(status1="approved",type='shop')
	return render(request,'user/home.html',{'fdb':food,'pdb':pets,'shop':shop})

########################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def about(request):
	return render(request,'user/about.html')

####################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def blog(request):
	return render(request,'user/blog.html')

####################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def blog_details(request):
	return render(request,'user/blog-details.html')

##################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def contact(request):
	return render(request,'user/contact.html')

####################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop(request):
	sid=request.GET['sid']
	pets=add_pets.objects.all().filter(pid=sid,status="available")
	foods=add_food.objects.all().filter(fid=sid,status="available")
	shop=register.objects.all().filter(id=sid)
	return render(request,'user/shopwise.html',{'pets':pets,'foods':foods,'shop':shop}) 

####################################### pets cart area ###################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def pets_addcart(request):
	if request.session.has_key('myid'):
		if request.method=='POST':
			pids=request.GET['id']
			petdet=add_pets.objects.all().filter(id=pids)
			for x in petdet:
				unitprice=x.Price
			qty=request.POST['qty']
			shop=int(request.POST['shop'])
			shipping=int(int(unitprice)*10/100)
			total=int(unitprice)*int(qty)+shipping
			date= datetime.datetime.now()
			ii=request.session["myid"]
			print(ii)				
			uid=register.objects.get(id=ii)
			x = datetime.datetime.now()
			pid=add_pets.objects.get(id=pids)
			ii=register.objects.get(id=ii)
			check=cart_tb.objects.all().filter(userid=ii,pid=pids,shipping=shipping,unitprice=unitprice,total=total,date=date)
			if check:
				mypet=cart_tb.objects.all().filter(userid=ii,status='pending',item="pet")
				myfood=cart_tb.objects.all().filter(userid=ii,status='pending',item="food")
				return render(request,'user/cart.html',{'uv':mypet,'xy':myfood,'msgkey':'Already Add to cart'})
			else:
				tocart=cart_tb(userid=ii,pid=pid,shipping=shipping,unitprice=unitprice,total=total,date=date,item='pet',quantity=qty,shopid=shop)
				tocart.save()
				thispet=add_pets.objects.all().filter(id=pids)
				for x in thispet:
					oldqty=x.availableqty
				newqty=int(oldqty)-int(qty)
				add_pets.objects.all().filter(id=pids).update(availableqty=newqty)
				mycart=cart_tb.objects.all().filter(userid=ii,status='pending')
				grandtotal=0
				for x in mycart:
					grandtotal=int(x.total)+grandtotal
				mypet=cart_tb.objects.all().filter(userid=ii,status='pending',item="pet")
				myfood=cart_tb.objects.all().filter(userid=ii,status='pending',item="food")
				return render(request,'user/cart.html',{'uv':mypet,'xy':myfood,'gt':grandtotal,'msgkey':'Add to cart'})
	else:
		print("*************************************************************")
		return render(request,'user/login-register.html')

###################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def delete_cartitem(request):
	ii=request.session['myid']
	cid=request.GET['id']
	cartitem=cart_tb.objects.all().filter(id=cid)
	for x in cartitem:
		items=x.item

	if items=="pet":
		for x in cartitem:
			itemid=x.pid.id
			quantity=x.quantity
		petsdata=add_pets.objects.all().filter(id=itemid)
		for x in petsdata:
			oldqty=x.availableqty
		newqty=int(oldqty)+int(quantity)
		add_pets.objects.all().filter(id=itemid).update(availableqty=newqty)
	elif items=="food":
		for x in cartitem:
			itemid=x.fid.id
			quantity=x.quantity
		petsdata=add_food.objects.all().filter(id=itemid)
		for x in petsdata:
			oldqty=x.availableqty
		newqty=int(oldqty)+int(quantity)
		add_food.objects.all().filter(id=itemid).update(availableqty=newqty) 
	cart_tb.objects.all().filter(id=cid).delete()
	mycart=cart_tb.objects.all().filter(userid=ii,status='pending')
	grandtotal=0
	for x in mycart:
		grandtotal=int(x.total)+grandtotal
	mypet=cart_tb.objects.all().filter(userid=ii,status='pending',item="pet")
	myfood=cart_tb.objects.all().filter(userid=ii,status='pending',item="food")
	return render(request,'user/cart.html',{'uv':mypet,'xy':myfood,'gt':grandtotal,'msg':'Successfully deleted'})

###################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def clear_mycart(request):
	ii=request.session['myid']
	cart_tb.objects.all().filter(userid=ii,status='pending').delete()
	mypet=cart_tb.objects.all().filter(userid=ii,status='pending',item="pet")
	myfood=cart_tb.objects.all().filter(userid=ii,status='pending',item="food")
	return render(request,'user/cart.html',{'uv':mypet,'xy':myfood,'msg':'Successfully cleared'})

###################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def cart(request):
	if request.session['myid']:
		ii=request.session['myid']
		mycart=cart_tb.objects.all().filter(userid=ii,status='pending')
		grandtotal=0
		for x in mycart:
			grandtotal=int(x.total)+grandtotal
		mypet=cart_tb.objects.all().filter(userid=ii,status='pending',item="pet")
		myfood=cart_tb.objects.all().filter(userid=ii,status='pending',item="food")
		return render(request,'user/cart.html',{'uv':mypet,'xy':myfood,'gt':grandtotal})
	else:
		return render(request,'user/login-register.html')

##################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def food_addcart(request):
	if request.method=='POST':
		print("=============================================")

		fids=request.GET.get('id')
		print(fids)
		fid=add_food.objects.get(id=fids)
		ii=request.session["myid"]
		print(ii)				
		uid=register.objects.get(id=ii)
		fooddet=add_food.objects.all().filter(id=fids)
		for x in fooddet:
			unitprice=x.Price
		qty=request.POST['qty']
		shop=int(request.POST['shop'])
		shipping=int(int(unitprice)*10/100)
		total=int(unitprice)*int(qty)+shipping
		date= datetime.datetime.now()
		ii=request.session["myid"]
		print(ii)				
		uid=register.objects.get(id=ii)
		x = datetime.datetime.now()
		ii=register.objects.get(id=ii)
		check=cart_tb.objects.all().filter(userid=ii,fid=fid,shipping=shipping,unitprice=unitprice,total=total,date=date)
		if check:
			mycart=cart_tb.objects.all().filter(userid=ii,status='pending')
			return render(request,'user/cart.html',{'uv':mycart,'msgkey':'Already Add to cart'})
		else:
			tocart=cart_tb(userid=ii,fid=fid,shipping=shipping,unitprice=unitprice,total=total,date=date,item='food',quantity=qty,shopid=shop)
			tocart.save()
			thisfood=add_food.objects.all().filter(id=fids)
			for x in thisfood:
				oldqty=x.availableqty
			newqty=int(oldqty)-int(qty)
			add_food.objects.all().filter(id=fids).update(availableqty=newqty)
			mycart=cart_tb.objects.all().filter(userid=ii,status='pending')
			grandtotal=0
			for x in mycart:
				grandtotal=int(x.total)+grandtotal
			mypet=cart_tb.objects.all().filter(userid=ii,status='pending',item="pet")
			myfood=cart_tb.objects.all().filter(userid=ii,status='pending',item="food")
			return render(request,'user/cart.html',{'uv':mypet,'xy':myfood,'gt':grandtotal,'msgkey':'Add to cart'})
	else:
		print("*************************************************************")
		return render(request,'user/login-register.html')

###########################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def checkout(request):
	return render(request,'user/checkout.html')

##################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def wishlist(request):
	return render(request,'user/wishlist.html')

##################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def my_account(request):
	return render(request,'user/my-account.html')

##################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def shop_list(request):
	return render(request,'user/shop-list.html')

#####################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def cat_food(request):
	cat=add_food.objects.all().filter(Category="cat",status="available")
	if cat.exists():
		return render(request,'user/cat_food.html',{'cfood':cat})
	else:
		print('failed to get data')

		return render(request,'user/index.html',{"data":'error'})

#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def dog_food(request):
	dog=add_food.objects.all().filter(Category="dog",status="available")
	if dog.exists():
		return render(request,'user/dog_food.html',{'dfood':dog})
	else:
		print('failed to get data')

		return render(request,'user/index.html',{"data":'error'})

#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def bird_food(request):
	bird=add_food.objects.all().filter(Category="bird",status="available")
	return render(request,'user/bird_food.html',{'bfood':bird})

#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def fish_food(request):
	fish=add_food.objects.all().filter(Category="fish",status="available")
	if fish.exists():
		return render(request,'user/fish_food.html',{'ffood':fish})
	else:
		print('failed to get data')

		return render(request,'user/index.html',{"data":'error'})

#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def adopt_cats(request):
	if request.method=='POST':
		petname=request.POST['petname']
		cat=add_pets.objects.all().filter(Category="cat",status="available",name=petname)
		return render(request,'user/cats.html',{'cat':cat})
	else:
		cat=add_pets.objects.all().filter(Category="cat",status="available")
		return render(request,'user/cats.html',{'cat':cat})
		

#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def adopt_dogs(request):
	if request.method=='POST':
		petname=request.POST['petname']
		dog=add_pets.objects.all().filter(Category="dog",status="available",name=petname)
		return render(request,'user/dogs.html',{'dog':dog}) 
	else:
		dog=add_pets.objects.all().filter(Category="dog",status="available")
		return render(request,'user/dogs.html',{'dog':dog}) 

	
#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def adopt_birds(request):
	if request.method=='POST':
		petname=request.POST['petname']
		bird=add_pets.objects.all().filter(Category="bird",status="available",name=petname)
		return render(request,'user/birds.html',{'bird':bird}) 
	else:
		bird=add_pets.objects.all().filter(Category="bird",status="available")
		return render(request,'user/birds.html',{'bird':bird}) 

	
#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def adopt_fishes(request):
	if request.method=='POST':
		petname=request.POST['petname']
		fish=add_pets.objects.all().filter(Category="fish",status="available",name=petname)
		return render(request,'user/fishes.html',{'fish':fish}) 
	else:
		fish=add_pets.objects.all().filter(Category="fish",status="available")
		return render(request,'user/fishes.html',{'fish':fish}) 


#######################################################################################################

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def pets_details(request):
	if request.session.has_key('myid'):
		ids=request.GET['id']
		print('inside getData')
		fromform=add_pets.objects.all().filter(id=ids)
		if fromform.exists():
			return render(request,'user/pets_details.html',{'db':fromform})
		else:
			return render(request,'user/login-register.html',{"data":'error'})
	else:
		return render(request,'user/login-register.html',{"data":'error'})

###########################################################################################################

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def food_details(request):
	if request.session.has_key('myid'):
		ids=request.GET['id']
		print('inside getData')
		fromform=add_food.objects.all().filter(id=ids)
		if fromform.exists():
			return render(request,'user/food_details.html',{'db':fromform})
		else:
			return render(request,'user/login-register.html',{"data":'error'})
	else:
		print('faied to get data')
		return render(request,'user/login-register.html',{"data":'error'})

##########################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login_register(request):
	return render(request,'user/login-register.html')

##################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_registrations(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		mobile=request.POST['number']
		address=request.POST['address']
		check=register.objects.all().filter(email=email)
		if check:
			return render(request,'user/login-register.html',{'msg':'Email already exists'})
		add=register(name=name,email=email,password=password,phone=mobile,address=address,type="user",status1="active")
		add.save()
		fname=register.objects.all()
		return render(request,'user/login-register.html',{'db':fname,'msg':'success'})
	else:
		fname=register.objects.all()
		return render(request,'user/login-register.html',{'msg':"error",'db':fname})

##################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_login(request):
	if request.method=="POST":
		username=request.POST['name']
		password1=request.POST['password']
		print("UUUUUUUUUUUUUUUUUUUUUU",username)
		print("PPPPPPPPPPPPPPPPP",password1)
		log=register.objects.all().filter(email=username,password=password1,type="user",status1='active')
		print(log)
		if log:
			for x in log:
				request.session["myid"]=x.id
				myid=x.id
			food=add_food.objects.all().filter(status="available")
			pets=add_pets.objects.all().filter(status="available")
			shop=register.objects.all().filter(status1="approved",type='shop')

			mycart=cart_tb.objects.all().filter(id=myid).count()
			return render(request,'user/home.html',{'db':log,'fdb':food,'pdb':pets,'shop':shop,'mc':mycart})
		else:
			print("---------------failed----------------")
			return render(request,'user/login-register.html',{'message':'invalid credential'})
	else:
		print("login failed")
		return render(request,'user/login-register.html')

#################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login_home(request):
	return render(request,'user/home.html')

#################################################################################################################

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def user_profile(request):
	ids=request.session['myid']
	print('inside getData')
	fromform=register.objects.all().filter(id=ids)

	return render(request,'user/user_profile.html',{'db':fromform})

###################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_update_profile(request):
	if request.method=='POST':
		id2=request.session['myid']
		fromReg=register.objects.all().filter(id=id2)
		print(fromReg)
		if fromReg.exists():
			return render(request,'user/user_profile.html',{'db':fromReg})
		else:
			return render(request,"user/user_profile.html")

###########################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_view_update_profile(request):
	if request.method=="POST":
		uid=request.session['myid']
		name=request.POST['name']
		password=request.POST['password']
		mobile=request.POST['number']
		address=request.POST['address']
		register.objects.filter(id=uid).update(name=name,password=password,phone=mobile,address=address,type="shop",status1="pending")
		up=register.objects.all().filter(id=uid)
		return render(request,'user/user_profile.html',{'db':up})
	elif request.method=="GET":
		id1=request.GET['id']
		up=register.objects.all().filter(id=up)
		return render(request,'user/user_profile.html',{'db':up})

####################################################################################################################

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def buynow(request):
	if request.session.has_key('myid'):
		gt=request.GET['gt']
		if request.method=='GET':
			pid=request.GET.get('id')
			ii=request.session["myid"]
			pview=add_pets.objects.all().filter(id=pid)
			uview=register.objects.all().filter(id=ii)
			return render(request,'user/user_payment.html',{'pb':pview,'ub':uview,'amount':gt})

	else:
		return render(request,'user/login-register.html')


#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def makepayment(request):
	if request.session['myid']:
		ids=request.session['myid']
		if request.method=='POST':
			amount=request.POST['amount']
			x = datetime.datetime.now()
			id1=register.objects.get(id=ids)
			topay=payment_tb(userid=id1,amount=amount,status='Paid',date=x)
			topay.save()
			cart_tb.objects.all().filter(userid=ids,status='pending').update(status='Paid',date=x)
			check=payment_tb.objects.all().filter(userid=id1)
			if check:
				mypet=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=ids,item="pet")
				myfood=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=ids,item="food")
				return render(request,'user/user_orders.html',{'uv':mypet,'xy':myfood})
			else:
				mycart=cart_tb.objects.all().filter(userid=ids,status='pending')
				grandtotal=0
				for x in mycart:
					grandtotal=int(x.total)+grandtotal
				mypet=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=ids,item="pet")
				myfood=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=ids,item="food")
				return render(request,'user/cart.html',{'uv':mypet,'xy':myfood,'gt':grandtotal})
		else:
			return render(request,'user/cart.html')
	else:
		return render(request,'user/login-register.html')
#######################################################################################################

def cancelpayment(request):
	if request.session['myid']:
		ii=request.session['myid']
		mycart=cart_tb.objects.all().filter(userid=ii,status='pending')
		grandtotal=0
		for x in mycart:
			grandtotal=int(x.total)+grandtotal
		return render(request,'user/cart.html',{'uv':mycart,'gt':grandtotal})
	else:
		return render(request,'user/login-register.html')

#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def orders(request):
	if request.session['myid']:
		ii=request.session['myid']
		mypet=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered") ,item="pet",userid=ii)
		myfood=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=ii,item="food")
		return render(request,'user/user_orders.html',{'uv':mypet,'xy':myfood})
	else:
		return render(request,'user/login-register.html')





#######################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def mypayments(request):
	if request.session.has_key('myid'):
		ii=request.session['myid']
		mypay=payment_tb.objects.all().filter(userid=ii)
		return render(request,'user/my_payments.html',{'uv':mypay})
	else:
		return render(request,'user/login-register.html')
		
########################################################################################################################	

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_view_result(request):
	id1=request.session['myid']
	ab=user_apply__tb.objects.all().filter(userid=id1)
	return render(request,'user_view_result.html',{'db':ab})

########################################################################################################################################################################
##########################################---LOGOUT---##########################################################################
########################################################################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		if request.session.has_key('mycartsess'):
			del request.session['mycartsess']
		logout(request)
	return HttpResponseRedirect('/')

#########################################################################################################################
def review(request):
	if request.session.has_key('myid'):
		userid=request.session['myid']
		userid=register.objects.get(id=userid)
		cid=request.GET['cartid']
		cartid=cart_tb.objects.get(id=cid)
		item=request.GET['item']
		if item=="pet":
			pid=request.GET['pid']
			rating=request.GET["val"]
			pids=add_pets.objects.get(id=pid)
			check=review_tb.objects.all().filter(userid=userid,pid=pids,cartid=cid)
			if check:
				mypet=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered") ,item="pet",userid=userid)
				myfood=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=userid,item="food")
				return render(request,'user/user_orders.html',{'uv':mypet,'xy':myfood})
			toreview=review_tb(userid=userid,pid=pids,item="pet",rating=rating,cartid=cartid)
			toreview.save()
			pet=add_pets.objects.all().filter(id=pid)
			ratingcount=review_tb.objects.all().filter(pid=pids).count()
			ratings=review_tb.objects.all().filter(pid=pids)
			totalrating=0
			for x in ratings:
				totalrating=totalrating+int(x.rating)
			newrating=totalrating/ratingcount
			add_pets.objects.all().filter(id=pid).update(rating=newrating)
		elif item=="food":
			fid=request.GET['fid']
			rating=request.GET["val"]
			fids=add_food.objects.get(id=fid)
			check=review_tb.objects.all().filter(userid=userid,fid=fids,cartid=cid)
			if check:
				mypet=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered") ,item="pet",userid=userid)
				myfood=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=userid,item="food")
				return render(request,'user/user_orders.html',{'uv':mypet,'xy':myfood})
			toreview=review_tb(userid=userid,fid=fids,item="food",rating=rating,cartid=cartid)
			toreview.save()
			food=add_food.objects.all().filter(id=fid)
			ratingcount=review_tb.objects.all().filter(fid=fids).count()
			ratings=review_tb.objects.all().filter(fid=fids)
			totalrating=0
			for x in ratings:
				totalrating=totalrating+int(x.rating)
			newrating=totalrating/ratingcount
			add_food.objects.all().filter(id=fid).update(rating=newrating)
		mypet=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered") ,item="pet",userid=userid)
		myfood=cart_tb.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=userid,item="food")
		return render(request,'user/user_orders.html',{'uv':mypet,'xy':myfood})


############################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def view_veterinerians(request):
	vet=vetenery_tb.objects.all().filter(status='approved')
	return render(request,'user/vetenarians.html',{'vet':vet}) 
	

############################################################################################################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def tutorials(request):
	return render(request,'user/tutorials.html') 

###############################################################################################################################
################################################# VETENARIAN ###################################################################
###############################################################################################################################
###########################################################################################################################

###########################################################################################################################


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def vetenery_login_register(request):
	return render(request,'vetenery/vetenery_login_register.html')

####################################################################################################################	

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def vetenery_registrations(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		mobile=request.POST['number']
		qualification=request.POST['qualification']
		experience=request.POST['experience']
		address=request.POST['address']
		image=request.FILES['image']
		check=register.objects.all().filter(email=email)
		if check:
			return render(request,'vetenery/vetenery_login_register.html',{'msg':"Email already exists"})
		add=register(name=name,email=email,password=password,phone=mobile,address=address,type="vetenery",status1="pending",Image=image)
		add.save()
		lstid = register.objects.latest('id')
		regid=register.objects.get(id=lstid.id)

		tovet=vetenery_tb(regid=regid,qualification=qualification,experience=experience)
		tovet.save()
		fname=register.objects.all()
		return render(request,'vetenery/vetenery_login_register.html',{'db':fname,'msg':'success'})
	else:
		fname=register.objects.all()
		return render(request,'vetenery/vetenery_login_register.html',{'msg':"error",'db':fname})

####################################################################################################################	
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def vetenery_login(request):
	if request.method=="POST":
		username=request.POST['name']
		password1=request.POST['password']
		log=register.objects.all().filter(email=username,password=password1,type="vetenery",status1='approved')
		print(log)
		if log:
			for x in log:
				request.session["myid"]=x.id
				return render(request,'vetenery/vetenery_home.html',{'db':log})
		else:
			return render(request,'vetenery/vetenery_login_register.html',{'msg':'invalid credential or not approved'})
	else:
		return render(request,'vetenery/vetenery_login_register.html')


#################################################################################################################
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def personal_vetenery(request):
	if request.session.has_key('myid'):
		myid=request.session['myid']
		if request.method=="POST":
			name=request.POST['name']
			address=request.POST['address']
			contact=request.POST['contact']
			imgupdate=request.POST['imgupdate']
			if imgupdate=='Yes':
				image1=request.FILES['image']
				oldrec=register.objects.all().filter(id=myid)
				updrec=register.objects.get(id=myid)
				for x in oldrec:
					imgurl=x.Image.url
					pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
					if os.path.exists(pathtoimage):
						os.remove(pathtoimage)
						print('Successfully deleted')
				updrec.Image=image1
				updrec.save()
			register.objects.all().filter(id=myid).update(name=name,address=address,phone=contact)
			data=register.objects.all().filter(id=myid)
			return render(request,'vetenery/vetenery_personaldetails.html',{'data':data,'success':'Successfully updated'})
		else:
			data=register.objects.all().filter(id=myid)
			return render(request,'vetenery/vetenery_personaldetails.html',{'data':data})
	else:
		return render(request,'vetenery/vetenery_login_register.html')



@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def qualexp_vetenery(request):
	if request.session.has_key('myid'):
		myid=request.session['myid']
		if request.method=="POST":
			qualification=request.POST['qualification']
			experience=request.POST['experience']
			vetenery_tb.objects.all().filter(regid=myid).update(experience=experience,qualification=qualification)
			data=vetenery_tb.objects.all().filter(regid=myid)
			return render(request,'vetenery/vetenery_expandqualifications.html',{'data':data,'success':'Successfully updated'})
		else:
			data=vetenery_tb.objects.all().filter(regid=myid)
			return render(request,'vetenery/vetenery_expandqualifications.html',{'data':data})
	else:
		return render(request,'vetenery/vetenery_login_register.html')




@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def consult_vetenery(request):
	if request.session.has_key('myid'):
		myid=request.session['myid']
		if request.method=="POST":
			days=request.POST['days']
			time=request.POST['time']
			clinic=request.POST['clinic']
			vetenery_tb.objects.all().filter(regid=myid).update(days=days,time=time,clinic=clinic)
			data=vetenery_tb.objects.all().filter(regid=myid)
			return render(request,'vetenery/vetenery_consultationdetails.html',{'data':data,'success':'Successfully updated'})
		else:
			data=vetenery_tb.objects.all().filter(regid=myid)
			return render(request,'vetenery/vetenery_consultationdetails.html',{'data':data})
	else:
		return render(request,'vetenery/vetenery_login_register.html')



@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def chngepwd_vetenery(request):
	if request.session.has_key('myid'):
		myid=request.session['myid']
		if request.method=="POST":
			old=request.POST['old']
			new=request.POST['new']
			cnew=request.POST['cnew']
			getdata=register.objects.all().filter(id=myid)
			for x in getdata:
				password=x.password
			if(password==old):
				if(new==cnew):
					register.objects.all().filter(id=myid).update(password=new)
					data=register.objects.all().filter(id=myid)
					return render(request,'vetenery/vetenery_changepassword.html',{'data':data,'success':'Successfully updated'})
				else:
					data=register.objects.all().filter(id=myid)
					return render(request,'vetenery/vetenery_changepassword.html',{'data':data,'error':'Password missmatch error..!!!'})					
			else:
				data=register.objects.all().filter(id=myid)
				return render(request,'vetenery/vetenery_changepassword.html',{'data':data,'error':'Incorrect old password'})
		else:
			data=register.objects.all().filter(id=myid)
			return render(request,'vetenery/vetenery_changepassword.html',{'data':data})
	else:
		return render(request,'vetenery/vetenery_login_register.html')






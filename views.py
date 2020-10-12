from django.shortcuts import render,redirect
from django.http import HttpResponse
from Covid19.models import *

# Create your views here.
def home(req):
	#data={'name':'nani','roll':452}
	#,{'data':data}
	return render(req,"Covid19/home.html")

def about(req,user,des):
	return HttpResponse("This is "+user+" I am "+des)
#def home(req,user,age,gender):
#	return HttpResponse("Hi This is "+user+" and my age is "+age+" , my Gender is "+gender)	

def welcome(req):
	return render(req,"Covid19/welcome.html")


def task2(request):
	return render(request,"Covid19/task2.html")

def register(req):
	if req.method=="POST":
		name=req.POST['uname']
		age=req.POST['age']
		email=req.POST['pemail']
		data=Patients.objects.create(P_name=name,P_age=age,P_email=email)
		return HttpResponse("data added succesfully")
	return render(req,"Covid19/register.html")

def student(req):
	if req.method=="POST":
		name=req.POST['name']
		age=req.POST['age']
		phone=req.POST['phone']
		email=req.POST['semail']
		rollno=req.POST['rollno']
		gender=req.POST['gender']
		address=req.POST['address']
		username=req.POST['username']
		password=req.POST['password']
		data=Students.objects.create(S_name=name,S_age=age,S_phone=phone,S_email=email,S_rollno=rollno,S_gender=gender,S_address=address,S_username=username,S_password=password)
		return HttpResponse('Data Added Succesfully')
	return render(req,"Covid19/student.html") 




def studentdisplay(req):
	data=Students.objects.all()
	return render(req,"Covid19/studentdisplay.html",{"info":data})


def sdeleteinfo(req,id):
	data=Students.objects.get(id=id)
	data.delete()
	return redirect('/studentdisplay.html')

def studentedit(req,id):
	data=Students.objects.get(id=id)
	return render(req,"Covid19/studentedit.html",{'data':data})

def studentupdate(req,id):
	if req.method=="POST":
		name=req.POST['a']
		age=req.POST['b']
		phone=req.POST['c']
		email=req.POST['d']
		rollno=req.POST['e']
		gender=req.POST['f']
		address=req.POST['g']
		username=req.POST['h']
		password=req.POST['i']
		data=Students.objects.filter(id=id).update(S_name=name,S_age=age,S_phone=phone,S_email=email,S_rollno=rollno,S_gender=gender,S_address=address,S_username=username,S_password=password)
		return HttpResponse("Data Updated Succesfully")
	return render(req,"Covid19/studentupdate.html")


def index(req):
	return render(req,"Covid19/index.html")

def display(req):
	data=Patients.objects.all()
	return render(req,"Covid19/display.html",{"info":data})

def edit(req,id):
	data=Patients.objects.get(id=id)
	return render(req,"Covid19/edit.html",{'data':data})

def update(req,id):
	if req.method=="POST":
		name=req.POST['a']
		age=req.POST['b']
		email=req.POST['c']
		data=Patients.objects.filter(id=id).update(P_name=name,P_age=age,P_email=email)
		return HttpResponse("Data Updated")
	return render(req,"Covid19/update.html")


def deleteinfo(req,id):
	data=Patients.objects.get(id=id)
	data.delete()
	return redirect('/display.html')



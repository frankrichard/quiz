from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .models import Questions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
import datetime
from django.utils import timezone
from datetime import datetime
import time


from django.views.decorators.cache import cache_control


from django.contrib import messages
mark = int(1)
count = int(1)
def index(request):
    #first page
   return render(request,"login.html",{})
def getData(request):
    #creating new questions
   if request.method=='POST':
       qno=int(request.POST.get('qno'))
       qno = qno + 1
       question_1=request.POST.get('question')
       option_1=request.POST.get('option1')
       option_2=request.POST.get('option2')
       option_3=request.POST.get('option3')
       option_4=request.POST.get('option4')
       answer = request.POST.get('answer')
       questi_no = Questions.objects.all().count()
       questi_no = questi_no + 1
       
       context={

                'ques':question_1,
                'op1':option_1,
                'op2':option_2,
                'op3':option_3,
                'op4':option_4,
               } 
       questions = Questions(question = question_1,option1 = option_1,option2 = option_2,option3 = option_3,option4 = option_4,answer = answer,questionno = questi_no)
       questions.save()
       if (qno == 11):
            qu = Questions.objects.all().count()
            counter = int((qu - (qu%10))/10)
            print(counter)
            list1 = []
            for i in range(0,counter):
                list1.append(i+1)
            
            return render(request,'adminlogin.html',{'list1':list1})
       else:
           return render(request,'createquiz.html',{'qno':qno})
def getData1(request):
    #checking user login(authentication)
    if request.method=='POST':
        username = request.POST['sname']
        spassword_1 = request.POST['spassword']
        
        user = authenticate(username = username, password = spassword_1)
        if user is not None:
            click = 1
            temp = 2
            mark = 0
            stud = Student.objects.filter(name = username).exists()
            if stud is True:
                stud1 = Student.objects.filter(name = username)
                print(stud1)
                
                request.session['username'] = username
                qu = Questions.objects.all().count()
                counter = int((qu - (qu%10))/10)
    
                list1 = []
                for i in range(0,counter):
                    list1.append(i+1)



                return render(request,"studentslogin.html",{'click':click,'list1':list1,'temp':temp,'mark':mark,'username':username,'stud1':stud1})
            else:
                print(username)
                stud2 = Student.objects.create(name = username,no_of_attempts = "0",total_marks = "0",stu_question = "0",youranswer = "0",crctans = "0")
                stud2.save()
                stud1 = Student.objects.filter(name = username)
                qu = Questions.objects.all().count()
                counter = int((qu - (qu%10))/10)
    
                list1 = []
                for i in range(0,counter):
                    list1.append(i+1)
                
                return render(request,"studentslogin.html",{'click':click,'temp':temp,'mark':mark,'username':username,'stud1':stud1,'list1':list1})
        else:
            messages.info(request,'invalid username')    
            return redirect('/')
def getData2(request):
    #checking admin login
    if request.method == 'POST':
        aname_1=request.POST.get('aname')
        apassword_1=request.POST.get('apassword')
        context={
                'ana':aname_1,
                'apass':apassword_1,
        }
        stu = Student.objects.all()
    if aname_1 == "admin":
        if apassword_1 == "admin1234":
            qu = Questions.objects.all().count()
            
            counter = int((qu - (qu%10))/10)
            print(counter)
            list1 = []
            for i in range(0,counter):
                list1.append(i+1)
              
            
            return render(request,"adminlogin.html",{'list1':list1})
        else:
            messages.info(request,'invalid password')
            return redirect('/')
    else:
        messages.info(request,'invalid username')
        return redirect('/')
def getData3(request):
    #creating new student
    if request.method == 'POST':
        sname_2=request.POST['sname2']
        spassword_2=request.POST['spassword2']
        if User.objects.filter(username=sname_2).exists():
            qu = Questions.objects.all().count()
            
            counter = int((qu - (qu%10))/10)
            print(counter)
            list1 = []
            for i in range(0,counter):
                list1.append(i+1)
              
            
            messages.info(request,'username taken')
            return render(request,"adminlogin.html",{'list1':list1})    
        else:

            user = User.objects.create_user(username=sname_2,password=spassword_2)
            user.save()
            print("user created")
            mes = "user created successfully"
            qu = Questions.objects.all().count()
            
            counter = int((qu - (qu%10))/10)
            print(counter)
            list1 = []
            for i in range(0,counter):
                list1.append(i+1)
              
            
            return render(request,"adminlogin.html",{'mes':mes,'list1':list1})     
        
    else:
        return render(request,"adminlogin.html")


def stuquestion(request):
    #displays questions one by one and saved student answers
    if request.method == 'POST':
        username = request.POST.get('username')
        
        id = request.POST['id']
        click1 = request.POST['click']
        if click1 == "":
            
            qnocount = int(request.POST.get('qnocount'))
            click2 = int(request.POST['click2'])
            mark = int(request.POST.get('mark'))
            opt = request.POST.get('selected_answer')
            print(click2)
            
            print(opt)
            if opt != None:
                
                
                ques1 = list(Questions.objects.filter(questionno = (click2-1)))
                for q in ques1:
                    store=q.answer
                    stud3 = Student.objects.create(name = username,total_marks = 0,no_of_attempts = 0,stu_question = q.question,youranswer = opt,crctans = store)
                    stud3.save()

                    if opt==store:
                    
                        mark = mark+1
                    
                    else:
                        print(0)
            else:
                
                
                starttime = time.time()
                request.session['hello'] = starttime
            temp = Questions.objects.all().count()+1
            ques = list(Questions.objects.filter(questionno = click2))
            print(ques)
            click2 = click2 + 1
            if click2 == qnocount+1:
                username = request.session['username']

                stud = Student.objects.filter(name = username).count()
                
                if stud == 1:
                    attempt = stud
                else:
                    attempt = stud + 1
                

                print(attempt)
                stud2 = Student.objects.create(name = username,no_of_attempts = attempt,total_marks = mark,stu_question = "0",youranswer = "0",crctans = "0")
                stud2.save()     

                endtime = time.time()
                print(endtime)
                sesmsg = request.session['hello']
                print(sesmsg)
                time_taken = round(endtime-sesmsg,0)
                
                
                           
                
                return render(request,"finish.html",{'mark':mark,'time_taken':time_taken})
            context={
                'click2':click2,
                'ques':ques,
                'temp':temp,
                'mark':mark,    
                'username':username,
                'qnocount':qnocount,
            }
            return render(request,'studentslogin.html',context)
        else:
            click = int(click1)
            click =""
            
            mark = 0
            qno = (int(request.POST.get('quiz1'))-1)*10
            click2 = qno + 1
            print(qno)
            qnocount = click2 + 10
            context={
                'click':click,
                'click2':click2,
                'mark':mark,
                'username':username,
                'qnocount':qnocount,
                
            }
            return render(request,'studentslogin.html',context)        
def logout(request):
    #redirecting to home page
    return render(request,'login.html',{})

@cache_control(no_cache=False, must_revalidate=False)

def func():
    return render("login.html")
def newquiz(request):
    #displays the textboxes to record the answer for question creation
    qno = 1
    return render(request,"createquiz.html",{'qno':qno})
  #some code
def dele(request,p):
    #displaying all the quiz in admin page
    
    p = p - 1
    p = (p * 10)
    
    q = Questions.objects.all()[p:p+10]
    no = p
    
    return render(request,"quizview.html",{'q':q,'no':no})
def delete(request,s):
    #deleting the quiz
    n = Questions.objects.all().count()
    for i in range(0,10):
        s = s+1
        Questions.objects.filter(questionno=s).delete()
    
    
    for i in range(s,n):
        s=s+1
        print(s)
        Qu = Questions.objects.filter(questionno = s).update(questionno=s-10)
        
    
    qu = Questions.objects.all().count()
    counter = int((qu - (qu%10))/10)
    
    list1 = []
    for i in range(0,counter):
        list1.append(i+1)
    


    return render(request,"adminlogin.html",{'list1':list1})

# Create your views here.

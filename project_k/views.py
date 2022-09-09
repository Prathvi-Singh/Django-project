from django.http import HttpResponse
from django.shortcuts import render
# import pandas as pd
def index(request):

    return render(request , 'index.html')
def academics(request):
    return render(request ,'academics.html')

def library(request):
    return render(request,'library.html')

def mess(request):
    return render(request,'mess.html')

def scholarship(request):
    return render(request,'scholarship.html')
def sports(request):
    return render(request,'sports.html')
def hostel(request):
    return render(request,'hostel.html')
def department(request):
    return render(request,'department.html')
def analyze(request):
    a=request.GET.get("text",'default')
    b=request.GET.get("problem","OFF")









    # t=""
    a=a.lower()
    count=0
    t=""
    if(b=="on"):
        f=open("problems.txt",'a')
        f.write(a)
        f.close()
        g=open("problems.txt",'r')
        t=g.read()
        g.close()
        param={'p':t}
        return render(request , 'analyze.html' , param)


    if 'cricket' in a:
        count=count+1
        f = open("cricket.txt", "r")
        t = f.read() + "\n"
        f.close()

    if 'badminton' in a:
        count=count+1
        f = open("badminton.txt", "r")
        t = t+ f.read() +"\n"
        f.close()
        # return render(request,'sports.html')
    if 'sports' in a:
        # count=count+1
        # f = open("badminaton.txt", "r")
        # t = t+ f.read() +"\n"
        # f.close()
        return render(request, 'sports.html')

    if 'kabaddi' in a:
        count=count+1
        f = open("kabaddi.txt", "r")
        t =t+ f.read() + "\n"
        f.close()

    if 'chess' in a:
        count=count+1
        f = open("chess.txt", "r")
        t =t+ f.read() +"\n"
        f.close()



    if 'carram' in a:
        count=count+1
        f = open("carram.txt", "r")
        t =t+ f.read() +"\n"
        f.close()

    if 'football' in a:
        count=count+1
        f = open("football.txt", "r")
        t =t+ f.read() +"\n"
        f.close()
    if 'department' in a:
        return render(request, 'department.html')

    if 'academics' in a:
        # count=count+1
        # f = open("prathvi.txt", "r")
        # t =t+ f.read() +"\n"
        # f.close()
        return render(request,'academics.html')

    if 'library' in a:
        # count=count+1
        # f = open("library.txt", "r")
        # t = t+f.read()+ "\n"
        # f.close()
        return render(request,'library.html')

    if 'scholarship' in a:
        # count=count+1
        # f = open("scholarship.txt", "r") + "\n"
        # t =t+ f.read()
        # f.close()
        return render(request,'scholarship.html')
    #
    #
    #
    if 'mess' in a:
        # count=count+1
        # f = open("mess.txt", "r")
        # t =t+ f.read() +"\n"
        # f.close()
        return render(request,'mess.html')

    if 'club' in a:
        count=count+1
        f = open("club.txt", "r")
        t =t+ f.read()+"\n"
        f.close()
    if 'placement' in a:
        count=count+1
        f = open("placement.txt", "r")
        t =t+ f.read()+"\n"
        f.close()
    if 'hostel' in a:
        # count=count+1
        # f = open("hostel.txt", "r")
        # t =t+f.read()+"\n"
        # f.close()
        return render(request,'hostel.html')
    if 'cse' in a:
        count=count+1
        f = open("cse.txt", "r")
        t =t+ f.read()+"\n"
        f.close()
        param={'r':t}
        # return render(request, 'cse.html',param)
    if 'ece' in a:
        count=count+1
        f = open("ece.txt", "r")
        t =t+ f.read()+"\n"
        f.close()

    if 'mechanical' in a:
        count=count+1
        f = open("mehanical.txt", "r")
        t =t+ f.read()+"\n"
        f.close()
    if 'aids' in a:
        count=count+1
        f = open("aids.txt", "r")
        t =t +f.read()+"\n"
        f.close()
    if 'exam' in a:
        count=count+1
        f = open("exam.txt", "r")
        t =t+f.read()+"\n"
        f.close()
    if 'fee' in a:
        count=count +1
        f = open("fee.txt", "r")
        t = t + f.read() + "\n"
        f.close()

    # if (a.isdigit()):
    #     t="Try again"
    #
    else:
        if(count==0):
            f = open("all.txt", "r")
            t = f.read()
            f.close()



    # a={
    #     'Name':'Awdhesh Kumar',
    #     'roll': '120cs0026',
    #     'email':"120cs0026@iiitk.ac.in",
    #     'phone':'9'
    # }
    # c="prathvi"
    # b=list(c)
    #
    # if "academics" in a:
    #
    #
    #     f=open("prathvi.txt","r")
    #     t=f.read()
    #     f.close()
    # f = open("prathvi.txt", "r")
    # t=f.read()
    # f.close()
    #
    # t1=pd.Series(t)



    param={'p':t}

    return render(request , 'analyze.html' , param)
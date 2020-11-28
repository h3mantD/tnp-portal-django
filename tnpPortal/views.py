from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import loginDataForm, studDataForm
from .models import Logindata, Studdata, Admindata, Selectedstud
from django.contrib import messages

import mysql.connector



def logout(request):
    request.session.flush()
    return redirect('index')

def home(request):
    return render(request, 'logins.html', {
        'link':'signUp',
        't': 'Sign Up',
    })

def signUp(request):

    form = loginDataForm()

    if request.method == "POST":
        form = loginDataForm(request.POST)

        if form.is_valid:
            form.save()
        
        return redirect('studLogin')

    return render(request, 'signup.html', {
        'link':'student',
        't': 'Log In',
        'form':form,
    })


class studInfo:
    fname = ""
    lname = ""
    email = ""
    cno = ""
    b_name = ""
    cyear = ""
    roll = ""
    address = ""
    tenth = ""
    twelth = ""
    avg_marks = ""
    nback = ""
    add_info = ""


def studLogin(request):

    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pass']

        data = Logindata.objects.values().get(uname=username)
        
        if password == data['password']:
            #request.session['user'] = data[5]
            request.session['id'] = str(data['id'])
            count = Studdata.objects.filter(studid=data['id']).count()
            
            if count < 1:
                return redirect('student/'+str(data['id']))

            return render(request, 'studPortal.html', {
                'id':data['id'],
            })


    return render(request, 'studLogin.html', {
        'link':'signUp',
        't': 'Sign Up',
    })

def studDetails(request, id):
    
    if 'id' in request.session and request.session['id'] == str(id):

        data = studInfo()
        count = Studdata.objects.filter(studid=id).count()
        print(count)

        values = Logindata.objects.values().get(pk=id)
            
            
        data.fname = values['fname']
        data.lname = values['lname']
        data.email = values['e_mail']
        data.cno = values['mob_no']


        form = studDataForm(initial={
                'studid':values['id'],
                'fname':data.fname,
                'lname':data.lname,
                'e_mail':data.email,
                'mob_no':data.cno,
                
            })

        if request.method == "POST":
            if count < 1:
                updatedForm = studDataForm(request.POST)
                
                if updatedForm.is_valid():
                    
                    print(updatedForm.as_table())
                    
                    updatedForm.save()

                    Logindata.objects.filter(pk=id).update(info_stat='y')
                    messages.add_message(request, messages.INFO, 'you have updated your information')
                    return render(request, 'studPortal.html', {
                        'link':'logout',
                        't':'Logout'
                    } )
                else:
                    err = updatedForm.errors
                    print(err)
                    return render(request, 'studInfo.html', {
                        'form':updatedForm,
                        'err':err,
                        'link':'logout',
                        't':'Logout'
                    })
            else:
                updatedForm = studDataForm(request.POST)

                print(updatedForm['roll'].value())

                if updatedForm.is_valid():
                    data = Studdata.objects.get(studid=id)
                    data.fname = updatedForm['fname'].value()
                    data.lname = updatedForm['lname'].value()
                    data.b_name = updatedForm['b_name'].value()
                    data.cyear = updatedForm['cyear'].value()
                    data.roll = updatedForm['roll'].value()
                    data.address = updatedForm['address'].value()
                    data.e_mail = updatedForm['e_mail'].value()
                    data.mob_no = updatedForm['mob_no'].value()
                    data.tenth = updatedForm['tenth'].value()
                    data.twelth = updatedForm['twelth'].value()
                    data.avg_marks = updatedForm['avg_marks'].value()
                    data.nback = updatedForm['nback'].value()
                    data.add_info = updatedForm['add_info'].value()

                    data.save()
                    
                    #return HttpResponse('<h1>form updated again</h1>')
                    return redirect('http://127.0.0.1:8000/student/'+str(id))

        if count < 1:
            values = Logindata.objects.values().get(pk=id)
            
            
            data.fname = values['fname']
            data.lname = values['lname']
            data.email = values['e_mail']
            data.cno = values['mob_no']


            form = studDataForm(initial={
                    'studid':values['id'],
                    'fname':data.fname,
                    'lname':data.lname,
                    'e_mail':data.email,
                    'mob_no':data.cno,
                    
                })

            return render(request, 'studInfo.html', {
                'form':form,
                'link':'logout',
                't':'Logout'
                })
        else:
            values = Studdata.objects.values().get(studid=id)
            data.fname = values['fname']
            data.lname = values['lname']
            data.email = values['e_mail']
            data.cno = values['mob_no']
            
            form = studDataForm(initial={
                    'studid':values['id'],
                    'fname':data.fname,
                    'lname':data.lname,
                    'e_mail':data.email,
                    'mob_no':data.cno,
                    'b_name':values['b_name'],
                    'roll':values['roll'],
                    'address':values['address'],
                    'tenth':values['tenth'],
                    'twelth':values['twelth'],
                    'avg_marks':values['avg_marks'],
                    'nback':values['nback'],
                    'add_info':values['add_info'],
                    'cyear':values['cyear'],

                })
            messages.add_message(request, messages.INFO, 'Already you have updated your information')
            return render(request, 'studInfo.html', {
                'form':form,
                'link':'logout',
                't':'Logout'
                })
    else:
        return HttpResponse('<h1>403!! not accessable</h1>')

            
def adminLogin(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pass']

        passw = Admindata.objects.get(uname=username)

        if password == str(passw):
            request.session['user'] = 'admin'
            return render(request, 'adminPortal1.html')

    return render(request, 'adminlogin.html')

def connectToDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="kakashi",
        password="hemant_D",
        database="tnp",
    )
    return mydb

def shortList(request):
    if 'user' in request.session and request.session['user'] == 'admin':
        if request.method == "POST":
            mydb = connectToDB()
            myc = mydb.cursor()            

            cname = request.POST["cname"]
            tenth = request.POST["10th"]
            twelth = request.POST["12th"]
            degree = request.POST["degree"]
            nback = request.POST["backlogs"]
            # where tenth >= %s and twelth >= %s and avg_marks >= %s and nback <= %s', (tenth, twelth, degree, nback,)
            myc.execute('select studid from studdata where tenth >= %s and twelth >= %s and avg_marks >= %s and nback <= %s', (tenth, twelth, degree, nback,) )
            res = myc.fetchall()
            
            for x in res:
                f = Selectedstud(company=cname, studid=x[0])
                f.save()

            messages.add_message(request, messages.INFO, "Students are shortlisted successfully")

            return render(request, 'adminPortal1.html')

        return render(request, 'shortList.html')

class compData:
    id = ""
    comp = ""

def getStudData(request):

    if 'user' in request.session and request.session['user'] == 'admin':
        
        mydb = connectToDB()
        myc = mydb.cursor()
        
        myc.execute('select * from selectedstud')
        data = myc.fetchall()

        compSet = set()
        for x in data:
            compSet.add(x[2])

        dataList = []
        if request.method == "POST":
            comp = request.POST['domain']

            myc.execute('select * from selectedstud where company=%s',(comp,))
            data = myc.fetchall()
            

            #print(data)

            for x in data:
                obj = compData()
                obj.id = x[1]
                obj.comp = x[2]
                dataList.append(obj)
        
            return render(request, 'studData.html', {
                    't':"Logout",
                    'link':"logout",
                    'dataList': dataList,
                    'comp': compSet,
                    'count': len(dataList)
            })

        else:
            dataList = []
            myc.execute('select * from selectedstud')
            data = myc.fetchall()

            compSet = set()
            for x in data:
                obj = compData()
                obj.id = x[1]
                obj.comp = x[2]
                compSet.add(x[2])
                dataList.append(obj)
        
            return render(request, 'studData.html', {
                    't':"Logout",
                    'link':"logout",
                    'dataList': dataList,
                    'comp':compSet,
                    'count': len(dataList)
            })


def notify(request, id):

    data = Selectedstud.objects.filter(studid=id)
    
    return render(request, 'temp.html', {
        't':"Logout",
        'link':"logout",
        'comp':data,
    })
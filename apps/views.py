from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from datetime import date
from .models import rooms, booking, admin_table, payments, phone
from django.contrib.auth import logout
from django.utils.dateparse import parse_date
from django.core.mail import EmailMessage

import datetime

# Create your views here.

'''def base(request):
    return render(request, 'base1.html')'''

'''def adminhome(request):
    return render(request,'adminhome.html')'''


def signup1(request):
    if request.method == "POST":
        name = request.POST['name']
        passwd = request.POST['password']
        passcomf = request.POST['password2']
        email = request.POST['email']
        pho_no = request.POST['ph_no']
        if passwd == passcomf:
            user = User.objects.create_user(username=name, password=passwd, email=email)
            user.save()
            t = User.objects.get(username=name)
            det = phone.objects.create(users_id=t.id, phone=pho_no)
            det.save()
            return redirect('login')
        else:
            return redirect('chanjal')
    else:
        return render(request, 'signup.html')


def login(request):
    try:
        y = admin_table.objects.get(user_name=request.POST['name'])
        if y.password == request.POST['password']:
            request.session['user_id'] = y.id
            return redirect('adminhome')
        else:
            return redirect('login')

    except:
        if request.method == "POST":
            name = request.POST['name']
            paswd = request.POST['password']
            user = auth.authenticate(username=name, password=paswd)
            if user is not None:
                auth.login(request, user)
                return render(request, 'base1.html')
            else:
                return redirect('login')
        else:
            return render(request, 'login.html')


def adminhome(request):
    return render(request, 'admin/adminhome.html')


def viewdetails(request):
    r = rooms.objects.all()
    return render(request, 'list.html', {'l': r})


def addrooms(request):
    if request.method == "POST":

        c = request.POST['date']
        d = request.POST['price']
        q = request.POST['room_number']
        f = request.POST['room_type']
        data = rooms(date=c, price=d, room_type=f, room_no=q)
        data.save()
        return redirect('adminhome')
    else:
        return render(request, 'admin/addroom.html')


def roomtype_view(request):
    if request.method == "POST":
        a = request.POST['cars']
        print(a)
        abc = rooms.objects.filter(room_type=a)
        return render(request, 'booking.html', {'abc': abc})
    else:
        return render(request,'base1.html')


'''
def booking(request):
    if request.method == "POST":
        r = request.method.POST['room_number']
        fr = request.method.POST['from_date']
        am = request.method.POST['amount']
        no_days = request.method.POST['no_of_days']
        # tot=request.method.POST['total_amount']

        a = rooms.objects.get(id=id)
        tot = int(a.price) * int(no_days)

        print(tot)
        abc = booking.objects.create(room_number=r, from_date=fr, amount=am, no_of_days=no_days, total_amount=tot)
        abc.save()
        return render(request, 'booking.html')
'''


def booking_page(request, id):
    room = rooms.objects.filter(id=id)
    return render(request, 'booking.html', {'room': room})


def conf_booking(request, id):
    room = rooms.objects.get(id=id)
    # fr = float(request.POST['from_date'])
    # to = float(request.POST['to_date'])
    fr_d = request.POST['from_date']
    to_d = request.POST['to_date']
    fdate = parse_date(fr_d)
    tdate = parse_date(to_d)
    n_bed = request.POST['bed']
    if n_bed == '1':
        z = tdate - fdate
        print(room.room_no)
        no_days = z.days
        tot = int(room.price) * int(no_days)
        uid = request.user
        booked = booking.objects.create(from_date=fr_d, amount=room.price, no_of_days=no_days, room_no=room.room_no,
                                        total_amount=tot, u_id=uid.id, to_date=to_d, no_bed=n_bed)
        booked.save()
        return redirect('booked_view')
    elif n_bed == '2':
        z = tdate - fdate
        print(room.room_no)
        no_days = z.days
        tot = int(room.price) * int(no_days)
        x = int(no_days)*100
        total = tot + x
        uid = request.user
        booked = booking.objects.create(from_date=fr_d, amount=room.price, no_of_days=no_days, room_no=room.room_no,
                                        total_amount=total, u_id=uid.id, to_date=to_d, no_bed=n_bed)
        booked.save()
        return redirect('booked_view')
    else:
        pass


def booked_view(request):
    if request.method == "POST":
        n = request.POST['cname']
        j = request.POST['cardno']
        k = request.POST['month']
        l = request.POST['year']
        m = request.POST['cvv']
        z = payments(name=n, card_no=j, year=l, cvv=m, month=k)
        z.save()
    uid = request.user
    bkd = booking.objects.filter(u_id=uid.id).latest('date_now')
    temp = booking.objects.filter(date_now=bkd.date_now)
    return render(request, 'comfirm.html', {'temp': temp})


def adm_logout_view(request):
    del request.session['user_id']
    return redirect("login")


def logout_request(request):
    logout(request)
    return redirect("login")


def password_reset(request):
    if request.method == 'POST':
        a = request.POST['email']
        if User.objects.filter(email=a).exists():
            email = EmailMessage('forgot password',
                                 'Reset your password here:http://127.0.0.1:8000/reset_password_page', to=[a])
            email.send()
            return redirect(login)
        else:
            messages.error(request, 'Invalid email!!')
    else:
        return redirect('login')


def payment(request):
    return render(request, 'payment.html')


def reset_password_page(request):
    if request.method == 'POST':
        y=request.POST['email']
        passw = request.POST['password1']
        repass = request.POST['password2']
        if passw == repass:
            temp = User.objects.get(email=y)
            temp.set_password(passw)
            temp.save()
            messages.success(request, 'password updated')
            return redirect('login')
        else:
            messages.error(request, 'password does not match')
            return redirect('reset_password_page')
    else:
        return render(request,'pass_rest.html')


def success(request):
    return render(request, 'success.html')

def summary(request):
    user = request.user
    history=booking.objects.filter(u_id=user.id)
    return render(request,'history.html',{'temp':history})


def viewbookadmin(request):
    b=booking.objects.all()
    users=User.objects.all()
    return render(request,'admin/admin_booked_view.html',{'book':b,'user':users})

def viewroom(request):
    t=rooms.objects.all()
    return render(request, 'admin/viewroom.html', {'room':t})
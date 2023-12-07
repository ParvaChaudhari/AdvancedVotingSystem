from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
# Create your views here.
import base64
import os
from django.shortcuts import redirect
import smtplib
import math, random,datetime
from voting.models import Voter,Time_Num,PoliticalParty,Vote,Result
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from cryptography.fernet import Fernet
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')


def send_otp(mail,otp):
    sender_mail = 'votingsystem42@gmail.com'
    sender_pass = 'qawcspdmpkaidvno'  
    reciever_mail = mail
    s = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 is a port number
    s.starttls()
    s.login(sender_mail,sender_pass)
    tmp = f'your otp for enhanced voting system is {otp}'
    s.sendmail(sender_mail,reciever_mail,tmp)
    print("OTP sent succesfully..")
    s.quit()

def check_obj(num):
    c = Voter.objects.filter(Aadhar_no=num)
    if len(c)>0:
        return Voter.objects.get(Aadhar_no=num)
    else:
        return None

@csrf_exempt
def verify(request):
    context = {}
    if request.method == 'POST':
        dt = datetime.datetime.now()
        dt = dt.strftime("%H:%M:%S")
        rotp = str(random.randint(1000, 9999))
        nobj = Time_Num(num=rotp,time=dt,an='')
        nobj.save()
        if 'btn1' in request.POST:
            num=request.POST.get('n1')
            request.session['val'] = num
            timeobj = Time_Num.objects.get(time=dt)
            timeobj.an = num
            timeobj.save(update_fields=['an'])
            try:
                obj = Voter.objects.get(Aadhar_no=num)
                if obj.vote_done==False:
                    mail = obj.email
                    context['mail']=mail
                    send_otp(mail,rotp)
                else:
                    context['result']='You Have already voted.'
                    return render(request, 'finish.html',context)
            except:
                context['result'] = 'User not found!!'
                return render(request, 'finish.html', context)
        elif 'btn2' in request.POST:
            t1 = Time_Num.objects.filter(time=dt)
            t1 = t1[0]
            otp = request.POST.get('otp')
            stamp = t1.id
            otp_obj = Time_Num.objects.filter(id=stamp-1)[0]
            #print(otp_obj)
            if otp_obj.num == int(otp):
                an = otp_obj.an
                obj = Voter.objects.get(Aadhar_no=an)
                context['vi'] = f'Voter ID : {obj.Voter_id}'
                context['an'] = f'Aadhar Number : {an}'
                context['nm'] = f'Name : {obj.Firstname} {obj.Lastname}'
                context['dob'] = f'Date of Birth : {obj.day}-{obj.month}-{obj.year}'
                context['pc'] = f'Pincode : {obj.pincode}'
                context['rg'] = f'Region : {obj.region}'
                context['em'] = f'Email : {obj.email}'
                context['vd'] = f'Vote Done : {obj.vote_done}'
                return render(request, 'details.html',context)
            context['check'] = 'Try Again !'
    return render(request, 'verify.html',context) 

def details(request):
    return render(request, 'details.html')

def decrypt(key,token):
    f = Fernet(key)
    res = f.decrypt(token)
    f = res.decode()
    return f


def calcres():
    v = Vote.objects.all()
    p = PoliticalParty.objects.all()
    vd = {}
    for i in p:
        dk = i.party_name+'-'+i.candidate_name
        vd[dk]=[]
    for i in v:
        k = i.Vid2[2:].encode()
        uid = i.Usrid[2:].encode()
        pn = i.Vid1[2:].encode()
        uid,pn = decrypt(k,uid),decrypt(k,pn)
        vd[pn].append(uid)
    for k in vd:
        ro = Result(pn=k,vc=len(vd[k]))
        ro.save()

def party(request):
    num = request.session.get('val')
    vtr = Voter.objects.get(Aadhar_no=num)
    if vtr.vote_done:
        return render(request,'index.html')
    obj = PoliticalParty.objects.all()
    context = {'lis':obj}
    if request.method == 'POST':
        v = request.POST.get('vote')
        pty = PoliticalParty.objects.get(party_id=v)
        pn = pty.party_name+'-'+pty.candidate_name
        key = Fernet.generate_key()
        f = Fernet(key)
        token1 = f.encrypt(num.encode())
        token2 = f.encrypt(pn.encode())
        vo = Vote(Usrid=token1,Vid1 = token2,Vid2 = key)
        vo.save()
        vtr.vote_done = True
        vtr.save()
        context['result'] = f'You have Voted Successfully Now you can close the site.'
        calcres()
        return render(request,'finish.html',context)
    return render(request, 'party.html',context)   

def info(request):
    return render(request, 'info.html') 

def finish(request):
    return render(request,'finish.html')


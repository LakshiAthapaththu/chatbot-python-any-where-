from django.contrib.auth import authenticate
from django.views.generic import View
from useract.models import Inquiry, ProfilePic
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from useract.forms import editProfile
import re
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from useract.functions import chat

class viewInqury(View):
    temp = 'view history/view_history.html'
    def get(self,request):
        user_name = request.session['users']
        user_id = User.objects.get(username=user_name).pk
        object = Inquiry.objects.filter(USERNAME=user_id)
        return render(request, self.temp, {'user':user_name.upper(), 'obj':object})

class editDetails(View):
    form_class = editProfile
    temp = 'editDetails/editDetails.html'
    msg1 = 'valid'

    # add the template
    def get(self, request):
        form = self.form_class(None)
        # if user requst to make his acc return blank page
        return render(request, self.temp, {'form': form,'user':request.session['users']})
        #add user session

    def post(self, request):
        msg1 = 'Successfully Updated'
        msg2 = 'Invalid Entry'
        form = self.form_class(request.POST)
        pass_word = ''
        if form.is_valid():
            user_name = request.session['users']
            obj_user = User.objects.filter(username=user_name)
            newUserName = request.POST.get('username')
            current_pw = form.cleaned_data['current_password']
            new_pw = form.cleaned_data['new_password'].strip()
            confirm_pw = form.cleaned_data['confirm_password'].strip()
            user = authenticate(username=user_name, password=current_pw)
            anotherUser = authenticate(user_name=newUserName)
            regUserName = re.compile("[a-z,A-Z,0-9]+([\s\-]?[a-z,A-Z,0-9])*")
            Fields = ['first_name','last_name','email','username']
            #update username finally
            UpdateFields =[]
            valid = True
            userOblj = obj_user[0]

            for field in Fields:
                if(form.cleaned_data[field] != ''):
                    UpdateFields.append(field)

            if(user is not None):
                if(anotherUser is None):


                            for updateField in UpdateFields:
                                if(regUserName.match(form.cleaned_data[updateField]) == False):
                                    valid = False
                                    break
                            if (confirm_pw != '' or new_pw != ''):
                                UpdateFields.append('password')
                            if (len(UpdateFields) != 0):
                                    if('password' in UpdateFields):
                                        if not(confirm_pw == new_pw):
                                            valid = False

                                    if(valid == True):
                                        if('first_name' in UpdateFields):
                                            obj_user.update(first_name=form.cleaned_data['first_name'])
                                        if ('last_name' in UpdateFields):
                                            obj_user.update(last_name=form.cleaned_data['last_name'])
                                        if ('password' in UpdateFields):
                                            first_pass = obj_user[0].password.split('$')
                                            hasher = first_pass[0]
                                            salt = first_pass[1]
                                            # grabbing salt from the first password of the database
                                            make_password(new_pw, salt, hasher)
                                            #make encrypted password
                                            obj_user.update(password = make_password(new_pw, salt, hasher))
                                        if('email' in UpdateFields):
                                            obj_user.update(email=form.cleaned_data['email'])
                                        if('username' in UpdateFields):
                                            #inqObj = Inquiry.objects.filter(USERNAME=str(user_name))
                                            #for inqObject in inqObj:
                                                #inqObject.update(USERNAME = form.cleaned_data['username'])
                                            obj_user.update(username=form.cleaned_data['username'])
                                            request.session['users'] = form.cleaned_data['username']
                                            user_name = request.session['users']
                                        return render(request, self.temp, {'form': form, 'msg': msg1})
                                    else:
                                        return render(request, self.temp, {'form': form, 'msg':msg2})
                            else:
                                    return render(request, self.temp, {'form': form, 'msg':msg2})
                else:
                    return render(request, self.temp, {'form': form, 'msg': "user name already exists"})
            else:
                return render(request, self.temp, {'form': form, 'msg': msg2})
        else:
            return render(request, self.temp, {'form': form})


#def getpage(request):
    #return render(request,"test/test.html")


def testing(request):
    data = request.GET.get('val', None)
    user = request.session['users']
    reply = chat.reply(data,user)
    return JsonResponse({'msg':reply})

def getProPic(request):
    username = request.session['users']
    profic = ProfilePic.objects.filter(username=User.objects.get(username=username))
    url=''
    for u in profic:
        url = u.picture.url
    if(url == ''):
        url = "../../media/pictures/propic1.png"
    return JsonResponse({'urlof':str(url),'username':username})

#only for some testing purposes
def getAllsets(request):
    temp = "index.html"
    data = Inquiry.objects.all()
    #inq = Inquiry(description="hi",add_state=False)
    #inq.save()
    return render(request,temp,{'data':data})
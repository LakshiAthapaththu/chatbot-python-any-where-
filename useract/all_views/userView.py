from django.http import HttpResponse
from django.template import loader
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from useract.forms import SignUpForm,ImageForm
from useract.models import ProfilePic,UserType,AuthofUser
from django.contrib.auth.models import User
from chatbot.models import Layers,Classes
from useract.functions import chat
class SignIn(View):
    temp = 'home/home.html'
    temp1 = 'registration/login.html'
    temp2 = 'adminHome/adminHome.html'
    temp3 = "reportsearch/report.html"
    msg = ""
    def post(self,request):
        chat.setTo(0)
        username = request.POST.get('username')
        password=request.POST.get('password')
        staff_state = "no"
        #user1=User.objects.filter(username=username,password=password)
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['users'] = username
            type_obj = UserType.objects.get(username=User.objects.get(username=username))
            type = type_obj.type
            if (type == "external"):
                auth = AuthofUser.objects.get(username=User.objects.get(username=username))
                request.session['auth'] = auth.auth.authority_id
                return render(request, self.temp3)

            elif(user.is_staff):
                all_layer_objects = Layers.objects.all()
                all_class_objects = Classes.objects.all()
                return render(request, self.temp2, {'user': request.session['users'].upper() , 'layers': all_layer_objects,
                                                       'classes': all_class_objects})

            else:
                return render(request, self.temp, {'user':request.session['users'].upper()})
        else:
            msg="invalid"
            return render(request, self.temp1, {'msg':msg})

    def get(self,request):
        msg = ""
        return render(request, self.temp1,{'msg':msg})

class SignUp(View):
        form_class = SignUpForm
        #form_class_2 = ImageForm
        temp = 'form/user_form.html'

        # add the template
        def get(self, request):
            form = self.form_class(None)
            # if user requst to make his acc return brank page
            #form2 = self.form_class_2(None)
            return render(request, self.temp, {'form': form})

        def post(self, request):
            form = self.form_class(request.POST)
            #form2 = self.form_class_2(request.POST)
            if (form.is_valid()):
                user = form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                # user.set_password(password)

                try:
                    pic = request.FILES['picture']
                except KeyError:
                    pic=""

                user.save()
                #picture = ProfilePic(username=User.objects.get(username=username),picture=pic)
                user_obj = User.objects.get(username=username)
                type = UserType(username=user_obj)
                type.save()
                if(pic is not None):
                    picture_obj = ProfilePic(username=user_obj,picture=pic)
                    picture_obj.save()

                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('login')

            return render(request, self.temp, {'form': form})



def logout_view(request):

    template = loader.get_template('registration/login.html')
    logout(request)
    return HttpResponse(template.render(request))
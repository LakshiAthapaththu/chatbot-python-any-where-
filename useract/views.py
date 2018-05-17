from django.views.generic import View
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from chatbot.models import  Classes,Layers
from .models import Inquiry
from useract.functions import chat
from useract.models import Report,Inquiry,Authority,User
from django.contrib.auth.decorators import login_required
#load home page

#@login_required(login_url="/useract/home/")
#class getHomePage(View):
    #template = 'home/home.html'
     #def get(self,request):
        #chat.setTo(0)
        #return render(request, self.template, {'user': request.session['users'].upper(), #})


def getHomePage(request):
    chat.setTo(0)
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render(request),{'user': request.session['users'].upper()})




class getAdminPage(View):
    template = 'adminHome/adminHome.html'
    def post(self,request):
        all_layer_objects = Layers.objects.all()
        all_class_objects = Classes.objects.all()
        return render(request, self.template, {'user': request.session['users'], 'layers': all_layer_objects,
                                                   'classes': all_class_objects})
    def get(self,request):
        all_layer_objects = Layers.objects.all()
        all_class_objects = Classes.objects.all()
        return render(request, self.template,{'user':request.session['users'],'layers':all_layer_objects,
                                              'classes':all_class_objects})


def userGuide(request):
    #addInqdatefortrain()
    #adddatabus()
    #addtotrain()

    #abc()

    #addToBusDate()
    template = loader.get_template('user_guidances/userguide.html')
    return HttpResponse(template.render(request))

def viewReport(request):
    template = loader.get_template('viewReport/daily_report.html')
    return HttpResponse(template.render(request))

def getChatWindow(request):

    template = loader.get_template('chatWindow/chatWindow.html')
    return HttpResponse(template.render(request))



def adddatabus():
    #for busses
    r0 = Report(report_id='115052018',authority_id=Authority.objects.get(authority_id=1))
    r0.save()
    r1 = Report(report_id='112052018',authority_id=Authority.objects.get(authority_id=1))
    r1.save()
    r2 = Report(report_id='112042018',authority_id=Authority.objects.get(authority_id=1))
    r2.save()
    r3=Report(report_id='112032018', authority_id=Authority.objects.get(authority_id=1))
    r3.save()
    r4 = Report(report_id='112022018',authority_id=Authority.objects.get(authority_id=1))
    r4.save()
    r5=Report(report_id='112012018',authority_id=Authority.objects.get(authority_id=1))
    r5.save()
    r6 = Report(report_id='112122017', authority_id=Authority.objects.get(authority_id=1))
    r6.save()
    r7 = Report(report_id='112112017', authority_id=Authority.objects.get(authority_id=1))
    r7.save()
    r8 = Report(report_id='112102017', authority_id=Authority.objects.get(authority_id=1))
    r8.save()
    r9 = Report(report_id='112092017', authority_id=Authority.objects.get(authority_id=1))
    r9.save()
    r10 = Report(report_id='112082017', authority_id=Authority.objects.get(authority_id=1))
    r10.save()
    r11 = Report(report_id='112072017', authority_id=Authority.objects.get(authority_id=1))
    r11.save()
    r12 = Report(report_id='112062017', authority_id=Authority.objects.get(authority_id=1))
    r12.save()

    #new
    r13 = Report(report_id='114052018',authority_id=Authority.objects.get(authority_id=1))
    r13.save()
    r14 = Report(report_id='113052018', authority_id=Authority.objects.get(authority_id=1))
    r14.save()





    i1 = Inquiry(reported_date='12/04/2018',reported_time='13:00',USERNAME=User.objects.get(username='Lakshi'),
                 description="conductor does not give change money",report_id=r2,add_state=False)
    i1.save()
    i2 = Inquiry(reported_date='12/03/2018', reported_time='12:34', USERNAME=User.objects.get(username='Lakshi'),
                 description="conductor is misbahaving", report_id=r3,add_state=False)
    i2.save()
    i3 = Inquiry(reported_date='12/02/2018', reported_time='5:33', USERNAME=User.objects.get(username='Lakshi'),
                 description="conductor brhavior is unacceptable", report_id=r4,add_state=False)
    i3.save()
    i4  = Inquiry(reported_date='12/01/2018',reported_time='14:23',USERNAME=User.objects.get(username='Lakshi'),
                 description="The route is needed another bus",report_id=r5,add_state=False)
    i4.save()
    i5 = Inquiry(reported_date='12/12/2017', reported_time='14:12', USERNAME=User.objects.get(username='Lakshi'),
                 description="very old bus not suitable for usage", report_id=r5, add_state=False)
    i5.save()
    i6 = Inquiry(reported_date='12/11/2017', reported_time='19:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="driver is drunken", report_id=r6, add_state=False)
    i6.save()
    i7 = Inquiry(reported_date='12/10/2017', reported_time='13:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavey crowd for the bus", report_id=r7, add_state=False)
    i7.save()
    i8 = Inquiry(reported_date='12/09/2017', reported_time='10:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="bus goes very slowly", report_id=r8, add_state=False)
    i8.save()
    i9 = Inquiry(reported_date='12/08/2018', reported_time='15:34', USERNAME=User.objects.get(username='Lakshi'),
                 description="driver misbehaviors", report_id=r9, add_state=False)
    i9.save()
    i10 = Inquiry(reported_date='12/07/2018', reported_time='10:44', USERNAME=User.objects.get(username='Lakshi'),
                 description="driver drives fast", report_id=r10, add_state=False)
    i10.save()
    i11 = Inquiry(reported_date='12/06/2018', reported_time='9:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="bus does not come at time", report_id=r11, add_state=False)
    i11.save()
    i12 = Inquiry(reported_date='12/05/2018', reported_time='17:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="pocket pickings are happening in the bus", report_id=r12, add_state=False)
    i12.save()

    i8.save()
    i9 = Inquiry(reported_date='12/08/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="busgoing fast", report_id=r9, add_state=False)
    i9.save()
    i10 = Inquiry(reported_date='12/07/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                  description="busgoing fast", report_id=r10, add_state=False)
    i7 = Inquiry(reported_date='12/10/2017', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="busgoing fast", report_id=r7, add_state=False)
    i7.save()
    i8 = Inquiry(reported_date='12/09/2017', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="busgoing fast", report_id=r8, add_state=False)

    i8.save()

    i9 = Inquiry(reported_date='12/08/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="busgoing fast", report_id=r9, add_state=False)
    i12 = Inquiry(reported_date='12/05/2018', reported_time='17:45', USERNAME=User.objects.get(username='Lakshi'),
                  description="pocket pickings are happening in the bus", report_id=r12, add_state=False)
    i12.save()


    i9 = Inquiry(reported_date='12/08/2018', reported_time='17:33', USERNAME=User.objects.get(username='Lakshi'),
                 description="bus has unacceptable speed", report_id=r9, add_state=False)
    i9.save()
    i10 = Inquiry(reported_date='12/07/2018', reported_time='11:55', USERNAME=User.objects.get(username='Lakshi'),
                  description="there are too mush crowd for the bus", report_id=r10, add_state=False)
    i7 = Inquiry(reported_date='12/10/2017', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="busgoing fast", report_id=r7, add_state=False)
    i7.save()
    i8 = Inquiry(reported_date='12/09/2017', reported_time='20:13', USERNAME=User.objects.get(username='Lakshi'),
                 description="annoying money collecters are in the bus", report_id=r8, add_state=False)
    i8.save()
    i9 = Inquiry(reported_date='12/08/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="busgoing fast", report_id=r9, add_state=False)



def addtotrain():
    r1 = Report(report_id='212052018', authority_id=Authority.objects.get(authority_id=2))
    r1.save()
    r2 = Report(report_id='212042018', authority_id=Authority.objects.get(authority_id=2))
    r2.save()
    r3 = Report(report_id='212032018', authority_id=Authority.objects.get(authority_id=2))
    r3.save()
    r4 = Report(report_id='212022018', authority_id=Authority.objects.get(authority_id=2))
    r4.save()
    r5 = Report(report_id='212012018', authority_id=Authority.objects.get(authority_id=2))
    r5.save()
    r6 = Report(report_id='212122017', authority_id=Authority.objects.get(authority_id=2))
    r6.save()
    r7 = Report(report_id='212112017', authority_id=Authority.objects.get(authority_id=2))
    r7.save()
    r8 = Report(report_id='212102017', authority_id=Authority.objects.get(authority_id=2))
    r8.save()
    r9 = Report(report_id='212092017', authority_id=Authority.objects.get(authority_id=2))
    r9.save()
    r10 = Report(report_id='212082017', authority_id=Authority.objects.get(authority_id=2))
    r10.save()
    r11 = Report(report_id='212072017', authority_id=Authority.objects.get(authority_id=2))
    r11.save()
    r12 = Report(report_id='212062017', authority_id=Authority.objects.get(authority_id=2))
    r12.save()

    i1 = Inquiry(reported_date='12/04/2018', reported_time='3:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="train is too slow", report_id=r2, add_state=False)
    i1.save()
    i2 = Inquiry(reported_date='12/03/2018', reported_time='12:56', USERNAME=User.objects.get(username='Lakshi'),
                 description="over crowded train", report_id=r3, add_state=False)
    i2.save()
    i3 = Inquiry(reported_date='12/02/2018', reported_time='6:00', USERNAME=User.objects.get(username='Lakshi'),
                 description="train is always late", report_id=r4, add_state=False)
    i3.save()
    i4 = Inquiry(reported_date='12/01/2018', reported_time='9:50', USERNAME=User.objects.get(username='Lakshi'),
                 description="train geting late", report_id=r5, add_state=False)
    i4.save()
    i5 = Inquiry(reported_date='12/12/2017', reported_time='10:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="rail roads are not in good condition", report_id=r5, add_state=False)
    i5.save()
    i6 = Inquiry(reported_date='12/11/2017', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="signal lights are not working properly", report_id=r6, add_state=False)
    i6.save()
    i7 = Inquiry(reported_date='12/10/2017', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="train is late", report_id=r7, add_state=False)
    i7.save()
    i8 = Inquiry(reported_date='12/09/2017', reported_time='9:56', USERNAME=User.objects.get(username='Lakshi'),
                 description="very old train and not good for passenger health", report_id=r8, add_state=False)
    i8.save()
    i9 = Inquiry(reported_date='12/08/2018', reported_time='10:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="train is getting late", report_id=r9, add_state=False)
    i9.save()
    i10 = Inquiry(reported_date='12/07/2018', reported_time='12:35', USERNAME=User.objects.get(username='Lakshi'),
                  description="train does not come on time", report_id=r10, add_state=False)
    i10.save()
    i11 = Inquiry(reported_date='12/06/2018', reported_time='10:15', USERNAME=User.objects.get(username='Lakshi'),
                  description="pocket pickings are happening in the train", report_id=r11, add_state=False)
    i11.save()
    i12 = Inquiry(reported_date='12/05/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                  description="train is late", report_id=r12, add_state=False)
    i12.save()

    i8.save()
    i9 = Inquiry(reported_date='12/08/2018', reported_time='11:22', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavey crowd for train at the office times", report_id=r9, add_state=False)
    i9.save()
    i10 = Inquiry(reported_date='12/07/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                  description="rail gates are not working properly", report_id=r10, add_state=False)
    i10.save()
    i7 = Inquiry(reported_date='12/10/2017', reported_time='13:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="annoying money collecters are within the train", report_id=r7, add_state=False)
    i7.save()
    i8 = Inquiry(reported_date='12/09/2017', reported_time='12:30', USERNAME=User.objects.get(username='Lakshi'),
                 description="no enough space in the train", report_id=r8, add_state=False)
    i8.save()
    i9 = Inquiry(reported_date='12/08/2018', reported_time='16:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavyly loaded train", report_id=r9, add_state=False)

    i9.save()
    i5.save()
    i2.save()


def abc():
    r4 = Report(report_id='213052018', authority_id=Authority.objects.get(authority_id=2))
    r4.save()
    i1 = Inquiry(reported_date='13/05/2018', reported_time='13:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="train does not come on time", report_id=r4, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='13/05/2018', reported_time='13:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="train does not come on time", report_id=r4, add_state=False)
    i1.save()

    r5 = Report(report_id='212052018', authority_id=Authority.objects.get(authority_id=2))
    r5.save()

    i1 = Inquiry(reported_date='12/05/2018', reported_time='12:23', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavyly loaded train", report_id=r5, add_state=False)

    i1.save()
    r5 = Report(report_id='211052018', authority_id=Authority.objects.get(authority_id=2))
    r5.save()

    i1 = Inquiry(reported_date='11/05/2018', reported_time='12:23', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavyly loaded train", report_id=r5, add_state=False)

    i1.save()


def addInqdatefortrain():
    r1 = Report(report_id='212052018', authority_id=Authority.objects.get(authority_id=2))
    r1.save()
    i1 = Inquiry(reported_date='12/05/2018', reported_time='3:10', USERNAME=User.objects.get(username='Lakshi'),
                 description="train go fast", report_id=r1, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='12/05/2018', reported_time='4:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="signal lights are not working properly", report_id=r1, add_state=False)

    i1.save()
    #
    r2 = Report(report_id='211052018', authority_id=Authority.objects.get(authority_id=2))
    r2.save()
    i1 = Inquiry(reported_date='11/05/2018', reported_time='10:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavy crowd in the train", report_id=r2, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='11/05/2018', reported_time='7:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="old train", report_id=r2, add_state=False)

    i1.save()
    i1 = Inquiry(reported_date='11/05/2018', reported_time='8:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="uncomfirtable train", report_id=r2, add_state=False)

    i1.save()
    #
    r3 = Report(report_id='214052018', authority_id=Authority.objects.get(authority_id=2))
    r3.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='13:25', USERNAME=User.objects.get(username='Lakshi'),
                 description="broken train", report_id=r3, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='18:56', USERNAME=User.objects.get(username='Lakshi'),
                 description="routes are not in good condition", report_id=r3, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="over loaded train", report_id=r3, add_state=False)

    i1.save()
    #
    r4 = Report(report_id='215052018', authority_id=Authority.objects.get(authority_id=2))
    r4.save()
    i1 = Inquiry(reported_date='15/05/2018', reported_time='13:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="huge crowd in train", report_id=r4, add_state=False)
    r5 = Report(report_id='208052018', authority_id=Authority.objects.get(authority_id=2))
    r5.save()
    i1.save()
    i1 = Inquiry(reported_date='15/05/2018', reported_time='12:23', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavyly loaded train", report_id=r4, add_state=False)

    i1.save()
    #

def addToBusDate():
    r1 = Report(report_id='112052018', authority_id=Authority.objects.get(authority_id=1))
    r1.save()
    i1 = Inquiry(reported_date='12/05/2018', reported_time='3:10', USERNAME=User.objects.get(username='Lakshi'),
                 description="bus go fast", report_id=r1, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='12/05/2018', reported_time='4:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="routes are broken", report_id=r1, add_state=False)

    i1.save()
    #
    r2 = Report(report_id='111052018', authority_id=Authority.objects.get(authority_id=1))
    r2.save()
    i1 = Inquiry(reported_date='11/05/2018', reported_time='10:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavy crowd in the bus", report_id=r2, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='11/05/2018', reported_time='7:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="old bus", report_id=r2, add_state=False)

    i1.save()
    i1 = Inquiry(reported_date='11/05/2018', reported_time='8:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="uncomfirtable bus", report_id=r2, add_state=False)

    i1.save()
    #
    r3 = Report(report_id='114052018', authority_id=Authority.objects.get(authority_id=1))
    r3.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='13:25', USERNAME=User.objects.get(username='Lakshi'),
                 description="broken bus", report_id=r3, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='18:56', USERNAME=User.objects.get(username='Lakshi'),
                 description="routes are not in good condition", report_id=r3, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="over loaded bus", report_id=r3, add_state=False)

    i1.save()
    #
    r4 = Report(report_id='115052018', authority_id=Authority.objects.get(authority_id=1))
    r4.save()
    i1 = Inquiry(reported_date='15/05/2018', reported_time='13:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="huge crowd in bus", report_id=r4, add_state=False)
    r5 = Report(report_id='114052018', authority_id=Authority.objects.get(authority_id=1))
    r5.save()
    i1.save()
    i1 = Inquiry(reported_date='15/05/2018', reported_time='12:23', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavyly loaded bus", report_id=r4, add_state=False)

    i1.save()
    #
    r1 = Report(report_id='111052018', authority_id=Authority.objects.get(authority_id=1))
    r1.save()
    i1 = Inquiry(reported_date='11/05/2018', reported_time='3:10', USERNAME=User.objects.get(username='Lakshi'),
                 description="bus go fast", report_id=r1, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='11/05/2018', reported_time='4:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="routes are broken", report_id=r1, add_state=False)

    i1.save()
    #
    r2 = Report(report_id='110052018', authority_id=Authority.objects.get(authority_id=1))
    r2.save()
    i1 = Inquiry(reported_date='10/05/2018', reported_time='10:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavy crowd in the bus", report_id=r2, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='10/05/2018', reported_time='7:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="old bus", report_id=r2, add_state=False)

    i1.save()
    i1 = Inquiry(reported_date='10/05/2018', reported_time='8:45', USERNAME=User.objects.get(username='Lakshi'),
                 description="uncomfirtable bus", report_id=r2, add_state=False)

    i1.save()
    #
    r3 = Report(report_id='114052018', authority_id=Authority.objects.get(authority_id=1))
    r3.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='13:25', USERNAME=User.objects.get(username='Lakshi'),
                 description="broken bus", report_id=r3, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='18:56', USERNAME=User.objects.get(username='Lakshi'),
                 description="routes are not in good condition", report_id=r3, add_state=False)
    i1.save()
    i1 = Inquiry(reported_date='14/05/2018', reported_time='3:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="over loaded bus", report_id=r3, add_state=False)

    i1.save()
    #
    r4 = Report(report_id='115052018', authority_id=Authority.objects.get(authority_id=1))
    r4.save()
    i1 = Inquiry(reported_date='15/05/2018', reported_time='13:55', USERNAME=User.objects.get(username='Lakshi'),
                 description="huge crowd in bus", report_id=r4, add_state=False)
    r5 = Report(report_id='114052018', authority_id=Authority.objects.get(authority_id=1))
    r5.save()
    i1.save()
    i1 = Inquiry(reported_date='15/05/2018', reported_time='12:23', USERNAME=User.objects.get(username='Lakshi'),
                 description="heavyly loaded bus", report_id=r4, add_state=False)

    i1.save()
    #




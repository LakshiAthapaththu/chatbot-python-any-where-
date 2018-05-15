import datetime
from django.shortcuts import render
from django.views.generic import View
from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.http import HttpResponse, HttpResponseRedirect
from useract.models import  Inquiry,Report,Authority
from chatbot.models import Layers,Classes,sets,train
import re
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from  chatbot.functions import trainData
from chatbot.functions.storeSynapes import read,write,incrementCount,readNumOfUnTrains,writeNumOfTrains
from useract.functions import validate_inputs

class PdfPrint():
    def __init__(self, buffer, pageSize):
        self.buffer = buffer
        # default format is A4
        if pageSize == 'A4':
            self.pageSize = A4
        elif pageSize == 'Letter':
            self.pageSize = letter
        self.width, self.height = self.pageSize

    def report(self,title,inquiry_content):
        now = datetime.datetime.now()
        # set some characteristics for pdf document
        doc = SimpleDocTemplate(
            self.buffer,
            rightMargin=72,
            leftMargin=72,
            topMargin=30,
            bottomMargin=72,
            pagesize=self.pageSize)
        styles = getSampleStyleSheet()
        data = []
        data.append(Paragraph(title, styles['Title']))
        count = 1
        for objec in inquiry_content:
            inq = str(objec.description).replace(",", "<br/>")
            data.append(Paragraph('INQUIRY'+" "+str(count),styles["BodyText"]))
            data.append(Paragraph('REPORTED DATE :'+objec.reported_date+"<br/>"
                                  +'REPORTED TIME :' + objec.reported_time+"<br/>"+
                                  'INQUIRY :  ' + inq+'<br/>', styles['BodyText']))
            #data.append(Paragraph('REPORTED TIME :' + objec.reported_time, styles['BodyText']))

            #data.append(Paragraph('INQUIRY :  '+inq,styles['BodyText']))
            data.append(Paragraph('', styles['Bullet']))
            count +=1

        data.append(Paragraph('<br/>'+'<br/>'+'................................'
                              +'<br/>'+'Director,<br/>InquaMaK.com.<br/>'+str(now.date()),styles["BodyText"]))
        #data.append(table)
        doc.build(data)
        #doc.build(table)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf


class getReport(View):
    temp = 'viewReport/daily_report.html'
    temp1 = 'adminHome/adminHome.html'

    def post(self,request):

            all_layer_objects = Layers.objects.all()
            all_class_objects = Classes.objects.all()

            msg2 = "invalid entry"
            if(request.POST.get('date') is None or request.POST.get('authority') is None):
                return render(request, self.temp1, {'user': request.session['users'], 'layers': all_layer_objects,
                                                           'classes': all_class_objects,'msg':msg2})
            else:
                #reg = re.compile("[\d]{1,2}/[\d]{1,2}/[\d]{2}")
                date = request.POST.get('date')
                authority = request.POST.get('authority')
                new_date = ""
                dateValidity = validate_inputs.validDate(str(date))
                if(dateValidity[0] == True):
                    for letter in date:
                        if(letter != "/"):
                            new_date = new_date + letter
                    report_id = str(authority)+str(new_date)
                    authorityName = Authority.objects.filter(authority_id=int(authority))
                    authNameStr = ''
                    for auth in authorityName:
                        authNameStr = auth.authority_name
                    obj = Inquiry.objects.filter(report_id=report_id)
                    if (request.POST.get('btn') == 'view'):
                        return render(request, self.temp, {'date':date,'authority':authorityName,'object':obj})
                    elif (request.POST.get('btn') == 'pdf'):
                        response = HttpResponse(content_type='application/pdf')
                        filename = 'report_of_'+authNameStr+"_"+date
                        response['Content-Disposition'] = 'attachement; filename={0}.pdf'.format(filename)
                        buffer = BytesIO()
                        report = PdfPrint(buffer, 'A4')
                        pdf = report.report("Report of"+" "+authNameStr+" "+"for"+" "+date,obj)
                        response.write(pdf)
                        return response

                else:
                    return render(request, self.temp1, {'user': request.session['users'], 'layers': all_layer_objects,
                                                               'classes': all_class_objects,'msg':msg2})


class addTrainingSets(View):
    temp1 = "adminHome/adminHome.html"
    #temp = "tem.html"
    def post(self,request):
        layer = request.POST.get('layer')
        clas = request.POST.get('class')
        parent = request.POST.get('parent')
        sentence = request.POST.get('sentence')
        all_layer_objects = Layers.objects.all()
        all_class_objects = Classes.objects.all()
        msg1 = "invalid entry"
        if(layer is None or clas is None or parent is None or sentence == '' ):
            return render(request, self.temp1,
                          {'msg1': msg1, 'user': request.session['users'], 'layers': all_layer_objects,
                           'classes': all_class_objects})
        else:
            obj = sets.objects.filter(class_id_of=int(clas),layer_id_of=int(layer),parent_id=int(parent))
            set_id=None

            set_object=''
            for obje in obj:
                set_id = obje.set_id
                set_object = obje
            if set_id is not None:
                newObj = train(sentence=sentence, set_id=set_object,train_state=False)
                newObj.save()
                #writeNumOfTrains(str(layer),str(parent))
                #increment number of trains
                incrementCount(str(layer),str(parent))
                numOfunTrains = readNumOfUnTrains(str(layer),str(parent))
                #change this number as you wish
                if(int(numOfunTrains)>=1000):
                    writeNumOfTrains(layer,parent)
                    finalSet = (trainData.makeBags(set_object))
                    set = finalSet[0]
                    write(set[0],set[1], str(layer), str(parent),finalSet[1])
                    #write(set[0],set[1],layer,parent)
                    result = read(layer,parent)
                    #result =  clasify("bus does not come at time",1,0,set[0],set[1],list(["bus","train"]))
                    return render(request,self.temp1,{'layer':layer, 'clas':clas ,'parent':parent,
                                                     'sentence':sentence,'obj':obj,'msg':"yes",
                                                     'words':finalSet[1],'allsent':finalSet[2],'classe':finalSet[3],

                                                     'untrains':numOfunTrains,
                                                     'user': request.session['users'], 'layers': all_layer_objects,
                                                     'classes': all_class_objects}
                    )


                else:
                    return render(request, self.temp1,
                                  { 'user': request.session['users'], 'layers': all_layer_objects,
                                   'classes': all_class_objects})

            else:


                return render(request,self.temp1,{'msg1':msg1,'user': request.session['users'], 'layers': all_layer_objects,
                    'classes': all_class_objects})







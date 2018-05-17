from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from useract.functions import validate_inputs
from useract.models import Authority, Inquiry


class getReport(View):
    template = 'reportofauth/reportofauth.html'
    template1='reportsearch/report.html'
    def post(self,request):
        date = request.POST.get('date')
        validity = validate_inputs.validDate(date)
        new_date =''
        if(validity[0]):
            for letter in date:
                if (letter != "/"):
                    new_date = new_date + letter
            #just put a number change later
            authr = request.session['auth']
            report_id = str(authr) + str(new_date)
            authorityName = Authority.objects.filter(authority_id=int(authr))
            authNameStr = ''
            da = generateReportData(date,int(authr))
            array = da[0]
            for auth in authorityName:
                authNameStr = auth.authority_name
            obj = Inquiry.objects.filter(report_id=report_id)
            array1 = da[2]
            array2 = generateReportData2(date,int(authr))
            return render(request, self.template,{'r':report_id,'obj':obj,'var1':array[0],'var2':array[1],
                                                  'var3':array[2],'var4':array[3],'var5':array[4],
                                                  'var6':array[5],'var7':array[6],'var8':array[7],'var9':array[8],
                                                  'var10':array[9],'var11':array[10],'var12':array[11],
                                                  'm1': array1[0], 'm2': array1[1],
                                                  'm3': array1[2], 'm4': array1[3], 'm5': array1[4],
                                                  'm6': array1[5], 'm7': array1[6], 'm8': array1[7],
                                                  'm9': array1[8],
                                                  'm10': array1[9], 'm11': array1[10], 'm12': array1[11],
                                                  'array':array2[0],'cnt':array2[1],'d1':array2[1][0],'d2':array2[1][1],
                                                  'd3': array2[1][2],'d4':array2[1][3],'d5':array2[1][4],
                                                  'd6': array2[1][5],'d7':array2[1][6],
                                                  })

        else:
            return render(request, self.template1, {'user': request.session['users'],'msg':"INVALID"})

    def get(self,request):
        return render(request, self.template1,{'user':request.session['users'],'msg':""})


class getSearchHome(View):
    template = "reportsearch/report.html"

    def post(self, request):
        return render(request, self.template, )

    def get(self, request):
        return render(request, self.template, {'user': request.session['users']})


def generateReportData(date,auth):
    dic= {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun','7':'Jul',
          '8':'Aug','9':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    template = "test/test.html"
    nameofmonths = []
    num_of_inquiry = []
    authority = auth
    months = []
    day = date[0:2]
    month = int(date[3:5])
    year = int(date[6:])
    for i in range(0,12):
       if(month != 0):
           id=''
           if(len(str(month))==1):
                id = "0"+str(month)
           else:
               id = str(month)
           months.append(id+str(year))
           nameofmonths.append(dic[str(month)])
           month = month-1

       else:
           month = 12
           id = ''
           if (len(str(month)) == 1):
               id = "0" + str(month)
           else:
               id = str(month)
           months.append(id+str(year-1))
           nameofmonths.append(dic[str(month)])
           month = month-1
           year = year-1



    all_inq = Inquiry.objects.all()
    for j in months:
        count= 0
        for inq in all_inq:
            if(str(inq.report_id.report_id)[3:] == j and str(inq.report_id.report_id)[0]==str(authority)):
                count+=1

        num_of_inquiry.append(count)

    return num_of_inquiry,months,nameofmonths

def generateReportData2(date,auth):
    dic = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun', '7': 'Jul',
           '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

    dic2 = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':31,'7':31,'8':30,'9':31,'10':31,'11':30,'12':31}
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:])
    rep_id =[]
    for i in range(0,7):
        id =''
        if(int(day) !=0):
           if(len(str(day)) == 1):
               id = "0"+str(day)
           else:
               id = str(day)

           if(len(str(month))==1):
               id = id+"0"+str(month)
           else:
               id = id+str(month)
           id = str(auth)+id+str(year)
           day =day-1
           rep_id.append(id)

        if(day == 0):
            if(month!=1):
                month = month-1
                day = dic2[str(month)]

                if (len(str(day)) == 1):
                        id = "0" + str(day)
                else:
                    id = str(day)

                if (len(str(month)) == 1):

                    id = id + "0" + str(month)
                else:
                    id = id + str(month)
                id = str(auth) + id + str(year)
                rep_id.append(id)
                day = day - 1

            elif(month == 1):
                month =12
                day =31
                year =year-1
                if (len(str(day)) == 1):
                    id = "0" + str(day)
                else:
                    id = str(day)

                if (len(str(month)) == 1):
                    id = id + "0" + str(month)
                else:
                    id = id + str(month)
                id = str(auth) + id + str(year)
                rep_id.append(id)
                day = day - 1
    all_inq = Inquiry.objects.all()
    num_of_inq2 = []
    for j in rep_id:
        count = 0
        for inq in all_inq:
            if (str(inq.report_id.report_id) == (j)):
                count += 1

        num_of_inq2.append(count)


    return rep_id,num_of_inq2




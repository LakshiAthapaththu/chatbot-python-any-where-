from django.shortcuts import render
from django.conf.urls import url
from django.views.generic import View
from chatbot.functions.storeSynapes import read, write
from chatbot.functions.chat import clasify
from chatbot.models import sets
from chatbot.functions import trainData
from chatbot.models import train
#for testing purposes
#class getbag(View):
    #def get(self,request):
        #words = storeSynapes.readwords()
        #result = give_word_bag("conductor behavior is not acceptable",words)
        #temp = "tem.html"
        #return render(request,temp)

#class chat(View):
    #temp1 = "chat_window.html"
    #temp2= "result.html"
    #def get(self,request):
        #return render(request, self.temp1)
    #def post(self,request):
        #sentence = request.POST.get('text')
        #synap = read(1,0)
        #result = clasify(sentence,1,0,synap[0],synap[1],list(["bus","train"]))

        #return render(request, self.temp2, {'result': result,'words':synap[2]})

#class trainManually(View):
    #temp = "train.html"

    #def get(self,request):
        #allo = train.objects.all()
        #return render(request,self.temp,{'all':allo})

    #def post(self,request):
        #allo = train.objects.all()
        #obj = sets.objects.get(class_id_of=int(1), layer_id_of=int(1), parent_id=int(0))
        #finalSet = (trainData.makeBags(obj))
        #set = finalSet[0]
        #write(set[0], set[1], str(1), str(0), finalSet[1])
        #obj = sets.objects.get(class_id_of=int(3), layer_id_of=int(2), parent_id=int(1))
        #return render(request, self.temp,{'all':allo})




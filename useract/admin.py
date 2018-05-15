from django.contrib import admin
from .models import Inquiry,Authority,Report,BusDetails,TrainDetails,ProfilePic,UserType,AuthofUser

# Register your models here.
admin.site.register(Inquiry)
admin.site.register(Authority)
admin.site.register(Report)
admin.site.register(BusDetails)
admin.site.register(TrainDetails)
admin.site.register(ProfilePic)
admin.site.register(UserType)
admin.site.register(AuthofUser)


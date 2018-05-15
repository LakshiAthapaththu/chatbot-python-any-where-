import datetime
from useract.models import Report,User,Inquiry,Authority

def saveInq(user,inquiry,authority):
    cnt = 0
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    date = str(now.day)
    if(len(month) != 2):
        month = "0"+month

    if(len(date) !=2):
        date = "0"+date

    rep_id = date+month+year
    if(authority == 1):
        rep_id = str(1)+rep_id

    if(authority == 2):
        rep_id = str(2) + rep_id

    authority = Authority.objects.filter(authority_id=int(authority))
    auth = ''

    for a in authority:
        auth = a

    #get relevant report object
    report = Report.objects.filter(report_id = int(rep_id))
    report_obj_for_save = ''

    for rep in report:
        cnt = 1

    if (cnt == 0):
        report_obj = Report(report_id=int(rep_id), authority_id=auth)
        report_obj.save()

    report = Report.objects.filter(report_id=int(rep_id))

    for rep_object in report:
        report_obj_for_save = rep_object

    #get relavant user object
    user_obj = User.objects.filter(username=user)
    user_for_save = ''
    for u in user_obj:
        user_for_save = u
    inquiry = str(inquiry).replace("<br>", ","+" ")
    inq = Inquiry(description=str(inquiry), add_state=False, USERNAME=user_for_save,report_id=report_obj_for_save,
                  reported_date=now.date(),reported_time=(str(now.hour)+":"+str(now.minute)))

    inq.save()


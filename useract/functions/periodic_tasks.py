from celery.schedules import crontab
from celery.task import periodic_task
from useract.models import Report,Authority
import datetime

@periodic_task(run_every=crontab(hour=12, minute=54, day_of_week="mon"))
def every_monday_morning():
    addReport()
    Auth = Authority.objects.all()
    for a in Auth:
        report_obj = Report(report_id=int(5), authority_id=a)
        report_obj.save()


def addReport():
    Auth = Authority.objects.all()
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    date = str(now.day)
    if (len(month) != 2):
        month = "0" + month

    if (len(date) != 2):
        date = "0" + date

    rep_id = date + month + year


    for authority in Auth:
        autho_id = authority.authority_id
        report_id = str(autho_id)+rep_id
        report_obj = Report(report_id=int(report_id),authority_id=authority)


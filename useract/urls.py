from django.conf.urls import url
from . import views
from .all_views import userView,adminView,customerView,externalUserView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required
urlpatterns = [
#url(r'^$',views.getLoginPage,name='login_page'),
#urls accessible without log in

#user views
url(r'^login/$', userView.SignIn.as_view(), name='login'),
url(r'^register/$',userView.SignUp.as_view(),name='register'),
url(r'^logout/$', userView.logout_view, name='logout'),

#views
url(r'^home/$',views.getHomePage,name = 'home'),
url(r'^admin/$',views.getAdminPage.as_view(),name = 'adminpage'),
url(r'^userguide/$',views.userGuide,name='userguide'),


#admin views
url(r'^viewreport/$',adminView.getReport.as_view(),name= 'viewreport'),
url(r'^addData/$',adminView.addTrainingSets.as_view(),name= 'addData'),


#customer view
url(r'^viewhistory/$',customerView.viewInqury.as_view(),name='viewhistory'),
url(r'^edit/$',customerView.editDetails.as_view(),name='editDetails'),
url(r'^test/$',customerView.testing,name='test'),
url(r'^getProPic/$',customerView.getProPic,name='getProPic'),

#external user vies
url(r'^authreport/$',externalUserView.getReport.as_view(),name='authreport'),
url(r'^exhome/$',externalUserView.getSearchHome.as_view(),name='exhome'),
#testing purposes

#url(r'^chatWindow/$',views.getChatWindow,name='chatWindow'),
#get the chatwindow remove later
#url(r'^get/$',customerView.getpage,name='get'),
#for some testing purpposes
url(r'^getsets/$',customerView.getAllsets,name='getsets')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


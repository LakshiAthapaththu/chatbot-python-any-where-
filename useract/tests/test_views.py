from django.core.urlresolvers import reverse
from django.test import TestCase
from useract.models import User

class TestUrls(TestCase):
    def test_view_history(self):

        User.objects.create(username='Lakshi',password='123abc345')
        self.client.login(username='Lakshi', password='123abc345')

        session = self.client.session
        session['users'] = 'Lakshi'
        session.save()

        resp = self.client.get('/useract/viewhistory/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'view history/view_history.html')

        #resp = self.client.get('/useract/addData/')
        #self.assertEqual(resp.status_code, 200)

    def test_view_url_exists_at_desired_location(self):

         #urls with sessions cannot be checked in this method
        resp = self.client.get('/useract/login/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/useract/home/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/useract/logout/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/useract/register/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/useract/edit/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'registration/login.html')

        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home/home.html')

        resp = self.client.get(reverse('logout'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'registration/login.html')

        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'form/user_form.html')

        resp = self.client.get(reverse('editDetails'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'editDetails/editDetails.html')



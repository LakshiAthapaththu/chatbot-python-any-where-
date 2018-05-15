from useract.forms import SignUpForm,editProfile
from django.test import TestCase

class TestSignUpForm(TestCase):

    def test_user_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['username'].label == 'Username')


    def test_user_first_name_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['first_name'].label == 'First name')

    def test_last_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['last_name'].label == 'Last name')

    def test_email_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['email'].label == 'Email address')

    def test_password_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['password1'].label == 'Password')

    def test_pw_confirmation_field_label(self):
        form = SignUpForm()
        self.assertTrue(
           form.fields['password2'].label == 'Password confirmation')

class testEditProfile(TestCase):
    def test_user_name_field_label(self):
        form = editProfile()
        self.assertTrue(
            form.fields['username'].label == 'Username' or form.fields['username'].label == None)


    def test_user_first_name_label(self):
        form = editProfile()
        self.assertTrue(
            form.fields['first_name'].label == 'First name')

    def test_last_name_field_label(self):
        form = editProfile()
        self.assertTrue(
            form.fields['last_name'].label == 'Last name')

    def test_email_field_label(self):
        form = editProfile()
        self.assertTrue(
            form.fields['email'].label == 'Email address')


    def test_new_pw_label(self):
        form = editProfile()
        self.assertTrue(
            form.fields['new_password'].label == 'New password' or form.fields['new_password'].label == None)

    def test_confirm_pw_label(self):
        form = editProfile()
        self.assertTrue(
            form.fields['confirm_password'].label == 'Confirm password' or form.fields['confirm_password'].label == None)

    def test_current_pw_label(self):
        form = editProfile()
        self.assertTrue(
            form.fields['current_password'].label == 'Current password' or
            form.fields['current_password'].label == None)

    #test for form inputs

    def test_new_pw(self):
        #give only password
        pw = "123"
        form_data = {'new_password': pw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        pw = "abc"
        form_data = {'new_password': pw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        pw = "abc123"
        form_data = {'new_password': pw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        #current password is required field form is invalid without current password
        pw = "abc123def"
        form_data = {'new_password': pw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        #give correct password and username
        pw = "abc123456"
        username = 'LakshiAthapaththu'
        form_data = {'current_password': pw,'username':username}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        #give password with less than 8 characters
        pw = "abc" #current password cannot be less than 8 characters
        username = 'Lakshi'
        form_data = {'current_password': pw, 'username': username}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        newpw = '123abcdefg'
        currentpw = '123abcdef'
        form_data = {'current_password': currentpw, 'new_password': newpw}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        newpw = '123abcdefg'
        form_data = {'new_password': newpw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        newpw = '123ab*'
        currentpw = '123abcdef'
        form_data = {'current_password': currentpw, 'new_password': newpw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        newpw = '123ab*'
        currentpw = '123abcdef'
        confpw = '123ab*'
        form_data = {'current_password': currentpw, 'new_password': newpw,'confirm_password':confpw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        newpw = '123ab*def'
        currentpw = '123abcdef'
        confpw = '123ab*'
        form_data = {'current_password': currentpw, 'new_password': newpw, 'confirm_password': confpw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        newpw = '123ab*def'
        currentpw = '123abcdef'
        confpw = '123ab*def'
        form_data = {'current_password': currentpw, 'new_password': newpw, 'confirm_password': confpw}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        newpw = '123ab*def'
        currentpw = '123abcdef'
        confpw = '123ab*defghi'
        form_data = {'current_password': currentpw, 'new_password': newpw, 'confirm_password': confpw}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        newpw = '123ab*def'
        currentpw = '123ab'
        confpw = '123ab*defhij'
        form_data = {'current_password': currentpw, 'new_password': newpw, 'confirm_password': confpw}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        newpw = '123ab*def'
        currentpw = '123abcdef'
        confpw = '123ab*defhi'
        form_data = {'new_password': newpw, 'confirm_password': confpw}
        form = editProfile(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {'usrename':'Lakshi','current_password':currentpw}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'usrename': 'Lakshi','first_name':'laki','last_name':'kav','current_password': currentpw}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'usrename': None, 'current_password': currentpw}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        #this is checked in view level
        user_n = ''

        form_data = {'usrename':user_n , 'current_password': currentpw}
        form = editProfile(data=form_data)
        self.assertTrue(form.is_valid())

        def test_current_pw_help_text(self):
            form = editProfile()
            self.assertEqual(form.fields['current_password'].help_text, 'You need to enter your current password')


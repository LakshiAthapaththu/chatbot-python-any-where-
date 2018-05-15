from django.test import TestCase
from useract.models import User,Authority,Inquiry,TrainDetails,BusDetails,Report


class AuthorityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Authority.objects.create(authority_id=1,authority_name='SLTB')

    def test_for_authority_id_lable(self):
        auth_n = Authority.objects.get(authority_id=1)
        label = auth_n._meta.get_field('authority_id').verbose_name
        self.assertEquals(label, 'authority id')

    def test_for_authority_name_lable(self):
        auth_n = Authority.objects.get(authority_id=1)
        label = auth_n._meta.get_field('authority_name').verbose_name
        self.assertEquals(label, 'authority name')

    def test_for_status_lable(self):
        auth_n = Authority.objects.get(authority_id=1)
        label = auth_n._meta.get_field('status').verbose_name
        self.assertEquals(label, 'status')

    def test_for_e_mail_lable(self):
        auth_n = Authority.objects.get(authority_id=1)
        label = auth_n._meta.get_field('e_mail').verbose_name
        self.assertEquals(label, 'e mail')

    def test_for_telephone_lable(self):
        auth_n = Authority.objects.get(authority_id=1)
        label = auth_n._meta.get_field('telephone').verbose_name
        self.assertEquals(label, 'telephone')

    def test_for_address_lable(self):
        auth_n = Authority.objects.get(authority_id=1)
        label = auth_n._meta.get_field('address').verbose_name
        self.assertEquals(label, 'address')

    def test_max_length_auth_name(self):
        auth_n = Authority.objects.get(authority_id=1)
        max_len = auth_n._meta.get_field('authority_name').max_length
        self.assertEquals(max_len, 100)

    def test_max_length_status(self):
        auth_n = Authority.objects.get(authority_id=1)
        max_len = auth_n._meta.get_field('status').max_length
        self.assertEquals(max_len, 10000)

    def test_max_length_address(self):
        auth_n = Authority.objects.get(authority_id=1)
        max_len = auth_n._meta.get_field('address').max_length
        self.assertEquals(max_len, 100)

    def test_max_length_tp(self):
        auth_n = Authority.objects.get(authority_id=1)
        max_len = auth_n._meta.get_field('telephone').max_length
        self.assertEquals(max_len, 100)

class ReportModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Authority.objects.create(authority_id=1, authority_name='SLTB')
        auth = Authority.objects.get(authority_id=1)
        Report.objects.create(report_id=1,authority_id=auth)

    def test_rep_id_label(self):
            roport_n = Report.objects.get(report_id=1)
            label =roport_n._meta.get_field('report_id').verbose_name
            self.assertEquals(label, 'report id')

    def test_auth_id_label(self):
            roport_n = Report.objects.get(report_id=1)
            label =roport_n._meta.get_field('authority_id').verbose_name
            self.assertEquals(label, 'authority id')



class InquiryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Lakshi',password='123')
        Authority.objects.create(authority_id=1, authority_name='SLTB')
        auth = Authority.objects.get(authority_id=1)
        Report.objects.create(report_id=1, authority_id=auth)
        rep = Report.objects.get(report_id=1)
        user =User.objects.get(username='Lakshi')
        Inquiry.objects.create(inquiry_id=1,report_id=rep,USERNAME=user,add_state=False)

    def test_lable_inquiry_id(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        label = inq_n._meta.get_field('inquiry_id').verbose_name
        self.assertEquals(label,'inquiry id')


    def test_lable_reported_date(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        label = inq_n._meta.get_field('reported_date').verbose_name
        self.assertEquals(label,'reported date')

    def test_lable_reported_time(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        label = inq_n._meta.get_field('reported_time').verbose_name
        self.assertEquals(label, 'reported time')

    def test_lable_username(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        label = inq_n._meta.get_field('USERNAME').verbose_name
        self.assertEquals(label,'USERNAME')

    def test_lable_description(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        label = inq_n._meta.get_field('description').verbose_name
        self.assertEquals(label,'description')

    def test_lable_add_state(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        label = inq_n._meta.get_field('add_state').verbose_name
        self.assertEquals(label,'add state')

    def test_lable_report_id(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        label = inq_n._meta.get_field('report_id').verbose_name
        self.assertEquals(label,'report id')

    def test_max_reported_date(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        l = inq_n._meta.get_field('reported_date').max_length
        self.assertEquals(l, 20)

    def test_max_reported_time(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        l = inq_n._meta.get_field('reported_time').max_length
        self.assertEquals(l, 10)

    def test_max_description(self):
        inq_n = Inquiry.objects.get(inquiry_id=1)
        l = inq_n._meta.get_field('description').max_length
        self.assertEquals(l,1000)

class BusDetailModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        BusDetails.objects.create(bus_id=1,route_no=123)


    def test_bus_id_label(self):
            bus_n = BusDetails.objects.get(bus_id=1)
            label =bus_n._meta.get_field('bus_id').verbose_name
            self.assertEquals(label, 'bus id')

    def test_bus_route_no(self):
            bus_n = BusDetails.objects.get(bus_id=1)
            label =bus_n._meta.get_field('route_no').verbose_name
            self.assertEquals(label, 'route no')

    def test_bus_no_label(self):
            bus_n = BusDetails.objects.get(bus_id=1)
            label =bus_n._meta.get_field('bus_no').verbose_name
            self.assertEquals(label, 'bus no')

    def test_start_destination_label(self):
            bus_n = BusDetails.objects.get(bus_id=1)
            label =bus_n._meta.get_field('start_destination').verbose_name
            self.assertEquals(label, 'start destination')


    def test_end_destination_label(self):
            bus_n = BusDetails.objects.get(bus_id=1)
            label =bus_n._meta.get_field('end_destination').verbose_name
            self.assertEquals(label, 'end destination')

    def test_type_label(self):
            bus_n = BusDetails.objects.get(bus_id=1)
            label =bus_n._meta.get_field('type').verbose_name
            self.assertEquals(label, 'type')


    def test_max_bus_no(self):
        bus_n = BusDetails.objects.get(bus_id=1)
        l = bus_n._meta.get_field('bus_no').max_length
        self.assertEquals(l,10)


    def test_max_start_destination(self):
        bus_n = BusDetails.objects.get(bus_id=1)
        l = bus_n._meta.get_field('start_destination').max_length
        self.assertEquals(l,25)

    def test_max_end_destination(self):
        bus_n = BusDetails.objects.get(bus_id=1)
        l = bus_n._meta.get_field('end_destination').max_length
        self.assertEquals(l,25)

    def test_max_type(self):
        bus_n = BusDetails.objects.get(bus_id=1)
        l = bus_n._meta.get_field('type').max_length
        self.assertEquals(l,10)


class TrainDetailModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        TrainDetails.objects.create(train_id=1,route_no=123)


    def test_train_id_label(self):
            train_n = TrainDetails.objects.get(train_id=1)
            label =train_n._meta.get_field('train_id').verbose_name
            self.assertEquals(label, 'train id')


    def test_strart_destination_label(self):
            train_n = TrainDetails.objects.get(train_id=1)
            label =train_n._meta.get_field('strart_destination').verbose_name
            self.assertEquals(label, 'strart destination')

    def test_train_name_label(self):
            train_n = TrainDetails.objects.get(train_id=1)
            label =train_n._meta.get_field('train_name').verbose_name
            self.assertEquals(label, 'train name')

    def test_train_route_no(self):
            train_n = TrainDetails.objects.get(train_id=1)
            label =train_n._meta.get_field('route_no').verbose_name
            self.assertEquals(label, 'route no')

    def test_train_end_destination(self):
            train_n = TrainDetails.objects.get(train_id=1)
            label =train_n._meta.get_field('end_destination').verbose_name
            self.assertEquals(label, 'end destination')

    def test_max_start_destination(self):
        train_n = TrainDetails.objects.get(train_id=1)
        l = train_n._meta.get_field('strart_destination').max_length
        self.assertEquals(l,25)

    def test_max_end_destination(self):
        train_n = TrainDetails.objects.get(train_id=1)
        l = train_n._meta.get_field('end_destination').max_length
        self.assertEquals(l, 25)

    def test_max_train_name(self):
        train_n = TrainDetails.objects.get(train_id=1)
        l = train_n._meta.get_field('train_name').max_length
        self.assertEquals(l, 100)

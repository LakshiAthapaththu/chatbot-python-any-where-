from django.test import TestCase
from chatbot.models import Classes,Layers,train,sets



class ClassesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Classes.objects.create(class_name = 'bus')


    def test_for_class_name_label(self):
        class_n = Classes.objects.get(class_id=1)
        label = class_n._meta.get_field('class_name').verbose_name
        self.assertEquals(label,'class name')

    def test_max_length_class_name(self):
        class_n = Classes.objects.get(class_id=1)
        max_len = class_n._meta.get_field('class_name').max_length
        self.assertEquals(max_len,100)


    def test_for_class_id_label(self):
        class_n = Classes.objects.get(class_id=1)
        label = class_n._meta.get_field('class_id').verbose_name
        self.assertEquals(label,'class id')

class LayersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Layers.objects.create(layer_name = 'layer 0')

    def test_for_layer_name_label(self):
        layer_n = Layers.objects.get(layer_id=1)
        label = layer_n._meta.get_field('layer_name').verbose_name
        self.assertEquals(label,'layer name')

    def test_max_length_Layer_name(self):
        layer_n = Layers.objects.get(layer_id=1)
        max_len = layer_n._meta.get_field('layer_name').max_length
        self.assertEquals(max_len, 100)

    def test_for_class_id_label(self):
        layer_n = Layers.objects.get(layer_id=1)
        label = layer_n._meta.get_field('layer_id').verbose_name
        self.assertEquals(label, 'layer id')



class trainModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Classes.objects.create(class_name='bus')
        Layers.objects.create(layer_name='layer 0')
        class_obj = Classes.objects.get(class_id=1)
        layer_obj = Layers.objects.get(layer_id=1)
        sets.objects.create(class_id_of=class_obj,layer_id_of=layer_obj,parent_id=1)
        set_obj = sets.objects.get(set_id=1)
        train.objects.create(sentence = 'bus goes fast',set_id=set_obj,train_state=False)

    def test_for_sentence_lable(self):

        sentence_n = train.objects.get(sentence_id =1)
        label = sentence_n._meta.get_field('sentence').verbose_name
        self.assertEquals(label,'sentence')

    def test_for_set_id_lable(self):

        sentence_n = train.objects.get(sentence_id =1)
        label = sentence_n._meta.get_field('set_id').verbose_name
        self.assertEquals(label,'set id')

    def test_for_class_bag_lable(self):

        sentence_n = train.objects.get(sentence_id =1)
        label = sentence_n._meta.get_field('class_bag').verbose_name
        self.assertEquals(label,'class bag')

    def test_for_word_bag_lable(self):

        sentence_n = train.objects.get(sentence_id =1)
        label = sentence_n._meta.get_field('word_bag').verbose_name
        self.assertEquals(label,'word bag')

    def test_for_train_state_lable(self):

        sentence_n = train.objects.get(sentence_id =1)
        label = sentence_n._meta.get_field('train_state').verbose_name
        self.assertEquals(label,'train state')

    def test_for_sentence_length(self):

        sentence_n = train.objects.get(sentence_id =1)
        l = sentence_n._meta.get_field('sentence').max_length
        self.assertEquals(l,100000)

    def test_for_wordbag_length(self):

        sentence_n = train.objects.get(sentence_id =1)
        l = sentence_n._meta.get_field('word_bag').max_length
        self.assertEquals(l,100000000)

    def test_for_class_bag_length(self):

        sentence_n = train.objects.get(sentence_id =1)
        l = sentence_n._meta.get_field('class_bag').max_length
        self.assertEquals(l,100000000)

class setsModelTest(TestCase):
    @classmethod
    #check the forign key constrains
    def setUpTestData(cls):
        Classes.objects.create(class_name='bus')
        Layers.objects.create(layer_name='layer 0')
        class_obj = Classes.objects.get(class_id=1)
        layer_obj = Layers.objects.get(layer_id=1)
        sets.objects.create(class_id_of=class_obj, layer_id_of=layer_obj, parent_id=1)

    def test_for_class_id_of_label(self):
        set_n = sets.objects.get(set_id=1)
        label = set_n._meta.get_field('class_id_of').verbose_name
        self.assertEquals(label,'class id of')

    def test_for_layer_id_label(self):
        set_n = sets.objects.get(set_id=1)
        label = set_n._meta.get_field('layer_id_of').verbose_name
        self.assertEquals(label,'layer id of')

    def test_for_set_id_label(self):
        set_n = sets.objects.get(set_id=1)
        label = set_n._meta.get_field('parent_id').verbose_name
        self.assertEquals(label,'parent id')



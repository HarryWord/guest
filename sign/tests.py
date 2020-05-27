from django.test import TestCase
from sign.models import Event,Guest

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self) :
        Event.objects.create(id=1,name="oneplus 3 event",status = True,limit = 2000, address = '798 in Beijing', start_time = '2020-05-30 10:00:00')
        Guest.objects.create(id = 1, event_id = 1, realname = 'Alen', phone = '17671468132', email = 'alen@mail.com', sign = False)

        def test_event_models(self):
            result = Event.objects.get(name="oneplus 3 event")
            self.assertEqual(result.address, "798 in Beijing")
            self.assertTrue(result.status)

        def test_guest_models(self):
            result = Guest.objects.get(phone = '17671468132')
            self.assertEqual(result.realname,"Alen")
            self.assertFalse(result.sign)

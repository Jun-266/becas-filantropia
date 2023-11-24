from django.test import TestCase
from app_becas.models import Scholarship 
from app_becas.models import User 

class ScholarshipTests(TestCase):
    def setUp(self):
        Scholarship.objects.create(name="Santiago",
                                   description="Beca de Santiago",
                                   amount = 2000
                                   )
        

    def test_schorlarship_creation(self):
        obj = Scholarship.objects.get(name="Santiago")


        self.assertEqual(obj.name, "Santiago")
        self.assertEqual(obj.description, "Beca de Santiago")
        self.assertEqual(obj.amount, 2000)


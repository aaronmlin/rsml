
from django.test import TestCase, Client

from main.models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    # def create_product(self, name = "Valk M", amount = 5, price = 30, description = "Newest model!"):
    #     return Product.objects.create(name = name, amount = amount, price = price, description = description)

    # def test_create(self):
    #     p = self.create_product()
    #     self.assertTrue(isinstance(p, Product))
    #     self.assertEqual(p.__str__(), p.name)

    # def test_product_name_max_length(self):
    #     p = self.create_product()
    #     max_length = p._meta.get_field('name').max_length
    #     self.assertEqual(max_length, 255)
    
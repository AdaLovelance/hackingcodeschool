from django.test import TestCase

from apps.users.models import User
from apps.discuss.models import Question

class SimpleTest(TestCase):

	def test_save_slug(self):
		user = User.objects.create_user(username = 'Testito', email = 'testito@soyunaprueba.es')
		question = Question.objects.create(user = user,
					title = 'pregunta 1',
					description = ' lalallalallalalala' )
		self.assertEqual(question.slug , 'pregunta-1'  )
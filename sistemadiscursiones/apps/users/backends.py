from .models import User


class EmailAuthentication(object):

	def authenticate(self, email, password):
		try:
			user = User.objects.get(email=email)
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None


	def get_user(self, user_id):
		try:
			return User.objects.get( id = user_id)
		except:
			return None
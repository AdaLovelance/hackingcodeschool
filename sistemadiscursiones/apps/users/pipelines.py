def get_avatar(backend, strategy, details, response, user=None,
				*args, **kwargs):
	url = None
	if backend.name == 'facebook':
		url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
	if backend.name == 'twitter':
		url = response.get('profile_image_url' , '').replace('medium','')
	if backend.name == 'google-oauth2' and "picture" in response:
		url = response["picture"]



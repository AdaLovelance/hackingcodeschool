from django.db import models
from django.template.defaultfilters import slugify
from apps.users.models import User


class TimeStampModel(models.Model):

	user = models.ForeignKey(User, db_index=True, null=True, blank=True)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	etiqueta = models.TextField(max_length = 20, db_index=True, null=True, blank=True)


	class Meta:
		abstract = True


class Tag(models.Model):

	nombre = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.nombre


class Question(TimeStampModel):

	etiqueta = TimeStampModel
	tag = models.ManyToManyField(Tag)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, editable=False, unique=True)

	def __unicode__(self):
		return '%s %s %s' % (self.user, self.title, self.tag)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
			print self.slug
		super(Question, self).save(*args,**kwargs)


class Answer(TimeStampModel):

	question = models.ForeignKey(Question)
	
	def __unicode__(self):
		return self.user.username


"""
class Buscador(TimeStampModel):

	question = models.ForeignKey(Question)
	
	def __unicode__(self):
		return self.question

"""
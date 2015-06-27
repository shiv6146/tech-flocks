from django.db import models
import lxml.html

class Post(models.Model):
	title = models.CharField(max_length=200,default='sample')
	url = models.URLField(default='sample')
	likes = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now_add=True)

	def clean(self):
		if self.title == 'sample' and self.url != 'sample':
			print 'hi'
			temp = lxml.html.parse(self.url)
			self.title = temp.find(".//title").text

	def __unicode__(self):
		return self.title
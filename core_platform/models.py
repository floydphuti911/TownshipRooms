from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils.text import slugify

# Create your models here.
class RoomManager(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=150,null=True,blank=True)
	ussd = models.CharField(max_length=150,null=True,blank=True)
	mobile = models.CharField(max_length=150,null=True,blank=True)

	def __unicode__(self):
		return self.user.get_full_name()
		
class Tenant(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.get_full_name()
		
class RoomLease(models.Model):
	room = models.ForeignKey('Room',related_name='lease_room')
	tenant = models.ForeignKey('Tenant',related_name='lease_tenant')
	def __unicode__(self):
		return self.room.__unicode__()
		
		
class Room(models.Model):
	"""A model to store extra information for each property"""
	manager = models.ForeignKey(RoomManager,related_name='room_manager')
	name = models.CharField(max_length=100, default="Property")
	slug = models.CharField(max_length=100, blank=True)
	picture = models.ImageField(null=True,blank=True,upload_to='rooms_pictures')
	description = models.TextField(max_length=500, default="Description")
	price = models.DecimalField(default=0, decimal_places=2, max_digits=20)
	street_address = models.CharField(max_length=150)
	suburb = models.CharField(max_length=150)
	published = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

	def get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while Room.objects.filter(slug=unique_slug).exists():
			if Room.objects.get(slug=unique_slug).pk != self.pk:
				unique_slug = '{}-{}'.format(slug, num)
				num += 1
			else:
				return unique_slug
		return unique_slug
 
	def save(self, *args, **kwargs):
		self.slug = self.get_unique_slug()
		super(Room, self).save()		
from django.db import models
import uuid


# Create your models here.
class Platform(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=30)
	website = models.URLField(default='')
	isValid = models.BooleanField(default=False)

	def __str__(self):
		return self.name


class RatingOrganization(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class LabelText(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name=models.CharField(max_length=30)
	def __str__(self):
		return self.name

class PlatformLabel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	platForm = models.ForeignKey(Platform)
	label = models.ForeignKey(LabelText)
	def __str__(self):
		return self.platForm.name + "-" + self.label.name

class LinkToWx(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	platForm = models.OneToOneField(Platform)
	wxText=models.TextField()
	isValid = models.BooleanField(default=False)
	image = models.ImageField(upload_to="static/img/toWx", blank=True, null=True)

	def __str__(self):
		return self.platForm.name

class PlatformRating(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	platForm = models.ForeignKey(Platform)
	ratingOrganization = models.ForeignKey(RatingOrganization)
	url = models.URLField(default='')
	ratingValue = models.CharField(max_length=10)

	def __str__(self):
		return self.ratingOrganization.name + "-" + self.platForm.name


class PromotionAgency(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name


class PromotionInfo(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	platForm = models.ForeignKey(Platform)
	promotionAgency = models.ForeignKey(PromotionAgency)
	url = models.URLField(default='')
	isValid = models.BooleanField(default=False)

	def __str__(self):
		return self.promotionAgency.name + "-" + self.platForm.name

class ClickTrace(models.Model):
	id=models.IntegerField(primary_key=True)
	cookieId=models.UUIDField()
	areaType=models.CharField(max_length=30)
	target=models.CharField(max_length=30)
	propertyData=models.CharField(max_length=30)
	clickTime=models.DateTimeField()

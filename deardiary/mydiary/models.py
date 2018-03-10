from django.db import models
import os
from django.utils import timezone
# from PIL import Image
# from resizeimage import resizeimage
#
#
# def profile_path_and_rename(instance, filename):
#     upload_to = 'static/profile/'+str(instance.phone)
#     return os.path.join(upload_to, filename)
#
# def image_resize(image, image_path):
#     image = Image.open(image)
#     if image.size[0] > 400:  # if width is greater than 400
#         new_image = resizeimage.resize_width(image, 400)
#         new_image.save(image_path)
#
#     elif image.size[1] > 400:  # if height is greater than 400
#         new_image = resizeimage.resize_height(image, 400)
#         new_image.save(image_path)
#
#
# class DearUser(models.Model):
#     phone = models.BigIntegerField(blank=True, unique=True)
#     name = models.CharField(max_length=60, blank=True, unique=False)
#     email = models.EmailField(unique=False, blank=True, null=True)
#     image = models.ImageField(upload_to=profile_path_and_rename, blank=True, null=True)
#     time = models.DateTimeField(default=timezone.now)
#     last_updated = models.DateTimeField(blank=True, null=True)
#
#
#     def __str__(self):
#         return str(self.phone)
#
#     def save(self, *args, **kwargs):
#         super(DearUser, self).save()
#         if self.image not in [None, '']:
#             image_resize(self.image, self.image.path)


# User model to create a user collection
class User(models.Model):
    name = models.BigIntegerField(max_length=120)
    password = models.BigIntegerField(max_length=120)
    dateModified = models.DateTimeField(default=timezone.now, required=True)
    isVerified = models.BooleanField(required=True)

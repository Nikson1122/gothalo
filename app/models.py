# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import FileExtensionValidator

# # Create your models here.
# class ProfileModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.png', upload_to='profile', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
#     # image = models.ImageField(default='default.png', upload_to='profile', validators=[FileExtensionValidator('png', 'jpg','JPEG')])
#     phone_number = models.CharField(max_length=15, blank=True)

#     def __str__(self):
#         return self.user.username
    

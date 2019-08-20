from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
#from django.utils.text import slugify
from slugify import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=16)
    is_phone_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, unique=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Job(models.Model):
    OBJECT_TYPES = [
        ('house', 'house'),
        ('office', 'office'),
        ('shop', 'shop'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    object_type = models.CharField(max_length=32, choices=OBJECT_TYPES, default='house')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Job in {self.address} {self.object_type} from {self.start_date}'


class Photo(models.Model):
    image_field = models.ImageField(max_length=256, blank=True, null=True, upload_to='jobs_images')
    alt = models.CharField(max_length=32)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.job}'

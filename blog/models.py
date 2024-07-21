from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

MALE, FEMALE = ("Male", "Female")


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    GENDER_CHOICES = (
        (MALE, MALE),
        (FEMALE, FEMALE),
    )
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def __str__(self):
        return self.username


class Category(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.title


class Post(BaseModel, models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    def __str__(self):
        return self.title


class PostDetail(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='psotdetail')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Post tafsiloti"
        verbose_name_plural = "Post tafsilotlari"

    def __str__(self):
        return f"{self.post.title} - tafsiloti"


class Comment(BaseModel, models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()

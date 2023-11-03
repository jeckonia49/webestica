from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    BaseUserManager,
    AbstractBaseUser,
)
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class AccountManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, username=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, username, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = AccountManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self, *args, **kwargs):
        return reverse("accounts:user_detail", args=[self.pk])


class Profile(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="user_profile"
    )
    avatar = models.ImageField(upload_to="profile/avatar/", blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    full_name = models.CharField(max_length=300, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    updatedAt = models.DateTimeField(auto_now=True)

    @property
    def username(self):
        if self.full_name is not None:
            return f"{self.full_name.split(' ')[0]}".title()
        else:
            return f"{self.user.email[:self.user.email.index('@')]}".title()

    def __str__(self):
        return f"{self.user.email}" or f"{self.full_name}"

    def get_posts(self):
        return self.post_author.all()

    def get_absolute_url(self):
        return reverse("writer:writer_view", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        return super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get(user=instance).save()


class Social(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_social"
    )
    name = models.CharField(max_length=100, default="lionnic")
    social = models.URLField(max_length=255, default="https://www.webestica.com/")

    def __str__(self):
        return self.name

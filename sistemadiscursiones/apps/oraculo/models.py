from django.db import models
from apps.users.models import *
from apps.discuss.models import *
# Create your models here.
from apps.users.forms import ExtraDataForm
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
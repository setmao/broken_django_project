from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Engineer(models.Model):
    name = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)


class Skill(models.Model):
    engineer = models.ForeignKey(Engineer)
    name = models.CharField(max_length=64)

    SCORE_NA = 0
    SCORE_1 = 1
    SCORE_2 = 2
    SCORE_3 = 3
    SCORE_4 = 4
    SCORE_5 = 5

    score = models.PositiveIntegerField(
        default=SCORE_NA,
        validators=[
            MaxValueValidator(SCORE_5),
            MinValueValidator(SCORE_NA)
        ]
    )

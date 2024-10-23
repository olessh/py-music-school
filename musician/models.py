from django.core.exceptions import ValidationError
from django.db import models


def validate_age(value):
    if value < 14:
        raise ValidationError("Musician must be at least 14 years old.")


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(validators=[validate_age])
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

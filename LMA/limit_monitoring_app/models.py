from django.db import models

# Create your models here.
class Criterias(models.Model):
    COMPARISON_CHOICES = [
        ('<', '<'),
        ('<=', '<='),
        ('>', '>'),
        ('>=', '>='),
        ('==', '=='),
    ]


    comparison_operator = models.CharField(max_length=2, choices=COMPARISON_CHOICES)
    Temperature         = models.FloatField()
    status              = models.BooleanField(default=False)
    about               = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.comparison_operator} {self.Temperature}, {self.about} ,id={self.id}"




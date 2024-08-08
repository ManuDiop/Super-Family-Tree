from django.db import models

class SuperHero(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    skill1 = models.CharField(max_length=100)
    skill2 = models.CharField(max_length=100, null=True, blank=True)
    skill3 = models.CharField(max_length=100, null=True, blank=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        related_name='children',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name
    
    def get_skills(self):
        return [skill for skill in [self.skill1, self.skill2, self.skill3] if skill]
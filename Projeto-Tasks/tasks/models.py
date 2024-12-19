from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    describe = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('NewTask', 'Nova'),
        ('InProgress', 'Em andamento'),
        ('Completed', 'Concluído'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NewTask')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Se o status mudou para "Concluído" e datecompleted ainda não está definido
        if self.status == 'Completed' and not self.datecompleted:
            self.datecompleted = timezone.now()  # Define datecompleted como o tempo atual
        super().save(*args, **kwargs)
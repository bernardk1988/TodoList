from django.db import models

class Todo1(models.Model):
    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    ]
    task = models.CharField(max_length=2000)
    datetime = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
    )
    class Meta:
        db_table = 'todo1'
        ordering = ['-datetime']
    def __str__(self):
        return self.task
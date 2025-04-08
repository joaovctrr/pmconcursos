from django.db import models

class Subject(models.Model):  
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Question(models.Model):  
    LEVEL_CHOICES = [
        ('E', 'Easy'),
        ('M', 'Medium'), 
        ('H', 'Hard'),
    ]
    statement = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.statement[:50]}..."

class Alternative(models.Model):  
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='alternatives')
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.text[:50]} ({'Correct' if self.is_correct else 'Incorrect'})"
from django.db import models

# Create your models here.

from django.db import models

LEVEL_OF_STUDY = (
('Elementary', 'Elementary'),
('High School', 'High School'),
('College', 'College'),
('Professional', 'Professional'),
)

BUDGET_RANGE = (
('$5 - $10 per hour', '$5 - $10 per hour'),
('$10 - $15 per hour', '$10 - $15 per hour'),
('$15 - $20 per hour', '$15 - $20 per hour'),
('$20 - $25 per hour', '$20 - $25 per hour'),
('$25 - $30 per hour', '$25 - $30 per hour'),
('$30 - $40 per hour', '$30 - $40 per hour'),
('$40 - $50 per hour', '$40 - $50 per hour'),
)

class JobDescription(models.Model):
    title = models.CharField(max_length=150,null=True, blank=True)
    level = models.CharField(choices=LEVEL_OF_STUDY, max_length=50,null=True, blank=True)
    gender_preference = models.CharField( max_length=50,null=True, blank=True)
    qualification = models.CharField( max_length=100,null=True, blank=True)
    budget = models.CharField(choices=BUDGET_RANGE, max_length=100,null=True, blank=True)
    description = models.TextField()
    experience = models.CharField(max_length=50,null=True, blank=True)
    status = models.CharField(max_length=10, default='Pending')
    job_posted_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title
    

class ProhibitedPattern(models.Model):
    pattern = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


    def __str__(self):
        return f' {self.description} : {self.pattern}'
    
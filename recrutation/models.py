from django.db import models

STATUS_CHOICES = (
    ('c', 'czeka na akceptacje'),
    ('a', 'zaakceptowany'),
    ('n', 'niezaakceptowany')
)


class Recruiter(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    presentation = models.CharField(max_length=360, null=False)

    def __str__(self):
        return self.email

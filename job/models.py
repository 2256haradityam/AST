import random
import string
from djongo import models

def generate_unique_id():
    """Generate a 16-character alphanumeric unique ID (`a-z`, `0-9`) that doesn't exist in the database."""
    while True:
        random_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))  # Alphanumeric ID
        if not Job.objects.filter(id=random_id).exists():
            return random_id

class Job(models.Model):
    id = models.CharField(
        max_length=16, 
        unique=True, 
        primary_key=True, 
        default=generate_unique_id, 
        editable=False
    )
    positionName = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = "python_jobs"

    def __str__(self):
        return self.positionName if self.positionName else "No Title"

    def delete(self, *args, **kwargs):
        """Ensure deletion works, and assign a random ID if missing before deletion."""
        if not self.pk:  # If no ID exists, assign a temporary random ID before deletion
            self.id = generate_unique_id()
        super().delete(*args, **kwargs)

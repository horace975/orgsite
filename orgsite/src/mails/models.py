from django.db import models

# Create your models here.

class LeaveMessage(models.Model):
	name = models.CharField(
		verbose_name='Name',
        max_length=100,
    )
	email = models.EmailField(
		verbose_name='E-mail',
        max_length=255, 
        # unique=True, 
        # db_index=False,
    )
	content = models.TextField(
		verbose_name='Message',
		max_length=500,
        help_text="Leave us a message.",
    )
	created_at = models.DateTimeField(
		verbose_name='DateTime',
        auto_now_add=True,
    )

	def __str__(self):
		return self.name + self.email + self.content

	class Meta:
		ordering = ['-created_at']

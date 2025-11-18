from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
	book_title = models.CharField("Título del libro", max_length=255)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
	rating = models.PositiveSmallIntegerField("Puntuación", validators=[MinValueValidator(1), MaxValueValidator(5)], default=5)
	text = models.TextField("Reseña", blank=True)
	created_at = models.DateTimeField("Creado", default=timezone.now)
	updated_at = models.DateTimeField("Actualizado", auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.book_title} — {self.author.username} ({self.rating})"



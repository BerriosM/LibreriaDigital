from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

try:
    from .models import Review
except Exception:
    Review = None
from .forms import ReviewForm


@login_required
def profile(request):
    # Si el modelo Review no está disponible (p. ej. migraciones pendientes),
    # devolver una lista vacía en lugar de provocar una excepción.
    if Review is None:
        reviews = []
    else:
        reviews = Review.objects.filter(author=request.user)
    return render(request, 'profile.html', {'reviews': reviews})


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
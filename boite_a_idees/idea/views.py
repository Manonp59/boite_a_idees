from django.shortcuts import render
from .models import Idea, Likes
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Idea, Likes,Dislikes


class IdeaListView(LoginRequiredMixin,ListView):
    model = Idea
    template_name = "idea/idea_list.html"
    context_object_name = "idea_list"

class IdeaDetailView(LoginRequiredMixin, DetailView):
    model = Idea
    template_name = "idea/idea_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        idea = self.get_object()
        context['user_liked'] = idea.idea_likes.filter(user=user).exists()
        context['user_disliked'] = idea.idea_dislikes.filter(user=user).exists()
        return context


#LoginRequiredMixin remplace le décorateur @login_required
class IdeaCreateView(LoginRequiredMixin,CreateView):
    model = Idea
    template_name = "idea/idea_create.html"
    fields = ['titre','description']
    # on peut aussi mettre fields= ['name','description'], c'est comme ça qu'on choisit quels champs on veut si on ne les veut pas tous
    success_url = reverse_lazy('idea-list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



@login_required
def like(request, pk):
    user = request.user
    idea = get_object_or_404(Idea, pk=pk)
    current_likes = idea.likes
    current_dislikes = idea.dislikes
    liked = Likes.objects.filter(user=user, idea=idea).count()
    disliked = Dislikes.objects.filter(user=user, idea=idea).count()
    if not liked and not disliked:
        Likes.objects.create(user=user, idea=idea)
        current_likes += 1
    elif (not liked) and (disliked) : 
        Likes.objects.create(user=user, idea=idea)
        current_likes += 1
        Dislikes.objects.filter(user=user, idea=idea).delete()
        current_dislikes -= 1
    else:
        Likes.objects.filter(user=user, idea=idea).delete()
        current_likes -= 1
    idea.likes = current_likes
    idea.dislikes = current_dislikes
    idea.save()
    return HttpResponseRedirect(reverse('idea-detail', args=[pk]))


@login_required
def dislike(request, pk):
    user = request.user
    idea = get_object_or_404(Idea, pk=pk)
    current_dislikes = idea.dislikes
    current_likes = idea.likes
    disliked = Dislikes.objects.filter(user=user, idea=idea).count()
    liked = Likes.objects.filter(user=user, idea=idea).count()
    if not disliked and not liked :
        Dislikes.objects.create(user=user, idea=idea)
        current_dislikes += 1
    elif not disliked and liked : 
        Dislikes.objects.create(user=user, idea=idea)
        current_dislikes += 1
        Likes.objects.filter(user=user, idea=idea).delete()
        current_likes -= 1
    else:
        Dislikes.objects.filter(user=user, idea=idea).delete()
        current_dislikes -= 1
    idea.dislikes = current_dislikes
    idea.likes = current_likes
    idea.save()
    return HttpResponseRedirect(reverse('idea-detail', args=[pk]))


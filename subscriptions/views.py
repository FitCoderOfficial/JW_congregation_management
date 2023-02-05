# subscriptions/views.py
from .models import Magazine, Subscription
from django.views.generic import ListView, DetailView


# @login_required
# def subscribe(request, magazine_id):
#     magazine = Magazine.objects.get(id=magazine_id)
#     subscription, created = Subscription.objects.get_or_create(user=request.user, magazine=magazine)

#     if created:
#         messages.success(request, f"You have subscribed to {magazine.name}")
#     else:
#         messages.warning(request, f"You are already subscribed to {magazine.name}")

#     return redirect("subscriptions:list")

# @login_required
# def subscriptions_list(request):
#     subscriptions = Subscription.objects.filter(user=request.user)
#     context = {"subscriptions": subscriptions}
#     return render(request, "subscriptions/list.html", context)


class MagazineListView(ListView):
    model = Magazine
    template_name = 'magazine_list.html'

class MagazineDetailView(DetailView):
    model = Magazine
    template_name = 'magazine_detail.html'

class SubscriptionListView(ListView):
    model = Subscription
    template_name = 'subscription_list.html'

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
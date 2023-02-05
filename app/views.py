from django.shortcuts import render, redirect
from django.utils import timezone


from app.models import User, Counter
from app.forms import CounterForm


def home(request):
    users = User.objects.all()
    data = {}
    for user in users:
        data[user] = Counter.objects.filter(user=user)

    if request.method == 'POST':
        form = CounterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("home")

    else:
        form = CounterForm()

    return render(request, 'home.html', {'form': form, "data": data})


def reset(request, counter_id):
    counter = Counter.objects.get(id=counter_id)
    counter.date = timezone.now()
    counter.save()
    return redirect(home)


def delete(request, counter_id):
    counter = Counter.objects.get(id=counter_id)
    counter.delete()
    return redirect(home)


from django.shortcuts import render, redirect
from .forms import RegistrationForm


def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_pasword(user.pasword)
            user.save()
            return redirect('/')

    return render(request, 'main/registration.html', context={
        'form': form
    })

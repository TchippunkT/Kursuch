from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.smartif import prefix
from .forms import RegisterForm, ProfileForm
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from .models import User, MyUser
from django.http import HttpResponse

from django.forms import modelformset_factory

def RegisterFormView(request):
    # my_user_form = modelformset_factory(MyUser, fields='__all__')
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES, prefix='profile')
        user_form = RegisterForm(request.POST,request.FILES, prefix='user')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            profile = profile_form.save(commit=False)

            profile.user = user
            profile.save()

            # return RegisterForm.form_valid(form)
            return HttpResponseRedirect("/auth/")
    else:
        user_form = RegisterForm(prefix='user')
        profile_form = ProfileForm(prefix='profile')
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request,'register.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def users(request):
    user_list = MyUser.objects.order_by('id')
    user_list = user_list[1::]
    for user in user_list:
        print(user.avatar.url)

    return render(request, 'users.html', {'user_list': user_list})

def details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user.html', {'user': user})

# def goods(request):
#     goods_list = Goods.objects.order_by('id')
#     return render(request, 'goods.html', {'goods_list':goods_list})
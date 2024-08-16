from django.contrib.auth import views as auth_views

# Create your views here.
# def login_view(request):
#     if request.method == "GET":
#         return_to = request.GET.get("next")
#         context = {
#             'return_to': return_to
#         }
#         return render(request, template_name="acc/login.html", context=context)
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         redirect_to = request.POST.get("next", "/")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(redirect_to)
#         else:
#             context = {
#                 'error_message': 'Неправильный логин и/или пароль',
#                 'username': username
#             }
#             return render(request, "acc/login.html", context)


class MyLoginView(auth_views.LoginView):
    template_name = "acc/login.html"
    
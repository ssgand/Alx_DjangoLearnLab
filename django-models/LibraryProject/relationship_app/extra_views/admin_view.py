from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render

@user_passes_test(lambda user: user.userprofile.role == 'ADMIN')
def admin_view(request):
    # return render(request, 'relationship_app/admin_view.html', {})
    return HttpResponse("Admin View Content")
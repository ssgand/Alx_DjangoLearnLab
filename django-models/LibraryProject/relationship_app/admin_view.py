from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(lambda user: user.userprofile.role == 'ADMIN')
def AdminView(request):
    return render(request, 'relationship_app/admin_view.html', {})
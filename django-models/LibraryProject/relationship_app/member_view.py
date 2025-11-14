from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(lambda user: user.userprofile.role == 'MEMBER')
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})
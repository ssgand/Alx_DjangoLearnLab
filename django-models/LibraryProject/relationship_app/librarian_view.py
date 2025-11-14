from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(lambda user: user.userprofile.role == 'LIBRARIAN')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {})
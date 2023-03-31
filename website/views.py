from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {'name':'Sara', 'lastname':'Najafi', 'job':'Technical Writer', 'degree2':'MS in Artificial Intelligence', 'university2':'Islamic Azad University',
    'degree1':'BSc in Software Engineering', 'university1':'Isfahan University','lang1':'Persian', 'lang2':'English','lang3':'Arabic',
    'career':'I was Technical Writer for 6 years, And now I want to be a Software Engineer.', 'skill1':'Python & Django', 'skill2':'Git', 'Skill3':'React & Angular',
    'project1':'Launch', 'desc1':'A responsive website template designed to help startups promote their products or services.', 'project2':'devCard', 'desc2':'A portfolio website template designed for software developers.',
    'phone':'02111112222'}
    return render(request,"website/index.html", context)
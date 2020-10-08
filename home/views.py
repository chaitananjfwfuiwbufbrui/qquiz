from django.shortcuts import render,redirect
from home.models import * 
# Create your views here.
def home(request):
    dataa = Topics.objects.all()
    context = {'dataa' :dataa}
    if request.method =="POST":
            testname = request.POST['testname']
            name = request.POST['name']
            slug = request.POST['name']
            print(testname)
            slugs = slug.replace(' ',"_")
            ins = users(name=name,slug=slugs)
            ins.save()
            print("done for the data")
    return render(request,'ho.html',context)
    # Create your views here.




def questions(request,slug,id):
    if id == 1:

        marks = 0
        if request.method =="POST":
            testnamee = request.POST['testname']
            print(testnamee)
            tes = Topics.objects.filter(id=testnamee).first()
            sosss = tes.heading
            print(request.user,sosss)
            created = no_tests.objects.get_or_create(nameofthetest=tes,user_name=request.user,nomarks=marks)
    elif id >1:
        
        if request.method =="POST":
            answers = request.POST['answer']
            testnamee = request.POST['testname']
            print(testnamee)
            
            tes = Topics.objects.filter(heading=testnamee).first()

            sosss = Quuestions.objects.filter(s_n_o=id-1).first()
            created = no_tests.objects.get_or_create(nameofthetest=tes,user_name=request.user)
            correctans = sosss.correct
            if answers == correctans:
                marks = no_tests.objects.filter(nameofthetest=tes,user_name=request.user).first()
                print(marks)
                print(marks.nomarks)
                marks.nomarks = marks.nomarks + 1
                marks.save()
                print("vachesina ra bulloda"+sosss.questions)
            print(request.user,sosss.correct)

    topic = Topics.objects.filter(slug=slug).first()
    dataa = Topics.objects.all()
    choicess = Quuestions.objects.filter(Topicss= topic)
    total = len(choicess)
    soss = choicess.filter(s_n_o=id)
    s_n_oo = id
    slugs = topic.slug
    
    
    prs = id
    if id > 1:
        prev = id-1
    else:
        prev = None
    if id < len(choicess):
        nxt = id+1
    else:
        nxt = None
    
    sos = {'soss' :soss,'slugs':slugs,'topic':topic,'dataa':dataa,'prev':prev,'nxt':nxt,'total':total,'prs':prs }

    return render(request,'questions.html',sos)
def tests(request):
    pass
    
from django.shortcuts import render, redirect, HttpResponse
from home.models import *
# Create your views here.


def home(request):
    dataa = Topics.objects.all()
    context = {'dataa': dataa}
    if request.method == "POST":
        testname = request.POST['testname']
        name = request.POST['name']
        slug = request.POST['name']
        print(testname)
        slugs = slug.replace(' ', "_")
        ins = users(name=name, slug=slugs)
        ins.save()
        print("done for the data")
    return render(request, 'ho.html', context)
    # Create your views here.


def questions(request, slug, id):
    topic = Topics.objects.filter(slug=slug).first()
    dataa = Topics.objects.all()
    choicess = Quuestions.objects.filter(Topicss=topic)
    total = len(choicess)
    soss = choicess.filter(s_n_o=id)
    s_n_oo = id
    slugs = topic.slug
    if id == 1:

        marks = 0
        if request.method == "POST":
            testnamee = request.POST['testname']
            print(testnamee)
            tes = Topics.objects.filter(id=testnamee).first()
            sosss = tes.heading
            print(request.user, sosss)
            created = no_tests.objects.get_or_create(
                nameofthetest=tes, user_name=request.user, nomarks=marks)
    elif id > 1:

        if request.method == "POST":
            answers = request.POST['answer']
            testnamee = request.POST['testname']
            print(testnamee)

            tes = Topics.objects.filter(heading=testnamee).first()

            sosss = Quuestions.objects.filter(s_n_o=id-1).first()
            created = no_tests.objects.get_or_create(
                nameofthetest=tes, user_name=request.user)
            correctans = sosss.correct
            if answers == correctans:
                marks = no_tests.objects.filter(
                    nameofthetest=tes, user_name=request.user).first()
                print(marks)
                if marks.nomarks < total+1:

                    print(marks.nomarks)
                    marks.nomarks = marks.nomarks + 1
                    marks.save()
                    print("vachesina ra bulloda"+sosss.questions)
                elif marks.nomarks > total:
                    HttpResponse("error")

            print(request.user, sosss.correct)

    prs = id
    if id > 1:
        prev = id-1
    else:
        prev = None
    if id < len(choicess):
        nxt = id+1
    else:

        nxt = str(total) + "/results"

    sos = {'soss': soss, 'slugs': slugs, 'topic': topic, 'dataa': dataa,
           'prev': prev, 'nxt': nxt, 'total': total, 'prs': prs}

    return render(request, 'questions.html', sos)


def tests(request):
    pass


def results(request, slug, id):
    # topic and user n.o of questions are taken and marks
    topic = Topics.objects.filter(slug=slug).first()
    user = request.user
    choicess = Quuestions.objects.filter(Topicss=topic)
    total = len(choicess)
    print(total,choicess)
    marks = no_tests.objects.filter(
        nameofthetest=topic, user_name=request.user).first()

    gained = marks.nomarks

    print("1statge:all inputs are taken")

    id == total

    print(id)

    s_n_oo = id
    dataa = Topics.objects.all()
    soss = choicess.filter(s_n_o=total)
    slugs = topic.slug

    if id == 1:

        if request.method == "POST":
            testnamee = request.POST['testname']
            print(testnamee)
            tes = Topics.objects.filter(id=testnamee).first()
            sosss = tes.heading
            print(request.user, sosss)
            created = no_tests.objects.get_or_create(
                nameofthetest=tes, user_name=request.user, nomarks=marks)
    elif id > 1:
        print("2statge")
        if request.method == "POST":
            answers = request.POST['answer']
            testnamee = request.POST['testname']
            print("launched")

            tes = Topics.objects.filter(heading=testnamee).first()

            sosss = Quuestions.objects.filter(s_n_o=total,Topicss=topic).first()

            print("your ans:", answers)
            created = no_tests.objects.get_or_create(
                nameofthetest=topic, user_name=request.user)
            correctans = sosss.correct

            print("coreect one:", correctans)
            marks = no_tests.objects.filter(
                nameofthetest=tes, user_name=request.user).first()
            print(marks)
            print(marks.nomarks)

            if marks.nomarks <= total:
                if answers == correctans:

                    print(marks.nomarks)
                    marks.nomarks = marks.nomarks + 1
                    marks.save()
                    print("vachesina ra bulloda"+sosss.questions)
                    print("3statge")
                    redirect(results, slug, id)
                else:

                    print("not correct")

            else:
                print("akkuvaindhi ra bhjai")
                marks.nomarks = total
                marks.save()
                gained = total
                print(marks.nomarks)

        wroung = total - gained

        context = { 'wroung':wroung,'slugs': slugs, 'topic': topic,
                   'dataa': dataa, 'total': total, 'gained': gained}
    return render(request, 'results.html', context)

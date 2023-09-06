from django.shortcuts import render
def base(request):
    return render(request, 'jinja_app/base.html')

def child(request):
    return render(request, 'jinja_app/child_home.html')

def home(request):
    actors=[

        {'actor1':'karina'},
        {'actor2':'katrina'},
        {'actor3':'dipika'},
        {'actor4':'kangna'}
    ]
    print(actors)
    for i in actors:
        print(i)
    Emp=[
        {'Name':'xyz','cmpny_name':'HCL','cont':9923,'addr':'x'},
        {'Name':'sum','cmpny_name':'kept','cont':9950,'addr':'y'},
        {'Name':'abc', 'cmpny_name':'IBM', 'cont': 9890,'addr':'z'},
        {'Name':'dyz', 'cmpny_name':'GOGGLE', 'cont': 9159,'addr':'a'},
        {'Name': 'pqr', 'cmpny_name': 'Gmail', 'cont': 2020,'addr':'p'}
    ]
    return render(request,'jinja_app/home.html',context={'actor':actors,'Employee':Emp})


def table_home(request):
    datas=[
        {'Name':'sara','Age':11},
        {'Name':'tara','Age': 20},
        {'Name':'pinky','Age':18},
        {'Name':'tiny','Age': 24},
        {'Name': 'tiny', 'Age':12}
    ]
    return render(request,'table_based_jinja/table.html',context={'data':datas})


def text_home(request):
    colors=['red','black','blue','green','white','yellow','orange','pink']
    print(colors[2])
    text="""Ismail ibn Musa Menk (Arabic: إسماعيل بن موسى مِنك, romanized: ʾismāʿ īl ibn mūsā mink; born 27 June 1975) is a Zimbabwean Islamic scholar,[6][7][8] best known as Mufti Menk. He is the Grand Mufti[9][10] of Zimbabwe's Muslim community,[11][12] which makes up roughly 1% of the country's total population,[13] and head of the fatwa department for the Council of Islamic Scholars of Zimbabwe.

                 Menk was named one of The 500 Most Influential Muslims in the world by the Royal Aal al-Bayt Institute for Islamic Thought in Jordan in 2013, 2014 and 2017.[14][15] """
    return render(request,'text/text_file.html', context={'text':text,'colors':colors})

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')

def index(request):
    return render(request,'home/index.html')
from django.shortcuts import render , redirect #biz templatesde html sayfamızı olusturduktan sonra bu renderı kullanırız ve ilk parametre bır ıtek belırtme anlamında olan requwst tir sonra ise sayfamızın yolunu belırtırız
from django.http import HttpResponse# eger bır templates mız yoksa bu kutuphaneyı kullanırız 
from .models import TOdos
from .forms import Listform

# Create your views here.
#biz simdi database deki objelerı viewsimize cekmemizlaazım
#biz data base birsey atıyorsak bunu post metodu ıle yapıyoruz cunku verılerın gızlı olması gerekır get metodu ise gizlemez ve bide database gonderılen seyler postla gıder djangonun bunu anlayabılmesı ıcın ıf kosulu koyduk
def index(request):
   if request.method=="POST":
       form = Listform(request.POST or None)
       if form.is_valid :
           form.save()
           todo_list=TOdos.objects.all()
           return render(request,"todo_app/index.html",{"todo_list":todo_list})

   
   
   
   
   else:
     #return render(request,"todo_app/index.html",{"name":"Emin Can"})#ikinci kısım biz name adında bir değişkene isim atadık ve bunu cift sözlük kullanarak hangi fonksiyonda kullanıyorsan ordaki html sayfasında cagırabilirz bubir jinja kullanımına ornek.
     #name = "Emin Can Kurt"
     #return render(request,"todo_app/index.html",{"name":name})#dısrada bir degıskene atayarak da kullanabılırız.
   
      todo_list=TOdos.objects.all()# data basede olusturdugumuz objelerın hpsını bu sekılde todo_list in içine attık
     #sonra bunu aldıgımızı almak ıstedıgımız sayfada gosermemızlazım
      return render(request,"todo_app/index.html",{"todo_list":todo_list})#nerede cagıracaksak o fonksıyonda degıskene alıp bu seıldde cagııryoruz
def about(request):
    return render(request,"todo_app/about.html")


def create(request):
   if request.method=="POST":
       form = Listform(request.POST or None)
       if form.is_valid :
           form.save()
           todo_list=TOdos.objects.all()
           return render(request,"todo_app/create.html",{"todo_list":todo_list})   
   else:
     #return render(request,"todo_app/index.html",{"name":"Emin Can"})#ikinci kısım biz name adında bir değişkene isim atadık ve bunu cift sözlük kullanarak hangi fonksiyonda kullanıyorsan ordaki html sayfasında cagırabilirz bubir jinja kullanımına ornek.
     #name = "Emin Can Kurt"
     #return render(request,"todo_app/index.html",{"name":name})#dısrada bir degıskene atayarak da kullanabılırız.
   
      todo_list=TOdos.objects.all()# data basede olusturdugumuz objelerın hpsını bu sekılde todo_list in içine attık
     #sonra bunu aldıgımızı almak ıstedıgımız sayfada gosermemızlazım
      return render(request,"todo_app/create.html",{"todo_list":todo_list})#nerede cagıracaksak o fonksıyonda degıskene alıp bu seıldde cagııryoruz


def delete(request,TOdos_id):#id mize gore alacagımız belırtıyoruz burda da
    todo = TOdos.objects.get(pk=TOdos_id)
    todo.delete()
    return redirect("index") # buda bir metod ımport etmeyı unutma render ile aynı yerden bu ıslemlerden sonra su sayfaya gıt demek

def yes_finish(request,TOdos_id):#id mize gore alacagımız belırtıyoruz burda da
    todo = TOdos.objects.get(pk=TOdos_id)
    todo.finished = False
    todo.save()
    return redirect("index") # buda bir metod ımport etmeyı unutma render ile aynı yerden bu ıslemlerden sonra su sayfaya gıt demek

def no_finish(request,TOdos_id):#id mize gore alacagımız belırtıyoruz burda da
    todo = TOdos.objects.get(pk=TOdos_id)
    todo.finished = True
    todo.save()
    return redirect("index") # buda bir metod ımport etmeyı unutma render ile aynı yerden bu ıslemlerden sonra su sayfaya gıt demek

def update(request,TOdos_id):
   if request.method=="POST":
       todo_list = TOdos.objects.get(pk=TOdos_id)#ıd ye gore cagırdıktansonra bız bunları ınstance ıle form parametremızızın içine koyduk
       form = Listform(request.POST or None,instance=todo_list)
       if form.is_valid :#işlem  gerceklestı ise sunu yap demek burası
           form.save()
           todo_list=TOdos.objects.all()
           return redirect("index")    
   else:
     #return render(request,"todo_app/index.html",{"name":"Emin Can"})#ikinci kısım biz name adında bir değişkene isim atadık ve bunu cift sözlük kullanarak hangi fonksiyonda kullanıyorsan ordaki html sayfasında cagırabilirz bubir jinja kullanımına ornek.
     #name = "Emin Can Kurt"
     #return render(request,"todo_app/index.html",{"name":name})#dısrada bir degıskene atayarak da kullanabılırız.
   
      todo_list=TOdos.objects.all()# data basede olusturdugumuz objelerın hpsını bu sekılde todo_list in içine attık
     #sonra bunu aldıgımızı almak ıstedıgımız sayfada gosermemızlazım
      return render(request,"todo_app/create.html",{"todo_list":todo_list})
      
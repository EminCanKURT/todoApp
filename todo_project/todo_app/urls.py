from django.urls import path
from.import views
urlpatterns = [ #yani biiz ana yerden buraya yınlendırdı ve bu sayfayı bız kendıız olsuruduk
    path('',views.index,name="index" ),#burada ise biz nereye gidecek onu soyluyoruz yani vievwse gidip ordaki fonksıyonu kullanıcan demek
    path('about/',views.about,name="about" ),
    path('create/',views.create,name="create"),
    path('delete/<TOdos_id>',views.delete,name="delete"),#biz silme işlemlerını tektek yapmak ıstedıgımız ıcın verı tabanındaki tablodan idleri kullanacagımızı belirttik
    path('yes_finish/<TOdos_id>',views.yes_finish,name="yes_finish"),#biz silme işlemlerını tektek yapmak ıstedıgımız ıcın verı tabanındaki tablodan idleri kullanacagımızı belirttik
    path('no_finish/<TOdos_id>',views.no_finish,name="no_finish"),#biz silme işlemlerını tektek yapmak ıstedıgımız ıcın verı tabanındaki tablodan idleri kullanacagımızı belirttik
    path('update/<TOdos_id>',views.update,name="update"),#biz silme işlemlerını tektek yapmak ıstedıgımız ıcın verı tabanındaki tablodan idleri kullanacagımızı belirttik






]


from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    OnefPageView,
    KebabsPageView,
    TwoPageView,
    ItPageView,
    WaterPageView,
    ChettilPageView,
    HomePageDetailView,
    ItPageDetailView,
    JahonPageDetailView,
    BadiyPageDetailView,
    BolalarPageDetailView,
    DinPageDetailView,
    ChetPageDetailView

)

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('onef/',OnefPageView.as_view() ,name = 'onef'),
    path('kebabs/',KebabsPageView.as_view(),name= 'kebabs'),
    path('two/',TwoPageView.as_view(),name= 'twof'),
    path('it/',ItPageView.as_view(),name= 'it'),
    path('water/',WaterPageView.as_view(),name= 'water'),
    path('chettil/',ChettilPageView.as_view(),name= 'chettil'),
    path('<int:pk>/',HomePageDetailView.as_view(), name='pages_detail'),
    path('<int:pk>/it/',ItPageDetailView.as_view(), name='pagesit_detail'),
    path('<int:pk>/ja/',JahonPageDetailView.as_view(), name='pagesjahon_detail'),
    path('<int:pk>/ba/',BadiyPageDetailView.as_view(), name='pagesbadiy_detail'),
    path('<int:pk>/bol/',BolalarPageDetailView.as_view(), name='pagesbolalar_detail'),
    path('<int:pk>/din/',DinPageDetailView.as_view(), name='pagesdin_detail'),
    path('<int:pk>/cet/',ChetPageDetailView.as_view(), name='pageschet_detail'),

]
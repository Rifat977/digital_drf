from django.urls import path, include
import api.views as api_view
urlpatterns = [
    path('category/', api_view.CategoryList.as_view()),
    path('category/<int:pk>', api_view.CategoryDetail.as_view()),
    
    path('subcategory/', api_view.SubcategoryList.as_view()),
    path('subcategory/<int:pk>', api_view.SubcategoryDetail.as_view()),

    path('person/', api_view.PersonList.as_view()),
    path('person/<int:pk>', api_view.PersonDetail.as_view()),
    path('person/search/', api_view.PersonSearch.as_view()),

    path('category/person/<int:id>/', api_view.GetPersonByCategory.as_view()),
    path('<int:cat_id>/<int:sub_id>/<int:per_id>/', api_view.PersonDetailWithSubCat.as_view()),
]

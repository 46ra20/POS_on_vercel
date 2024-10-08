from django.urls import path,include
from rest_framework import routers
from .views import ProductView,CategoryView,BrandView,ProductSearchByName,UnitView,PurchaseView,StockView

router = routers.DefaultRouter()
router.register(r'product_category',CategoryView)
router.register(r'product_brand',BrandView)
router.register(r'product_unit',UnitView)
urlpatterns = [
    path('get_all/<key>/',ProductView.as_view({'get':'list'})),
    path('add_product/<userId>/',ProductView.as_view({'post':'create'})),
    path('update_product/<id>/',ProductView.as_view({'update':'patch'})),
    path('delete_product/<id>/',ProductView.as_view({'delete':'destroy'})),
    path('search_product/<key>/',ProductSearchByName.as_view({'get':'list'})),
    path('purchase/',PurchaseView.as_view({'post':'create'})),
    path('view_purchase/',PurchaseView.as_view({'get':'list'})),
    path('view_stock/',StockView.as_view({'get':'list'})),

    path('',include(router.urls)),
    # path('',include(router.urls))
]

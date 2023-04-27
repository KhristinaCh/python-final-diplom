from django.urls import path
from .views import PartnerUpdate, RegisterAccount, ProductInfoView, CategoryView, ShopView

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner_update'),
    path('user/register', RegisterAccount.as_view(), name='register_account'),
    path('products', ProductInfoView.as_view(), name='products'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
]

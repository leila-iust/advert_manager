from django.urls import path

from .views import AdvertismentView, CommentView

urlpatterns = [
    path("get_adverts", AdvertismentView.as_view(), name="advert_view"),
    path("comments", CommentView.as_view(), name="comments"),
    # path("purchase-history/", PurchaseHistoryAPIView.as_view(), name="purchase-history"),
]

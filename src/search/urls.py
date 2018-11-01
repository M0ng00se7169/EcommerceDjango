from django.conf.urls import url

from .views import (
    SearchProductView,
)

app_name = 'products'

urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name="query"),
]

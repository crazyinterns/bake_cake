from django.urls import path
from statistic.views import show_admin_stat_page
from django.contrib.auth.decorators import user_passes_test


urlpatterns = [
    path('admin-stat-page/', user_passes_test(lambda u: u.is_superuser)(show_admin_stat_page), name='show_admin_custom_page'),

]

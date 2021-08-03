from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'customer'

urlpatterns = [
	path('landing', views.LandingIndexView.as_view(), name="landing_view"),
  	path('customerRegistration', views.CustomerRegistrationView.as_view(), name="customerRegistration_view"),
    path('dashboard', views.DashboardIndexView.as_view(), name="dashboard_view"),
    path('registration', views.MedicineRegistrationView.as_view(), name="registration_view")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

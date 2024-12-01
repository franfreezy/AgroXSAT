from django.urls import path
from .views import get_location,get_gs,saTracker,CommandView,PayloadHandling,save_gs_coordinates,imagesapi,groundstationCoordinates,TelemetryHandling


urlpatterns = [
    path('', get_gs, name="Ground"),
    path('satLocation/', get_location, name="satTracker"),#get
    path('sat/', saTracker.as_view(), name="satTracker"),#post
    path('images/', imagesapi.as_view(), name="images"),
    path('baseStation/', groundstationCoordinates.as_view(), name="station"),  
    path('setGS/' , save_gs_coordinates.as_view(),name="basestation setting"),
    path('command/',CommandView.as_view()),
    path('payload/',PayloadHandling.as_view()),
    path('telemetry/',TelemetryHandling.as_view())
]
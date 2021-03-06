from django.urls import path
from . import views

app_name = "personal_website"

urlpatterns = [
    path ("profile/",views.Profile.as_view(),name="profile"),
    path ("about_me/",views.AboutMe.as_view(),name="about_me"),
    path ("projects/",views.Projects.as_view(),name="projects"),
    path ("contacts/reply/",views.Reply_on_message.as_view (),name="reply"),
    path ("",views.Index.as_view(),name="index"),
    path ("message/list/",views.MessageListView.as_view(),name="list"),
    path ("message/delete/<int:pk>", views.DeleteMessage.as_view(), name="delete"),
    path ("contacts/", views.Contacts.as_view(), name="contacts"),
]

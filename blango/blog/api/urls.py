from django.urls import path, include

urlpatterns =[
  path("", include(router.urls)),
  path(
        "posts/by-time/<str:period_name>/",
        PostViewSet.as_view({"get": "list"}),
        name="posts-by-time",
    ),
]
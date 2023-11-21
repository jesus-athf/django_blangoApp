from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns =[
  path("", include(router.urls)),
  path(
        "posts/by-time/<str:period_name>/",
        PostViewSet.as_view({"get": "list"}),
        name="posts-by-time",
    ),
  path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
  path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
]
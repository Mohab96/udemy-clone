# from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('courses', views.GeneralCourseViewSet)
router.register('enrollments', views.GeneralEnrollmentViewSet)
router.register('reviews', views.GeneralReviewViewSet)
router.register('categories', views.GeneralCategoryViewSet)
router.register('users', views.UserViewSet)
router.register('carts', views.CartViewSet)

courses_router = routers.NestedDefaultRouter(
    router, 'courses', lookup='course')
courses_router.register('reviews', views.CoursesReviewViewSet,
                        basename='course-reviews')
courses_router.register('enrollments', views.CoursesEnrollmentViewSet,
                        basename='course-enrollments')
courses_router.register('items', views.CourseItemsViewSet,
                        basename='course-items')


carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

users_router = routers.NestedDefaultRouter(router, 'users', lookup='user')
users_router.register('questions', views.QuestionViewSet,
                      basename='user-questions')


# URLConf
urlpatterns = router.urls + \
    courses_router.urls + \
    carts_router.urls + \
    users_router.urls

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from django.views.generic import TemplateView
from Post  import urls as PostUrls
from Course import urls as CourseUrls
from Portfolio import urls as PortfolioUrls
from Comment import urls as CommentUrls

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('about',TemplateView.as_view(template_name='about.html')),
    path('',include(PostUrls)),
    path('',include(CourseUrls)),
    path('',include(PortfolioUrls)),
    # path('',include(CommentUrls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

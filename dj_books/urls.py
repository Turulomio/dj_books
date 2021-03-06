from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns, set_language

## @todo Change views import to a generic way
from . import views as dj_books_views
from books import views as books_view

urlpatterns = i18n_patterns(
    path('i18n/setlang/',  set_language, name="set_language"), 
    path('admin/', admin.site.urls,  name="admin-site"),
    path('signup/', dj_books_views.signup, name='signup'),
    
    path('account_activation_sent/', dj_books_views.account_activation_sent, name='account_activation_sent'),
    path('activate/(<uidb64>/<token>/',  dj_books_views.activate, name='activate'),
    
    path('login/', LoginView.as_view(template_name='login.html'), name="login"), 
    path('logout/', logout_then_login, name="logout"), 
    path('', books_view.home, name='home'),
    path('profile/', dj_books_views.profile_edit, name="profile"), 

    path('books/author/create/', books_view.AuthorCreate.as_view(), name='author-add'),
    path('books/author/<int:pk>/', books_view.author_read, name='author-read'), 
    path('books/author/<int:pk>/update/', books_view.AuthorUpdate.as_view(), name='author-edit'),
    path('books/author/<int:pk>/delete/', books_view.AuthorDelete.as_view(), name='author-delete'),

    path('books/book/create/<int:author_id>', books_view.book_new, name='book-add'),
    path('books/book/<int:pk>/', books_view.book_read, name='book-read'),
    path('books/book/<int:pk>/update/', books_view.BookUpdate.as_view(), name='book-edit'),
    path('books/book/<int:pk>/delete/', books_view.BookDelete.as_view(), name='book-delete'),

    path('books/valoration/list/', books_view.valoration_list, name='valoration-list'),
    path('books/valoration/read/<slug:pk>/', books_view.valoration_read, name='valoration-read'),
    path('books/valoration/create/<int:book_id>/', books_view.valoration_new, name='valoration-add'),
    path('books/valoration/update/<slug:pk>/', books_view.ValorationUpdate.as_view(), name='valoration-update'),
    path('books/valoration/delete/<slug:pk>/', books_view.ValorationDelete.as_view(), name='valoration-delete'),

    path('books/querys/valued/', books_view.most_valuated_books, name='query_books_valued'),
    path('books/querys/unfinished_books/', books_view.unfinished_books, name='unfinished-books'),

    path('statistics_global/', books_view.statistics_global, name='statistics-global'),
    path('statistics_user/', books_view.statistics_user, name='statistics-user'),
)

handler403 = 'books.views.error_403'



from django import template
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

"""
    Esta clase la cree después de probar la app django-sitemaps, tenía cosas buenas, tree, breadcumb, title
    Era muy complicada y luego me liaba cuando el menu necesitaba parámetros
"""

class Action:
    def __init__(self,name,permissions,url):
        self.name=name
        self.permissions=permissions
        self.url=url

    def render(self, userpers, user):
        if self.__has_all_user_permissions(userpers) or user.is_superuser:
            return """<li><a href="{}">{}</a></li>\n""".format(self.url,self.name)
        else:
            return ""
       
       
    def __has_all_user_permissions(self, userpers):
        for p in self.permissions:
            if p not in userpers:
                return False
        return True

## Can have actions or other menus
"""
<nav>
    <ul class="nav nav_level_1">
        <li><a href="database/">All database</a></li>
        <li><a href="#" class="toggle-custom" id="btn-1" data-toggle="collapse" data-size="small" data-target="#submenu1" aria-expanded="false">My Library...</a>
             <ul class="nav collapse nav_level_2" id="submenu1" role="menu" aria-labelledby="btn-1">
                  <li><a href="books/author/new/">Add author</a></li>
                  <li><a  href="books/book/new/">Add book</a></li>
                  <li><a href="#" class="toggle-custom" id="btn-3" data-toggle="collapse" data-target="#submenu3" aria-expanded="false">My valorations...</a>
                      <ul class="nav collapse nav_level_3" id="submenu3" role="menu" aria-labelledby="btn-3">
                          <li><a href="books/valoration/new/">Add a new valoration</a></li>
                          <li><a href="books/valoration/list/">Valoration list</a></li>
                      </ul>
                  </li>
             </ul>
        </li>
    </ul>
</nav>

"""


## Arr can be actions or a group object
## No tiene permisos, busca en las acciones internas.
class Group:
    def __init__(self,level,name, id):
        self.arr=[]
        self.level=level
        self.name=name
        self.id=id
        
    ## Search for some permissions, not all
    def __user_has_some_children_permissions(self, userpers):
        for p in self.get_all_permissions():
            if p in userpers:
                return True
        return False
        
    def get_all_permissions(self):        
        r=set()
        for item in self.arr:
            if item.__class__==Group:
                for p in item.get_all_permissions():
                    r.add(p)
            else:#Action
                for p in item.permissions:
                    r.add(p)
        return r
    
    def render(self, userpers, user):
        r=""
        #        print("Group render", self.get_all_permissions(), userpers, self.__user_has_some_children_permissions(userpers))
        if self.__user_has_some_children_permissions(userpers) or user.is_superuser:
            r=r+"""<li><a href="#" class="toggle-custom" id="btn-{0}" data-toggle="collapse" data-target="#submenu{0}" aria-expanded="false">{1} ...</a>\n""".format(self.id,self.name)
            r=r+"""<ul class="nav collapse nav_level_{0}" id="submenu{1}" role="menu" aria-labelledby="btn-{1}">\n""".format(self.level+1,self.id)
            for item in self.arr:
                if item.__class__==Group:
                    r=r+item.render(userpers, user)
                else:#Action
                    r=r+item.render(userpers, user)
            r=r+"""</ul>\n"""
            r=r+"""</li>\n"""
        return r

    def append(self,o):
        self.arr.append(o)


class Menu:
    def __init__(self, user):
        self.arr=[]
        self.level=None
        self.user=user


    ## Renders an HTML menu
    ## @todo Leave selected current action
    def render(self):
        r="<nav>\n"
        r=r+"""<ul class="nav nav_level_1">\n"""
        for item in self.arr:
            r=r+item.render(self.user.get_all_permissions(), self.user)#Inherited from group and from user)
        r=r+"""</ul>\n"""
        r=r+"</nav>\n"
        r=r+"<p>"
        return r
    

    def append(self,o):
        self.arr.append(o)
        
        

register = template.Library()


@register.simple_tag(takes_context=True)
def mymenu(context):
    """
        books.change_valoration
        books.add_valoration
        books.change_author
        books.add_book
        books.delete_book
        books.change_book
        books.delete_valoration
        books.delete_author
        books.add_author
    """
    user=context['user']
    url_name=context['request'].resolver_match.url_name
    dir(url_name)
    print(url_name)#"home", 
    
    
    menu=Menu(user)
    menu.append(Action(_("Search"), ['books.search_author', 'books.search_book'],  reverse_lazy("home")))
    menu.append(Action(_("All database"), ['database_all_view', ],  reverse_lazy("database")))
    grLibrary=Group(1,_("My Library"),"10")
    grLibrary.append(Action(_("Add author"), ['books.add_author', ], reverse_lazy("author-add")))
    menu.append(Action(_("My valorations"), ['books.search_valoration'], reverse_lazy("valoration-list")))

    grQuerys=Group(1, _("Queries"), "12")
    grQuerys.append(Action(_("Last books"),['books.search_author','books.search_book'], reverse_lazy("query-books-last")))
    grQuerys.append(Action(_("Most valued books"),['books.search_author','books.search_book'], reverse_lazy("query-books-valued")))
    
    
    grQuerys=Group(1, _("Statistics"), "13")
    grQuerys.append(Action(_("Global"),['books.statistics_global',], reverse_lazy("statistics-global")))
    grQuerys.append(Action(_("User"),['books.statistics_user',], reverse_lazy("statistics-user")))
    menu.append(grLibrary)
    menu.append(grQuerys)
    return menu.render()

@register.simple_tag(takes_context=True)
def mypagetitle():
    
    pass


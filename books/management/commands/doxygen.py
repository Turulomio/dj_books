from django.core.management.base import BaseCommand
from os import system, chdir
from books.__init__ import __version__

class Command(BaseCommand):
    help = 'Create doxygen documentation'

    def handle(self, *args, **options):
        system("""sed -i -e "41d" doc/Doxyfile""")#Delete line 41
        system("""sed -i -e "41iPROJECT_NUMBER         = {}" doc/Doxyfile""".format(__version__))#Insert line 41
        chdir("doc")
        system("doxygen Doxyfile")
        system("rsync -avzP -e 'ssh -l turulomio' html/ frs.sourceforge.net:/home/users/t/tu/turulomio/userweb/htdocs/doxygen/dj_books/ --delete-after")
        chdir("..")


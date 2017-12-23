import os
import traceback

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            pwd = os.environ["company_PWD"]
        except KeyError:
            traceback.print_exc()
            pwd = "company"
        try:
            if len(pwd) == 0:
                pwd = "company"
            User.objects.create_user("company", password=pwd)
        except:
            traceback.print_exc()

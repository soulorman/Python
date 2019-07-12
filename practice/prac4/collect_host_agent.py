#encoding: utf-8

from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        conn = redis.StrictRedis(**setting.REDIS)
        while True:
            rt = conn.brpop('', timeout=5)
            print(rt)
from django.db import models
import uuid

class ThreadManager(models.Manager):
    def get_or_create_personal_thread(self, user1, user2):
        pass
        
    def by_user(self, user):
        pass
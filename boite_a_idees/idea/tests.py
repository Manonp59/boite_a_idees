from django.test import TestCase

# Create your tests here.
from .models import Idea

class IdeaModelTest(TestCase):
    
    def test_idea_unique(self):
        idea = Idea(titre="unique-idea")
        idea.save()
    
        duplicate_idea = Idea(titre='unique-idea')
        with self.assertRaises(Exception):
            duplicate_idea.save()
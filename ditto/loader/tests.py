from django.test import TestCase
import os

# Create your tests here.
current_dir = os.path.abspath(__file__)
print(os.path.dirname(current_dir) + '/videostorage')
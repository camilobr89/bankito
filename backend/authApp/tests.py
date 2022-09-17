import json
import jwt

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.

# class TestAPI(TestCase):

#     def test_signUp(self):
#         client = APIClient()
#         response = client.post(
#             '/user/',
#             {
#                 "username": "user_prueba_1",
#                 "password": "password_prueba_1",
#                 "name": "user prueba",
#                 "email": "user_prueba_1@misionTIC.com",
#                 "account": {
#                     "lastChangeDate": "2021-09-23T10:25:43.511Z",
#                     "balance": 20000,
#                     "isActive": "true"
#                 }
#             },
#             format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual('refresh' in response.data.keys(), True)
#         self.assertEqual('access' in response.data.keys(), True)

#     def test_login(self):
#         client = APIClient()
#         response = client.post(
#             '/login/',
#             {
#                 "username":"camilobr89",
#                 "password":"Regedit-1"
#             },
#             format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual('refresh' in response.data.keys(), True)
#         self.assertEqual('access' in response.data.keys(), True)

#     def test_user(self):
#         client = APIClient()

#         token_access = client.post(
#                             '/login/',
#                             {"username":"camilobr89", "password":"Regedit-1"},
#                             format='json'
#                             ).data["access"]

#         secret = 'django-insecure-sks*=(o^!bv)-r6fg+jz0tv@dz_=1+0++(s+ibzk9w*-(=iv4e'
#         user_id = jwt.decode( token_access, secret, algorithms=["HS256"] )["user_id"]

#         url = '/user/'+ str(user_id) + '/'
#         auth_headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token_access,}

#         response = client.get(url, **auth_headers)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["username"], "camilobr89")
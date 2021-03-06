# Copyright 2014 NeuroData (http://neurodata.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from ndauth.authentication import PublicAuthentication
from nduser.models import Dataset
from ndproj.nddataset import NDDataset

# @authentication_classes((SessionAuthentication, TokenAuthentication))
# @permission_classes((IsAuthenticated,))
# class DatasetView(generics.GenericAPIView):
class DatasetView(View):

  def get(self, request, dataset_name):
    try:
      ds = NDDataset.fromName(dataset_name)
      return HttpResponse(ds.serialize(), content_type='application/json')
    except Dataset.DoesNotExist as e:
      return HttpResponseNotFound()
    except Exception as e:
      return HttpResponseBadRequest()

  def post(self, request, dataset_name):
    try:
      ds = NDDataset.fromJson(request.body)
      if request.user.is_authenticated():
        ds.user_id = request.user.id
      else:
        ds.user_id = User.objects.get(username='neurodata').id
      ds.create()
      return HttpResponse(status=201)
    except Exception as e:
      return HttpResponseBadRequest()

  def put(self, request, web_args):
    return NotImplemented

  def delete(self, request, dataset_name):
    try:
      ds = NDDataset.fromName(dataset_name)
      ds.delete()
      return HttpResponse(status=204)
    except Exception as e:
      return HttpResponseBadRequest()

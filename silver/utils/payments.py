# Copyright (c) 2016 Presslabs SRL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import datetime

import jwt

from django.conf import settings
from rest_framework.reverse import reverse


def _get_jwt_token(transaction):
     return jwt.encode({
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        'transaction': str(transaction.uuid)
    }, settings.PAYMENT_METHOD_SECRET)


def get_payment_url(transaction, request):
    kwargs = {'token': str(_get_jwt_token(transaction))}
    return reverse('payment', kwargs=kwargs, request=request)


def get_payment_complete_url(transaction, request):
    kwargs = {'token': str(_get_jwt_token(transaction))}
    return reverse('payment-complete', kwargs=kwargs, request=request)
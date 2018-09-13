# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class WhatsAppBusinessAccount(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isWhatsAppBusinessAccount = True
        super(WhatsAppBusinessAccount, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        analytics = 'analytics'
        business_type = 'business_type'
        currency = 'currency'
        friendly_name = 'friendly_name'
        hsm_namespace = 'hsm_namespace'
        id = 'id'
        on_behalf_of_business_computed_info = 'on_behalf_of_business_computed_info'
        primary_funding_id = 'primary_funding_id'
        status = 'status'
        timezone_id = 'timezone_id'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=WhatsAppBusinessAccount,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_assigned_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.assigneduser import AssignedUser
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AssignedUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AssignedUser, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_hsms(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'tag': 'list<tag_enum>',
            'status': 'list<status_enum>',
            'element': 'string',
            'language': 'list<string>',
            'name_or_element': 'string',
        }
        enums = {
            'tag_enum': [
                'ACCOUNT_UPDATE',
                'PAYMENT_UPDATE',
                'PERSONAL_FINANCE_UPDATE',
                'SHIPPING_UPDATE',
                'RESERVATION_UPDATE',
                'ISSUE_RESOLUTION',
                'APPOINTMENT_UPDATE',
                'TRANSPORTATION_UPDATE',
                'TICKET_UPDATE',
                'ALERT_UPDATE',
            ],
            'status_enum': [
                'APPROVED',
                'PENDING',
                'REJECTED',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/hsms',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_in_progress_on_behalf_request(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessownedobjectonbehalfofrequest import BusinessOwnedObjectOnBehalfOfRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/in_progress_onbehalf_request',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessOwnedObjectOnBehalfOfRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessOwnedObjectOnBehalfOfRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_phone_number_statuses(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/phone_number_statuses',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'analytics': 'Object',
        'business_type': 'string',
        'currency': 'string',
        'friendly_name': 'string',
        'hsm_namespace': 'string',
        'id': 'string',
        'on_behalf_of_business_computed_info': 'Object',
        'primary_funding_id': 'string',
        'status': 'string',
        'timezone_id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info

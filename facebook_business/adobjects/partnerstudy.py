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

class PartnerStudy(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPartnerStudy = True
        super(PartnerStudy, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        additional_info = 'additional_info'
        brand = 'brand'
        client_name = 'client_name'
        emails = 'emails'
        id = 'id'
        input_ids = 'input_ids'
        is_export = 'is_export'
        lift_study = 'lift_study'
        location = 'location'
        match_file_ds = 'match_file_ds'
        name = 'name'
        partner_defined_id = 'partner_defined_id'
        partner_household_graph_dataset_id = 'partner_household_graph_dataset_id'
        status = 'status'
        study_end_date = 'study_end_date'
        study_start_date = 'study_start_date'
        study_type = 'study_type'
        submit_date = 'submit_date'

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
            target_class=PartnerStudy,
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

    def get_partners(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adsdatapartner import AdsDataPartner
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/partners',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsDataPartner,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsDataPartner, api=self._api),
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

    def get_submitters(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/submitters',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=User,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=User, api=self._api),
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
        'additional_info': 'string',
        'brand': 'string',
        'client_name': 'string',
        'emails': 'string',
        'id': 'string',
        'input_ids': 'list<string>',
        'is_export': 'bool',
        'lift_study': 'AdStudy',
        'location': 'string',
        'match_file_ds': 'string',
        'name': 'string',
        'partner_defined_id': 'string',
        'partner_household_graph_dataset_id': 'string',
        'status': 'string',
        'study_end_date': 'datetime',
        'study_start_date': 'datetime',
        'study_type': 'string',
        'submit_date': 'datetime',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info

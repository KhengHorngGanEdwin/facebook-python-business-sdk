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

class AdAccountUserSettings(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountUserSettings = True
        super(AdAccountUserSettings, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_account = 'ad_account'
        ad_object_export_format = 'ad_object_export_format'
        auto_review_video_caption = 'auto_review_video_caption'
        column_suggestion_status = 'column_suggestion_status'
        default_account_overview_agegender_metrics = 'default_account_overview_agegender_metrics'
        default_account_overview_location_metrics = 'default_account_overview_location_metrics'
        default_account_overview_metrics = 'default_account_overview_metrics'
        default_account_overview_time_metrics = 'default_account_overview_time_metrics'
        default_builtin_column_preset = 'default_builtin_column_preset'
        default_nam_time_range = 'default_nam_time_range'
        draft_mode_enabled = 'draft_mode_enabled'
        export_deleted_items_with_delivery = 'export_deleted_items_with_delivery'
        export_summary_row = 'export_summary_row'
        id = 'id'
        last_used_columns = 'last_used_columns'
        last_used_pe_filters = 'last_used_pe_filters'
        rb_export_format = 'rb_export_format'
        rb_export_raw_data = 'rb_export_raw_data'
        rb_export_summary_row = 'rb_export_summary_row'
        show_archived_data = 'show_archived_data'
        user = 'user'

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
            target_class=AdAccountUserSettings,
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

    def get_column_presets(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/column_presets',
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

    def get_filters(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/filters',
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
        'ad_account': 'AdAccount',
        'ad_object_export_format': 'string',
        'auto_review_video_caption': 'bool',
        'column_suggestion_status': 'string',
        'default_account_overview_agegender_metrics': 'list<string>',
        'default_account_overview_location_metrics': 'list<string>',
        'default_account_overview_metrics': 'list<string>',
        'default_account_overview_time_metrics': 'list<string>',
        'default_builtin_column_preset': 'string',
        'default_nam_time_range': 'string',
        'draft_mode_enabled': 'bool',
        'export_deleted_items_with_delivery': 'bool',
        'export_summary_row': 'bool',
        'id': 'string',
        'last_used_columns': 'Object',
        'last_used_pe_filters': 'list<Object>',
        'rb_export_format': 'string',
        'rb_export_raw_data': 'bool',
        'rb_export_summary_row': 'bool',
        'show_archived_data': 'bool',
        'user': 'User',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info

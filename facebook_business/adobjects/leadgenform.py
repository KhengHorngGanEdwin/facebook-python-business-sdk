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

class LeadgenForm(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isLeadgenForm = True
        super(LeadgenForm, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        allow_organic_lead = 'allow_organic_lead'
        block_display_for_non_targeted_viewer = 'block_display_for_non_targeted_viewer'
        context_card = 'context_card'
        created_time = 'created_time'
        creator = 'creator'
        creator_id = 'creator_id'
        cusomized_tcpa_content = 'cusomized_tcpa_content'
        expired_leads_count = 'expired_leads_count'
        extra_details = 'extra_details'
        follow_up_action_text = 'follow_up_action_text'
        follow_up_action_url = 'follow_up_action_url'
        id = 'id'
        is_optimized_for_quality = 'is_optimized_for_quality'
        leadgen_export_csv_url = 'leadgen_export_csv_url'
        leads_count = 'leads_count'
        legal_content = 'legal_content'
        locale = 'locale'
        messenger_welcome_message = 'messenger_welcome_message'
        name = 'name'
        organic_leads_count = 'organic_leads_count'
        page = 'page'
        page_id = 'page_id'
        privacy_policy_url = 'privacy_policy_url'
        qualifiers = 'qualifiers'
        question_page_custom_headline = 'question_page_custom_headline'
        questions = 'questions'
        status = 'status'
        tcpa_compliance = 'tcpa_compliance'
        thank_you_page = 'thank_you_page'
        tracking_parameters = 'tracking_parameters'

    class Locale:
        en_us = 'EN_US'
        it_it = 'IT_IT'
        fr_fr = 'FR_FR'
        es_es = 'ES_ES'
        es_la = 'ES_LA'
        de_de = 'DE_DE'
        en_gb = 'EN_GB'
        pt_br = 'PT_BR'
        zh_tw = 'ZH_TW'
        zh_hk = 'ZH_HK'
        tr_tr = 'TR_TR'
        ar_ar = 'AR_AR'
        cs_cz = 'CS_CZ'
        da_dk = 'DA_DK'
        fi_fi = 'FI_FI'
        he_il = 'HE_IL'
        hi_in = 'HI_IN'
        hu_hu = 'HU_HU'
        id_id = 'ID_ID'
        ja_jp = 'JA_JP'
        ko_kr = 'KO_KR'
        nb_no = 'NB_NO'
        nl_nl = 'NL_NL'
        pl_pl = 'PL_PL'
        pt_pt = 'PT_PT'
        ro_ro = 'RO_RO'
        ru_ru = 'RU_RU'
        sv_se = 'SV_SE'
        th_th = 'TH_TH'
        vi_vn = 'VI_VN'
        zh_cn = 'ZH_CN'

    class Status:
        active = 'ACTIVE'
        archived = 'ARCHIVED'
        deleted = 'DELETED'
        draft = 'DRAFT'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'leadgen_forms'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
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
            target_class=LeadgenForm,
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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'context_card_id': 'string',
            'legal_content_id': 'string',
            'locale': 'locale_enum',
            'name': 'string',
            'questions': 'list<Object>',
            'status': 'status_enum',
            'thank_you_page_id': 'string',
        }
        enums = {
            'locale_enum': LeadgenForm.Locale.__dict__.values(),
            'status_enum': LeadgenForm.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadgenForm,
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

    def get_ad_sets(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'query': 'string',
            'campaign': 'string',
            'adsets': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adsets',
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

    def get_campaigns(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'query': 'string',
            'campaigns': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/campaigns',
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

    def get_leads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.lead import Lead
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Lead,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Lead, api=self._api),
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

    def create_lead(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.lead import Lead
        param_types = {
            'start_time': 'datetime',
            'end_time': 'datetime',
            'session_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Lead,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Lead, api=self._api),
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

    def get_test_leads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.lead import Lead
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/test_leads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Lead,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Lead, api=self._api),
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

    def create_test_lead(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.lead import Lead
        param_types = {
            'field_data': 'list<Object>',
            'custom_disclaimer_responses': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/test_leads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Lead,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Lead, api=self._api),
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
        'allow_organic_lead': 'bool',
        'block_display_for_non_targeted_viewer': 'bool',
        'context_card': 'LeadGenContextCard',
        'created_time': 'datetime',
        'creator': 'User',
        'creator_id': 'int',
        'cusomized_tcpa_content': 'string',
        'expired_leads_count': 'unsigned int',
        'extra_details': 'list<string>',
        'follow_up_action_text': 'string',
        'follow_up_action_url': 'string',
        'id': 'string',
        'is_optimized_for_quality': 'bool',
        'leadgen_export_csv_url': 'string',
        'leads_count': 'unsigned int',
        'legal_content': 'LeadGenLegalContent',
        'locale': 'string',
        'messenger_welcome_message': 'string',
        'name': 'string',
        'organic_leads_count': 'unsigned int',
        'page': 'Page',
        'page_id': 'string',
        'privacy_policy_url': 'string',
        'qualifiers': 'list<LeadGenQualifier>',
        'question_page_custom_headline': 'string',
        'questions': 'list<LeadGenQuestion>',
        'status': 'string',
        'tcpa_compliance': 'bool',
        'thank_you_page': 'Object',
        'tracking_parameters': 'list<Object>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Locale'] = LeadgenForm.Locale.__dict__.values()
        field_enum_info['Status'] = LeadgenForm.Status.__dict__.values()
        return field_enum_info

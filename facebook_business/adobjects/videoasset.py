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

class VideoAsset(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isVideoAsset = True
        super(VideoAsset, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        broadcast_id = 'broadcast_id'
        broadcast_planned_start_time = 'broadcast_planned_start_time'
        can_viewer_edit = 'can_viewer_edit'
        created_time = 'created_time'
        creator = 'creator'
        description = 'description'
        download_hd_url = 'download_hd_url'
        download_sd_url = 'download_sd_url'
        embeddable = 'embeddable'
        expiration = 'expiration'
        feed_type = 'feed_type'
        id = 'id'
        is_crossposting_eligible = 'is_crossposting_eligible'
        is_crossposting_within_bm_eligible = 'is_crossposting_within_bm_eligible'
        is_crossposting_within_bm_enabled = 'is_crossposting_within_bm_enabled'
        is_episode = 'is_episode'
        is_featured = 'is_featured'
        is_live_premiere = 'is_live_premiere'
        is_video_asset = 'is_video_asset'
        last_added_time = 'last_added_time'
        latest_creator = 'latest_creator'
        latest_owned_description = 'latest_owned_description'
        latest_owned_title = 'latest_owned_title'
        length = 'length'
        live_status = 'live_status'
        no_story = 'no_story'
        owner_name = 'owner_name'
        owner_picture = 'owner_picture'
        owner_post_state = 'owner_post_state'
        permalink_url = 'permalink_url'
        picture = 'picture'
        posts_count = 'posts_count'
        posts_ids = 'posts_ids'
        posts_status = 'posts_status'
        published = 'published'
        scheduled_publish_time = 'scheduled_publish_time'
        secret = 'secret'
        secure_stream_url = 'secure_stream_url'
        social_actions = 'social_actions'
        status = 'status'
        stream_url = 'stream_url'
        thumbnail_while_encoding = 'thumbnail_while_encoding'
        title = 'title'
        views = 'views'

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
            target_class=VideoAsset,
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

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, pending=False):
        from facebook_business.adobjects.insightsresult import InsightsResult
        if is_async:
          return self.get_insights_async(fields, params, batch, pending)
        param_types = {
            'metric': 'list<metric_enum>',
            'period': 'period_enum',
        }
        enums = {
            'metric_enum': InsightsResult.Metric.__dict__.values(),
            'period_enum': InsightsResult.Period.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InsightsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InsightsResult, api=self._api),
            include_summary=False,
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

    def get_video_stats(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videostats import VideoStats
        param_types = {
            'metrics': 'list<metrics_enum>',
            'page_list': 'list<string>',
            'requested_fields': 'list<requested_fields_enum>',
            'since': 'datetime',
            'until': 'datetime',
            'unified_metrics_list': 'list<map>',
        }
        enums = {
            'metrics_enum': VideoStats.Metrics.__dict__.values(),
            'requested_fields_enum': VideoStats.RequestedFields.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/video_stats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoStats,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoStats, api=self._api),
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

    def get_videos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/videos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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
        'broadcast_id': 'string',
        'broadcast_planned_start_time': 'datetime',
        'can_viewer_edit': 'bool',
        'created_time': 'datetime',
        'creator': 'User',
        'description': 'string',
        'download_hd_url': 'string',
        'download_sd_url': 'string',
        'embeddable': 'bool',
        'expiration': 'Object',
        'feed_type': 'string',
        'id': 'string',
        'is_crossposting_eligible': 'bool',
        'is_crossposting_within_bm_eligible': 'bool',
        'is_crossposting_within_bm_enabled': 'bool',
        'is_episode': 'bool',
        'is_featured': 'bool',
        'is_live_premiere': 'bool',
        'is_video_asset': 'bool',
        'last_added_time': 'datetime',
        'latest_creator': 'User',
        'latest_owned_description': 'string',
        'latest_owned_title': 'string',
        'length': 'float',
        'live_status': 'string',
        'no_story': 'bool',
        'owner_name': 'string',
        'owner_picture': 'string',
        'owner_post_state': 'string',
        'permalink_url': 'string',
        'picture': 'string',
        'posts_count': 'unsigned int',
        'posts_ids': 'list<string>',
        'posts_status': 'Object',
        'published': 'bool',
        'scheduled_publish_time': 'datetime',
        'secret': 'bool',
        'secure_stream_url': 'string',
        'social_actions': 'bool',
        'status': 'Object',
        'stream_url': 'string',
        'thumbnail_while_encoding': 'string',
        'title': 'string',
        'views': 'unsigned int',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info

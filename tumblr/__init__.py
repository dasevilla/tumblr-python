import json
import logging
import oauth2 as oauth
import urllib
import urlparse


class TumblrClient(object):
    """A Python client for accessing the Tumblr v2 API"""

    API_SCHEME = 'http'
    API_HOST = 'api.tumblr.com'

    BLOG_URLS = {
        'info': '/v2/blog/%(hostname)s/info',
        'avatar': '/v2/blog/%(hostname)s/avatar',
        'avatar/size': '/v2/blog/%(hostname)s/avatar/%(size)s',
        'followers': '/v2/blog/%(hostname)s/followers',
        'posts': '/v2/blog/%(hostname)s/posts',
        'posts/type': '/v2/blog/%(hostname)s/posts/%(type)s',
        'queue': '/v2/blog/%(hostname)s/posts/queue',
        'draft': '/v2/blog/%(hostname)s/posts/draft',
        'submission': '/v2/blog/%(hostname)s/posts/submission',
        'post': '/v2/blog/%(hostname)s/post',
        'edit': '/v2/blog/%(hostname)s/post/edit',
        'reblog': '/v2/blog/%(hostname)s/post/reblog',
        'delete': '/v2/blog/%(hostname)s/post/delete',
    }

    def __init__(self, hostname, consumer, token=None):
        self.hostname = hostname
        self.consumer = consumer
        self.token = token

    def get_api_key(self):
        return self.consumer.key

    def build_api_key_url(self, format_string, format_params={},
        query_params={}):
        """Builds a URL and adds the client's API key"""
        if 'api_key' not in query_params:
            query_params['api_key'] = self.get_api_key()
        return self.build_url(format_string, format_params, query_params)

    def build_url(self, format_string, format_params={}, query_params={}):
        if 'hostname' not in format_params:
            format_params['hostname'] = self.hostname
        path = format_string % format_params
        query_string = urllib.urlencode(query_params)

        parsed_url = urlparse.SplitResult(scheme=self.API_SCHEME,
            netloc=self.API_HOST, path=path, query=query_string,
            fragment=None)

        request_url = urlparse.urlunsplit(parsed_url)

        logging.debug('Built URL: %s ' % request_url)

        return request_url

    def make_unauthorized_request(self, request_url):
        response = urllib.urlopen(request_url)

        try:
            json_response = json.load(response)
        except ValueError, e:
            logging.error('Invalid response: %s (%d)' % (e,
                response.getcode()))
            return None

        return json_response

    def make_oauth_request(self, request_url, method='GET', body=None):
        if not self.consumer or not self.token:
            logging.error('Missing OAuth credentials')
            return None

        oauth_client = oauth.Client(self.consumer, self.token)
        if body:
            response, content = oauth_client.request(request_url, method,
                body)
        else:
            response, content = oauth_client.request(request_url, method)

        try:
            json_response = json.loads(content)
        except ValueError, e:
            logging.error('Invalid response: %s (%s)' % (e,
                response['status']))
            return None

        return json_response

    def get_blog_info(self):
        request_url = self.build_api_key_url(self.BLOG_URLS['info'])
        return self.make_unauthorized_request(request_url)

    def get_blog_posts(self, post_type=None, request_params={}):
        if post_type:
            format_params = {
                'type': post_type,
            }
            request_url = self.build_api_key_url(self.BLOG_URLS['posts/type'],
                format_params=format_params, query_params=request_params)
        else:
            request_url = self.build_api_key_url(self.BLOG_URLS['posts'],
                query_params=request_params)

        return self.make_unauthorized_request(request_url)

    def get_blog_avatar_url(self, size=None):
        if size:
            format_params = {
                'size': size,
            }
            return self.build_url(self.BLOG_URLS['avatar/size'],
                format_params=format_params)
        else:
            return self.build_url(self.BLOG_URLS['avatar'])

    def get_blog_followers(self, request_params={}):
        request_url = self.build_api_key_url(self.BLOG_URLS['followers'],
            query_params=request_params)

        return self.make_oauth_request(request_url)

    def get_blog_queue(self, request_params={}):
        request_url = self.build_api_key_url(self.BLOG_URLS['queue'],
            query_params=request_params)

        return self.make_oauth_request(request_url)

    def get_blog_drafts(self, request_params={}):
        request_url = self.build_api_key_url(self.BLOG_URLS['draft'],
            query_params=request_params)

        return self.make_oauth_request(request_url)

    def get_blog_submissions(self, request_params={}):
        request_url = self.build_api_key_url(self.BLOG_URLS['submission'],
            query_params=request_params)

        return self.make_oauth_request(request_url)

    def create_post(self, request_params={}):
        request_url = self.build_url(self.BLOG_URLS['post'])

        return self.make_oauth_request(request_url, method='POST',
            body=urllib.urlencode(request_params))

    def edit_post(self, post_id, request_params={}):
        request_url = self.build_url(self.BLOG_URLS['edit'])

        if 'id' not in request_params:
            request_params['id'] = post_id

        return self.make_oauth_request(request_url, method='POST',
            body=urllib.urlencode(request_params))

    def reblog_post(self, reblog_key, request_params={}):
        request_url = self.build_url(self.BLOG_URLS['edit'])

        if 'reblog_key' not in request_params:
            request_params['reblog_key'] = reblog_key

        return self.make_oauth_request(request_url, method='POST',
            body=urllib.urlencode(request_params))

    def delete_post(self, post_id):
        request_url = self.build_url(self.BLOG_URLS['delete'])

        request_params = {
            'id': post_id,
        }

        return self.make_oauth_request(request_url, method='POST',
            body=urllib.urlencode(request_params))

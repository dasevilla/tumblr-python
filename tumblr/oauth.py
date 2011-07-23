import urlparse
import oauth2 as oauth


class TumblrOAuthClient(object):
    REQUEST_TOKEN_URL = 'https://www.tumblr.com/oauth/request_token'
    AUTHORIZE_URL = 'https://www.tumblr.com/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://www.tumblr.com/oauth/access_token'
    XAUTH_ACCESS_TOKEN_URL = 'https://www.tumblr.com/oauth/access_token'

    def __init__(self, consumer_key, consumer_secret):
        self.consumer = oauth.Consumer(consumer_key, consumer_secret)

    def get_authorize_url(self):
        client = oauth.Client(self.consumer)
        resp, content = client.request(self.REQUEST_TOKEN_URL, "GET")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])

        self.request_token = dict(urlparse.parse_qsl(content))
        return "%s?oauth_token=%s" % (self.AUTHORIZE_URL,
            self.request_token['oauth_token'])

    def get_access_token(self, oauth_verifier):
        token = oauth.Token(self.request_token['oauth_token'],
            self.request_token['oauth_token_secret'])
        token.set_verifier(oauth_verifier)
        client = oauth.Client(self.consumer, token)

        resp, content = client.request(self.ACCESS_TOKEN_URL, "POST")
        access_token = dict(urlparse.parse_qsl(content))

        return oauth.Token(access_token['oauth_token'],
            access_token['oauth_token_secret'])

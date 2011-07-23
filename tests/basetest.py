import unittest
import oauth2 as oauth

from tumblr import TumblrClient

import config


class BaseTestCase(unittest.TestCase):
    VALID_RESPONSE_CODES = [200, 201, 404]

    def setUp(self):
        hostname = config.TEST_HOSTNAME
        consumer = oauth.Consumer(config.TEST_CONSUMER_KEY,
            config.TEST_CONSUMER_SECRET)
        token = oauth.Token(config.TEST_ACCESS_KEY,
            config.TEST_ACCESS_SECRET)

        self.client = TumblrClient(hostname, consumer, token)

    def assertSuccessResponse(self, json_response):
        self.assertIsNotNone(json_response, 'Response should not be None')
        response_code = json_response['meta']['status']
        self.assertIn(response_code, self.VALID_RESPONSE_CODES)

import unittest

import basetest


class TestGetPost(basetest.BaseTestCase):

    def test_get_posts(self):
        json_response = self.client.get_blog_posts()
        self.assertSuccessResponse(json_response)

    def test_get_text_post(self):
        json_response = self.client.get_blog_posts(post_type='text')
        self.assertSuccessResponse(json_response)

    def test_get_quote_post(self):
        json_response = self.client.get_blog_posts(post_type='quote')
        self.assertSuccessResponse(json_response)

    def test_get_link_post(self):
        json_response = self.client.get_blog_posts(post_type='link')
        self.assertSuccessResponse(json_response)

    def test_get_answer_post(self):
        json_response = self.client.get_blog_posts(post_type='answer')
        self.assertSuccessResponse(json_response)

    def test_get_video_post(self):
        json_response = self.client.get_blog_posts(post_type='video')
        self.assertSuccessResponse(json_response)

    def test_get_audio_post(self):
        json_response = self.client.get_blog_posts(post_type='audio')
        self.assertSuccessResponse(json_response)

    def test_get_photo_post(self):
        json_response = self.client.get_blog_posts(post_type='photo')
        self.assertSuccessResponse(json_response)

    def test_post_limit(self):
        params = {
            'limit': 1
        }
        json_response = self.client.get_blog_posts(request_params=params)
        self.assertSuccessResponse(json_response)

    def test_post_format(self):
        params = {
            'format': 'raw'
        }
        json_response = self.client.get_blog_posts(request_params=params)
        self.assertSuccessResponse(json_response)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestGetPost)


if __name__ == '__main__':
    unittest.main()

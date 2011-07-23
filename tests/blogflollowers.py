import unittest

import basetest


class TestBlogFollowers(basetest.BaseTestCase):

    def test_get_blog_followers(self):
        json_response = self.client.get_blog_followers()
        self.assertSuccessResponse(json_response)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBlogFollowers)


if __name__ == '__main__':
    unittest.main()

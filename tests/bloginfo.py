import unittest

import basetest


class TestBlogInfo(basetest.BaseTestCase):

    def test_blog_info(self):
        json_response = self.client.get_blog_info()
        self.assertSuccessResponse(json_response)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBlogInfo)


if __name__ == '__main__':
    unittest.main()

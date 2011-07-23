import unittest

import basetest


class TestBlogSubmissions(basetest.BaseTestCase):

    def test_blog_info(self):
        json_response = self.client.get_blog_submissions()
        self.assertSuccessResponse(json_response)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBlogSubmissions)


if __name__ == '__main__':
    unittest.main()

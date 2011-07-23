import unittest

import basetest


class TestBlogQueue(basetest.BaseTestCase):

    def test_get_blog_queue(self):
        json_response = self.client.get_blog_queue()
        self.assertSuccessResponse(json_response)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBlogQueue)


if __name__ == '__main__':
    unittest.main()

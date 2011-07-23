import unittest

import basetest


class TestBlogDrafts(basetest.BaseTestCase):

    def test_get_blog_drafts(self):
        json_response = self.client.get_blog_drafts()
        self.assertSuccessResponse(json_response)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBlogDrafts)


if __name__ == '__main__':
    unittest.main()

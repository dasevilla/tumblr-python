import unittest

import basetest


class TestBlogAvatar(basetest.BaseTestCase):

    def test_get_avatar(self):
        url = self.client.get_blog_avatar_url()
        self.assertRegexpMatches(url, '/avatar$')

    def test_get_16(self):
        url = self.client.get_blog_avatar_url(size=16)
        self.assertRegexpMatches(url, '/avatar/16$')

    def test_get_24(self):
        url = self.client.get_blog_avatar_url(size=24)
        self.assertRegexpMatches(url, '/avatar/24$')

    def test_get_30(self):
        url = self.client.get_blog_avatar_url(size=30)
        self.assertRegexpMatches(url, '/avatar/30$')

    def test_get_40(self):
        url = self.client.get_blog_avatar_url(size=40)
        self.assertRegexpMatches(url, '/avatar/40$')

    def test_get_48(self):
        url = self.client.get_blog_avatar_url(size=48)
        self.assertRegexpMatches(url, '/avatar/48$')

    def test_get_64(self):
        url = self.client.get_blog_avatar_url(size=64)
        self.assertRegexpMatches(url, '/avatar/64$')

    def test_get_96(self):
        url = self.client.get_blog_avatar_url(size=96)
        self.assertRegexpMatches(url, '/avatar/96$')

    def test_get_128(self):
        url = self.client.get_blog_avatar_url(size=128)
        self.assertRegexpMatches(url, '/avatar/128$')

    def test_get_512(self):
        url = self.client.get_blog_avatar_url(size=512)
        self.assertRegexpMatches(url, '/avatar/512$')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBlogAvatar)


if __name__ == '__main__':
    unittest.main()

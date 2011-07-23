import unittest

import basetest


class TestPostCreate(basetest.BaseTestCase):

    def test_create_text(self):
        params = {
            'type': 'text',
            'title': 'Sample text title',
            'body': 'Sample text body',
        }
        json_response = self.client.create_post(request_params=params)
        self.assertSuccessResponse(json_response)

    def test_create_draft(self):
        params = {
            'type': 'text',
            'title': 'Sample text draft title',
            'body': 'Sample text draft body',
            'status': 'draft',
        }
        json_response = self.client.create_post(request_params=params)
        self.assertSuccessResponse(json_response)

    def test_create_queue(self):
        params = {
            'type': 'text',
            'title': 'Sample text queue title',
            'body': 'Sample text queue body',
            'status': 'queue',
        }
        json_response = self.client.create_post(request_params=params)
        self.assertSuccessResponse(json_response)

    def test_create_tags(self):
        params = {
            'type': 'text',
            'title': 'Sample tag title',
            'body': 'Sample tag body',
            'tags': 'test, sample, example',
        }
        json_response = self.client.create_post(request_params=params)
        self.assertSuccessResponse(json_response)

    def test_create_quote(self):
        params = {
            'type': 'quote',
            'quote': 'Sample quote',
            'source': 'Sample quote source',
        }
        json_response = self.client.create_post(request_params=params)
        self.assertSuccessResponse(json_response)

    def test_create_link(self):
        params = {
            'type': 'link',
            'title': 'Sample link title',
            'description': 'Sample link description',
            'url': 'http://www.example.com/',
        }
        json_response = self.client.create_post(request_params=params)
        self.assertSuccessResponse(json_response)

    def test_create_chat(self):
        params = {
            'type': 'chat',
            'title': 'Sample chat title',
            'conversation': 'Sample chat conversation',
        }
        json_response = self.client.create_post(request_params=params)
        self.assertSuccessResponse(json_response)

    def test_create_audio_url(self):
        params = {
            'type': 'audio',
            'caption': 'Sample audio caption',
            'external_url': 'http://www.example.com/test.mp3',
        }
        json_response = self.client.create_post(request_params=params)
        self.assertSuccessResponse(json_response)

    # def test_create_video_embed(self):
    #     params = {
    #         'type': 'video',
    #         'caption': 'Sample video caption',
    #         'embed': '<iframe width="560" height="349" \
    #              src="http://www.youtube.com/embed/9JTcHtNMl8s" \
    #              frameborder="0" \
    #              allowfullscreen></iframe>',
    #     }
    #     json_response = self.client.create_post(request_params=params)
    #     self.assertSuccessResponse(json_response)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPostCreate)


if __name__ == '__main__':
    unittest.main()

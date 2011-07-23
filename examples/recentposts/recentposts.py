import oauth2 as oauth

from tumblr import TumblrClient


def lister(client, count, params={}):
    client.get_blog_posts()

    total = 0
    while True:
        print "making a request"
        params['offset'] = total
        json_response = client.get_blog_posts(request_params=params)
        for post in json_response['response']['posts']:
            total += 1
            if total > count:
                raise StopIteration
            yield post


def main():
    hostname = 'EXAMPLE.tumblr.com'

    consumer_key = 'API_KEY'
    consumer_secret = 'API_SECRET'

    access_key = 'ACCESS_KEY'
    access_secret = 'ACCESS_KEY'

    consumer = oauth.Consumer(consumer_key, consumer_secret)
    token = oauth.Token(access_key, access_secret)

    params = {
        'type': 'quote',
    }

    client = TumblrClient(hostname, consumer, token)
    for post in lister(client, 10, params):
        print post['id']


if __name__ == '__main__':
    main()

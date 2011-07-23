from tumblr.oauth import TumblrOAuthClient


def main():
    consumer_key = 'API_KEY'
    consumer_secret = 'API_SECRET'

    tumblr_oauth = TumblrOAuthClient(consumer_key, consumer_secret)

    authorize_url = tumblr_oauth.get_authorize_url()
    print "Visit: %s" % authorize_url

    oauth_verifier = raw_input('What is the oauth_verifier?')
    access_token = tumblr_oauth.get_access_token(oauth_verifier)
    print "Access key:", access_token.key
    print "Access Secret:", access_token.secret


if __name__ == '__main__':
    main()

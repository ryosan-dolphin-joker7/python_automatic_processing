import tweepy

# 以下にTwitter APIの認証情報を記述 --- (*1)
api_key = 'm8aIkLUtTuo94zNiMnNN6zdov'
api_secret = '4h8WzEi0IpJYrEildgKRgYSf9ErY6C95xq46J0aXIZZItbzJIo'
access_token = '6739522-HXU3oPmoS1hP0KGBHBdNS5JnenMlwvV90wfFsEQDPs'
access_secret = 'HeV7WnSqAP1phthNdF1Sva805noJZlhil3qbwVU6u5W50'

# Twitterオブジェクトの生成 --- (*2)
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# 任意のメッセージを投稿 --- (*3)
api.update_status('@kujirahand Pythonの本買ったよ')


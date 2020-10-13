import requests
import json

#Insert facebook token here
access_token = "EAAFVAZAv5s34BACUGzc03N5QbVVzmZAkfUPOohB2GEE0QZCDZANPnDHj117WYYVzKOXmbtHZAELkyDJqVZCXm8ZBMp8eHVZC57ZAQNuLtR8yRw94liS7Xb6Jvv2PRtgKZAUzWyjBkSuQgrv29pqjJDaltJniqnrNiIJXxC8e6YNZB0vA0h7MAZB7fSdGgvpOo6yhSx4IjEcVhPFPi3CMBhtsPTWZBGY2mBy8XLs5NxYAKb9hHE8gsA90Hkpfc"

def comment_on_posts(posts, amount):
    counter = 0
    for post in posts:
        if counter >= amount:
            break
        else:
            counter = counter + 1
        url = "https://graph.facebook.com/{0}/comments".format(post['id'])
        message = "Hi bro!"
        parameters = {'access_token' : access_token, 'message' : message}
        s = requests.post(url, data = parameters)

def get_posts():
    payload = {'access_token' : access_token}
    r = requests.get('https://graph.facebook.com/me/feed', params=payload)
    result = json.loads(r.text)
    return result['data']

if __name__ == "__main__":
    print('Hello')
    posts = get_posts()
    comment_on_posts(posts, 10)
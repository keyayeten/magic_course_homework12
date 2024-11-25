import requests

base_url = 'http://127.0.0.1:8000/'

class Avtorizacia:
    @staticmethod
    def avrorizacia_user():
        path_post = 'auth/jwt/create/'
        json_p = {
            "username": "dasha20",
            "password": "2345670dima"
            }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        post_url = base_url + path_post
        res_post = requests.post(post_url, headers=headers, json=json_p)
        print(res_post.text)
        return res_post
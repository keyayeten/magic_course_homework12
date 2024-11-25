import requests

base_url = 'http://127.0.0.1:8000/'

class Ragister:
    @staticmethod
    def register_user():
        path_post = 'auth/users/'
        json_p = {
            "email": "dasha20@yandex.ru",
            "username": "dasha20",
            "password": "2345670dima",
            "re_password": "2345670dima"
            }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        post_url = base_url + path_post
        res_post = requests.post(post_url, headers=headers, json=json_p)
        check_post = res_post.json()
        return res_post







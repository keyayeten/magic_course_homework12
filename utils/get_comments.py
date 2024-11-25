import requests



base_url = 'http://127.0.0.1:8000/'
class GetLstPost:
    @staticmethod
    def get_lst_posts_user(authorization):
        path_get = 'api/posts/32/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }

        get_url = base_url + path_get
        res_get = requests.get(get_url, headers=headers)
        print(res_get.text)
        return res_get
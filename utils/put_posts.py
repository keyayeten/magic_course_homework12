import requests



base_url = 'http://127.0.0.1:8000/'
class PutPosts:
    @staticmethod
    def put_lst_posts(authorization, id):
        path_put = f'api/posts/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }
        json_body = {
            "title": "Petter",
            "content": "50"
        }
        put_url = base_url + path_put
        res_put = requests.put(put_url, headers=headers, json=json_body)
        print(res_put.text)
        return res_put
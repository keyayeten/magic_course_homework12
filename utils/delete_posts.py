import requests



base_url = 'http://127.0.0.1:8000/'
class DeletePosts:
    @staticmethod
    def delete_lst_posts(authorization, id):
        path_delete = f'api/posts/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }
        delete_url = base_url + path_delete
        res_delete = requests.delete(delete_url, headers=headers)
        print(res_delete.text)
        return res_delete
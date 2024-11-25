import json

from utils.regisr_user import Ragister
from utils.avtoriz_user import Avtorizacia
from utils.lst_posts import LstPost
from utils.created_posts import CreatedLstPost
from utils.created_comments import CreatedComments
from utils.get_comments import GetLstPost
from utils.put_posts import PutPosts
from utils.delete_posts import DeletePosts


class Test_user():
    # def test_reg(self):
    #     res_post = Ragister.register_user()
    #     check_post = res_post.json()
    #     if res_post.status_code == 201:
    #         print('Регистрация прошла успешна')
    #     else:
    #         print('Ошибка регистрации')

    def test_avtorizacia_user(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        # res = check_post.get("access")
        # print(res)
        if res_post.status_code == 200:
            print('Авторизация прошла успешна')
        else:
            print('Авторизация прошла не успешна')

    def test_lst_stat(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_get = LstPost.lst_posts_user(res)
        lst_stat = res_get.text
        print(res_get.json())
        if res_get.status_code == 200:
            print('Список статей найден')
        else:
            print('Список статей не найден')

    def test_created_lst_stat(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_post = CreatedLstPost.created_lst_posts_user(res)
        lst_stat = res_post.text
        print(res_post.json())
        if res_post.status_code == 201:
            print('Статья создана')
        else:
            print('Ошибка')

    def test_created_comments(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_post_2 = CreatedLstPost.created_lst_posts_user(res)
        check_post_2 = res_post_2.json()
        ids = check_post_2.get("id")
        res_posts = CreatedComments.created_comments(res, ids)
        lst_stat = res_posts.text
        print(res_posts.json())
        if res_posts.status_code == 201:
            print('Комментарий создан')
        else:
            print('Ошибка')


    def test_get_comments(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_gets = GetLstPost.get_lst_posts_user(res)
        lst_stat = res_gets.text
        print(res_gets.json())
        if res_gets.status_code == 200:
            print('Список комментариев получен')
        else:
            print('Списка нет')


    def test_put_user_posts(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_post_2 = CreatedLstPost.created_lst_posts_user(res)
        c = res_post_2.json()
        res_2 = c.get("id")
        res_put = PutPosts.put_lst_posts(res, res_2)
        print(res_put.json())
        if res_put.status_code == 200:
            print('Пост обновлен')
        else:
            print('Ошибка обновления')


    def test_delete_user_posts(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_post_2 = CreatedLstPost.created_lst_posts_user(res)
        c = res_post_2.json()
        res_2 = c.get("id")
        res_delete = DeletePosts.delete_lst_posts(res, res_2)
        print(res_delete.text)
        if res_delete.status_code == 204:
            print('Пост удален')
        else:
            print('Ошибка удаления поста')




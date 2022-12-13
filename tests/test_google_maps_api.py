import json
import allure
from utils.api import Google_maps_api
from utils.checking import Checking

"""Creation, change, deleting a new location"""
@allure.epic("Test create new location")
class Test_create_place():

    @allure.description("Test create, update, delete new location")
    def test_create_new_place(self):

        print("Method POST")
        result_post = Google_maps_api.creat_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        print(result_post.status_code)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)  # get list of fields
        # print(list(token))
        Checking.check_json_value(result_post, 'status', 'OK')


        print("Method GET checking POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        # token = json.loads(result_get.text)  # get list of fields
        # print(list(token))
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')


        print("Method PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        print(result_put.status_code)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')


        print("Method GET - checking PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        # check_put = result_get.json()
        # check_address = check_put.get("address")
        # new_address = "100 Lenina street, RU"
        # assert check_address == new_address

        print("Method DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        print(result_delete.status_code)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Method GET - checking DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        print(result_get.status_code)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_word_in_value(result_get, 'msg', 'failed')


        print("Test for create, put, delete is PASSED")


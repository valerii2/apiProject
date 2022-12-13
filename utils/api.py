from utils.http_methods import Http_methods

"""Methods for Google Maps API testing"""

base_url = "https://rahulshettyacademy.com"   # base url
key = "?key=qaclick123"   # parameter for request

class Google_maps_api():

    """Method for create new location"""

    @staticmethod
    def creat_new_place():

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # resource for post method
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_location)
        print(result_post.text)
        return result_post

    """Method for checking new location"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json"  # resource for get method
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Method for changing new location"""

    @staticmethod
    def put_new_place(place_id):

        json_for_change_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        put_resource = "/maps/api/place/update/json"  # resource for put method
        put_url = base_url + put_resource + key
        print(put_url)
        result_put = Http_methods.put(put_url, json_for_change_new_location)
        print(result_put.text)
        return result_put

    """ Method DELETE"""

    @staticmethod
    def delete_new_place(place_id):

        json_for_delete_new_location = {
            "place_id": place_id
        }

        delete_resource = "/maps/api/place/delete/json"   # resource for delete method
        delete_url = base_url + delete_resource + key
        print(delete_url)
        result_delete = Http_methods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete

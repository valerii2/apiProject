import json


"""Methods for checking our responses"""

class Checking():

    """Method for checking status code"""
    @staticmethod
    def check_status_code(response, status_code):
        assert status_code == response.status_code
        if status_code == response.status_code:
            print("Status code is OK: " + str(response.status_code))
        else:
            print("Status code is NOT OK: " + str(response.status_code))

    """Method for checking existence required fields in response"""
    @staticmethod
    def check_json_token(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields existence")

    """Method for checking fields value"""
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + "  is RIGHT")


    """Method for checking fields value on search word"""
    @staticmethod
    def check_json_word_in_value(response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(search_word + " - EXIST")
        else:
            print(search_word + " - does NOT EXIST")
import pytest
from create_folder import check_path


class TestCheckPath:
    correct_token = 'correct_token'
    incorrect_token = 'incorrect_token'
    folder_names = ['123', '1/2']
    test_data = [
        (correct_token, folder_names[0], [200, 201]),
        (incorrect_token, folder_names[0], [200, 201]),
        (correct_token, folder_names[1], [200, 201])
        ]

    @pytest.mark.parametrize('a, b, result', test_data)
    def test_check_path_response_code(self, a, b, result):
        check_result = check_path(a, b)
        assert check_result[1] in result

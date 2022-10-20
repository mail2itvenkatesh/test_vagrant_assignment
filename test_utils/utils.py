import os
import json


class UtilityHelper:
    """Utility Class"""

    def __init__(self):
        """Constructor"""
        self.project_dir_path = os.path.abspath(os.path.dirname(__file__))

    def load_json_file(self,team_name:str = "rcb"):  # default team_name is rcb
        """
        Utility method to fetch the json file in relevant path, loads and return json object
        :param team_name: team_name as str. Example values like rcb,csk, kkr, etc
        :return: tuple of records(json resp loaded and if any error message available)

        Set of Validations done are
        1. If file path/file name is invalid, user friendly exception would be thrown and return None
        2. If length of the json file is zero, return None
        3. If type of the object is not dict then, return None
        """
        error_msg = ""
        try:
            file_path = os.path.join(self.project_dir_path,r"../test_data/team_{}.json".format(team_name))
            with open(file_path, 'r') as fp:
                info_retrieved = json.load(fp)

        except FileNotFoundError as e:
            error_msg = {"generic_exception": "Please check the file name or file path provided", "detailed_exception": f"{e}"}
            return None, error_msg

        except Exception as e:
            error_msg = f"{e}"
            return None, error_msg

        else:
            if len(info_retrieved) == 0:
                error_msg = f"Length of the json file provided is {len(info_retrieved)}"
                return None, error_msg

            if not isinstance(info_retrieved, dict):
                error_msg = "json object received is not in a dict format or key value pairs. Please revisit the *.json file provided"
                return None, error_msg

            return info_retrieved, error_msg

# uh = UtilityHelper()
# resp,err_msg = uh.load_json_file("rcb2")
# print(resp, err_msg)

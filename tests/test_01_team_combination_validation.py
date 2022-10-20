import pytest
from test_utils.utils import UtilityHelper


class TestTeamCombinationAvailability:
    """
    This class contains the executable test cases.
    """

    # Object setup initialization and it is like before() hook in javascript or TestNG frameworks
    # Pytest will autouse it across the tests
    @pytest.fixture(autouse=True)
    def objectSetup(self):
        # self.util_helper = UtilityHelper()
        self.resp_fetched, self.err_msg_fetched = UtilityHelper().load_json_file()

    @pytest.mark.parametrize("country, player_count", [
        ("India", 4)])  # Pytest parametrization is applied and we can try with other set of test datas as well
    def test_01_verify_availability_of_4_foreign_players(self, country: str, player_count: int):
        """
        This test is to validate the availability of 4 foreign players in the team playing eleven for the match
        :param country: country as str
        :param player_count: player_count as int
        :return: return test status as True | False
        """
        if self.resp_fetched is not None:
            if not isinstance(self.resp_fetched['player'], list):
                print(f"Exception Message Occurred while running test --> Player key in json is not of type list")
                assert False

            # for index in range(len(self.resp_fetched['player'])):
            #     if self.resp_fetched['player'][index]['country'] != country:
            #         print(self.resp_fetched['player'][index]['country'], self.resp_fetched['player'][index]['name'])

            # Above snippets of code is equivalent in one line. List comprehension in python is used
            foreign_player_country_fetched = [{"country": self.resp_fetched['player'][index]['country'],
                                               "name": self.resp_fetched['player'][index]['name']}
                                              for index in range(len(self.resp_fetched['player'])) if
                                              self.resp_fetched['player'][index]['country'] != country]
            print(f"Fetched foreign players info are {foreign_player_country_fetched}")

            # If player count is not equal to 4, then test will be failed else would be passed.
            if player_count != len(foreign_player_country_fetched):
                print(
                    f"Expected foreign player count is {player_count} and available/actual player count is {len(foreign_player_country_fetched)}")
                assert False
            else:
                print(f"Expected foreign player count is {player_count} and available/actual player count is {len(foreign_player_country_fetched)}")
                assert True
        else:
            print(self.err_msg_fetched)
            assert False

    @pytest.mark.parametrize("player_role, player_count", [("Wicket-keeper",1)])
    def test_02_verify_availability_of_atleast_one_wicket_keeper(self, player_role: str, player_count: int):
        """
        This test is to validate that there is at least one wicket keeper is available
        :param player_role: player_role as str
        :return: return test status as True | False
        """
        if self.resp_fetched is not None:
            if not isinstance(self.resp_fetched['player'], list):
                print(f"Exception Message Occurred while running test --> Player key in json is not of type list")
                assert False

            # for index in range(len(self.resp_fetched['player'])):
            #     if self.resp_fetched['player'][index]['role'] == player_role:
            #         print(self.resp_fetched['player'][index]['name'],self.resp_fetched['player'][index]['role'])

            # Above snippets of code is equivalent in one line. List comprehension in python is used
            player_details = [{"country": self.resp_fetched['player'][index]['country'],
                                               "name": self.resp_fetched['player'][index]['name'],"role": self.resp_fetched['player'][index]['role']}
                                              for index in range(len(self.resp_fetched['player'])) if
                                              self.resp_fetched['player'][index]['role'] == player_role]

            print(f"Fetched players info are {player_details}")

            # If player count is not equal to 1, then test will be failed else would be passed.
            if player_count != len(player_details):
                print(f"Expected player count is {player_count} and available/actual player count is {len(player_details)}")
                assert False
            else:
                print(f"Expected player count is {player_count} and available/actual player count is {len(player_details)}")
                assert True
        else:
            print(self.err_msg_fetched)
            assert False
from user.user import Player, Admin
import pytest


class TestUser:

    @pytest.fixture(scope='class')
    def setup(self):
        player = Player("user")
        return player

    @pytest.mark.parametrize("test_input,expected",
                             [("50", "50"),
                              ("100", "100"),
                              ("200", "200")
                              ]
                             )
    def test_add_cash(self, setup, test_input, expected):
        setup.add_cash(test_input)
        assert setup.result == expected

    @pytest.mark.parametrize("test_input,expected",
                             [("50", "50"),
                              ("100", "100"),
                              ("200", "200")
                              ]
                             )
    def test_get_result(self, setup, test_input, expected):
        setup.add_cash(test_input)
        assert setup.get_result() == expected

    @pytest.mark.parametrize("test_input,expected",
                             [("tm", "tm"),
                              ("asw", "asw"),
                              ("200", "200")
                              ]
                             )
    def test_get_player_nick(self, setup, test_input, expected):
        setup.nick = test_input
        assert setup.get_player_nick() == expected


class TestAdmin:

    @pytest.fixture(scope='class')
    def setup(self):
        admin = Admin("admin", "admin777")
        return admin

    def test_authorization(self, setup):
        assert setup.authorization()




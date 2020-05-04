from millionaires.user import Player, Admin
import pytest


class TestUser:

    @pytest.fixture(name='player')
    def setup(self):
        player = Player("user")
        return player

    @pytest.mark.parametrize("test_input,expected",
                             [("tm", "tm"),
                              ("asw", "asw"),
                              ("200", "200")
                              ]
                             )
    def test_get_player_nick(self, test_input, expected):
        player = Player(test_input)
        assert player.player_nick == expected







import pytest

from millionaires.user import Admin, Player


class TestUser:
    @pytest.fixture(name="player")
    def setup(self):
        player = Player("user")
        return player

    @pytest.mark.parametrize(
        "test_input,expected", [("tm", "tm"), ("asw", "asw"), ("200", "200")]
    )
    def test_get_player_nick(self, test_input, expected):
        player = Player(test_input)
        assert player.player_nick == expected

    def test_create_player(self):
        player = Player.create_player("tm")
        assert isinstance(player, Player)


class TestAdmin:
    @pytest.fixture(name="admin")
    def setup(self):
        admin = Admin("admin", "admin777")
        return admin

    def test_initialization(self, admin):
        assert admin

    def test_authorization1(self, admin):
        assert admin.authorization()

    def test_authorization2(self):
        admin1 = Admin("user", "user777")
        assert not admin1.authorization()

    def test_authorization3(self):
        admin1 = Admin("pl456", "pass9090")
        assert not admin1.authorization()

    def test_create_admin(self):
        admin = Admin.create_admin("tm", "tm1")
        assert isinstance(admin, Admin)

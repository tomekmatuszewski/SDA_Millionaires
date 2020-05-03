from millionaires.game import Game
from millionaires.user import Player,Admin
from millionaires.utils import *

game = Game()
print(game)
username = input("Enter [P] if you want to play [A] if you want to log as Admin: ")
username = check_username(username)
if username == "P":
    nick = input("Enter your nick (max 10 chars [a-Z, 0-9]): ")
    player = Player.create_player(nick)
elif username == "A":
    nick = input("Enter your nick: ")
    password = input("Enter your password: ")
    admin = Admin.create_admin(nick, password)
    if admin.authorization():
        admin.add_question()
if player:
    game.play_game(player)
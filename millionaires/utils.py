import re

# functions responsible for checking if plyaer input is correct
def check_username(username):
    pattern = re.compile(r"^(P|A)$")
    while not re.search(pattern, username):
        username = input("Please enter correct character P - player, A- admin: ")
    return username


def check_player_nick(nick):
    pattern = re.compile(r"^([a-zA-z0-9]){1,10}$")
    while not re.search(pattern, nick):
        nick = input("Please enter correct nick - max 10 charakters [a-Z, 0-9]: ")
    return nick


def check_user_choice(log):
    pattern = re.compile(r"(C|S)")
    while not re.search(pattern, log):
        log = input("Please enter correct character S - log out, C- continue: ")
    return log


def check_chooser(chooser):
    pattern = re.compile(r"(Y|N)")
    while not re.search(pattern, chooser):
        chooser = input(
            "Please enter correct character Y - add question to base, N- log out: "
        )
    return chooser


def check_hint(hint):
    pattern = re.compile(r"(Y|N)")
    while not re.search(pattern, hint):
        hint = input(
            "Please enter correct character Y - take hint N- continue without hint: "
        )
    return hint


def check_correct_answer(answer):
    pattern = re.compile(r"(A|B|C|D)")
    while not re.search(pattern, answer):
        answer = input("Please enter correct answer [A - D]: ")
    return answer


def check_id(id_):
    while True:
        try:
            int(id_)
            return int(id_)
        except ValueError:
            id_ = input("ID must be Integer - Select the ID: ")
            continue


if __name__ == "__main__":
    pass

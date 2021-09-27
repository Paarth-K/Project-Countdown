import random
import time
from threading import Timer

points = 0

words = open("words_list.txt", "r")
content = words.read()
content_list = content.split(",")
words.close()
words = content_list[0].replace("\n", " ").lower().split()

vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")
nice_letters_vowels = list("aei")
etters_gotten = ""
numbers = []


def choose_vowel():
    # ran_list_v = random.choice([nice_letters_vowels] * 51 + [bad_letters_vowels] * 49)
    ran_list_v = vowels
def choose_vowel():
    return ran_v


def choose_consonants():
    ran_list_c = random.choice([nice_letters_consonants] * 51 + [bad_letters_consonants] * 49)
    ran_list_c = consonants
@ -34,6 +39,7 @@ def choose_consonants():
    return ran_c


def ask_user():
    global letters_gotten
    v_or_c = input("Choose! Vowel or Consonant: ").strip().replace(" ", "").lower()
@ -50,6 +56,7 @@ def ask_user():
    return "pass"


def countdown_timer(time_to):
    print(f"You have {time_to} seconds to think (don't type)", end="")
    print("\b" * len(f"{time_to} seconds to think (don't type)"), end="")
@ -62,6 +69,7 @@ def countdown_timer(time_to):
    print("\b" * len("You have "))


def word_check_ask():
    timeout = 10
    t = Timer(timeout, print, ['Times up! You have been disqualified'])
@ -71,6 +79,7 @@ def word_check_ask():
    return answer


def restart_prompt():
    global points
    global letters_gotten
@ -85,6 +94,7 @@ def restart_prompt():
        exit(f"Ok your final score was: {points}")


def round_chooser():
    print("Welcome to Countdown!")
    round_name = input("Choose! Number round! or Word Round!").lower().strip()
@ -99,6 +109,7 @@ def round_chooser():
        round_chooser()


def num_check_ask():
    timeout = 30
    t = Timer(timeout, print, ['Times up! You have been disqualified'])
@ -108,6 +119,7 @@ def num_check_ask():
    return answer


def num_chooser():
    global numbers
    if len(numbers) == 6:
@ -126,14 +138,35 @@ def num_chooser():
        num_chooser()


def main_num_round():
    global numbers
    print(f"Your numbers are {numbers}!")
    target_num = random.randint(100, 1000)
    print(f"Your target is {target_num}!")
    print("You have to use * to multiply, - to subtract, + to add and / to divide")
    num_check_ask()
<<<<<<< HEAD
    user_guess = eval(num_check_ask())
    diff = abs(target_num - user_guess)
    print(f"That makes: {user_guess}")
    if diff == 0:
        print("Wow! Exact guess with a difference of 0! You have gained 5 points")
        points += 5
    elif diff <= 5:
        print(f"You were very close! {diff} numbers away! You have gained 4 points")
        points += 4
    elif diff <= 10:
        print(f"You were very close! {diff} numbers away! You have gained 3 points")
        points += 3
    elif diff <= 20:
        print(f"You were not very close! {diff} numbers away! You have gained 1 point")
        points += 1
    else:
        print(f"Your guess was very far away! {diff} numbers away! You have gained no points")
    restart_prompt()

=======
>>>>>>> parent of d602ca1 (Code push 3)

def main_word_round():
    global letters_gotten
    global words
@ -165,4 +198,5 @@ def main_word_round():
    restart_prompt()


<<<<<<< HEAD
# Start the main program
round_chooser()
=======
round_chooser()
>>>>>>> parent of d602ca1 (Code push 3)

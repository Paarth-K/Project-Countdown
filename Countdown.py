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
bad_letters_vowels = random.choice(vowels)
nice_letters_consonants = list("tns")
bad_letters_consonants = list("vkxjqz")
letters_gotten = ""
numbers = []


def choose_vowel():
    # ran_list_v = random.choice([nice_letters_vowels] * 51 + [bad_letters_vowels] * 49)
    ran_list_v = vowels
    ran_v = random.choice(ran_list_v)
    return ran_v


def choose_consonants():
    ran_list_c = random.choice([nice_letters_consonants] * 51 + [bad_letters_consonants] * 49)
    ran_list_c = consonants
    ran_c = random.choice(ran_list_c)
    return ran_c


def ask_user():
    global letters_gotten
    v_or_c = input("Choose! Vowel or Consonant: ").strip().replace(" ", "").lower()
    if v_or_c in ["vowel", "v", "1"]:
        letter = choose_vowel()
        letters_gotten += letter
    elif v_or_c in ["consonant", "c", "2"]:
        letter = choose_consonants()
        letters_gotten += letter
    else:
        print("invalid input")
        return "fail"
    print(f"You got \"{letter}\"")
    return "pass"


def countdown_timer(time_to):
    print(f"You have {time_to} seconds to think (don't type)", end="")
    print("\b" * len(f"{time_to} seconds to think (don't type)"), end="")
    for i in range(1, time_to):
        i -= time_to
        i = abs(i)
        print(f"{i} seconds to think (don't type)", end="")
        time.sleep(1)
        print("\b" * (len(f" {i} seconds to think (don't type)") - 1), end="")
    print("\b" * len("You have "))


def word_check_ask():
    timeout = 10
    t = Timer(timeout, print, ['Times up! You have been disqualified'])
    t.start()
    answer = input(f"You have {timeout} seconds to type the answer: ")
    t.cancel()
    return answer


def restart_prompt():
    global points
    global letters_gotten
    global numbers
    res = input("Do you want to restart (Y/N): ")
    if res.lower().strip().replace(" ", "") in ["y", "yes"]:
        print("\n" * 10000)
        letters_gotten = ""
        numbers = []
        round_chooser()
    else:
        exit(f"Ok your final score was: {points}")


def round_chooser():
    print("Welcome to Countdown!")
    round_name = input("Choose! Number round! or Word Round!").lower().strip()
    possible_ans_num = ["n", "nr", "num", "number round", "num r", "num round", "n r", "n.", "n.r"]
    possible_ans_word = ["w", "wr", "word", "word round", "word r", "w round", "w r", "w.", "w.r"]
    if round_name in possible_ans_num:
        main_num_round()
    if round_name in possible_ans_word:
        main_word_round()
    else:
        print("Invalid input")
        round_chooser()


def num_check_ask():
    timeout = 30
    t = Timer(timeout, print, ['Times up! You have been disqualified'])
    t.start()
    answer = input(f"You have {timeout} seconds to type the answer: ").strip().replace(" ", "").lower()
    t.cancel()
    return answer


def num_chooser():
    global numbers
    if len(numbers) == 6:
        main_num_round()
    l_or_s = input("Choose! Large number or small number!").strip().lower().replace(" ", "")
    possible_ans_l = ["l", "largenumber", "ln", "l.n", "largenum"]
    possible_ans_s = ["s", "smallnumber", "sn", "s.n", "smallnum"]
    if l_or_s in possible_ans_l:
        print("Large number it is!")
        numbers.append(random.randint(10, 20))
    if l_or_s in possible_ans_s:
        print("Small number it is!")
        numbers.append(random.randint(1, 10))
    else:
        print("Invalid input")
        num_chooser()


def main_num_round():
    global numbers
    print(f"Your numbers are {numbers}!")
    target_num = random.randint(100, 1000)
    print(f"Your target is {target_num}!")
    print("You have to use * to multiply, - to subtract, + to add and / to divide")
    num_check_ask()

def main_word_round():
    global letters_gotten
    global words
    global points
    i = 0
    while i != 9:
        a = ask_user()
        if a == "fail":
            continue
        if a == "pass":
            i += 1
    print(f"\nYour letters are!: \n{letters_gotten}\n")
    countdown_timer(20)
    answer = word_check_ask()
    let_match = False
    for i in list(answer.lower().strip()):
        if i in list(letters_gotten):
            let_match = True
        else:
            let_match = False

    if answer.lower().strip() in words and let_match:
        print(f"Congratulations, {answer} is a word! And can be made using {letters_gotten}, you gained "
              f"{len(answer.lower().strip())} points")
        points += len(answer.lower().strip())
    else:
        print(f"Unfortunately, {answer} is a not a word that can be made from {letters_gotten}, you gained 0 points")
    print(f"You have {points} point(s)")
    restart_prompt()


round_chooser()

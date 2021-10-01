import random
import time
from threading import Timer

# Points score
points = 0

# Reading the word list
words = open("words_list.txt", "r")
content = words.read()
content_list = content.split(",")
words.close()
words = content_list[0].replace("\n", " ").lower().split()

# Making a list of vowel or consonants
vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")
nice_letters_vowels = list("aei")
bad_letters_vowels = random.choice(vowels)
nice_letters_consonants = list("tns")
bad_letters_consonants = list("vkxjqz")
letters_gotten = ""
numbers = []


# Chooses random consonants, the probability part is really working right now
def choose_vowel():
    # ran_list_v = random.choice([nice_letters_vowels] * 51 + [bad_letters_vowels] * 49)
    ran_list_v = vowels
    ran_v = random.choice(ran_list_v)
    return ran_v


# Chooses random consonants, the probability part is really working right now for this too
def choose_consonants():
    ran_list_c = random.choice([nice_letters_consonants] * 51 + [bad_letters_consonants] * 49)
    ran_list_c = consonants
    ran_c = random.choice(ran_list_c)
    return ran_c


# Asks user for vowel or Consonant
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


# Timer to countdown
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


# Asks word for main_word_round()
def word_check_ask():
    timeout = 10
    t = Timer(timeout, print, ['Times up! You have been disqualified'])
    t.start()
    answer = input(f"You have {timeout} seconds to type the answer: ")
    t.cancel()
    return answer


# Asks user whether to restart program or not, maintains points if restarted
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


# Chooses rounds
def round_chooser():
    print("Welcome to Countdown!")
    round_name = input("Choose! Number round! or Word Round!: ").lower().strip()
    possible_ans_num = ["n", "nr", "num", "number round", "num r", "num round", "n r", "n.", "n.r", "number"]
    possible_ans_word = ["w", "wr", "word", "word round", "word r", "w round", "w r", "w.", "w.r"]
    if round_name in possible_ans_num:
        main_num_round()
    if round_name in possible_ans_word:
        main_word_round()
    else:
        print("Invalid input")
        round_chooser()


# Function that takes the input for the main_num_round()
def num_check_ask(x=30):
    timeout = x
    t = Timer(timeout, print, ['Times up! You have been disqualified'])
    t.start()
    answer = input(f"You have {timeout} seconds to type the answer: ").strip().replace(" ", "").lower()
    t.cancel()
    return answer


# Function to choose the random number for main_num_round()
def num_chooser():
    global numbers
    if len(numbers) == 6:
        main_num_round()
    l_or_s = input("Choose! Large number or small number!: ").strip().lower().replace(" ", "")
    possible_ans_l = ["l", "largenumber", "ln", "l.n", "largenum", "large"]
    possible_ans_s = ["s", "smallnumber", "sn", "s.n", "smallnum", "small"]
    if l_or_s in possible_ans_l:
        num_given = random.randint(10, 20)
        print(f"Large number it is!: {num_given}")
        numbers.append(num_given)
    elif l_or_s in possible_ans_s:
        num_given = random.randint(1, 10)
        print(f"Small number it is!: {num_given}")
        numbers.append(num_given)
    else:
        print("Invalid input")
        num_chooser()


# Number round
def main_num_round():
    global numbers
    global points
    for i in range(6):
        num_chooser()
    print(f"Your numbers are {numbers}!")
    target_num = random.randint(100, 1000)
    print(f"Your target is \"{target_num}\"!")
    print("You have to use * to multiply, - to subtract, + to add and / to divide, you may use brackets \"()\"")
    print("YOU MUST USE ALL NUMBERS!!!")
    user_guess_str = num_check_ask(60)
    user_guess_list = user_guess_str.replace("*", " ").replace("/", " ").replace(")", " ").replace("(", " ").replace(
        "+", " ").replace("-", " ").split()
    user_guess_list = [int(i) for i in user_guess_list]
    user_guess_list.sort()
    numbers.sort()
    print(user_guess_list)
    print(numbers)
    if user_guess_list == numbers:
        pass
    else:
        print("Invalid input, disqualified")
        exit(f"Your final score was: {points}")
    try:
        user_guess = eval(user_guess_str)
    except NameError:
        print("Invalid input, disqualified")
        exit(f"Your final score was: {points}")
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


# Word round
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


# Start the main program
round_chooser() 

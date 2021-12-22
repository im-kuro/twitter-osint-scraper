# Made by im-kuro or @im_kuro_offical
# a python twitter OSINT scraper

import tweepy
import os
import time


consumer_key =''
consumer_secret_key =''
access_token =''
access_token_secret =''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

os.system("clear")
print("░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄")
time.sleep(0.2)
print("░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄")
time.sleep(0.2)
print("░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█")
time.sleep(0.2)
print("░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█")
time.sleep(0.2)
print("░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█")
time.sleep(0.2)
print("█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█")
time.sleep(0.2)
print("█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█")
time.sleep(0.2)
print("░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█")
time.sleep(0.2)
print("░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█")
time.sleep(0.2)
print("░░░█░░██░░▀█▄▄▄█▄▄█▄████░█")
time.sleep(0.2)
print("░░░░█░░░▀▀▄░█░░░█░███████░█")
time.sleep(0.2)
print("░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█")
time.sleep(0.2)
print("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█")
time.sleep(0.2)
print("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█")
time.sleep(0.2)
print("░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█")
time.sleep(0.2)
try:
    target = input("Enter twitter screen name: ")
except:
    print("whoops there was a error with the username you enterd.")

x = api.get_user(screen_name=target)
print(f"Target id set = {x.id}")
print("============================================================================")
print("|                                                                          |")
print("|     Get user twitter id = 1           Get user name = 2                  |")
print("|                                                                          |")
print("|     Get user location = 3             Get amount of friends = 4          |")
print("|                                                                          |")
print("|     Get user profile picture = 5      Get user description = 6           |")
print("|                                                                          |")
print("|     Get when account was made = 7     Get user background image = 8      |")
print("|                                                                          |")
print("|     Get user possible time zone = 9   Get if the user is verified = 10   |")
print("|                                                                          |")
print("|                check if user had geo enabled = 11                        |")
print("|                                                                          |")
print("============================================================================")
print("**NOTICE** if there is no output when you run a option, there was probably no data for it to give you")

option_input = input("Choose a option: ")

print("\n")
print("\n")


if option_input == "1":
    print(f"here is the users {target} twitter id: {x.id}")

if option_input == "2":
    print(f"here is the users {target} twitter username: {x.screen_name}")

if option_input == "3":
    print(f"here is the users {target} twitter location: {x.location}")

if option_input == "4":
    print(f"here is the users {target} twitter friends: {x.friends_count}")

if option_input == "5":
    print(f"here is the users {target} twitter profile picture: {x.profile_image_url}")

if option_input == "6":
    print(f"here is the users {target} twitter description: {x.description}")

if option_input == "7":
    print(f"here is the users {target} twitter was made on: {x.created_at}")

if option_input == "8":
    print(f"here is the users {target} twitter background image: {x.profile_background_image_url}")

if option_input == "9":
    print(f"here is the users {target} twitter time zone: {x.time_zone}")

if option_input == "10":
    print(f"here is the users {target} twitter verification: {x.verified}")

if option_input == "11":
    print(f"here is the users {target} twitter geo enabled option: {x.ge0_enabled}")


# The data list has a few dictionary entries currently. 
# Feel free to populate the list with as much data as you want.

import random


data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]

first_pick = random.choice(data)
next_pick = random.choice(data)

score = 0
attempts = 7

first_name = first_pick['name']
first_number_of_followers = first_pick['follower_count']
first_description = first_pick['description']
first_country = first_pick['country']

next_name = next_pick['name']
next_number_of_followers = next_pick['follower_count']
next_description = next_pick['description']
next_country = next_pick['country']

while attempts > 0:

    make_choice = input(f"Does {first_name}, a {first_description} from {first_country}, have more or less followers than {next_name} a {next_description} from {next_country}. Enter 'less' or 'more'? ")

    if make_choice == 'more':
        if first_number_of_followers > next_number_of_followers or first_number_of_followers == next_number_of_followers:
            score += 1
            attempts -= 1
            print(
                f"You are correct. {first_name} , a {first_description} from {first_country}, has {first_number_of_followers} and {next_name}, a {next_description} from {next_country} has {next_number_of_followers}")
            print(f"Your current score is {score}")
            first_pick = next_pick
            next_pick = random.choice(data)
            first_name = first_pick['name']
            first_number_of_followers = first_pick['follower_count']
            first_description = first_pick['description']
            first_country = first_pick['country']

            next_name = next_pick['name']
            next_number_of_followers = next_pick['follower_count']
            next_description = next_pick['description']
            next_country = next_pick['country']



        elif first_number_of_followers < next_number_of_followers:
            attempts -= 1
            print(
                f"You are incorrect. {first_name} , a {first_description} from {first_country}, has {first_number_of_followers} and {next_name}, a {next_description} from {next_country} has {next_number_of_followers}")

            print(f"Your current score is {score}")
            first_pick = next_pick
            next_pick = random.choice(data)
            first_name = first_pick['name']
            first_number_of_followers = first_pick['follower_count']
            first_description = first_pick['description']
            first_country = first_pick['country']

            next_name = next_pick['name']
            next_number_of_followers = next_pick['follower_count']
            next_description = next_pick['description']
            next_country = next_pick['country']




    elif make_choice == 'less':
        if first_number_of_followers < next_number_of_followers or first_number_of_followers == next_number_of_followers :
            score += 1
            attempts -= 1
            print(
                f"You are correct. {first_name} , a {first_description} from {first_country}, has {first_number_of_followers} and {next_name}, a {next_description} from {next_country} has {next_number_of_followers}")

            print(f"Your current score is {score}")
            first_pick = next_pick
            next_pick = random.choice(data)
            first_name = first_pick['name']
            first_number_of_followers = first_pick['follower_count']
            first_description = first_pick['description']
            first_country = first_pick['country']

            next_name = next_pick['name']
            next_number_of_followers = next_pick['follower_count']
            next_description = next_pick['description']
            next_country = next_pick['country']




        elif first_number_of_followers > next_number_of_followers:
            attempts -= 1
            print(
                f"You are incorrect. {first_name} , a {first_description} from {first_country}, has {first_number_of_followers} and {next_name}, a {next_description} from {next_country} has {next_number_of_followers}")

            print(f"Your current score is {score}")
            first_pick = next_pick
            next_pick = random.choice(data)
            first_name = first_pick['name']
            first_number_of_followers = first_pick['follower_count']
            first_description = first_pick['description']
            first_country = first_pick['country']

            next_name = next_pick['name']
            next_number_of_followers = next_pick['follower_count']
            next_description = next_pick['description']
            next_country = next_pick['country']


print(f"Your final score is {score}.")

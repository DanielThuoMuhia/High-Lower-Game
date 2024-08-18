from art import logo, vs
from game_data import data
import random
import os

# Display Art

def format_data(account):
    """
    Format the account data into a printable format.
    
    Args:
    account (dict): A dictionary containing account details.
    
    Returns:
    str: A formatted string containing the account details.
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_follower, b_follower):
    """
    Check if the user's guess is correct.
    
    Args:
    guess (str): The user's guess ('a' or 'b').
    a_follower (int): Follower count of account A.
    b_follower (int): Follower count of account B.
    
    Returns:
    bool: True if the guess is correct, False otherwise.
    """
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

# Initialize score and game continuation flag
score = 0
game_should_continue = True   
# Generate the first random account for comparison
account_b = random.choice(data)

# Display the game logo
print(logo)

while game_should_continue:
    # Move previous account B to account A, then generate a new account B
    account_a = account_b
    account_b = random.choice(data)
    
    # Ensure account A and account B are not the same
    while account_a == account_b:
        account_b = random.choice(data)

    # Display the accounts for comparison
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts for both accounts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    # Check if the user's guess is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    
    if is_correct:
        # Increment score if the guess is correct
        score += 1
        print(f"You are right. Your current score: {score}.")
    else:
        # End the game if the guess is incorrect
        game_should_continue = False
        print(f"Sorry, you are wrong. Final score is: {score}")



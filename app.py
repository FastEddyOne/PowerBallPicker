import random
import sys

def generate_white_balls():
    return sorted(random.sample(range(1, 70), 5))

def generate_powerball():
    return random.randint(1, 26)

def display_generated_numbers(white_balls, powerball):
    print(f"\nWhite balls: {' '.join(map(str, white_balls))} | Powerball: {powerball}\n")

def get_num_draws_from_user():
    while True:  # Keep asking until valid input is provided
        num_draws = input("\nEnter the number of draws you want (or type 'exit' to quit): ")
        
        if num_draws.lower() == 'exit':
            sys.exit("Thanks for using the Powerball Number Generator. Goodbye!")
        
        try:
            num_draws = int(num_draws)
            if num_draws <= 0:
                raise ValueError
            return num_draws
        except ValueError:
            print("\nInvalid input. Please enter a positive integer.")

def display_welcome_message():
    print("\nWelcome to the Powerball Number Generator!")
    print("This app will help you generate random numbers for your Powerball lottery ticket.\n")

def main():
    display_welcome_message()
    
    while True:  # Main application loop
        num_draws = get_num_draws_from_user()
        for _ in range(num_draws):
            white_balls = generate_white_balls()
            powerball = generate_powerball()
            display_generated_numbers(white_balls, powerball)
        
        another_run = input("Would you like to generate more numbers? (yes/no): ")
        if another_run.lower() != 'yes':
            print("Thanks for using the Powerball Number Generator. Good luck!")
            break

if __name__ == "__main__":
    main()

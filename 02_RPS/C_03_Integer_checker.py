
# Checks that users enter an integer that is more than 13

def int_check():

    while True:
        error = "Please enter an integer that is 13 or more."

        try:
            game_goal = int(input("What is the game goal? "))

            # check that the number is more than / equal to 13
            if game_goal < 13:
                print(error)
            else:
                print(f"Game goal: {game_goal}")
                break

        except ValueError:
            print(error)

# main routine goes here
target_score = int_check()
print(target_score)
# Creates starting scores for all Big Five personality traits.
def make_scores():
    return{
        "openness": 0,
        "extraversion": 0,
        "agreeableness": 0,
        "conscientiousness": 0,
        "neuroticism": 0 }
    

def print_line():
    print("=" * 60)


def print_section(title):
    print_line()
    print(title.upper())
    print_line()

# Displays a scenario and then lets the player choose an option.
def play_scenario(scenario):
    print_section(scenario["title"])
    print(scenario["text"])
    print()

    for number, option in enumerate(scenario["options"], start=1):
        print(f"{number}. {option['text']}")

    while True:
        choice = input("\nChoose 1, 2, or 3: ")

        if choice in ["1", "2", "3"]:
            return scenario["options"][int(choice) - 1]

        print("Please enter 1, 2, or 3.")
    
# Updates the personality scores based on the player's choice.
def update_trait_scores (choice,scores):
    for trait, points in choice["traits"].items():
        scores[trait] += points

    return scores

def get_highest_trait(scores):
    return max(scores, key=scores.get)
       
# Will show the player's final result and description.
def show_final_result(scores):

    print("\nYour final trait scores:")
    print("\n" + "=" * 60)
    
    for trait, score in scores.items():
        print(f"{trait.title()}: {score}")
# Finds the trait with the highest score at the end of the game.
    highest_trait = get_highest_trait(scores)
    
    descriptions = {
        "openness": "You are curious, creative, and open to trying new things.",
        "conscientiousness": "You are organized, responsible, and goal focused.",
        "extraversion": "You are outgoing, social, and feel energized by other people.",
        "agreeableness": "You are caring, cooperative, and thoughtful toward others.",
        "neuroticism": "You may be more emotionally reactive or sensitive to stress." }
    
    print("\nFinal Personality Result!")
    print("\nYour strongest trait is:", highest_trait.title())
    print(descriptions[highest_trait])
    print("\nThanks for playing the College Personality Adventure Game :)")

def main():
   print("=" * 60)
print("       ✦ WELCOME TO THE COLLEGE DAY PERSONALITY ADVENTURE ✦")
print("                  WITH BIG FIVE TRAITS ")
print("=" * 60)

print("Make your most realistic choices throughout the day and see which personality trait shows up the most for you and what they mean!")
scores = make_scores()

morning_scenario = { 
        "title": "Morning Class",
         "text": "You wake up tired at around 7:30am and you realize you have class soon.",
         "options": [
             {
                 "text": "Get up right away and make it on time.",
                 "traits": {"conscientiousness": 2}
             },
             {
                 "text": "Text your friend in the class to see if they're going or not.",
                 "traits": {"extraversion": 2}
             },
             {
                 "text": "Stay in bed longer because you just can't start the day yet.",
                 "traits": {"neuroticism": 2}
                }
           ]
      }
    
group_project_scenario =  {
            "title": "Group Project",
            "text": "All of sudden you realize your group project is due tomorrow, but nobody else has started!",
            "options": [
                {
                    "text": "Make a firm plan about who is doing what and when it needs to be done.",
                    "traits": {"conscientiousness": 2}
                },
                {
                    "text": "Text everyone in the group to look at the project whenever they can.",
                    "traits": {"agreeableness": 2}
                },
                {
                    "text": "Suggest a different way everyone can do the project to make it more interesting.",
                    "traits": {"openness": 2}
                }
            ]
        }
    
coffee_scenario = {
        "title": "Campus Break",
        "text": "You have a short break after the group project crisis before your next class.",
        "options": [
            {
                "text": "Try a new cafe you heard about on Green Street.",
                "traits": {"openness": 2}
            },
            {
                "text": "Use the break to work on assignments.",
                "traits": {"conscientiousness": 2}
            },
            {
                "text": "Meet up with a friend for lunch.",
                "traits": {"extraversion": 2}
            }
        ]
    }

friend_scenario = {
        "title": "Friend Check In",
        "text": "A friend suddenly texts you saying they have had a stressful day.",
        "options": [
            {
                "text": "Call them and listen to what happened.",
                "traits": {"agreeableness": 2}
            },
            {
                "text": "Feel more stressed because you are already overwhelmed as is.",
                "traits": {"neuroticism": 2}
            },
            {
                "text": "Suggest doing something fun together later to cheer them up.",
                "traits": {"extraversion": 2}
            }
        ]
    }


evening_scenario =  {
            "title": "End of the day",
            "text": "You're finally at home and ready for dinner.",
            "options": [
                {
                    "text": "Make a new recipe you saw online for dinner.",
                    "traits": {"openness": 2}
                },
                {
                    "text": "Eat a quick and easy dinner and get back to work.",
                    "traits": {"conscientiousness": 2}
                },
                {
                    "text": "Invite your roommate to come make dinner with you and talk.",
                    "traits": {"extraversion": 2}
                }
            ]
        }
    


morning_choice = play_scenario(morning_scenario)
scores = update_trait_scores(morning_choice, scores)
# This section will change later events depending on the player's earlier choices.
if morning_choice["traits"] == {"conscientiousness": 2}:

        productive_scenario = {
            "title": "Study Session",
            "text": "Because you made it to class on time, you're feeling like continuing the momentum with a study session.",
            "options": [
                {
                    "text": "Head to the library to get ahead on assignments.",
                    "traits": {"conscientiousness": 2}
                },
                {
                    "text": "Invite classmates to study together after class.",
                    "traits": {"extraversion": 2}
                },
                {
                    "text": "Try studying somewhere new alone.",
                    "traits": {"openness": 2}
                }
            ]
        }

        next_choice = play_scenario(productive_scenario)

elif morning_choice["traits"] == {"extraversion": 2}:

        social_scenario = {
            "title": "Class Conversation",
            "text": "After you find out your friend is coming to class, you end up talking with classmates after class ends.",
            "options": [
                {
                    "text": "Stay and talk with everyone for a long time.",
                    "traits": {"extraversion": 2}
                },
                {
                    "text": "Make sure to ask questions to make sure nobody feels left out of the conversation.",
                    "traits": {"agreeableness": 2}
                },
                {
                    "text": "Bring up something interesting from the lecture that starts a debate.",
                    "traits": {"openness": 2}
                }
            ]
        }

        next_choice = play_scenario(social_scenario)

else:

        stressful_scenario = {
            "title": "Missed Class",
            "text": "Since you stayed in bed, you now feel stressed about missing class.",
            "options": [
                {
                    "text": "Email your professor to ask for any content you missed.",
                    "traits": {"conscientiousness": 2}
                },
                {
                    "text": "Text classmates to ask for notes.",
                    "traits": {"agreeableness": 2}
                },
                {
                    "text": "Avoid thinking about it too much and go back to sleep.",
                    "traits": {"neuroticism": 2}
                }
            ]
        }

        next_choice = play_scenario(stressful_scenario)



scores = update_trait_scores(next_choice, scores)

group_choice = play_scenario(group_project_scenario)
scores = update_trait_scores(group_choice, scores)

coffee_choice = play_scenario(coffee_scenario)
scores = update_trait_scores(coffee_choice, scores)

friend_choice = play_scenario(friend_scenario)
scores = update_trait_scores(friend_choice, scores)

evening_choice = play_scenario(evening_scenario)
scores = update_trait_scores(evening_choice, scores)

# This final scenario will change depending on the player's strongest trait so far.
current_trait = get_highest_trait(scores)

if current_trait == "conscientiousness":
   final_scenario = {
            "title": "Late Night",
            "text": "After a productive day, your brain still isn't fully ready to relax yet as you lay in bed. You are...",
            "options": [
                {
                    "text": "Sending your friends funny tiktoks.",
                    "traits": {"extraversion": 2}
                },
                {
                    "text": "Taking a melatonin to make sure you have enough sleep for tomorrow.",
                    "traits": {"conscientiousness": 2}
                },
                {
                    "text": "Researching something completely random that you for some reason must know right now.",
                    "traits": {"openness": 2}
                }
            ]
        }

elif current_trait == "openness":
    final_scenario = {
        "title": "Late Night",
        "text": "After a long day, you're still thinking of new things in bed. You are...",
        "options": [
            {
                "text": "Planning a future creative project.",
                "traits": {"openness": 2}
            },
            {
                "text": "Falling into a Youtube rabbit hole about deep sea creatures.",
                "traits": {"openness": 2}
            },
            {
                "text": "Texting your friends about all the things you tried today.",
                "traits": {"extraversion": 2}
            }
        ]
    }
    
else:
    final_scenario = { 
        "title": "Still Thinking",
        "text": "After a full day, you're lying in bed still thinking.",
        "options": [
            {
                "text": "Overthink about something embarrassing from earlier.",
                "traits": {"neuroticism": 2}
            },
            {
                "text": "Start reading old messages.",
                "traits": {"agreeableness": 2}
            },
            {
                "text": "Decide tomorrow is going to be your most productive day ever.",
                "traits": {"conscientiousness": 2}
            }
        ]
    }

final_choice = play_scenario(final_scenario)
scores = update_trait_scores(final_choice, scores)

print("\nThe day has finally come to an end...")
print("Your choices throughout the day shaped your personality result.")

show_final_result(scores)


if __name__ == "__main__":
    main() 

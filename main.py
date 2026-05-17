def make_scores():
    return{
        "openness": 0,
        "extraversion": 0,
        "agreeableness": 0,
        "conscientiousness": 0,
        "neuroticism": 0 }
    
def play_scenario (scenario):
    print("\n" + scenario["title"])
    print(scenario["text"])

    for number, option in enumerate(scenario["options"], start=1):
        print(f"{number}. {option['text']}")
        
    while True:
        choice = input("Choose 1, 2, or 3: ")
        
        if choice in ["1", "2", "3"]:
            return scenario["options"][int(choice) - 1]
            
        print("Please enter 1, 2, or 3.")
    
   
def update_trait_scores (choice,scores):
    for trait, points in choice["traits"].items():
        scores[trait] += points

    return scores

def get_highest_trait(scores):
    return max(scores, key=scores.get)
       

def show_final_result(scores):

    print("\nYour final trait scores:")
    for trait, score in scores.items():
        print(f"{trait.title()}: {score}")

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
    print("\nThanks for playing the College Personality Adventure Game!")

def main():
    print("Welcome to the College Day Personality Adventure Game!")
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
            "text": "You realize your group project is due tomorrow, but nobody else has started!",
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

        evening_scenario =  {
            "title": "End of the day",
            "text": "After the long day, you finally have some free time.",
            "options": [
                {
                    "text": "Try a new activity or hobby you have been curious about.",
                    "traits": {"openness": 2}
                },
                {
                    "text": "Go over your schedule for tomorrow again before you're able to relax.",
                    "traits": {"conscientiousness": 2}
                },
                {
                    "text": "Call a friend to discuss your day.",
                    "traits": {"extraversion": 2}
                }
            ]
        }
    ]



    morning_scenario = scenarios[0]
    group_project_scenario = scenarios[1]


    morning_choice = play_scenario(morning_scenario)
    scores = update_trait_scores(morning_choice, scores)

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
                    "text": "Try studying somewhere completely new alone.",
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
                    "text": "Make sure to ask questions and ensure nobody feels left out of the conversation.",
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

    evening_choice = play_scenario(evening_project_scenario)
    scores = update_trait_scores(evening_choice, scores)

    show_final_result(scores)


if __name__ == "__main__":
    main() 

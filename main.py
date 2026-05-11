def make_scores():
    return{
        "openness": 0,
        "extraversion": 0,
        "agreeableness": 0,
        "conscientiousness": 0,
        "neuroticism": 0, }
    
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
       

def show_final_result(scores):

    print("\nYour final trait scores:")
    for trait, score in scores.items():
        print(f"{trait.title()}: {score}")

    highest_trait = max(scores, key=scores.get)
    descriptions = {
        "openness": "You are curious, creative, and open to trying new things.",
        "conscientiousness": "You are organized, responsible, and goal focused.",
        "extraversion": "You are outgoing, social, and energized by other people.",
        "agreeableness": "You are caring, cooperative, and thoughtful toward others.",
        "neuroticism": "You may be more emotionally reactive or sensitive to stress." }
    print("\nYour strongest trait is:", highest_trait.title())
    print(descriptions[highest_trait])
    

def main():
    print("Welcome to the College Day Personality Adventure Game!")
    print("Make your most realistic choices throughout the day and see which personality trait shows up the most for you and what they mean!")
    scores = make_scores()

    scenarios = [
        { 
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
        },
        {
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
        },
        








             
     morning_scenario = scenarios[0]

    morning_choice = play_scenario(morning_scenario)
    scores = update_trait_scores(morning_choice, scores)

    show_final_result(scores)

if __name__ == "__main__":
    main() 

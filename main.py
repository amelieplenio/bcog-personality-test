def make_scores():
    return{
        "openness": 0,
        "extraversion": 0,
        "agreeableness": 0,
        "conscientousness": 0,
        "neuroticism": 0, }
    
def play_scenario (scenario):
    print("/n" + scenario[title"])
    print(scenario["text]")

    for number, option in enumerate(scenario["options"], start=1):
    while True
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
    for trait, score in scores.items()
        print(f"{trait.title()}: {score}")

    highest_trait = max(scores, key=scores.get)
    descriptions = {
        "openness": "You are curious, creative, and open to trying new things.",
        "conscientiousness": "You are organized, responsible, and goal focused.",
        "extraversion": "You are outgoing, social, and energized by other people.",
        "agreeableness": "You are caring, cooperative, and thoughtful toward others.",
        "neuroticism": "You may be more emotionally reactive or sensitive to stress." }
    print("/nYour strongest trait is:", highest_trait.title())
    print(description[highest_trait])
    

def main():
    """Run the whole game."""
    # future structure:
    # scores + {}
    # scenario = ...
    # choice = play_scenario(scenario)
    # scores = update_trait_scores(choice,scores)
    # show_final_results (scores)
    pass

if __name__ == "__main__":
    main() 

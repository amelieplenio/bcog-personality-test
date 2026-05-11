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
    
   
    pass
def update_trait_scores (choice,scores):
    """Update personality trait scores."""
    pass
def show_final_result(scores):
    """Display the final personality result."""
pass

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

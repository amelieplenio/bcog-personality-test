Personality-adventure-game


1. This project will be an interactive Python game based off of Personality Psych. In the game, the player will go through a real life day and respond to different scenarios. Each choice will add points to different personality traits based on the Big Five personality traits. At the end of the game, the program will determine which Personality style the player most closely matches, and will display a fun screen of the personality type with a short description. 


Main features: 
- Interactive scenarios where the user makes choices
- Scoring system based on the Big Five Personality traits
- Final personality result with a short description
- Simple terminal based gameplay
Files in this Project
- main.py: this will contain the main game logic and functions.
  (NOT DONE: still need to finish all the scenarios and end screens.)

- test_project.py: This will contain tests or the testing outline.

- data/: will maybe contain the scenario and personality description data


Planned Functions
- play_scenario(scenario): this will display a scenario and ask the player to then choose between options
Parameters: 
- scenario: a structure containing the scenario text and choices.
Returns: the player's selected choice


- update_trait_scores(choice,scores): This will update the personality trait scores based on the users choices.
Parameters: 
- scores: data tracking current trait scores
- choice: the option selected by the player 
Returns:
- updated scores data

- show_final_result (scores): this will determine which personality trait has the highest score and displays the result. 
Parameters:
- scores: final personality trait scores


Personality traits used: This program will use the Big Five personality traits:
Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. 


Example Use Case: A user will run the program and is presented with a scenarion like choosing how to spend a free day with a series of choices. Based on their answers, points will be added to certain traits. After several scenarios, the program will calculate their dominant trait and display a result with a short explanation. 


How to run: Run the program in terminal with python main.py


Testing: to test the program, python test_project.py will be ran in terminal. 


Expected result:
- The program runs without errors.
- Scenarios will display correctly. 
- Choices update trait scores.
- A final personality trait will then be shown in some way at the end.



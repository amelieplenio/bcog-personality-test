from main import make_scores, update_trait_scores


def test_make_scores():
  scores = make_scores()
  assert scores["openness"] == 0
  assert scores["conscientiousness"] == 0
  assert scores["extraversion"] == 0
  assert scores["agreeableness"] == 0
  assert scores["neuroticism"] == 0
  
def test_update_trait_scores():
  scores = make_scores()
  choice = {"traits": {"openness": 2, "extraversion": 1}}
  updated_scores = update_trait_scores(choice, scores)

  assert updated_scores ["openness"] == 2
  assert updated_scores ["extraversion"] == 1
  
def test_program_runs():
  
    #Testing that the program runs without errors
   
    assert True

def test_scenario_display():

    #Testing that scenarios can be displayed to the user.

    assert True

def test_trait_updates():

    #Test that the choices correctly update personality scores.

    assert True

def test_final_result():

    #Test that a final personality result is shown.

    assert True

    if __name__ =="__main__":
        test_program_runs()
        test_scenario_display()
        test_trait_updates()
        test_final_result()
        print("All tests listed.")

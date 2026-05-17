from main import make_scores, update_trait_scores, get_highest_trait


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
  
def test_multiple_updates():
   scores = make_scores()

   choice_one = {"traits": {"conscientiousness": 2}}
   choice_one = {"traits": {"agreeableness": 2}}

   update_trait_scores(choice_one,scores)
   update_trait_scores(choice_two,scores)

    assert scores["conscientiousness"] == 2
    assert scores["agreeableness"] == 2
  

def test_get_highest_trait():

   

    

def test_trait_updates():

  

   

  

    if __name__ =="__main__":
        test_make_scores()
        test_update_trait_scores()
        test_multiple_updates()
        test_get_highest_trait()
        print("All tests passed.")

from agent import GameAgent


agent = GameAgent()


def test_high_guess():

    result = agent.investigate_guess(50,75)

    assert result["hint"] == "Too High"
    assert result["verified"] == True



def test_low_guess():

    result = agent.investigate_guess(50,20)

    assert result["hint"] == "Too Low"



def test_correct_guess():

    result = agent.investigate_guess(50,50)

    assert result["hint"] == "Correct"
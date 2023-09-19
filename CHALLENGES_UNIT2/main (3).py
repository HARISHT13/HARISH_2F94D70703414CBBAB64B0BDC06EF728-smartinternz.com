class player:
  def play(self):
    print("The Player Is Playing Cricket")

class Batsman(player):
  def play(self):
    print("The Batsman Is Batting.")
    
class Bowler(player):
  def play(self):
    print("The Bowler Is Bowling")

Batsman=Batsman()
Bowler=Bowler()
Batsman.play()
Bowler.play()
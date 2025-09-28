class Solution:
    def findWinners(self, matches):
        losses = {}  
        players = set()  

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            if winner not in losses:
                losses[winner] = 0

            
            losses[loser] = losses.get(loser, 0) + 1

        no_loss = []
        one_loss = []

        for player in players:
            if losses.get(player, 0) == 0:
                no_loss.append(player)
            elif losses[player] == 1:
                one_loss.append(player)

       
        return [sorted(no_loss), sorted(one_loss)]
  
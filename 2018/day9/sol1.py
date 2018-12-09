players = 5
max_marble = 25

class Marble(object):
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
    
    def __str__(self):
        return str(self.val)
    
    def insert_next(self, m):
        assert isinstance(m, Marble)
        temp = self.next
        self.next = m
        m.next = temp
        temp.prev = m
        m.prev = self

    def remove(self):
        temp = self.next
        temp.prev = self.prev
        self.prev.next = temp
        self.next = None
        self.prev = None
        return self.val
        
current = Marble(0)
current.next = current
current.prev = current

playerScores = [0 for i in range(0,players)]
currentPlayer = 0
marbleValue = 1
while marbleValue <= max_marble:
    if marbleValue % 23 == 0:
        playerScores[currentPlayer] += 23
        
        temp = current
        for i in range(0,7):
            temp = temp.prev        

        current = temp.next
        playerScores[currentPlayer] += temp.remove()
    else:
        temp = Marble(marbleValue)
        current.next.insert_next(temp)
        current = temp
   
    currentPlayer = currentPlayer + 1 if currentPlayer < players - 1 else 0
    marbleValue += 1

# print playerScores
print max(playerScores)



#Creating a matrix of played rounds using data from a text file
A = []
with open("Cards100x20.txt") as file: 
    for line in file:
        row = line.strip().split()
        A.append(row)
players = (int(len(A[0])/5)) # determines the number of players
PlayerScore = [0] * players

#Evaluating each player's hand for a given round
for i in range(0,len(A)):
    playerNS = []
    PlayerHands = []
    AllCards = []
    for j in range (1,players + 1): #Flips between players
        hand = 'highcard'
        Ace = False
        NS = 0 # Numerical Score, higher valued hand --> higher score
        Diams = Hearts = Clubs = Spades = 0
        player = j
        PH = A[i][(player-1)*5:(player*5)] # Determines which player gets which hand from A
        PH = [x.replace ('A','14').replace ('K','13').replace ('Q','12').replace ('J','11').replace ('T','10') for x in PH] #Assigns a numerical value to aces, kings etc..
        PH = sorted(PH,key = lambda x: int(x[:-1])) #Sorts the hand by rank
        PHx = [int(card[:-1]) for card in PH] # PHx = array of hand without suits
        
        # Counting number of each suit in hand
        Diams = sum(1 for card in PH if 'D' in card)
        Hearts = sum(1 for card in PH if 'H' in card)
        Clubs = sum(1 for card in PH if 'C' in card)
        Spades = sum(1 for card in PH if 'S' in card)
        if PHx[4] == 14: Ace = True
        
        # Checking for Hands
        if Diams == 5 or Hearts == 5 or Clubs == 5 or Spades == 5: #is there a flush? 
            NS += 5000 + sum(PHx) 
            hand = 'flush'
            
        if PHx[4] - PHx[3] == 1 and PHx[3] - PHx[2] == 1 and PHx[2] - PHx[1] == 1 and PHx[1] - PHx[0] == 1: #is there a straight?
            NS += 4000 + sum(PHx)
            if hand == 'flush':
                hand = 'straight flush'
                
                if PHx[3] == 13: #is the flush royal?
                    NS += 1000
                    hand = 'royal flush'
            else: hand = 'straight'     
            
        elif Ace == True and PHx[4] - PHx[3] == 9 and PHx[3] - PHx[2] == 1 and PHx[2] - PHx[1] == 1 and PHx[1] - PHx[0] == 1: #is there a stright where an Ace = 1?
            NS += 4000 + sum(PHx)-13 
            hand = 'straight'
            
        pairs = 0
        PairNum = []
        for k in range(2,15):    
            RankNum = PHx.count(k) 
            if RankNum > 1:
                pairs += 1
                PairNum.append(k) #Stores the pair 
            if RankNum > 2:
                NS += 3000 + PHx[2] #PHx[2]  is the middle card of the sorted hand - which is garunteed to be the card that is a 3 of a kind  
                hand = '3 of a kind'
            if RankNum > 3:
                NS += 4000  
                hand = '4 of a kind'
                
        if pairs > 0 and hand != '3 of a kind': 
            NS += 1000 + PairNum[0]
            hand = 'pair'
            if pairs > 1:
                NS += 1000 + PairNum[1] 
                hand = '2 pair'
        if pairs == 2 and hand == '3 of a kind':
            NS += 3000 
            hand = 'full house'
        if hand == 'highcard':
            NS += PHx[4]
            
        AllCards.append(PHx) #Appends all players' cards in case there is a tie
        playerNS.append(NS) #Records the NS of each player
        PlayerHands.append(hand) #Records what hand was played for each player
        PlayerCards = [card for sublist in AllCards for card in sublist] #[[a,b,c],[d,e,f]] -> [a,b,c,d,e,f]
        NSmax = Winner = -1
       
    #Finding the best hand from each player
    for B in range (0,players):   
        if playerNS[B] > NSmax: #If this player has the highest scoring hand
            NSmax = playerNS[B]
            Winner = B
        elif playerNS[B] == NSmax:  #If this player ties for the current highest scoring hand
            for L in range (0,5):
                if PlayerCards[(5*B)+L] > PlayerCards[(5*Winner)+L]: #Ranking each highest card in both player's hands
                    Winner = B
                    break
                if PlayerCards[(5*B)+L] < PlayerCards[(5*Winner)+L]:
                    break         
    PlayerScore[Winner] += 1   
    
    print(f" player_{Winner+1} won round {i+1} with a {PlayerHands[Winner]}")        
for V in range (0,players): 
   print (f" player_{V+1} won {PlayerScore[V]} rounds")
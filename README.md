# poker-hand-scorer
A poker hand evaluator that reads dealt cards from a file, scores each player’s hand according to standard poker rules (from High Card up to Royal Flush), determines round winners, and keeps a running tally of wins.
Cards dealt are placed in a text file such as Cards100x20.txt

The program assigns the first 5 cards of each row to player 1, and the next 5 cards to player 2 and so on.
In the event of a tie, the highest value card is compared between players until there is a winner

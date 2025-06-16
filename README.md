# poker-hand-scorer
A poker hand evaluator that reads dealt cards from a file, scores each player’s hand according to standard poker rules (from High Card up to Royal Flush), determines round winners, and keeps a running tally of wins.
Cards dealt are placed in a text file such as [Cards100x20.txt](https://github.com/A1Hansel/poker-hand-scorer/commit/9e66fee69f89fb05c7ca9767a05930aba4aacab1#diff-c02d17dcba8979e5673acb3a7922aa2a21dde3ae555b6e15df8e1187a0af3150)

The first 5 cards of each row to player 1, and the next 5 cards to player 2 and so on. The program determines the number of players based on the text file it is reading.
In the event of a tie, the highest value card is compared between players until there is a winner.

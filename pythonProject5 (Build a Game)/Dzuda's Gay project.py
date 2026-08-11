# 10 Airports - A to J positions
# 40 Suitcases - 4 each Airport
# 2 Airplanes - Player 1 & Player 2
# Starting cash R100 - Increased/Decreased
# Obstacle disks - Cheat codes

# Red disk - 'Emergency disk' / No movement or Paid ticket for both players(expensive)
# Green disk - 'Manipulation disk' / Shuffle all cards each airport to the right
# Yellow disk - 'Manipulation disk' / Override Any airport. Swap cards, Shuffle 1 card to the right
# Cyan disk - 'Attack disk' / Opponent Pays previous flight
# Black disk - 'Strategy disk' / Reveal cards at current airport
# Magenta disk - 'Tactical disk' / Add more money depending on difference in opponent suitcases

# Cost Matrix - Get from skeletal code

# Goal of Game - 2 PLAYERS FLY TO DIFFERENT AIRPORTS. SUITCASES TO BE COLLECTED FROM 1-10 ORDER. FIRST PLAYER
# TO COLLECT IN ORDER WINS. DISKS MAY BE USED FOR ADVANTAGE AND DISRUPTION OVER OTHER PLAYER PURPOSES.
# FLYING COSTS MONEY. FLIP ONCE = TO 1 TURN. IF NO NUMBER FOUND AT AIRPORT, FLY TO OTHERS. REMEMBER
# ONLY 4 SUITCASES PER AIRPORT AND MAY NOT CONTAIN THE NUMBER YOU WANT (USE DISKS WISELY).

# win - IF ALL SUITCASES ARE TAKEN IN ORDER
# lose - IF NO MONEY LEFT, IF LANDS ON ALL CARDS ALREADY FLIPPED AIRPORT, IF NO USEFUL DISKS LEFT

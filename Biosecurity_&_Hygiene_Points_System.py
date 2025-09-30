# ===============================
# Biosecurity & Hygiene Points System
# ===============================

# Data Structures
BiosecurityPointsTable = {}   # Dictionary: {farmer_id: points}

# Function: Award points based on compliance
def update_biosecurity_points(farmer_id, vaccination_on_time, hygiene_submitted, missed_update):
    if vaccination_on_time:
        BiosecurityPointsTable[farmer_id] = BiosecurityPointsTable.get(farmer_id, 0) + 20
    if hygiene_submitted:
        BiosecurityPointsTable[farmer_id] = BiosecurityPointsTable.get(farmer_id, 0) + 10
    if missed_update:
        BiosecurityPointsTable[farmer_id] = BiosecurityPointsTable.get(farmer_id, 0) - 5

# Function: Generate leaderboard
def generate_leaderboard(top_n):
    sorted_leaderboard = sorted(
        BiosecurityPointsTable.items(), 
        key=lambda x: x[1], 
        reverse=True
    )
    return sorted_leaderboard[:top_n]

# Function: Provide rewards to top farmers
def reward_top_farmers(top_n):
    leaderboard = generate_leaderboard(top_n)
    for farmer, points in leaderboard:
        print(f"Farmer {farmer} is in top {top_n} with {points} points. Access granted to market insights.")

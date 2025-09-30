# ===============================
# Training Points Allocation System
# ===============================

# Data Structures
TrainingPointsTable = {}   # Dictionary: {farmer_id: points}

# Sample module database
Modules = {
    1: {"name": "Avian Flu Module", "points": 50},
    2: {"name": "Pigsty Hygiene Module", "points": 30},
    3: {"name": "Vaccination Awareness", "points": 40}
}

# Sample completion records
CompletedModules = {
    # farmer_id: [list of completed module_ids]
}

# ===============================
# Helper Functions
# ===============================

def check_module_completion(farmer_id, module_id):
    """
    Check if the farmer has completed the module.
    Returns True if completed, False otherwise.
    """
    completed = CompletedModules.get(farmer_id, [])
    return module_id in completed

def get_assigned_points(module_id):
    """
    Get the points assigned to the module.
    """
    return Modules.get(module_id, {}).get("points", 0)

# ===============================
# Main Functions
# ===============================

# Function: Award points for completed modules
def award_training_points(farmer_id, module_id):
    if check_module_completion(farmer_id, module_id):
        points = get_assigned_points(module_id)
        TrainingPointsTable[farmer_id] = TrainingPointsTable.get(farmer_id, 0) + points
        print(f"{points} points awarded to Farmer {farmer_id}")
    else:
        print("Module not completed. No points awarded.")

# Function: Redeem points for product discounts
def redeem_points(farmer_id, points_requested):
    if TrainingPointsTable.get(farmer_id, 0) >= points_requested:
        TrainingPointsTable[farmer_id] -= points_requested
        print(f"Redeemed {points_requested} points for Farmer {farmer_id}")
        return True
    else:
        print("Not enough points to redeem.")
        return False

# ===============================
# Example Usage
# ===============================

# Farmer 101 completes module 1 and 2
CompletedModules[101] = [1, 2]

# Award points
award_training_points(101, 1)  # Output: 50 points awarded to Farmer 101
award_training_points(101, 2)  # Output: 30 points awarded to Farmer 101

# Redeem points
redeem_points(101, 60)         # Output: Redeemed 60 points for Farmer 101
redeem_points(101, 30)         # Output: Not enough points to redeem

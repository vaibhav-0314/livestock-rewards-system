# ===============================
# Training Points Allocation System
# ===============================

# Data Structures
TrainingPointsTable = {}   # Dictionary: {farmer_id: points}

# Dummy function to check module completion
def check_module_completion(farmer_id, module_id):
    # Replace this logic with actual completion check
    return True

# Function: Award points for completed modules
def award_training_points(farmer_id, module_id):
    if check_module_completion(farmer_id, module_id):
        points = get_assigned_points(module_id)
        TrainingPointsTable[farmer_id] = TrainingPointsTable.get(farmer_id, 0) + points
        print(f"{points} awarded to Farmer {farmer_id}")
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

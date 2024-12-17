from itertools import product

def calculate_macros(weights, foods):
    """
    Calculate total macros and calories based on ingredient weights and macros.
    
    Args:
        weights (list): List of ingredient weights (in grams).
        foods (list of dict): List of dictionaries containing macros and calories per 100g for each ingredient.
    
    Returns:
        dict: Total protein, carbs, fat, and calories.
    """
    total_macros = {"protein": 0, "carbs": 0, "fat": 0, "calories": 0}
    
    for weight, food in zip(weights, foods):
        total_macros["protein"] += food["protein"] * weight / 100
        total_macros["carbs"] += food["carbs"] * weight / 100
        total_macros["fat"] += food["fat"] * weight / 100
        total_macros["calories"] += food["calories"] * weight / 100
    
    return total_macros


def optimize_macros(target_macros, foods, weight_ranges):
    """
    Brute-force optimization to find food weights that meet macro goals.

    Args:
        target_macros (dict): Target macros for protein, carbs, and fat.
        foods (list of dict): List of food macro and calorie data.
        weight_ranges (list of range): Ranges for possible weights of each food.

    Returns:
        dict: Best food weights and corresponding macro totals.
    """
    best_diff = float('inf')
    best_weights = None
    best_macros = None

    # Generate all weight combinations using product
    for weights in product(*weight_ranges):
        macros = calculate_macros(weights, foods)
        diff = (
            abs(macros["protein"] - target_macros["protein"]) +
            abs(macros["carbs"] - target_macros["carbs"]) +
            abs(macros["fat"] - target_macros["fat"])
        )
        
        if diff < best_diff:
            best_diff = diff
            best_weights = weights
            best_macros = macros

    return {"weights": best_weights, "macros": best_macros}


# Define food data (macros and calories per 100g)
foods = [
    {"name": "chicken_thigh", "protein": 25.0, "carbs": 0.0, "fat": 10.0, "calories": 225},  # Chicken thigh
    {"name": "white_rice", "protein": 2.7, "carbs": 28.0, "fat": 0.3, "calories": 130},    # White rice
    {"name": "cooking_oil", "protein": 0.0, "carbs": 0.0, "fat": 100.0, "calories": 900},  # Cooking oil
]

# Target macros
target_macros = {"protein": 130, "carbs": 360, "fat": 85}

# Define weight ranges for each food
weight_ranges = [
    range(300, 1000),  # Chicken thighs: 300g to 1000g
    range(500, 2000),  # White rice: 500g to 2000g
    range(0, 100)      # Oil: 0g to 100g
]

# Run optimization
result = optimize_macros(target_macros, foods, weight_ranges)

# Print results
print("Optimal Food Weights:")
for i, food in enumerate(foods):
    print(f"- {food['name']}: {result['weights'][i]}g")

print("\nMacronutrient Totals:")
for key, value in result["macros"].items():
    print(f"- {key.capitalize()}: {value:.1f}")

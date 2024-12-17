# Macro Targets
target_protein = 130  # grams
target_carbs = 360    # grams
target_fat = 85       # grams

# Macronutrient breakdown per 100 grams of food
# Chicken thigh, skin-on, baked
protein_per_100g_chicken = 25.0  # grams
fat_per_100g_chicken = 10.0      # grams
carbs_per_100g_chicken = 0.0     # grams

# White rice, cooked
protein_per_100g_rice = 2.7      # grams
carbs_per_100g_rice = 28.0       # grams
fat_per_100g_rice = 0.3          # grams

# Calorie breakdown per gram
calories_per_g_chicken = 2.25    # kcal
calories_per_g_rice = 1.3        # kcal
calories_per_g_oil = 9.0         # kcal

# Function to calculate macros
def calculate_macros(chicken_g, rice_g):
    protein = (protein_per_100g_chicken / 100) * chicken_g + (protein_per_100g_rice / 100) * rice_g
    carbs = (carbs_per_100g_chicken / 100) * chicken_g + (carbs_per_100g_rice / 100) * rice_g
    fat = (fat_per_100g_chicken / 100) * chicken_g + (fat_per_100g_rice / 100) * rice_g
    return protein, carbs, fat

# Brute-force search for approximate solution
best_diff = float('inf')
best_chicken = 0
best_rice = 0
best_macros = None

# Iterate over possible chicken and rice weights
for chicken_g in range(300, 1000):  # grams of chicken
    for rice_g in range(500, 2000):  # grams of rice
        protein, carbs, fat = calculate_macros(chicken_g, rice_g)
        # Calculate total difference from target macros
        diff = abs(protein - target_protein) + abs(carbs - target_carbs) + abs(fat - target_fat)
        if diff < best_diff:
            best_diff = diff
            best_chicken = chicken_g
            best_rice = rice_g
            best_macros = (protein, carbs, fat)

# Calculate remaining fat and required oil
remaining_fat = target_fat - best_macros[2]
oil_needed_g = remaining_fat / 1  # since oil is 100% fat

# Calculate calories
calories_chicken = best_chicken * calories_per_g_chicken
calories_rice = best_rice * calories_per_g_rice
calories_oil = oil_needed_g * calories_per_g_oil
total_calories = calories_chicken + calories_rice + calories_oil

# Display results
print(f"Daily Food Plan:")
print(f"- Chicken Thighs (baked, skin-on): {best_chicken}g")
print(f"- White Rice (cooked): {best_rice}g")
print(f"- Cooking Oil: {oil_needed_g:.1f}g")

print("\nMacronutrient Breakdown:")
print(f"- Protein: {best_macros[0]:.1f}g")
print(f"- Carbs: {best_macros[1]:.1f}g")
print(f"- Fat: {target_fat:.1f}g")

print("\nCalorie Breakdown:")
print(f"- Chicken Thighs: {calories_chicken:.0f} kcal")
print(f"- White Rice: {calories_rice:.0f} kcal")
print(f"- Cooking Oil: {calories_oil:.0f} kcal")
print(f"Total Calories: {total_calories:.0f} kcal")

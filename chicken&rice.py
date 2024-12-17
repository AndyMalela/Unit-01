#all are grams
target_protein = 130
target_carbs = 360
target_fat = 85

#chicken thighs
protein_per_100_chicken = 25.0
carbs_per_100_chicken = 10.0
fat_per_100_chicken = 10.0

#cooked white rice
protein_per_100_rice = 2.7
carbs_per_100_rice = 28.0
fat_per_100_rice = 0.3

#kilocalorie
calories_per_g_chicken = 2
calories_per_g_rice = 1.3
calories_per_g_canola = 8.9

#calculates all macros for given chicken and rice grams
def calc_macros(chicken_g, rice_g):
    total_protein = (protein_per_100_chicken/100)*chicken_g+(protein_per_100_rice/100)*rice_g
    total_carbs = (carbs_per_100_chicken/100)*chicken_g+(carbs_per_100_rice/100)*rice_g
    total_fat = (fat_per_100_chicken/100)*chicken_g+(fat_per_100_rice/100)*rice_g
    return total_protein, total_carbs, total_fat

diff_best = float(10000000000000000000000000000000)
best_chicken = 0
best_rice = 0
best_macros = None #why is this none?

#this should iterate over all possible grs of food and calculate the macros, then 
for chicken_g in range(200,400):
    for rice_g in range(100,2000):
        protein, carbs, fat = calc_macros(chicken_g, rice_g)
        #absolute value with python, how far is macro value from target?
        macro_diff = abs(target_protein-protein) + abs(target_carbs-carbs) + abs(target_fat-fat)
        if macro_diff < diff_best:
            diff_best = macro_diff
            best_chicken = chicken_g
            best_rice = rice_g
            best_macros = (protein, carbs, fat)

remaining_fat = target_fat - best_macros[2]


#calculate calories
total_calorie_chicken = best_chicken*calories_per_g_chicken
total_calorie_rice = best_rice*calories_per_g_rice
total_calories_oil = remaining_fat*calories_per_g_canola #if using canola
total_calories = total_calorie_chicken+total_calorie_rice+total_calories_oil

            
print(f"Daily Food Plan:")
print(f"-Chicken Thighs (baked, skin-on): {best_chicken}g")
print(f"-White Rice (cooked): {best_rice}g")
print(f"-Remaining fat: {remaining_fat:.1f}g")

print("\nMacronutrient Breakdown:")
print(f"-Protein: {best_macros[0]:.1f}g")
print(f"-Carbs: {best_macros[1]:.1f}g")
print(f"-Fat: {target_fat:.1f}g")

print("\nCalorie Breakdown:")
print(f"-Chicken Thighs: {total_calorie_chicken:.0f} kcal")
print(f"-White Rice: {total_calorie_rice:.0f} kcal")
print(f"-Cooking Oil: {total_calories_oil:.0f} kcal")
print(f"Total Calories: {total_calories:.0f} kcal")
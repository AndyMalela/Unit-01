#include <stdio.h>
#include <math.h>

// Constants for the number of foods and macro targets
#define NUM_FOODS 3
#define PROTEIN_TARGET 130
#define CARBS_TARGET 360
#define FAT_TARGET 85

// Food structure to hold macros and calories per 100g
typedef struct {
    char name[20];
    double protein;
    double carbs;
    double fat;
    double calories;
} Food;

// Function to calculate total macros and calories
void calculate_macros(double weights[], Food foods[], double *protein, double *carbs, double *fat, double *calories) {
    *protein = 0; *carbs = 0; *fat = 0; *calories = 0;

    for (int i = 0; i < NUM_FOODS; i++) {
        *protein += (foods[i].protein * weights[i]) / 100;
        *carbs   += (foods[i].carbs   * weights[i]) / 100;
        *fat     += (foods[i].fat     * weights[i]) / 100;
        *calories += (foods[i].calories * weights[i]) / 100;
    }
}

// Main optimization function
void optimize_macros(Food foods[], double weight_ranges[][2]) {
    double best_diff = 1e9;  // Initialize a large value
    double best_weights[NUM_FOODS] = {0};
    double best_protein, best_carbs, best_fat, best_calories;

    // Brute-force search over weight ranges
    for (double w1 = weight_ranges[0][0]; w1 <= weight_ranges[0][1]; w1 += 10) {
        for (double w2 = weight_ranges[1][0]; w2 <= weight_ranges[1][1]; w2 += 10) {
            for (double w3 = weight_ranges[2][0]; w3 <= weight_ranges[2][1]; w3 += 5) {
                double weights[NUM_FOODS] = {w1, w2, w3};
                double protein, carbs, fat, calories;
                calculate_macros(weights, foods, &protein, &carbs, &fat, &calories);

                double diff = fabs(protein - PROTEIN_TARGET) +
                              fabs(carbs - CARBS_TARGET) +
                              fabs(fat - FAT_TARGET);

                if (diff < best_diff) {
                    best_diff = diff;
                    best_weights[0] = w1;
                    best_weights[1] = w2;
                    best_weights[2] = w3;
                    best_protein = protein;
                    best_carbs = carbs;
                    best_fat = fat;
                    best_calories = calories;
                }
            }
        }
    }

    // Print the results
    printf("Optimal Food Weights:\n");
    for (int i = 0; i < NUM_FOODS; i++) {
        printf("- %s: %.0f g\n", foods[i].name, best_weights[i]);
    }

    printf("\nMacronutrient Totals:\n");
    printf("- Protein: %.1f g\n", best_protein);
    printf("- Carbs: %.1f g\n", best_carbs);
    printf("- Fat: %.1f g\n", best_fat);
    printf("- Calories: %.1f kcal\n", best_calories);
}

int main() {
    // Define the foods (name, protein, carbs, fat, calories per 100g)
    Food foods[NUM_FOODS] = {
        {"Chicken Thigh", 25.0, 0.0, 10.0, 225.0},
        {"White Rice", 2.7, 28.0, 0.3, 130.0},
        {"Cooking Oil", 0.0, 0.0, 100.0, 900.0}
    };

    // Define weight ranges for each food (min, max)
    double weight_ranges[NUM_FOODS][2] = {
        {300, 1000},  // Chicken Thigh: 300g to 1000g
        {500, 2000},  // White Rice: 500g to 2000g
        {0, 100}      // Cooking Oil: 0g to 100g
    };

    // Run the optimization
    optimize_macros(foods, weight_ranges);

    return 0;
}

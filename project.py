def get_workout_plan(age, weight, activity_level, gender, goal):
    """Returns a workout plan based on age, weight, activity level, gender, and goal."""
    workouts = {
        "weight_loss": {
            "low": ["Walking (45 mins)", "Light Yoga", "Stretching"],
            "moderate": ["Jogging (30 mins)", "Cycling (30 mins)", "Bodyweight exercises"],
            "high": ["HIIT (30 mins)", "Running (5km)", "Strength Training (Full Body)"]
        },
        "muscle_gain": {
            "low": ["Bodyweight exercises", "Basic resistance training"],
            "moderate": ["Weightlifting (Full Body)", "Push-ups & Pull-ups", "Cycling"],
            "high": ["Heavy Strength Training (5x/week)", "Deadlifts, Squats, Bench Press"]
        },
        "maintenance": {
            "low": ["Yoga", "Walking (30 mins)", "Stretching"],
            "moderate": ["Jogging", "Swimming", "Strength training (light)"],
            "high": ["Full-body strength training", "HIIT", "Sports (Basketball, Football)"]
        }
    }
    
    return workouts.get(goal, {}).get(activity_level, ["Invalid input. Please try again."])


def get_diet_plan(weight, activity_level, gender, goal):
    """Returns a diet plan based on weight, activity level, gender, and goal."""
    diets = {
        "weight_loss": {
            "low": ["Balanced diet, reduce carbs", "More fruits & vegetables", "Lean proteins (chicken, tofu)"],
            "moderate": ["Protein-rich diet (chicken, fish, eggs)", "Complex carbs (brown rice, quinoa)", "Healthy fats (nuts, avocado)"],
            "high": ["More protein (turkey, fish, eggs)", "Hydration (2-3L water)", "Green tea for metabolism"]
        },
        "muscle_gain": {
            "low": ["More protein (chicken, fish, lentils)", "Healthy fats (olive oil, avocado)", "Stay hydrated"],
            "moderate": ["High protein (steak, eggs, whey protein)", "Complex carbs (sweet potatoes, brown rice)", "More calories"],
            "high": ["Very high protein intake (1.5g per kg of body weight)", "More meals (5-6 per day)", "Creatine & supplements"]
        },
        "maintenance": {
            "low": ["Balanced diet with all macros", "More fiber (vegetables, fruits)", "Drink enough water"],
            "moderate": ["Protein & carb balance", "Healthy snacks (nuts, yogurt)", "Moderate portions"],
            "high": ["Keep calories balanced", "More protein post-workout", "Stay hydrated"]
        }
    }

    return diets.get(goal, {}).get(activity_level, ["Invalid input. Please try again."])

# User input
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
gender = input("Enter your gender (male/female): ").strip().lower()
activity_level = input("Enter your activity level (low, moderate, high): ").strip().lower()
goal = input("Enter your goal (weight_loss, muscle_gain, maintenance): ").strip().lower()

# Get workout and diet plans
workout_plan = get_workout_plan(age, weight, activity_level, gender, goal)
diet_plan = get_diet_plan(weight, activity_level, gender, goal)

# Output results
print("\nWorkout Plan:")
for workout in workout_plan:
    print(f"- {workout}")

print("\nDiet Plan:")
for diet in diet_plan:
    print(f"- {diet}")
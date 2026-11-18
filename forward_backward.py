# Rule-Based Expert System

rules = {
    "fever": "flu",
    "cough": "cold",
    "flu": "take_rest",
    "cold": "take_medicine",
    "take_rest": "recover"
}

# Forward Chaining
def forward_chaining(facts):
    print("\n--- Forward Chaining ---")

    while True:
        found = False

        for condition, result in rules.items():
            if condition in facts and result not in facts:
                facts.append(result)
                print("New Fact:", result)
                found = True

        if not found:
            break

    print("Final Facts:", facts)


# Backward Chaining
def backward_chaining(goal, facts):
    print("Checking Goal:", goal)

    if goal in facts:
        print(goal, "is TRUE")
        return True

    for condition, result in rules.items():
        if result == goal:
            if backward_chaining(condition, facts):
                print(goal, "is TRUE")
                return True

    print(goal, "is FALSE")
    return False


# Main Program
initial_facts = ["fever"]

print("Initial Facts:", initial_facts)

# Forward Chaining
forward_facts = initial_facts.copy()
forward_chaining(forward_facts)

# Backward Chaining
print("\n--- Backward Chaining ---")

backward_facts = initial_facts.copy()
goal = "recover"

if backward_chaining(goal, backward_facts):
    print("\nDecision: Patient may recover after taking rest.")
else:
    print("\nDecision: Goal cannot be proved.")

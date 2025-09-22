data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]

h = ["ϕ", "ϕ", "ϕ", "ϕ", "ϕ", "ϕ"]
G = [["?", "?", "?", "?", "?", "?"]]  

# Iterate through the data
for attribute in data:
    if attribute[6] == "Yes":
        # Update S: Specific Hypothesis
        for i in range(len(h)):
            if h[i] == "ϕ":
                h[i] = attribute[i]
            elif h[i] != attribute[i]:
                h[i] = "?"
        # Remove inconsistent hypotheses from G
        G = [g for g in G if all(g[i] == "?" or g[i] == h[i] for i in range(len(h)))]
    else:
        # Update G: General Hypotheses
        new_G = []
        for g in G:
            for i in range(len(h)):
                if g[i] == "?":
                    if attribute[i] != h[i]:  # Specialize g where it disagrees with negative example
                        temp = g[:]
                        temp[i] = h[i]
                        new_G.append(temp)
                elif g[i] != attribute[i]:
                    new_G.append(g)
        G = new_G

unique_G = []
for g in G:
    if g not in unique_G and g != ["?","?","?","?","?","?"]:
        unique_G.append(g)

print("The Final Hypothesis by Find-S:", h)
print("The Final Hypothesis by Find-G:", unique_G)

def predict(h, G, condition):
    # Check S
    for i in range(len(h)):
        if h[i] != "?" and h[i] != condition[i]:
            return "No"
    # Check G
    for g in G:
        if all(g[i] == "?" or g[i] == condition[i] for i in range(len(g))):
            return "Yes"
    return "No"

condition1 = ["Sunny", "Warm", "Normal", "Strong", "Cool", "Change"]
condition2 = ["Rainy", "Cold", "High", "Weak", "Cool", "Change"]

print("Possibility for Condition 1:", predict(h, unique_G, condition1))
print("Possibility for Condition 2:", predict(h, unique_G, condition2))
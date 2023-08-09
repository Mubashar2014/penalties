Drug=["Class A","Class B","Class C"]
Culpability=["Leading","Significiant","Lesser"]
Harm=[1,2,3,4]



penalties = {
        ('Class A', 'Leading', 1): '12 - 16 Years',
        ('Class A', 'Significant', 1): '9 - 12 Years',
        ('Class A', 'Lesser', 1): '6 - 9 Years',
        ('Class A', 'Leading', 2): '9 - 13 Years',
        ('Class A', 'Significant', 2): '6 1/2 - 10 Years',
        ('Class A', 'Lesser', 2): '3 1/2 - 7 Years',
        ('Class A', 'Leading', 3): '6 1/2 - 10 Years',
        ('Class A', 'Significant', 3): '3 1/2 - 7 Years',
        ('Class A', 'Lesser', 3): '2 - 4 1/2 Years',
        ('Class A', 'Leading', 4): '4 1/2 - 7 1/2 Years',
        ('Class A', 'Significant', 4): '2 - 5 Years',
        ('Class A', 'Lesser', 4): 'HCO - 3 Years',
        ('Class B', 'Leading', 1): '7 - 10 Years',
        ('Class B', 'Significant', 1): '5 - 7 Years',
        ('Class B', 'Lesser', 1): '2 1/2 - 5 Years',
        ('Class B', 'Leading', 2): '4 1/2 - 8 Years',
        ('Class B', 'Significant', 2): '2 1/2 - 5 Years',
        ('Class B', 'Lesser', 2): '26 wks - 3 Years',
        ('Class B', 'Leading', 3): '2 1/2 - 5 Years',
        ('Class B', 'Significant', 3): '26 wks - 3 Years',
        ('Class B', 'Lesser', 3): 'LCO - 26wks',
        ('Class B', 'Leading', 4): '26 wks - 3 Years',
        ('Class B', 'Significant', 4): 'MCO - 26 wks',
        ('Class B', 'Lesser', 4): 'BBF - MCO',
        ('Class C', 'Leading', 1): '4 - 8 Years',
        ('Class C', 'Significant', 1): '2 - 5 Years',
        ('Class C', 'Lesser', 1): '1 - 3 Years',
        ('Class C', 'Leading', 2): '2 - 5 Years',
        ('Class C', 'Significant', 2): '1 - 3 Years',
        ('Class C', 'Lesser', 2): '12 wks - 18 Mnths',
        ('Class C', 'Leading', 3): '1 - 3 Years',
        ('Class C', 'Significant', 3): '12 wks - 18 Mnths',
        ('Class C', 'Lesser', 3): 'LCO - 12 wks',
        ('Class C', 'Leading', 4): 'HCO - 18 Mnths',
        ('Class C', 'Significant', 4): 'LCO - 12 wks',
        ('Class C', 'Lesser', 4): 'BAF - MCO'
    }

def calculate_penalty(drug_class, culpability, harm):
    try:
        penalty = penalties[(drug_class, culpability, harm)]
        return penalty
    except KeyError:
        return "Penalty not found for the given combination"

# Input from user
drug_class = input("Enter drug class (Class A/B/C): ")
culpability = input("Enter culpability (Leading/Significant/Lesser): ")
harm = int(input("Enter harm (1/2/3/4): "))

# Calculate and display penalty
penalty = calculate_penalty(drug_class, culpability, harm)
print("Penalty:", penalty)
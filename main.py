
penalties = {
        ('Class A', 'Leading', 1): ('12 - 16 Years','14 years '),
        ('Class A', 'Significant', 1): ('9 - 12 Years','10 Years '),
        ('Class A', 'Lesser', 1): ('6 - 9 Years','7 Years '),
        ('Class A', 'Leading', 2): ('9 - 13 Years','11 years '),
        ('Class A', 'Significant', 2): ('6 1/2 - 10 Years','8 Years '),
        ('Class A', 'Lesser', 2): ('3 1/2 - 7 Years','5 Years '),
        ('Class A', 'Leading', 3): ('6 1/2 - 10 Years','8 1/2 Years '),
        ('Class A', 'Significant', 3): ('3 1/2 - 7 Years','4 1/2 Years '),
        ('Class A', 'Lesser', 3): ('2 - 4 1/2 Years','3 Years '),
        ('Class A', 'Leading', 4): ('4 1/2 - 7 1/2 Years','5 1/2 years '),
        ('Class A', 'Significant', 4): ('2 - 5 Years','3 1/2 Years '),
        ('Class A', 'Lesser', 4): ('HCO - 3 Years','18 Mnths'),
        ('Class B', 'Leading', 1): ('7 - 10 Years','8 Years '),
        ('Class B', 'Significant', 1): ('5 - 7 Years','5 1/2 Years '),
        ('Class B', 'Lesser', 1): ('2 1/2 - 5 Years','3 Years '),
        ('Class B', 'Leading', 2): ('4 1/2 - 8 Years','6 Years '),
        ('Class B', 'Significant', 2): ('2 1/2 - 5 Years','4 Years '),
        ('Class B', 'Lesser', 2): ('26 wks - 3 Years','1 Year '),
        ('Class B', 'Leading', 3): ('2 1/2 - 5 Years','4 Years '),
        ('Class B', 'Significant', 3): ('26 wks - 3 Years','1 Year'),
        ('Class B', 'Lesser', 3): ('LCO - 26wks','HCO'),
        ('Class B', 'Leading', 4): ('26 wks - 3 Years','18 Mnths '),
        ('Class B', 'Significant', 4): ('MCO - 26 wks','HCO'),
        ('Class B', 'Lesser', 4): ('BBF - MCO','LCO'),
        ('Class C', 'Leading', 1): ('4 - 8 Years','5 Years '),
        ('Class C', 'Significant', 1): ('2 - 5 Years','3 Years '),
        ('Class C', 'Lesser', 1): ('1 - 3 Years','18 Mnths '),
        ('Class C', 'Leading', 2): ('2 - 5 Years','3 1/2 Years '),
        ('Class C', 'Significant', 2): ('1 - 3 Years','18 Mnths '),
        ('Class C', 'Lesser', 2): ('12 wks - 18 Mnths','26 Wks'),
        ('Class C', 'Leading', 3): ('1 - 3 Years','18 Mnths '),
        ('Class C', 'Significant', 3): ('12 wks - 18 Mnths','26 Wks'),
        ('Class C', 'Lesser', 3): ('LCO - 12 wks','HCO'),
        ('Class C', 'Leading', 4): ('HCO - 18 Mnths','26 Wks '),
        ('Class C', 'Significant', 4): ('LCO - 12 wks','HCO'),
        ('Class C', 'Lesser', 4): ('BAF - MCO','LCO ')
    }


possession_of_a_drug={
        ('Class A'): ('12 - 16 Years','14 years '),
        ('Class B'): ('9 - 12 Years','10 Years '),
        ('Class C'): ('6 - 9 Years','7 Years ')
}

robbery_street = {
    (1, 'High'): ('7 - 12 Years', '8 Years'),
    (1, 'Medium'): ('4 - 8 Years', '5 Years'),
    (1, 'Lesser'): ('3 - 6 Years', '4 Years'),
    (2, 'High'): ('4 - 8 Years', '5 Years'),
    (2, 'Medium'): ('3 - 6 Years', '4 Years'),
    (2, 'Lesser'): ('1 - 4 Years', '2 Years'),
    (3, 'High'): ('3 - 6 Years', '4 Years'),
    (3, 'Medium'): ('1 - 4 Years', '2 Years'),
    (3, 'Lesser'): ('HCO - 3 Years', '1 Year')
}

robbery_professional = {
    (1, 'High'): ('16 - 20 Years', '16 Years'),
    (1, 'Medium'): ('7 - 14 Years', '9 Years'),
    (1, 'Lesser'): ('4 - 8 Years', '5 Years'),
    (2, 'High'): ('7 - 14 Years', '9 Years'),
    (2, 'Medium'): ('4 - 8 Years', '5 Years'),
    (2, 'Lesser'): ('2 - 5 Years', '3 Years'),
    (3, 'High'): ('4 - 8 Years', '5 Years'),
    (3, 'Medium'): ('2 - 5 Years', '3 Years'),
    (3, 'Lesser'): ('18 Mnths - 4 Years', '2 Years')
}


robbery_residential = {
    (1, 'High'): ('10 - 16 years', '13 years'),
    (1, 'Medium'): ('6 - 10 Years', '8 Years'),
    (1, 'Lesser'): ('4 - 8 Years', '5 Years'),
    (2, 'High'): ('6 - 10 Years', '8 Years'),
    (2, 'Medium'): ('4 - 8 Years', '5 Years'),
    (2, 'Lesser'): ('2 - 5 Years', '3 Years'),
    (3, 'High'): ('4 - 8 Years', '5 Years'),
    (3, 'Medium'): ('2 - 5 Years', '3 Years'),
    (3, 'Lesser'): ('1 - 3 Years', '18 Mnths')
}



burglary_domestic = {
    (1, 'High'): ('2 - 6 Years', '3 Years'),
    (1, 'Medium'): ('1 - 4 Years', '2 Years'),
    (1, 'Lesser'): ('6 Mnths - 3 Years', '1 1/2 Years'),
    (2, 'High'): ('1 - 4 Years', '2 Years'),
    (2, 'Medium'): ('6 Mnths - 3 Years', '1 1/2 Years'),
    (2, 'Lesser'): ('HCO - 2 years', '1 Year'),
    (3, 'High'): ('6 Mnths - 3 Years', '1 1/2 Years'),
    (3, 'Medium'): ('HCO - 2 years', '1 Year'),
    (3, 'Lesser'): ('LCO - 6 Mnths', 'HCO')
}

burglary_agravated = {
    (1, 'High'): ('9 - 13 Years', '10 Years'),
    (1, 'Medium'): ('6 - 11 Years', '8 Years'),
    (1, 'Lesser'): ('4 - 9 Years', '6 Years'),
    (2, 'High'): ('6 - 11 Years', '8 Years'),
    (2, 'Medium'): ('4 - 9 Years', '6 Years'),
    (2, 'Lesser'): ('2 - 6 Years', '4 Years'),
    (3, 'High'): ('4 - 9 Years', '6 Years'),
    (3, 'Medium'): ('2 - 6 Years', '4 Years'),
    (3, 'Lesser'): ('1 - 4 Years', '2 Years')
}


burglary_non_domestic = {
    (1, 'High'): ('1 - 5 Years', '2 Years'),
    (1, 'Medium'): ('HCO - 2 Years', '1 Year'),
    (1, 'Lesser'): ('MCO - 1 Year', '6 Mnths'),
    (2, 'High'): ('HCO - 2 Years', '1 Year'),
    (2, 'Medium'): ('MCO - 1 Year', '6 Mnths'),
    (2, 'Lesser'): ('LCO - HCO', 'MCO'),
    (3, 'High'): ('MCO - 1 Year', '6 Mnths'),
    (3, 'Medium'): ('LCO - HCO', 'MCO'),
    (3, 'Lesser'): ('Disc - LCO', 'BBF')
}




theft = {
    (1, 'High'): ('2 1/2 - 6 Years', '3 1/2 Years'),
    (1, 'Medium'): ('1 - 3 1/2 Years', '2 Years'),
    (1, 'Lesser'): ('26 Wks - 2 Years', '1 Year'),
    (2, 'High'): ('1 - 3 1/2 Years', '2 Years'),
    (2, 'Medium'): ('26 Wks - 2 Years', '1 Year'),
    (2, 'Lesser'): ('LCO - 36 Wks', 'HCO'),
    (3, 'High'): ('26 Wks - 2 Years', '1 Year'),
    (3, 'Medium'): ('LCO - 36 Wks', 'HCO'),
    (3, 'Lesser'): ('BBF - LCO', 'BCF'),
    (4, 'High'): ('MCO - 36 Wks', 'HCO'),
    (4, 'Medium'): ('BCF - MCO', 'LCO'),
    (4, 'Lesser'): ('Disc - BCF', 'BBF')
}

gbg_s_18 = {
    (1, 'High'): ('10 - 16 Years', '12 Years'),
    (1, 'Medium'): ('6 - 10 Years', '7 Years'),
    (1, 'Lesser'): ('4 - 7 Years', '5 Years'),
    (2, 'High'): ('6 - 10 Years', '7 Years'),
    (2, 'Medium'): ('4 - 7 Years', '5 Years'),
    (2, 'Lesser'): ('3 - 6 Years', '4 Years'),
    (3, 'High'): ('4 - 7 Years', '5 Years'),
    (3, 'Medium'): ('3 - 6 Years', '4 Years'),
    (3, 'Lesser'): ('2 - 4 Years', '3 Years')
}
gbg_s_20 = {
    (1, 'High'): ('3 - 4 1/2 Years', '4 Years'),
    (1, 'Medium'): ('2 - 4 Years', '3 Years'),
    (1, 'Lesser'): ('1 - 3 Years', '2 Years'),
    (2, 'High'): ('2 - 4 Years', '3 Years'),
    (2, 'Medium'): ('1 - 3 Years', '2 Years'),
    (2, 'Lesser'): ('HCO - 2 Years', '1 Year'),
    (3, 'High'): ('1 - 3 Years', '2 Years'),
    (3, 'Medium'): ('HCO - 2 Years', '1 Year'),
    (3, 'Lesser'): ('MCO - 1 Year', '26 Wks')
}


abh_s_29 = {
    1: ('1 - 3 Years', '1 1/2 Years'),
    2: ('LCO - 51 Wks', '26 Wks'),
    3: ('BAF - HCO', 'MCO')
}



assault_police = {
    1: ('LCO - 26 Wks', '12 Wks'),
    2: ('LCO - HCO', 'MCO'),
    3: ('BAF - BCF', 'BBF')
}

abh_s_47 = {
    (1, 'A'): ('1 1/2 - 4 Years', '2 1/12 Years'),
    (1, 'B'): ('36 Wks - 2 1/2 Years', '1 1/2 Years'),
    (1, 'C'): ('HCO - 1 1/2 Years', '36 Wks'),
    (2, 'A'): ('36 Wks - 2 1/2 Years', '1 1/2 Years'),
    (2, 'B'): ('HCO - 1 1/2 Years', '36 Wks'),
    (2, 'C'): ('LCO - 36 Wks', 'HCO'),
    (3, 'A'): ('HCO - 1 1/2 Years', '36 Wks'),
    (3, 'B'): ('LCO - 36 Wks', 'HCO'),
    (3, 'C'): ('BBF - 26 Wks', 'MCO')
}


rape = {
    (1, 'A'): ('13 - 19 Years', '15 Years'),
    (1, 'B'): ('10 - 15 Years', '12 Years'),
    (2, 'A'): ('9 - 13 Years', '10 Years'),
    (2, 'B'): ('7 - 9 Years', '8 Years'),
    (3, 'A'): ('6 - 9 Years', '7 Years'),
    (3, 'B'): ('4 - 7 Years', '5 Years')
}

assault_by_penetration = {
    (1, 'High'): ('13 - 19 Years', '15 Years'),
    (1, 'Medium'): ('10 - 15 Years', '12 Years'),
    (1, 'Lesser'): ('5 - 13 Years', '8 Years'),
    (2, 'High'): ('4 - 9 Years', '6 Years'),
    (2, 'Medium'): ('2 - 6 Years', '4 Years'),
    (2, 'Lesser'): ('HCO - 4 Years', '2 Years')
}

sexual_assault = {
    (1, 'A'): ('3 - 7 Years', '4 Years'),
    (1, 'B'): ('2 - 4 Years', '2 1/2 Years'),
    (2, 'A'): ('1 - 4 Years', '2 Years'),
    (2, 'B'): ('HCO - 2 Years', '1 Year'),
    (3, 'A'): ('HCO - 1 Year', '26 Wks'),
    (3, 'B'): ('MCO - 26 Wks', 'HCO')
}

rape_13 = {
    (1, 'A'): ('13 - 19 Years', '16 Years'),
    (1, 'B'): ('11 - 17 Years', '13 Years'),
    (2, 'A'): ('11 - 17 Years', '13 Years'),
    (2, 'B'): ('8 - 13 Years', '10 Years'),
    (3, 'A'): ('8 - 13 Years', '11 Years'),
    (3, 'B'): ('6 - 11 Years', '8 Years')
}

assault_13 = {
    (1, 'A'): ('13 - 19 Years', '16 Years'),
    (1, 'B'): ('11 - 17 Years', '13 Years'),
    (2, 'A'): ('7 - 15 Years', '11 Years'),
    (2, 'B'): ('5 - 13 Years', '8 Years'),
    (3, 'A'): ('4 - 9 Years', '6 Years'),
    (3, 'B'): ('2 - 6 Years', '4 Years')
}

sexual_assault_13 = {
    (1, 'A'): ('4 - 9 Years', '6 Years'),
    (1, 'B'): ('3 - 7 Years', '4 Years'),
    (2, 'A'): ('3 - 7 Years', '4 Years'),
    (2, 'B'): ('1 - 4 Years', '2 Years'),
    (3, 'A'): ('26 Wks - 2 Years', '1 Year'),
    (3, 'B'): ('HCO - 1 Year', '26 Wks')
}







def calculate_penalty(drug_class, culpability, harm):
    try:
        penalty = penalties[(drug_class, culpability, harm)]
        return penalty
    except KeyError:
        return "Penalty not found for the given combination"




drug_class = input("Enter drug class (Class A/B/C): ")
culpability = input("Enter culpability (Leading/Significant/Lesser): ")
harm = int(input("Enter harm (1/2/3/4): "))


penalty = calculate_penalty(drug_class, culpability, harm)
print("Penalty:", penalty[1])
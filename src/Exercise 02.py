from typing import Dict, List, Tuple
from random import shuffle
from collections import OrderedDict

capitals: Dict[str, str] = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}

# Create a list of tuples from the dictionary.
# This is done because pairs need to be picked at random from the dictionary.
# Note that dict.popitem() is NOT applicable. Arbitrary does not equal random!
# random.shuffle requires a type that can be indexed.
pairs: List[Tuple[str, str]] = list(capitals.items())
shuffle(pairs) # Shuffle the list.

# Score counters.
correct: int = 0
incorrect: int = 0

while pairs: # Loops until the list is empty.
    # Pops the last item in the list and unpacks the tuple it returns.
    state, capital = pairs.pop()
    answer: str = input(F"Enter the capital of {state}: ").lower()

    # Checks the user's answer and updates the score counters accordingly.
    if answer == capital.lower():
        correct += 1
    else:
        incorrect += 1

print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")

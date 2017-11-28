from typing import Dict

rooms: Dict[str, int] = {
    "CS101": 3004,
    "CS102": 4501,
    "CS103": 6755,
    "NT110": 1244,
    "CM241": 1411}

instructors: Dict[str, str] = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"}

times: Dict[str, str] = {
    "CS101": "8:00 a.m.",
    "CS102": "9:00 a.m.",
    "CS103": "10:00 a.m.",
    "NT110": "11:00 a.m.",
    "CM241": "1:00 p.m."}

inp: str = input("Enter a course number: ")

if inp not in rooms.keys():
    print(f"Could not find a course with the number '{inp}'.")
else:
    print(f"Room Number: {rooms[inp]}")
    print(f"Instructor: {instructors[inp]}")
    print(f"Meeting Time: {times[inp]}")

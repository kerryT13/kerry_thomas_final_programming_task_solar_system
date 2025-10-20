# Kerry Thomas
# Final Programming Task – Solar System (20 Oct 2025)
# GitHub Repository: https://github.com/kerryT13/kerry_thomas_final_programming_task_solar_system

class Moon:
    def __init__(self, name):
        self.name =name
    
    def __str__(self):
        return self.name

class Planet: 
    def __init__(self, name, mass, distance, position, moon_names=None, moon_count=0, description=""):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.position = position
        self.moon_count = moon_count
        self.moons = [Moon(name) for name in (moon_names or [])]  # main moons only
        self.description = description

    def summary (self):
        names_text=(", ".join(str(m) for m in self.moons)) if self.moons else "None listed"
        count = self.moon_count if self.moon_count is not None else len(self.moons)
        moons_text = f"{count} moon(s) - Main moon names are: {names_text}"
    
        return ( 
            f"\n{self.name}\n"
            f"Mass: {self.mass}\n"
            f"Distance from Sun: {self.distance}\n"
            f"Position: {self.position}\n"
            f"{moons_text}\n"
            f"Description: {self.description}\n"
        )

# Planet data was taken from wikipedia. 
planets = {

    "Sun": Planet(
        name = "Sun",
        mass = "1.989 x 10^30 kg", 
        distance = "Centre of the solar system.", 
        position = 0, 
        moon_names = [],
        moon_count = 0,
        description = ("The Sun is the star at the centre of the Solar System, providing light and heat to the planets.")
    ),
    
    "Mercury": Planet(
        name = "Mercury",
        mass = "3.30 x 10^23 kg", 
        distance = "57.9 million km", 
        position = 1, 
        moon_names = [],
        moon_count = 0,
        description = (
           "Mercury is the first planet from the Sun and the smallest in the Solar System. "
           "It is a rocky planet with a trace atmosphere and a surface gravity slightly higher than that of Mars."
           " The surface of Mercury is similar to Earth's Moon, being heavily cratered, "
           "with an expansive rupes system generated from thrust faults, and bright ray systems, "
           "formed by ejecta." 
        )
    ),

    "Venus": Planet(
        name = "Venus",
        mass = "4.87 x 10^24 kg", 
        distance = "108.2 million km", 
        position = 2, 
        moon_names = [],
        moon_count = 0,
        description = (
            "Venus is the second planet from the Sun. "
            "It is often called Earth's 'twin' or 'sister' among the planets of the Solar System for its orbit being the closest to Earth's, "
            "both being rocky planets, and having the most similar and nearly equal size, mass, and surface gravity. "
            "Venus, though, is significantly different, especially as it has no liquid water, "
            "and its atmosphere is far thicker and denser than that of any other rocky body in the Solar System. "
            "The atmosphere is composed mostly of carbon dioxide and has a thick cloud layer of sulfuric acid that spans the whole planet."
        )
    ),

    "Earth": Planet(
        name="Earth",
        mass="5.97 x 10^24 kg", 
        distance="149.6 million km",
        position=3,
        moon_names=["The Moon"],
        moon_count = 1,
        description=(
            "Earth is the third planet from the Sun and the only astronomical object known to harbor life. "
            "This is enabled by Earth being an ocean world, the only one in the Solar System sustaining liquid surface water. "
            "Almost all of Earth's water is contained in its global ocean, covering 70.8 percent of Earth's crust. "
            "The remaining 29.2 percent of Earth's crust is land, most of which is located in the form of continental landmasses. "
            "Most of Earth's land is at least somewhat humid and covered by vegetation, "
            "while large ice sheets at Earth's polar deserts retain more water than Earth's groundwater, lakes, rivers, and atmospheric water combined."
        )
    ),

    "Mars": Planet(
        name="Mars",
        mass="6.42 x 10^23 kg",
        distance="227.9 million km",
        position=4, 
        moon_names=["Phobos", "Deimos"],
        moon_count = 2,
        description=(
            "Mars is the fourth planet from the Sun. It is also known as the 'Red Planet', due to its orange-red appearance. "
            "Mars is a desert-like rocky planet with a thin atmosphere that is primarily carbon dioxide."
        )
    ),

    "Jupiter": Planet(
        name="Jupiter",
        mass="1.90 x 10^27 kg",
        distance="778.3 million km",
        position=5, 
        moon_names=["Io", "Europa", "Ganymede", "Callisto"], #only listed main moons 
        moon_count = 79,
        description=(
            "Jupiter is the fifth planet from the Sun and the largest in the Solar System. "
            "It is a gas giant with a mass nearly 2.5 times that of all the other planets in the Solar System combined, "
            "and slightly less than one-thousandth the mass of the Sun. "
            "Its diameter is 11 times that of Earth and a tenth that of the Sun."
        )
    ),

    "Saturn": Planet(
        name="Saturn",
        mass="5.68 x 10^26 kg",
        distance="1.43 billion km",
        position=6, 
        moon_names=["Titan", "Rhea", "Enceladus", "Dione"], #only listed main moons 
        moon_count = 274,
        description=(
            "Saturn is the sixth planet from the Sun and the second largest in the Solar System, after Jupiter. "
            "It is a gas giant with an average radius of about 9 times that of Earth. "
            "It has an eighth of the average density of Earth but is over 95 times more massive. "
            "Even though Saturn is almost as big as Jupiter, it has less than a third of Jupiter's mass."
        )
    ),

    "Uranus": Planet(
        name="Uranus",
        mass="8.68 x 10^25 kg",
        distance="2.87 billion km", 
        position=7, 
        moon_names=["Titania", "Oberon", "Umbriel", "Ariel"], #only listed main moons 
        moon_count = 28,
        description=(
            "Uranus is the seventh planet from the Sun. It is a gaseous cyan-coloured ice giant. "
            "Most of the planet is made of water, ammonia, and methane in a supercritical phase of matter, "
            "which astronomy calls 'ice' or volatiles. "
            "The planet's atmosphere has a complex layered cloud structure and has the lowest minimum temperature "
            "of all the Solar System's planets."
        )
    ),

    "Neptune": Planet(
        name="Neptune",
        mass="1.02 x 10^26 kg",
        distance="4.50 billion km", 
        position=8, 
        moon_names=["Triton", "Proteus"], #only listed main moon names 
        moon_count = 16,
        description=(
            "Neptune is the eighth and farthest known planet orbiting the Sun. "
            "It is the fourth-largest planet in the Solar System by diameter, the third-most-massive planet, "
            "and the densest giant planet. It is 17 times the mass of Earth."
        )
    )
}

#exclude the sun from planet list and sort planets by position
sorted_planets = sorted(
    [p for p in planets.values() if p.name != "Sun"],
    key=lambda p: p.position
)

# Display planet in order function
def display_sorted_planets (planet_list):
    for planet in planet_list:
       print (planet.name)

# The menu structure was based on the exercises from week 4  
# While working on those, I looked for help on stack overflow to understand how to handle user input and menu options
# I used the following post for referenece and guidance: 
# https://stackoverflow.com/questions/59138345/how-to-create-simple-menu-in-python-with-list-functions

def main ():
    menu_value = ""

    while menu_value != "4":
        menu_value = input(
            "\nWhat would you like to do?\n"
            "1. List all planets\n"
            "2. Tell me everything about a planet\n"
            "3. Ask a question (free text search)\n"
            "4. Quit\n"
            "Enter value: "
        )

# Menu 1 functionality
        if menu_value == "1":
            sub_menu = input(
                "\nDo you want to:\n"
                "1. Planets ordered closest to the Sun\n"
                "2. Planets ordered furthest from the Sun\n"
                "3. Check if a planet is on the list\n"
                "4. Return to Main Menu\n"
                "Enter a value: "
            )
            if sub_menu == "1":
                display_sorted_planets(sorted_planets)

            elif sub_menu == "2":
                display_sorted_planets(list(reversed(sorted_planets)))

            elif sub_menu == "3":
                planet_check = input("\nEnter the name of a planet to check: ").casefold().strip()
                if planet_check in [name.casefold() for name in planets.keys()]:
                    print(f"\nYes, {planet_check.capitalize()} is in the list of planets.\n")
                else:
                    print(f"\nNo, {planet_check.capitalize()} is not in the list of planets.\n")
            elif sub_menu == "4":
                print("\nReturning to main menu.\n")
        
            else:
                print("\nInvalid value, please enter 1, 2, 3 or 4.\n")

# Menu 2 functionality
        elif menu_value == "2":
            planet_name = input("Enter a planet name: ").casefold().strip()

# Case insensitive 
# During tests I noted that 'earth' would give me a 'No data available..' response but 'Earth' would give me the description
# I searched stack overflow for help with code to accept lower case input.
# I found the following discussion https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
# A comment in the thread mentioned using casefold, so I included it so that it would cover all combinations of upper and lower case.
            match = None
            for name, planet in planets.items():
                if name.casefold() == planet_name:
                    match = planet
                    break

            if match:
                print(match.summary())
            else: 
                print ("\nNo data available for that planet.\n")

# Menu 3 functionality
# For this section, I used ideas from Stack Overflow to understand how to:
#   - search strings for keywords https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
#   - how to use the max function using key and lambda https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
# Additionally I used the casefold funtionality which I discovered during my development of menu 2 


        elif menu_value == "3":
            question = input(
                "\nAsk a question (examples):\n"
                "'How many moons does Jupiter have?'\n"
                "'What planet has the most moons?'\n"
                "'How massive is Earth?'\n"
                "'How far from the sun is Venus?'\n"
                "Enter your question:"
            ).casefold().strip()

# Number of moons for a planet 
            if "moon" in question and "does" in question:
                found = False
                for planet in planets.values():
                    if planet.name.casefold() in question:
                        found = True
                        if planet.moon_count == 0:
                            print(f"\n{planet.name} has no moons.\n")
                        else:
                            print(f"\n{planet.name} has {planet.moon_count} moon(s).\n")
                        break
                if not found:
                    print("\nI couldn't identify the planet in your question.\n")

# Planet with most moons 
            elif "moon" in question and "most" in question:
                max_moons = max(planets.values(), key=lambda p: p.moon_count)
                print(f"\nThe planet with the most moons is {max_moons.name} ({max_moons.moon_count} moons).\n")

# Moon names for a planet 
            elif "moon" in question and "name" in question:
                found = False 
                for planet in planets.values():
                    if planet.name.casefold() in question: 
                        found = True 
                        if not planet.moons: 
                            print (f"\n{planet.name} has no moons.\n")
                        else: 
                            moon_names = ", ".join([moon.name for moon in planet.moons])
                            print (f"\nThe names of {planet.name}'s main moons are {moon_names}.\n")
                        break
                if not found:
                    print("\nI couldn't identify the planet in your question.\n")
                
# Mass of planet 
            elif "mass" in question or "massive" in question:
                for planet in planets.values():
                    if planet.name.casefold() in question:
                        print(f"\nThe mass of {planet.name} is {planet.mass}.\n")
                        break
                else:
                    print("\nI couldn't identify the planet in your question.\n")

# Distance of planet from sun 
            elif "far" in question or "distance" in question:
                for planet in planets.values():
                    if planet.name.casefold() in question and planet.name.casefold() != "sun":
                        print(f"\n{planet.name} is {planet.distance} from the Sun.\n")
                        break
                else:
                    if "sun" in question:
                        print("\nThe Sun is the centre of the Solar System.\n")
                    else:
                        print("\nI couldn't identify the planet in your question.\n")

# Unregognised question
            else: 
                print("\nSorry, I couldn't understand that question.\n"
                      "Try asking about moons, mass, or distance.\n")

# Menu 4 functionality (Goodbye)
        elif menu_value == "4":
            print("\nGoodbye!\n")

# Invalid input 
        else:
            print("\nInvalid value, please enter 1, 2, 3 or 4.\n")


if  __name__ == "__main__":
    main ()

#-------------------------------------------------------------------------------------------
# Reflection and Development Notes 
#-------------------------------------------------------------------------------------------
# When I first started this project, I built the solar system data using nested dictionaries 
# to hold each planet’s details. My main focus at that point was just to get the data structure 
# working properly and make sure I could access things like mass and distance.  

# I didn’t actually get access to my course until the third week, so even though I worked hard 
# to catch up, I was still slightly behind when I began the assessment. At that stage, I hadn’t 
# yet started Week 5 of the Codio lessons, which is where Object Oriented Programming is introduced. 
# Once I reached that section and checked the assessment criteria, I realised that I needed to use 
# classes throughout the program. I then completely reworked my code so that each planet became an 
# object of a Planet class rather than just being part of a dictionary.  

# Originally, I only stored a single number for each planet’s moons, but later I realised it would be 
# better to represent them properly. I created a separate Moon class and linked moon objects to their planets. 
# I also added a moon_count attribute so I could show the total number of moons as I only listed a few main examples
# and the code only counted the examples which was not a true reflection of the number of moons.  

# While improving my code, I ran into a few problems such as missing parameters, typos, and indentation 
# errors that happened when I moved things around. Each time, I used error messages and small tests to 
# figure out what was wrong. One of the biggest lessons was that the parameters in the class definition 
# have to exactly match the arguments when you create each planet a mistake I made a few times early on.  

# Through this project I also learned about handling case insensitive input using casefold(), sorting 
# planets with lambda functions, and checking for keywords in user questions using string search logic. 
# I found useful examples and explanations on Stack Overflow, W3Schools, and the SitePoint article on nested 
# dictionaries, all of which are referenced in the different versions of my code on. 

# My GitHub history shows the different stages of this project as I made improvements and tested each change.

# The brief mentioned that I could use a unit testing framework or Tkinter, but I decided to keep my test plan
# text based and focused on meeting the main functional requirements. As I completed this assessment before 
# finishing the final week’s lessons which cover testing due to not being able to catch up, I relied on my real
# world experience of writing and executing test plans instead. Adding those extra features would have meant a
# restructure, so I felt it was better to focus on ensuring the program worked correctly and was thoroughly
# tested through my own plan.



# -------------------------------------------------------------------------------------------
# AI USE STATEMENT
# -------------------------------------------------------------------------------------------
# I used AI tools (ChatGPT) during the early stages of this project to help me understand Python concepts,
# object-oriented design, and potential ways to structure the program. I used these tools to clarify ideas
# and check my understanding of syntax, but all program design decisions, coding, and debugging were
# completed independently.

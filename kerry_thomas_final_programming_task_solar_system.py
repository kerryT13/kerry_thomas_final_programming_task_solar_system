
# Planet data was taken from wikipedia. 
# My initial thought was to use separate dictionaries for things like radius and distance.
# I asked a former colleague who is a developer if this would be a good option, and he suggested that I should look into nested dictionaries. 
# A Google search explained that this helps organise grouped or more complex data, which led me to the SitePoint article https://www.sitepoint.com/python/dictionaries-nested/
# The structure looked similar to JSON, which I am already familiar with, so I felt more comfortable using it.
# I then restructured my planet data as a nested dictionary, with each planet holding its own set of details.

planets = {

    "Sun": {
        "mass": "1.989 x 10^30 kg", 
        "distance": "Centre", 
        "position": "Centre", 
        "moons": 0,
        "description": (
            "The Sun is the star at the centre of the Solar System, providing light and heat to the planets."
        )
        },
    
    "Mercury": {
        "mass": "3.30 x 10^23 kg", 
        "distance": "57.9 million km", 
        "position": "1", 
        "moons": 0,
        "description": ( 
           "Mercury is the first planet from the Sun and the smallest in the Solar System. "
           "It is a rocky planet with a trace atmosphere and a surface gravity slightly higher than that of Mars."
           " The surface of Mercury is similar to Earth's Moon, being heavily cratered, "
           "with an expansive rupes system generated from thrust faults, and bright ray systems, "
           "formed by ejecta." 
        )
        },

    "Venus": {
        "mass": "4.87 x 10^24 kg", 
        "distance": "108.2 million km", 
        "position": "2", 
        "moons": 0,
        "description": (
           "Venus is the second planet from the Sun. "
           "It is often called Earth's 'twin' or 'sister' among the planets of the Solar System for its orbit being the closest to Earth's, "
           "both being rocky planets, and having the most similar and nearly equal size, mass, and surface gravity. "
           "Venus, though, is significantly different, especially as it has no liquid water, "
           "and its atmosphere is far thicker and denser than that of any other rocky body in the Solar System. "
           "The atmosphere is composed mostly of carbon dioxide and has a thick cloud layer of sulfuric acid that spans the whole planet."
        )
        }, 

    "Earth": {
        "mass": "5.97 x 10^24 kg", 
        "distance": "149.6 million km",
        "position": "3",
        "moons": 1,
        "description": (
           "Earth is the third planet from the Sun and the only astronomical object known to harbor life."
           " This is enabled by Earth being an ocean world, the only one in the Solar System sustaining liquid surface water."
           " Almost all of Earth's water is contained in its global ocean, covering 70.8 percent of Earth's crust. "
           "The remaining 29.2 percentof Earth's crust is land, most of which is located in the form of continental "
           "landmasses within Earth's land hemisphere. Most of Earth's land is at least somewhat humid and covered by vegetation,"
           " while large ice sheets at Earth's polar deserts retain more water than Earth's groundwater, lakes, rivers, and atmospheric water combined."
        )
        },

    "Mars": {
        "mass": "6.42 x 10^23 kg",
        "distance": "227.9 million km",
        "position": "4", 
        "moons": 2,
        "description": (
            "Mars is the fourth planet from the Sun. It is also known as the 'Red Planet', due to its orange-red appearance. "
            "Mars is a desert-like rocky planet with a tenuous atmosphere that is primarily carbon dioxide."
        )
        },

    "Jupiter": {
        "mass": "1.90 x 10^27 kg",
        "distance": "778.3 million km",
        "position": "5", 
        "moons": 79,
        "description": (
            "Jupiter is the fifth planet from the Sun and the largest in the Solar System. "
            "It is a gas giant with a mass nearly 2.5 times that of all the other planets in the "
            "Solar System combined and slightly less than one-thousandth the mass of the Sun. "
            "Its diameter is 11 times that of Earth and a tenth that of the Sun."
        )
        },

    "Saturn": {
        "mass": "5.68 x 10^26 kg",
        "distance": "1.43 billion km",
        "position": "6", 
        "moons": 274,
        "description": "Saturn is the sixth planet from the Sun and the second largest in the Solar System, after Jupiter. It is a gas giant, with an average radius of about 9 times that of Earth. It has an eighth of the average density of Earth, but is over 95 times more massive. Even though Saturn is almost as big as Jupiter, Saturn has less than a third of its mass."
        },
    "Uranus": {
         "mass": "8.68 x 10^25 kg",
        "distance": "2.87 billion km", 
        "position": "7", 
        "moons": 29,
        "description": (
            "Uranus is the seventh planet from the Sun. It is a gaseous cyan-coloured ice giant."
            " Most of the planet is made of water, ammonia, and methane in a supercritical phase of matter, "
            "which astronomy calls 'ice' or volatiles. "
            "The planet's atmosphere has a complex layered cloud structure and has the lowest minimum temperature "
            "of all the Solar System's planets."
        )
        },
    "Neptune": {
         "mass": "1.02 x 10^26 kg",
        "distance": "4.50 billion km", 
        "position": "8", 
        "moons": 16,
        "description": (
            "Neptune is the eighth and farthest known planet orbiting the Sun. "
            "It is the fourth-largest planet in the Solar System by diameter, the third-most-massive planet, "
            "and the densest giant planet. It is 17 times the mass of Earth. "
        )
        }
}

#exclude the sun from planet list 
planet_items = [(name,data) for name, data in planets.items() if data ["distance"] != "Centre"]

# sort planets by position
# I modified the code from the lesson in week 4 relating to nested lists.
# I also used additional guidance from https://www.w3schools.com/python/python_lambda.asp
sorted_planets = sorted(
    planet_items, 
    key=lambda x: int(x[1]["position"])
)

#display planet in order function
def display_sorted_planets (planet_list):
   for name, data in planet_list:
       print (name)

# The menu structure was based on the exercises from week 4  
# While working on those, I looked for help on stack overflow to understand how to handle user input and menu options
# I used the following post for referenece and guidance: 
# https://stackoverflow.com/questions/59138345/how-to-create-simple-menu-in-python-with-list-functions

menu_value = ""

while menu_value != "4":
    menu_value = input(
        "\nWhat would you like to do?\n"
        "1. List all planets\n"
        "2. Description of a planet\n"
        "3. Ask a question (free text search)\n"
        "4. Quit\n"
        "Enter value: "
    )

    # menu 1 functionality
    if menu_value == "1":
        sub_menu = input(
            "\nDo you want to:\n"
            "1. Planets ordered closest to the Sun\n"
            "2. Planets ordered furthest from the Sun\n"
            "Enter a value: "
        )
        if sub_menu == "1":
            display_sorted_planets(sorted_planets)
        elif sub_menu == "2":
            display_sorted_planets(list(reversed(sorted_planets)))

    # menu 2 functionality
    elif menu_value == "2":
        planet_name = input("Enter a planet name to display the description: ")

     # Case insensitive 
     # During test i noted that 'earth' would work so i search stack overflow for help with coe to accept lower case.
     # I found this discussion https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
     # and the discussion let me to useing casefold so that it would cover all combinations of upper and lower case.
        match = None
        for name in planets:
            if name.casefold() == planet_name.casefold():
                match = name
                break

        if match:
            print(f"\n{planets[match]['description']}\n")
        else: 
            print ("\nNo data available for that planet.\n")

    # menu 3 functionality
    elif menu_value == "3":
        print("Search functionality")

    # menu 4 functionality (Goodbye)
    elif menu_value == "4":
        print("Goodbye!")

    # invalid input 
    else:
        print("Invalid value, please enter 1, 2, 3 or 4.")
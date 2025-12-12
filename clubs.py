from js import document, window

# dict clubs
CLUBS = {
    "Robotics Club": {
        "desc": "Design, build, and program robots. Compete in local and national contests.",
        "meet": "Tuesdays 3:30–5:30 PM",
        "place": "Robotics Lab",
        "adv": "Mr. Vegan",
        "members": 22,
        "category": "STEM / Competitive"
    },
    "Art Society": {
        "desc": "Painting, digital art, and creative workshops; showcase at school exhibits.",
        "meet": "Wednesdays 2:30–4:00 PM",
        "place": "Art Studio",
        "adv": "Ms. Bonak",
        "members": 28,
        "category": "Arts"
    },
    "Music Ensemble": {
        "desc": "Instrumental and vocal ensemble; performances during school events.",
        "meet": "Fridays 3:00–5:00 PM",
        "place": "Music Room",
        "adv": "Mr. Chicken Pop",
        "members": 18,
        "category": "Performing Arts"
    },
    "Science Explorers": {
        "desc": "Hands-on experiments, field trips, and science fairs.",
        "meet": "Thursdays 3:15–4:45 PM",
        "place": "Science Lab",
        "adv": "Dr. Mario",
        "members": 20,
        "category": "STEM"
    },
    "Gaming Guild": {
        "desc": "Casual and competitive gaming nights; game design jams.",
        "meet": "Mondays 4:00–6:00 PM",
        "place": "E-sports Room",
        "adv": "Mr. Salamalaikam",
        "members": 30,
        "category": "Recreation / eSports"
    },
    "Digital Creators Club": {
        "desc": "Video editing, animation, streaming, and content creation workshops.",
        "meet": "Wednesdays 4:00–5:30 PM",
        "place": "Media Lab",
        "adv": "Ms. Konnichiwarts",
        "members": 15,
        "category": "Media & Tech"
    }
}

# Get club dict when selected
def show_club(*args, **kwargs):
    sel = document.getElementById("club_select")
    if not sel:
        return
    name = sel.value
    info = CLUBS.get(name)
    target = document.getElementById("club_info")
    if not info:
        target.innerHTML = "<p>No information available.</p>"
        return

    html = f"""
      <h4 class='mb-2'>{name}</h4>
      <p class='mb-1'><strong>Description:</strong> {info['desc']}</p>
      <p class='mb-1'><strong>Meeting:</strong> {info['meet']}</p>
      <p class='mb-1'><strong>Location:</strong> {info['place']}</p>
      <p class='mb-1'><strong>Advisor:</strong> {info['adv']}</p>
      <p class='mb-1'><strong>Members:</strong> {info['members']}</p>
      <p class='mb-1'><strong>Category:</strong> {info['category']}</p>
    """
    window.show_club = show_club
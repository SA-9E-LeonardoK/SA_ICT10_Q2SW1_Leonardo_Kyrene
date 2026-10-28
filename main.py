from pyscript import document  # lets us get things from the webpage

# predefined sets of club members per grade level
grade7 = {"Gu Ran", "Caitlyn Kiramman", "John Reaction", "Steve Lacy"}
grade8 = {"Jiang Jia", "Rachel Green", "Faye Webster", "Hachiware"}
grade9 = {"Park Jihyo", "Chandler Bing", "Frank Ocean", "Cassandra Cain"}
grade10 = {"Beatrice Laus", "Kim Dahyun", "Rei Ayanami"}

club_members = grade7 | grade8 | grade9 | grade10

def show_members(e):  # e is for the event handler
    # get the first and last name from the text boxes
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    # combine the names into one and remove extra spaces
    full_name = f"{first} {last}".strip().title()

    # combine all the sets using the union operator (|)
    club_members = grade7 | grade8 | grade9 | grade10

    # sort the members so they show in order, then put each on a new line
    member_list = "<br>".join(sorted(club_members))

def candidate_checker(e):
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_checker = candidate in club_members

    messages = (f' Sorry {candidate}, your name is not on the list.', f'Congratulations, {candidate}! Welcome to the club!')
    document.getElementById('result').innerHTML = messages[member_checker]

    # shows the complete member list
    member_list = '<br>'.join(sorted(club_members))
    total = len(club_members)

    document.getElementById('output1').innerHTML = (
        f'<b>Current members:</b><br>{member_list}<br><br>'
        f'<b>Total members: {total}</b>'
    )
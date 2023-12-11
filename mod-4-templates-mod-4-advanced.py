'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
'''

def relationship_status(from_member, to_member, social_graph):
    # Check if from_member follows to_member
    if to_member in social_graph.get(from_member, {}).get("following", []):
        # Check if to_member follows from_member
        if from_member in social_graph.get(to_member, {}).get("following", []):
            return "friends"  # They follow each other, so they are friends
        else:
            return "follower"  # from_member follows to_member
    elif from_member in social_graph.get(to_member, {}).get("following", []):
        return "followed by"  # to_member follows from_member
    else:
        return "no relationship"  # Neither follows each other

# Example usage:
social_graph = {
    "@bongolpoc": {"first_name": "Joselito", "last_name": "Olpoc", "following": []},
    "@joaquin": {"first_name": "Joaquin", "last_name": "Gonzales", "following": ["@chums", "@jobenilagan"]},
    "@chums": {"first_name": "Matthew", "last_name": "Uy", "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]},
    "@jobenilagan": {"first_name": "Joben", "last_name": "Ilagan", "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]},
    "@joeilagan": {"first_name": "Joe", "last_name": "Ilagan", "following": ["@eeebeee", "@jobenilagan", "@chums"]},
    "@eeebeee": {"first_name": "Elizabeth", "last_name": "Ilagan", "following": ["@jobenilagan", "@joeilagan"]},
}

result = relationship_status("@joaquin", "@chums", social_graph)

'''

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
        
'''

def tic_tac_toe(board):
    # Check rows, columns, and diagonals
    for i in range(len(board)):
        # Check rows and columns
        if all(board[i][j] == board[i][0] for j in range(len(board[i]))) or \
           all(board[j][i] == board[0][i] for j in range(len(board[i]))):
            return board[i][0]

    # Check diagonals
    if all(board[i][i] == board[0][0] for i in range(len(board))) or \
       all(board[i][len(board) - 1 - i] == board[0][len(board) - 1] for i in range(len(board))):
        return board[0][0]

    return "NO WINNER"

# Example usage:
# result = tic_tac_toe([['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']])

'''

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
        
'''

def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    total_time = 0

    while current_stop != second_stop:
        leg = (current_stop, route_map[current_stop]['to_stop'])
        total_time += route_map[leg]['travel_time_mins']
        current_stop = route_map[leg]['to_stop']

    return total_time

# Example usage:
legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

first_stop = 'a1'
second_stop = 'b1'

result = eta(first_stop, second_stop, legs)

'''

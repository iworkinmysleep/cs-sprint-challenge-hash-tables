#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []
    # loop through the tickets and set up cache
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    
    # set cache equal to NONE and set up while loop
    destination = cache["NONE"]
    while destination != "NONE":
        #append destination to route and set cache
        route.append(destination)
        destination = cache[destination]
    # add "NONE" to the route
    route.append("NONE")


    return route

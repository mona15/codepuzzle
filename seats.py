
#return the first best seat available
def the_best_seat(columns, seats):
    best_seat = ''
    dist = 0
    for x in seats:
            current_seat = x
            if best_seat:
                if current_seat[0] < best_seat[0]:
                    best_seat = current_seat
                elif current_seat[0] == best_seat[0]:
                    dist2 = abs(columns - int(current_seat[1]))
                    if dist2 < dist:
                        best_seat = current_seat
                    elif dist2 == dist:
                        if current_seat[1] < best_seat[1]:
                            best_seat = current_seat

            else:
                best_seat = current_seat
                dist = abs(columns - int(best_seat[1]))
    return best_seat

# return all the available seat in a list starting from the Best to the leest best
def list_best_seats(columns, seats):
    if not seats:
        return []
    best_seats = []
    best_seats.append(the_best_seat(columns, seats))
    del seats[best_seats[0]]
    return  best_seats + list_best_seats(columns-1, seats)

# Return the best seat together in a full available row
def list_multiple_seat(tab, num):

    if not tab:
        return []
    if len(tab) < num:
        return []
    if num == 1:
        return tab[0]
    for x in tab:
        i=0
        new_tab = []
        while i < num and i < len(tab) - tab.index(x):
            y = tab.index(x)+i
            if tab[y][0] == tab[tab.index(x)][0]:
                new_tab.append(tab[y])
            else:
                break
            i = i + 1
        if len(new_tab) == num:
            if 0 < int(max(new_tab)[1]) - int(min(new_tab)[1]) < num:
                return new_tab
        
    return []


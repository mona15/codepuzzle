

def the_best_seat(columns, seats):
    """return the first best seat available
    """
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


def list_best_seats(columns, seats):
    """return all the available seats in a list starting from the Best to the worst
    """
    if not seats:
        return []
    best_seats = []
    best_seats.append(the_best_seat(columns, seats))

    del seats[best_seats[0]]
    return  best_seats + list_best_seats(columns-1, seats)


def one_row_requested_seats_old(tab, num):
    """Return the best seats together in a full available row
    """
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

def left(x):
    """return potentiel left element of the given element
    """
    i = list(x)
    i[1] = str(int(x[1]) - 1)
    i = "".join(i)
    return i

def right(x):
    """return potentiel right element of the given element
    """
    i = list(x)
    i[1] = str(int(x[1]) + 1)
    i = "".join(i)
    return i


def verify_around(tab_best, elt, around_available):
    """
    can verify left element and right element of elt based on around_available

    Parameters
    ----------
    tab_best : list
        the table with all element
    elt : string
        the element that we want to check
    around_available : string
        is a variable that tell if we can look left and right for the element
        or only left for the element or only right for the element
    """
    if around_available == "OK":
        if left(elt) in tab_best and right(elt) in tab_best:
            return 'OK'
        elif left(elt) in tab_best :
            return 'left'
        elif right(elt) in tab_best:
            return 'right'
    if around_available == "LEFT":
        if left(elt) in tab_best :
            return 'left'
    if around_available == "RIGHT":
        if right(elt) in tab_best:
            return 'right'
    else:
        return 'KO'


def one_row_requested_seats(tab_best, num, original_tab_best, around_available):
    """for a given row, based on requested seats, 
    give the maximum number of seats that are side by side 
    """
    if num == 1:
        return []
    potentiel = []
    if original_tab_best :
        s = verify_around(original_tab_best, tab_best[0], around_available)
    else: 
        return []
    if s == 'OK':
        if num == 2: 
            potentiel.append(tab_best[0])
            potentiel.append(left(tab_best[0]))
            return potentiel
            around_available = "OK"
        else:
            potentiel.append(tab_best[0])
            potentiel.append(left(tab_best[0]))
            potentiel.append(right(tab_best[0]))
            around_available = "OK"
            
    if s == 'left':
        potentiel.append(tab_best[0])
        potentiel.append(left(tab_best[0]))
        around_available = "LEFT"
    if s == 'right':
        potentiel.append(tab_best[0])
        potentiel.append(right(tab_best[0]))
        around_available = "RIGHT"
    if s == 'KO':
        potentiel.append(tab_best[0])
        return potentiel
    return potentiel + one_row_requested_seats(tab_best[1:], num-1, original_tab_best, around_available)


def requested_seats(potientiel_tab, num, original_tab_best, around_available):
    """with a table of best seats ordered, check rows until getting the best row with all requested seats
    """
    potientiel_tab =list(set(one_row_requested_seats(potientiel_tab, num, original_tab_best, around_available)))
    if len(potientiel_tab) == 0:
        return []

    if len(potientiel_tab) < num:
        count = 0
        for x in original_tab_best:
            if x[0] == potientiel_tab[0][0]:
                count = count + 1
        if original_tab_best[count:]:
            potientiel_tab = requested_seats(original_tab_best[count:], num, original_tab_best[count:], around_available)
        else:
            return []

    
    if len(potientiel_tab) > num:
        return potientiel_tab[:num]
    return potientiel_tab




"""
This is a playingBoard
"""


def playingBoard(rows, columns):
    max_columns = 120                                           # Defining columns
    max_rows = 8                                                # Defing rows
    rows = int(rows)
    columns = int(columns)
    if columns <= max_columns and rows <= max_rows:             # Stating the condition
        for row in range(rows):                                 # for loop used in looping for the conditions stated
            if row % 2 == 0:
                for col in range(1, columns):                   # for loop used in looping for the condition
                    if col % 2 == 1:
                        if col != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        return True                                              # After drawing is done return True
    else:
        reason = ""
        if columns > max_columns and rows > max_rows:
            reason = "columns and rows"
        elif columns > max_columns:
            reason += "columns"
        elif rows > max_rows:
            reason += "rows"
        print("Sorry, cannot create the board, too many {0:s}.".format(reason))
        return False                                             # Return False when matrix is not fitting the screen


playingBoard(8, 120)                                            # defining playingBoard


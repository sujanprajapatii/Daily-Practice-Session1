s = [
    " ***** ",
    "*     *",
    " ***** ",
    "      *",
    " ***** "
]

u = [
    "*     *",
    "*     *",
    "*     *",
    "*     *",
    " ***** "
]

j = [
    "   *** ",
    "     * ",
    "     * ",
    "*    * ",
    " ****  "
]

a = [
    "  ***  ",
    " *   * ",
    " ***** ",
    " *   * ",
    " *   * "
]

n = [
    "*     *",
    "**    *",
    "* *   *",
    "*  *  *",
    "*   ** "
]

# Combine the letters into the name "Sujan"
name = [s, u, j, a, n]

# Print the star pattern
for row in range(5):  # Each letter has 5 rows
    for letter in name:
        print(letter[row], end="  ")  # Print each row of the letter
    print()  # Move to the next line after printing a row
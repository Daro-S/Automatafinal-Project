# Prompt the user to enter their name
text = input("Enter your name: ")

# Find the length of the name
text_length = len(text)

# Generate ASCII art in the shape of a heart
print('\n'.join([''.join([  # Join each row of the ASCII art using an empty string
    (text[(x-y) % text_length]  # Print the user input text in a loop based on x-y position
        # Check if x,y coordinates fall within the heart shape
        if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0
        else ' ')  # Print a space character if the x,y coordinates are outside the heart shape
    for x in range(-30, 30)])  # Loop over x-axis coordinates from -30 to 30
    for y in range(15, -15, -1)]))  # Loop over y-axis coordinates from 15 to -15 (reverse order)

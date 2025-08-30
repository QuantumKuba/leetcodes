def imageSeg4Connectivity(image):

    # Create a 2D array that keeps track of which pixels have been checked already
    checked = [[False for _ in range(len(image[0]))] for _ in range(len(image))]


    def dfs(i, j):
        # Out of bounds
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
            return
        # Already checked or not part of a segment
        if checked[i][j] or image[i][j] != 1:
            return
        
        # Mark as checked
        checked[i][j] = True
        # Check all 4 directions (this could also be done by defining a list of directions and looping through it)
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    segments = 0
    # loop through all pixels in the image
    for i in range(len(image)):
        for j in range(len(image[0])):
            if not checked[i][j] and image[i][j] == 1:
                dfs(i, j)
                segments += 1

    return segments

if __name__ == "__main__":
    image = """000110001010
               111011110001
               111010010010
               100000000100"""
    # Convert the string representation of the image into a 2D list of integers
    image = [list(map(int, line.strip())) for line in image.split("\n")]
    print(imageSeg4Connectivity(image))  # should print 7


def dilate_image_count_1s(image: list[list[int]], se: list[list[int]]) -> int:
    rows, cols = len(image), len(image[0])
    se_rows, se_cols = len(se), len(se[0])

    # Create a blank (all zeros) output image for dilation
    dilated_image = [[0 for _ in range(cols)] for _ in range(rows)]

    # Apply the structuring element
    for i in range(rows):
        for j in range(cols):
            if image[i][j] == 1:
                for di in range(se_rows):
                    for dj in range(se_cols):
                        if se[di][dj] == 1:
                            ni, nj = i + di - se_rows // 2, j + dj - se_cols // 2
                            if 0 <= ni < rows and 0 <= nj < cols:
                                dilated_image[ni][nj] = 1

    # Count the number of 1s in the dilated image
    return sum(sum(row) for row in dilated_image)

def image_to_2d_list(image: str) -> list[list[int]]:
    return [list(map(int, line.strip())) for line in image.split("\n")]

def create_empty_2d_list(rows: int, cols: int) -> list[list[int]]:
    return [[0 for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":
    image = """0000000000
    0111111100
    0000111100
    0000111100
    0001111100
    0000111100
    0001100000
    0000000000
    0000000000"""

    image_2d = image_to_2d_list(image)
    empty_image_2d = create_empty_2d_list(len(image_2d), len(image_2d[0]))  
    se = [[1,1,1],[1,1,1],[1,1,1]]


    print(dilate_image_count_1s(image_2d, se))
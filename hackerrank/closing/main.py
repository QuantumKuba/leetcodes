
def closing(image:list[list[int]], se:list[list[int]]) -> int:
    eroded = erode_image_2d(image, se)
    dilated = dilate_image_count_1s(eroded, se)
    return sum(sum(row) for row in dilated)



def dilate_image_count_1s(image: list[list[int]], se: list[list[int]]) -> list[list[int]]:
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

    return dilated_image


def erode_image_2d(image: list[list[int]], se: list[list[int]]) -> list[list]:
    rows, cols = len(image), len(image[0])
    se_rows, se_cols = len(se), len(se[0])
    
    # Create a blank (all zeros) output image for erosion
    eroded_image = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Apply the structuring element for erosion
    for i in range(rows):
        for j in range(cols):
            fits = True
            for di in range(se_rows):
                for dj in range(se_cols):
                    if se[di][dj] == 1:
                        ni, nj = i + di - se_rows // 2, j + dj - se_cols // 2
                        if not (0 <= ni < rows and 0 <= nj < cols and image[ni][nj] == 1):
                            fits = False
                            break
                if not fits:
                    break
            if fits:
                eroded_image[i][j] = 1
    return eroded_image


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
    se = [[1,1,1],[1,1,1],[1,1,1]]

    print(closing(image_2d, se))

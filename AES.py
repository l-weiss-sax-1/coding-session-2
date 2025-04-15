FIXED_MATRIX = [
[2,3,1,1],
[1,2,3,1],
[1,1,2,3],
[3,1,1,2]
]

def main():
    result = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    handle_encryption(result)
    result2 = [[1,2,3,4], [5,6,7,8], [9,10,11,14], [13,14,15,16]]
    handle_encryption(result2)


def handle_encryption(result):
    print(f"the inital row is: {result}")
    for i in range(5):
        mixed_rows = mix_rows(result)
        result = mix_columns(mixed_rows)

    print(f"the output row is: {result}")


# def mix_rows(row :list[list[int]]) -> str:
#     result_row = row[1:] + [row[0]]  # Move first character to the end
#     return result_row  # Convert list back to string

def mix_rows(rows: list[list[int]]):
    result_rows = []
    
    for i, row in enumerate(rows):
        # if not isinstance(row, list):  
        #     raise TypeError("Each row must be a list of integers")

        shift = (i + 1) % len(row)  # Ensure shift wraps around if needed
        new_row = row[shift:] + row[:shift]  # Rotate row by `shift` positions
        result_rows.append(new_row)
    
    return result_rows

def mix_columns(rows: list[list[int]]) -> list[list[int]]:
    # The fixed AES matrix used for multiplication

    
    # Transpose the state to work on columns
    columns = list(zip(*rows))  # from rows to columns
    
    new_columns = []
    for col in columns:
        new_col = []
        for mix_row in FIXED_MATRIX:
            value = sum(mix_row[i] * col[i] for i in range(4))
            new_col.append(value)
        new_columns.append(new_col)
    
    # Transpose back to rows
    new_rows = [list(row) for row in zip(*new_columns)]
    return new_rows


def convertToUnicode(input: str) -> list:
    """
    Converts a string into a list of Unicode code points (integers).

    Args:
        input (str): The input string to convert.

    Returns:
        list: A list of integers representing Unicode code points.
    """
    return [ord(char) for char in input]


if __name__ == "__main__":
    # print("ERROR, please only run the test cases")
    main()
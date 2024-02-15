# def double_transposition_encrypt(plaintext, row_permutation, col_permutation):
#     # Calculate the dimensions of the matrix based on permutations
#     num_rows = len(row_permutation)
#     num_cols = len(col_permutation)
#
#     # Pad the plaintext with 'x' if necessary to fit the matrix size
#     plaintext += 'x' * (num_rows * num_cols - len(plaintext) % (num_rows * num_cols))
#
#     # Create the matrix for encryption
#     matrix = [[''] * num_cols for _ in range(num_rows)]
#     k = 0
#
#     # Fill the matrix with plaintext characters according to row and column permutations
#     for i, row in enumerate(row_permutation):
#         for j, col in enumerate(col_permutation):
#             matrix[i][j] = plaintext[k]
#             k += 1
#
#     # Read the matrix column-wise to generate the ciphertext
#     ciphertext = ''.join(matrix[i][j] for j in range(num_cols) for i in range(num_rows))
#
#     return ciphertext
#
# def double_transposition_decrypt(ciphertext, row_permutation, col_permutation):
#     # Calculate the dimensions of the matrix based on permutations
#     num_rows = len(row_permutation)
#     num_cols = len(col_permutation)
#
#     # Create the matrix for decryption
#     matrix = [[''] * num_cols for _ in range(num_rows)]
#
#     # Fill the matrix with the ciphertext characters according to column permutation
#     k = 0
#     for j, col in enumerate(col_permutation):
#         for i, row in enumerate(row_permutation):
#             matrix[row - 1][col - 1] = ciphertext[k]
#             k += 1
#
#     # Read the matrix row-wise to generate the plaintext
#     plaintext = ''.join(matrix[i][j] for i in range(num_rows) for j in range(num_cols))
#
#     return plaintext
#
#
# # Example usage
# plaintext = "attackxatxdawn"
# row_permutation = [3, 5, 1, 4, 2]  # Permute the rows
# col_permutation = [1, 3, 2]  # Permute the columns
#
# # Encryption
# ciphertext = double_transposition_encrypt(plaintext, row_permutation, col_permutation)
# print("Ciphertext:", ciphertext)
#
# # Decryption
# decrypted_text = double_transposition_decrypt(ciphertext, row_permutation, col_permutation)
# print("Decrypted Text:", decrypted_text)


def create_default_matrix(plaintext):
    num_cols = int(len(plaintext) ** 0.5)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    plaintext += 'x' * (num_rows * num_cols - len(plaintext))
    return [list(plaintext[i * num_cols: (i + 1) * num_cols]) for i in range(num_rows)]

def rearrange_matrix(matrix, row_permutation, col_permutation):
    new_matrix = [[matrix[i][j - 1] for j in col_permutation] for i in range(len(matrix))]
    new_matrix = [new_matrix[i - 1] for i in row_permutation]
    return new_matrix
def decrypt_matrix(matrix, row_permutation, col_permutation):
    inverse_row_permutation = [0] * len(row_permutation)
    for i, row in enumerate(row_permutation):
        inverse_row_permutation[row - 1] = i + 1
    inverse_col_permutation = [0] * len(col_permutation)
    for i, col in enumerate(col_permutation):
        inverse_col_permutation[col - 1] = i + 1
    new_matrix = [matrix[i - 1] for i in inverse_row_permutation]
    new_matrix = [[new_matrix[i][j - 1] for j in inverse_col_permutation] for i in range(len(new_matrix))]

    return new_matrix

def decrypt_text(ciphertext, row_permutation, col_permutation):
    # Rearrange the matrix based on the given row and column permutations
    rearranged_matrix = decrypt_matrix(ciphertext, row_permutation, col_permutation)
    # Convert the matrix back to plaintext
    plaintext = "".join(["".join(row) for row in rearranged_matrix])
    return plaintext
def print_matrix(matrix):
    for row in matrix:
        print("".join(row),end="")

default_columns = [1, 2, 3]
default_rows = [1, 2, 3, 4, 5]
col_permutation = list(map(int, input("Enter column permutation (e.g., 132): ")))
row_permutation = list(map(int, input("Enter row permutation (e.g., 35142): ")))


plaintext = "attackxatxdawn"

default_matrix = create_default_matrix(plaintext)
rearranged_matrix = rearrange_matrix(default_matrix, row_permutation, col_permutation)
ciphertext = rearranged_matrix
decrypted_text = decrypt_text(ciphertext, row_permutation, col_permutation)
print("Encripted Matrix:")
print_matrix(rearranged_matrix)
print("\nDecrypted Text:",decrypted_text)

import numpy as np
import pprint


def random_A_and_B_matrix() -> np.array:
    """Genereting two matrix

    Returns:
        two np.array
    """
    a = np.random.randint(0, 5, size=(3, 3))
    b = np.random.randint(0, 5, size=(3, 1))
    return a, b


def find_matrix_X(matrix_A_inv: np.array, matrix_B: np.array) -> np.array:
    """Function for finding X matrix

    Args:
        matrix_A (np.array): matrix with shape (3,3)
        matrix_B (np.array): matrix with shape (3,1)

    Returns:
        np.array: result of multiplying two matrix
    """
    matrix_result = np.matmul(matrix_A_inv, matrix_B)
    return matrix_result


def main():
    # first matrix, shape (3,3)
    matrix_A = np.array([[1, 2, 3], [0, 1, 2], [2, 0, 0]])
    # print(np.linalg.inv(matrix_A))

    # second matrix, shape (3,1)
    matrix_B = np.array([[1], [1], [0]])

    # find X matrix
    matrix_X = find_matrix_X(np.linalg.inv(matrix_A), matrix_B)
    print(f"Result X matrix - {matrix_X}")

    # random testing
    try:
        test_A_matrix, test_B_matrix = random_A_and_B_matrix()
        print(find_matrix_X(np.linalg.inv(test_A_matrix), test_B_matrix))
    except np.linalg.LinAlgError as e:
        print(
            f"Some errors occured.\nImpossible to find the inverse matrix.\nThe given matrix is - {e}"
        )


if __name__ == "__main__":
    main()

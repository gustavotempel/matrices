import pytest

from src.matrix import Matrix

# is_valid_matrix

def test_is_valid_matrix_1x1():
    assert Matrix([[5]]).is_valid_matrix() == True

def test_is_valid_matrix_3x3():
    assert Matrix([[1,2,3],[4,5,6],[7,8,9]]).is_valid_matrix() == True

def test_is_valid_matrix_1x5():
    assert Matrix([[1,2,3,4,5]]).is_valid_matrix() == True

def test_is_valid_matrix_false_list():
    assert Matrix([1,2,3,4,5]).is_valid_matrix() == False

def test_is_valid_matrix_false_list2():
    assert Matrix([[1,2,3],[4,5]]).is_valid_matrix() == False

# def test_is_valid_matrix_false_int():
#     assert Matrix(12345).is_valid_matrix() == False

def test_is_valid_matrix_false_str():
    assert Matrix("[[1,2,3,4,5]]").is_valid_matrix() == False

def test_is_valid_matrix_false_3():
    assert Matrix([[1,2,3],"123"]).is_valid_matrix() == False


# add_matrix

def test_add_matrix_1x1_1():
    assert Matrix([[0]]).add_matrix(Matrix([[1]])) == Matrix([[1]])

def test_add_matrix_1x1_2():
    assert Matrix([[1]]).add_matrix(Matrix([[1]])) == Matrix([[2]])

def test_add_matrix_1x1_3():
    assert Matrix([[1]]).add_matrix(Matrix([[2]])) == Matrix([[3]])

def test_add_matrix_2x2_1():
    assert Matrix([[1,0],[0,1]]).add_matrix(Matrix([[1,0],[0,1]])) == Matrix([[2,0],[0,2]])

def test_add_matrix_error_1():
    with pytest.raises(ValueError, match=r"You can't add matrices of different dimensions"):
        Matrix([[1]]).add_matrix(Matrix([[1,1]]))

def test_add_matrix_error_2():
    with pytest.raises(ValueError, match=r"One of the matrices is not rectangular"):
        Matrix([[1]]).add_matrix(Matrix([[1,2],[3]]))

def test_add_matrix_error_3():
    with pytest.raises(TypeError, match=r"The argument given is not a Matrix instance"):
        Matrix([[1,0],[0,1]]).add_matrix([[1,2],[3,4]])

# scalar_product

def test_scalar_product_1x1():
    assert Matrix([[5]]).scalar_product(3) == Matrix([[15]])

def test_scalar_product_3x3():
    assert Matrix([[1,2,3],[4,5,6],[7,8,9]]).scalar_product(3) == Matrix([[3,6,9],[12,15,18],[21,24,27]])

def test_scalar_product_1x5():
    assert Matrix([[1,2,3,4,5]]).scalar_product(3) == Matrix([[3,6,9,12,15]])

# matrices_mult

def test_matrices_mult_1x4_4x1():
    assert Matrix([[1,2,3,4]]).matrices_mult([[5],[6],[7],[8]]) == Matrix([[70]])

def test_matrices_mult_1x4_4x2():
    assert Matrix([[1,2,3,4]]).matrices_mult([[5,6],[6,7],[7,8],[8,9]]) == Matrix([[70,80]])

def test_matrices_mult_2x2_2x3():
    assert Matrix([[1,2],[3,4]]).matrices_mult([[5,6,7],[8,9,10]]) == Matrix([[21, 24, 27], [47, 54, 61]])

# transpose

def test_transpose_1x1_idty():
    assert Matrix([[1]]).transpose() == Matrix([[1]])

def test_transpose_2x2_1():
    assert Matrix([[1,0],[0,1]]).transpose() == Matrix([[1,0],[0,1]])

def test_transpose_2x2_2():
    assert Matrix([[1,2],[3,4]]).transpose() == Matrix([[1,3],[2,4]])

def test_transpose_3x3_2():
    assert Matrix([[1,2,3],[4,5,6],[7,8,9]]).transpose() == Matrix([[1,4,7],[2,5,8],[3,6,9]])

def test_transpose_4x4_2():
    assert Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]).transpose() == Matrix([[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]])

# submatrix

def test_submatrix_2x2_2():
    assert Matrix([[2,2],[2,2]]).submatrix(1,1) == Matrix([[2]])

def test_submatrix_3x3_2():
    assert Matrix([[2,2,2],[2,2,2],[2,2,2]]).submatrix(1,1) == Matrix([[2,2],[2,2]])

def test_submatrix_3x3_3():
    assert Matrix([[1,2,3],[4,5,6],[7,8,9]]).submatrix(1,1) == Matrix([[5,6],[8,9]])

def test_submatrix_3x3_4():
    assert Matrix([[1,2,3],[4,5,6],[7,8,9]]).submatrix(2,2) == Matrix([[1,3],[7,9]])

# determinant

def test_det_matrix_1x1_idty():
    assert Matrix([[1]]).determinant() == 1

def test_det_matrix_1x1_2():
    assert Matrix([[2]]).determinant() == 2

def test_det_matrix_2x2_123():
    assert Matrix([[1,2],[3,4]]).determinant() == -2

def test_det_matrix_3x3_123():
    assert Matrix([[1,2,3],[4,5,6],[7,8,9]]).determinant() == 0

def test_det_matrix_4x4_123():
    assert Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]).determinant() == 0

def test_det_matrix_4x4_1():  
    assert Matrix([[2,8,6,2],[0,6,1,7],[4,7,6,9],[5,7,9,2]]).determinant() == 56

def test_det_matrix_5x5_123():
    assert Matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]).determinant() == 0

def test_det_matrix_3x3_9():
    assert Matrix([[1,0,1],[3,1,5],[2,0,1]]).determinant() == -1

# adjugate_matrix

def test_adjugate_1x1_2():
    assert Matrix([[2]]).adjugate_matrix() == Matrix([[1]])

def test_adjugate_2x2_2():
    assert Matrix([[2,2],[2,2]]).adjugate_matrix() == Matrix([[2,-2],[-2,2]])

def test_adjugate_3x3_2():
    assert Matrix([[2,2,2],[2,2,2],[2,2,2]]).adjugate_matrix() == Matrix([[0,0,0],[0,0,0],[0,0,0]])

def test_adjugate_4x4_2():
    assert Matrix([[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]).adjugate_matrix() == Matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

def test_adjugate_5x5_2():
    assert Matrix([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]).adjugate_matrix() == Matrix([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

# inverse_matrix

def test_inverse_1x1_2():
    assert Matrix([[2]]).inverse_matrix() == Matrix([[0.5]])

def test_inverse_2x2_2():
    with pytest.raises(ValueError, match=r"Don't exists inverted matrix for singular matrix"):
        Matrix([[2,2],[2,2]]).inverse_matrix()

def test_inverse_2x2_123():
    assert Matrix([[1,2],[3,4]]).inverse_matrix() == Matrix([[-2,1],[1.5,-0.5]])

def test_inverse_3x3_123():
    with pytest.raises(ValueError, match=r"Don't exists inverted matrix for singular matrix"):
        Matrix([[1,2,3],[4,5,6],[7,8,9]]).inverse_matrix()

def test_inverse_3x3_9():
    assert Matrix([[1,0,1],[3,1,5],[2,0,1]]).inverse_matrix() == Matrix([[-1,0,1],[-7,1,2],[2,0,-1]])

# get_rows

def test_get_rows_5x5_1():
    assert Matrix([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]).get_rows(2,3,4) == \
    Matrix([[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]])

# get_columns

def test_get_columns_5x5_1():
    assert Matrix([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]).get_columns(1,3,5) == \
    Matrix([[1,3,5],[2,4,6],[3,5,7],[4,6,8],[5,7,9]])

# get_submatrix_by_columns

def test_get_submatrix_by_columns_5x5_1():
    assert Matrix([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]).get_submatrix_by_columns(2,3) == \
    Matrix([[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8]])

# __str__

def test_str_123():
    assert Matrix([[1,2,3],[4,5,6],[7,8,9]]).__str__() == "| 1 2 3 |\n| 4 5 6 |\n| 7 8 9 |\n"

def test_str_123_1():
    assert Matrix([[-1,2,-3],[4.0,5.00,6.10],[7.1,8,9]]).__str__() == "|  -1   2  -3 |\n|   4   5 6.1 |\n| 7.1   8   9 |\n"
"""
Matrix Calculation

Class which allows to represent a matrix of any order or shape (n x n, n x m).
It also allows the following operations with matrices:

- Matrices addition
- Scalar multiplication
- Matrices multiplication
- Matrix transpose
- Matrix determinant
- Adjugate matrix
- Inverted matrix
- Method to obtain a matrix row.
- Method to obtain a matrix column.
- Method to obtain part of the matrix from a certain column. 
- Method to show the matrix on screen as a matrix.

"""

class Matrix(list):
    """
    Matrix class
    
    """
    def __init__(self, *args):
        super().__init__(*args)
  
    def is_valid_matrix(self) -> bool:
        """Returns True if the object has a Matrix(list()) format and the inner lists are all the same lengths (rectangular)"""
        if isinstance(self, list):
            for i in range(len(self)):
                if isinstance(self[i], list):
                    if len(self[i]) != len(self[0]):
                        return False
                else:
                    return False
            return True
        return False

    def is_square_matrix(self) -> bool:
        """Returns True if the object is a square matrix"""
        if self.is_valid_matrix():
            if len(self) == len(self[0]):
                return True
            return False
        return False

    def add_matrix(self, matrix: "Matrix") -> "Matrix":
        """Returns the matrix resulting from the addition of the self matrix and another given matrix"""
        if isinstance(matrix, Matrix):
            if self.is_valid_matrix() and matrix.is_valid_matrix():
                if len(self) == len(matrix) and len(self[0]) == len(matrix[0]):
                    result_matrix = Matrix()
                    for i in range(len(self)):
                        row = []
                        for j in range(len(self[i])):
                            row.append(self[i][j] + matrix[i][j])
                        result_matrix.append(row)
                    return result_matrix
                raise ValueError("You can't add matrices of different dimensions")
            raise ValueError("One of the matrices is not rectangular")
        raise TypeError("The argument given is not a Matrix instance")

    def scalar_product(self, scalar: int) -> "Matrix":
        """Returns the matrix resulting from multiplying self by a scalar number"""
        result_matrix = Matrix()
        for i in range(len(self)):
            row = []
            for j in range(len(self[i])):
                row.append(self[i][j] * scalar)
            result_matrix.append(row)
        return result_matrix

    def matrices_mult(self, matrix: "Matrix") -> "Matrix":
        """Returns the matrix resulting from multiplying self by another matrix"""
        if len(self[0]) == len(matrix):
            r_matrix = Matrix()
            for i in range(len(self)):
                row = []
                for j in range(len(matrix[0])):
                    value = 0
                    for k in range(len(self[0])):
                        value += self[i][k] * matrix[k][j]
                    row.append(value)
                r_matrix.append(row)
            return r_matrix
        raise ValueError("These matrices can't multiply themselves")

    def transpose(self) -> "Matrix":
        """Returns the transpose matrix"""
        r_matrix = Matrix()
        for i in range(len(self[0])):
            row = []
            for j in range(len(self)):
                row.append(self[j][i])
            r_matrix.append(row)
        return r_matrix

    def submatrix(self, r: int, s: int) -> "Matrix":
        """Returns the resulting matrix of deleting the r row and the s column"""
        if len(self) > 1 and len(self[0]) > 1:
            matrix = Matrix()
            for i in range(len(self)):
                row = []
                for j in range(len(self[i])):
                    row.append(self[i][j])
                del row[s-1]
                matrix.append(row)
            del matrix[r-1]
            return matrix
        else:
            raise ValueError("Can't obtain submatrix from 1x1 matrix or less")
    
    def determinant(self) -> float or str:
        """Returns the determinant from the matrix"""
        if self.is_square_matrix():
            det = 0
            for i in range(len(self[0])):
                det += self[0][i] * pow(-1, i) * (self.submatrix(1, i + 1).determinant() if len(self) > 2 else (self.submatrix(1, i + 1)[0][0] if len(self) > 1 else 1))
            return det
        raise ValueError("Don't exists determinant for non square matrix")

    def adjugate_matrix(self) -> "Matrix":
        """Returns the adjugate matrix"""
        if self.is_square_matrix():
            matrix = Matrix()
            for i in range(len(self)):
                row = []
                for j in range(len(self[i])):
                    row.append(pow(-1, (i + j)) * (self.submatrix(i + 1, j + 1).determinant() if len(self) > 2 else (self.submatrix(i + 1, j + 1)[0][0] if len(self) > 1 else 1)))
                matrix.append(row)
            return matrix
        raise ValueError("Don't exists adjugate matrix for non square matrix")

    def inverse_matrix(self) -> "Matrix":
        """Returns the inverse matrix calculated by determinant"""
        if self.determinant() != 0:
            return self.adjugate_matrix().transpose().scalar_product(1/self.determinant())
        raise ValueError("Don't exists inverted matrix for singular matrix")

    def get_rows(self, *rows: int) -> "Matrix":
        """Returns a new Matrix with the specified rows"""
        result_matrix = []
        for i in range(len(self)):
            if i + 1 in rows:
                result_matrix.append(self[i])
        return result_matrix

    def get_columns(self, *columns: int) -> "Matrix":
        """Returns a new Matrix with the specified columns"""
        result_matrix = []
        for i in range(len(self)):
            row = []
            for j in range(len(self[i])):
                if j + 1 in columns:
                    row.append(self[i][j])
            result_matrix.append(row)
        return result_matrix

    def get_submatrix_by_columns(self, start_col: int, col_qty: int) -> "Matrix":
        """Returns a new matrix from a given column and a given quantity of columns"""
        result_matrix = []
        for i in range(len(self)):
            row = []
            for j in range(len(self[i])):
                if j + 1 in range(start_col, start_col + col_qty):
                    row.append(self[i][j])
            result_matrix.append(row)
        return result_matrix

    def __str__(self):
        """Shows the matrix like a matrix"""
        max_len = max(max(map(lambda x: len(str(f"{x:g}")), i)) for i in self)
        result = ""
        for i in range(len(self)):
            result += "|"
            for j in range(len(self[i])):
                result += f"{str(f'{self[i][j]:g}'):>{max_len + 1}}"
            result += " |\n"
        return result
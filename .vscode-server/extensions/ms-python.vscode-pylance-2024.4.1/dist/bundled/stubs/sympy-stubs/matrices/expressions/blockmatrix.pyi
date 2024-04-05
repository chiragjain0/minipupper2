from typing import Any, Literal, Self
from sympy.core.basic import Basic
from sympy.matrices.expressions.matadd import MatAdd
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.matpow import MatPow
from sympy.matrices.expressions.special import GenericIdentity, GenericZeroMatrix
from sympy.matrices.immutable import ImmutableDenseMatrix
from sympy.series.order import Order

class BlockMatrix(MatrixExpr):
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Any | Literal[0], Any | Literal[0]]:
        ...
    
    @property
    def blockshape(self):
        ...
    
    @property
    def blocks(self) -> Basic:
        ...
    
    @property
    def rowblocksizes(self) -> list[Any]:
        ...
    
    @property
    def colblocksizes(self) -> list[Any]:
        ...
    
    def structurally_equal(self, other) -> bool:
        ...
    
    def transpose(self) -> BlockMatrix:
        ...
    
    def schur(self, mat=..., generalized=...) -> Self:
        ...
    
    def LDUdecomposition(self) -> tuple[BlockMatrix, BlockDiagMatrix, BlockMatrix]:
        ...
    
    def UDLdecomposition(self) -> tuple[BlockMatrix, BlockDiagMatrix, BlockMatrix]:
        ...
    
    def LUdecomposition(self) -> tuple[BlockMatrix, BlockMatrix]:
        ...
    
    @property
    def is_Identity(self) -> bool:
        ...
    
    @property
    def is_structurally_symmetric(self) -> bool:
        ...
    
    def equals(self, other) -> bool:
        ...
    


class BlockDiagMatrix(BlockMatrix):
    def __new__(cls, *mats) -> BlockDiagMatrix:
        ...
    
    @property
    def diag(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def blocks(self) -> ImmutableDenseMatrix:
        ...
    
    @property
    def shape(self) -> tuple[int, int]:
        ...
    
    @property
    def blockshape(self) -> tuple[int, int]:
        ...
    
    @property
    def rowblocksizes(self) -> list[Any]:
        ...
    
    @property
    def colblocksizes(self) -> list[Any]:
        ...
    
    def get_diag_blocks(self) -> tuple[Basic, ...]:
        ...
    


def block_collapse(expr) -> Any:
    ...

def bc_unpack(expr):
    ...

def bc_matadd(expr):
    ...

def bc_block_plus_ident(expr) -> MatAdd | GenericZeroMatrix:
    ...

def bc_dist(expr) -> BlockDiagMatrix | BlockMatrix:
    ...

def bc_matmul(expr) -> MatPow | GenericIdentity | Order | object:
    ...

def bc_transpose(expr) -> Any:
    ...

def bc_inverse(expr) -> BlockMatrix:
    ...

def blockinverse_1x1(expr) -> BlockMatrix:
    ...

def blockinverse_2x2(expr) -> BlockMatrix:
    ...

def deblock(B) -> BlockMatrix:
    ...

def reblock_2x2(expr) -> BlockMatrix:
    ...

def bounds(sizes) -> list[Any]:
    ...

def blockcut(expr, rowsizes, colsizes) -> BlockMatrix:
    ...


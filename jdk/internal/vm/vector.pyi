from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class, Integer, Boolean
from java.util.function import BiFunction

VM = TypeVar('VM', default=Any)
M = TypeVar('M', default=Any)
E = TypeVar('E', default=Any)
V = TypeVar('V', default=Any)
S = TypeVar('S', default=Any)
VOUT = TypeVar('VOUT', default=Any)
VIN = TypeVar('VIN', default=Any)
C = TypeVar('C', default=Any)
W = TypeVar('W', default=Any)
VP = TypeVar('VP', default=Any)
SH = TypeVar('SH', default=Any)

class VectorSupport:

  BT_eq: int

  BT_ge: int

  BT_gt: int

  BT_le: int

  BT_lt: int

  BT_ne: int

  BT_no_overflow: int

  BT_overflow: int

  BT_uge: int

  BT_ugt: int

  BT_ule: int

  BT_ult: int

  BT_unsigned_compare: int

  T_BYTE: int

  T_DOUBLE: int

  T_FLOAT: int

  T_INT: int

  T_LONG: int

  T_SHORT: int

  VECTOR_OP_ABS: int

  VECTOR_OP_ACOS: int

  VECTOR_OP_ADD: int

  VECTOR_OP_AND: int

  VECTOR_OP_ASIN: int

  VECTOR_OP_ATAN: int

  VECTOR_OP_ATAN2: int

  VECTOR_OP_CAST: int

  VECTOR_OP_CBRT: int

  VECTOR_OP_COS: int

  VECTOR_OP_COSH: int

  VECTOR_OP_DIV: int

  VECTOR_OP_EXP: int

  VECTOR_OP_EXPM1: int

  VECTOR_OP_FMA: int

  VECTOR_OP_HYPOT: int

  VECTOR_OP_LOG: int

  VECTOR_OP_LOG10: int

  VECTOR_OP_LOG1P: int

  VECTOR_OP_LROTATE: int

  VECTOR_OP_LSHIFT: int

  VECTOR_OP_MASK_FIRSTTRUE: int

  VECTOR_OP_MASK_LASTTRUE: int

  VECTOR_OP_MASK_TOLONG: int

  VECTOR_OP_MASK_TRUECOUNT: int

  VECTOR_OP_MAX: int

  VECTOR_OP_MIN: int

  VECTOR_OP_MUL: int

  VECTOR_OP_NEG: int

  VECTOR_OP_OR: int

  VECTOR_OP_POW: int

  VECTOR_OP_REINTERPRET: int

  VECTOR_OP_RROTATE: int

  VECTOR_OP_RSHIFT: int

  VECTOR_OP_SIN: int

  VECTOR_OP_SINH: int

  VECTOR_OP_SQRT: int

  VECTOR_OP_SUB: int

  VECTOR_OP_TAN: int

  VECTOR_OP_TANH: int

  VECTOR_OP_URSHIFT: int

  VECTOR_OP_XOR: int

  @staticmethod
  def binaryOp(arg0: int, arg1: Class[VM], arg2: Class[M], arg3: Class[E], arg4: int, arg5: VectorSupport.VectorPayload, arg6: VectorSupport.VectorPayload, arg7: VectorSupport.VectorMask, arg8: VectorSupport.BinaryOperation) -> VectorSupport.VectorPayload: ...

  @staticmethod
  def blend(arg0: Class[V], arg1: Class[M], arg2: Class[E], arg3: int, arg4: VectorSupport.Vector, arg5: VectorSupport.Vector, arg6: VectorSupport.VectorMask, arg7: VectorSupport.VectorBlendOp) -> VectorSupport.Vector: ...

  @staticmethod
  def broadcastCoerced(arg0: Class[VM], arg1: Class[E], arg2: int, arg3: int, arg4: VectorSupport.VectorSpecies, arg5: VectorSupport.BroadcastOperation) -> VectorSupport.VectorPayload: ...

  @staticmethod
  def broadcastInt(arg0: int, arg1: Class[V], arg2: Class[M], arg3: Class[E], arg4: int, arg5: VectorSupport.Vector, arg6: int, arg7: VectorSupport.VectorMask, arg8: VectorSupport.VectorBroadcastIntOp) -> VectorSupport.Vector: ...

  @staticmethod
  def compare(arg0: int, arg1: Class[V], arg2: Class[M], arg3: Class[E], arg4: int, arg5: VectorSupport.Vector, arg6: VectorSupport.Vector, arg7: VectorSupport.VectorMask, arg8: VectorSupport.VectorCompareOp) -> VectorSupport.VectorMask: ...

  @staticmethod
  def convert(arg0: int, arg1: Class[Any], arg2: Class[Any], arg3: int, arg4: Class[Any], arg5: Class[Any], arg6: int, arg7: VectorSupport.VectorPayload, arg8: VectorSupport.VectorSpecies, arg9: VectorSupport.VectorConvertOp) -> VectorSupport.VectorPayload: ...

  @staticmethod
  def extract(arg0: Class[V], arg1: Class[E], arg2: int, arg3: VectorSupport.Vector, arg4: int, arg5: VectorSupport.VecExtractOp) -> int: ...

  @staticmethod
  def getMaxLaneCount(arg0: Class[Any]) -> int: ...

  @staticmethod
  def indexVector(arg0: Class[V], arg1: Class[E], arg2: int, arg3: VectorSupport.Vector, arg4: int, arg5: VectorSupport.VectorSpecies, arg6: VectorSupport.IndexOperation) -> VectorSupport.Vector: ...

  @staticmethod
  def insert(arg0: Class[V], arg1: Class[E], arg2: int, arg3: VectorSupport.Vector, arg4: int, arg5: int, arg6: VectorSupport.VecInsertOp) -> VectorSupport.Vector: ...

  @staticmethod
  def isNonCapturingLambda(arg0: object) -> bool: ...

  @staticmethod
  def load(arg0: Class[VM], arg1: Class[E], arg2: int, arg3: object, arg4: int, arg5: object, arg6: int, arg7: VectorSupport.VectorSpecies, arg8: VectorSupport.LoadOperation) -> VectorSupport.VectorPayload: ...

  @staticmethod
  def loadMasked(arg0: Class[V], arg1: Class[M], arg2: Class[E], arg3: int, arg4: object, arg5: int, arg6: VectorSupport.VectorMask, arg7: object, arg8: int, arg9: VectorSupport.VectorSpecies, arg10: VectorSupport.LoadVectorMaskedOperation) -> VectorSupport.Vector: ...

  @staticmethod
  def loadWithMap(arg0: Class[V], arg1: Class[M], arg2: Class[E], arg3: int, arg4: Class[VectorSupport.Vector[Integer]], arg5: object, arg6: int, arg7: VectorSupport.Vector, arg8: VectorSupport.VectorMask, arg9: object, arg10: int, arg11: list[int], arg12: int, arg13: VectorSupport.VectorSpecies, arg14: VectorSupport.LoadVectorOperationWithMap) -> VectorSupport.Vector: ...

  @staticmethod
  def maskReductionCoerced(arg0: int, arg1: Class[M], arg2: Class[Any], arg3: int, arg4: VectorSupport.VectorMask, arg5: VectorSupport.VectorMaskOp) -> int: ...

  @staticmethod
  def maybeRebox(arg0: VectorSupport.VectorPayload) -> VectorSupport.VectorPayload: ...

  @staticmethod
  def rearrangeOp(arg0: Class[V], arg1: Class[SH], arg2: Class[M], arg3: Class[E], arg4: int, arg5: VectorSupport.Vector, arg6: VectorSupport.VectorShuffle, arg7: VectorSupport.VectorMask, arg8: VectorSupport.VectorRearrangeOp) -> VectorSupport.Vector: ...

  @staticmethod
  def reductionCoerced(arg0: int, arg1: Class[V], arg2: Class[M], arg3: Class[E], arg4: int, arg5: VectorSupport.Vector, arg6: VectorSupport.VectorMask, arg7: VectorSupport.ReductionOperation) -> int: ...

  @staticmethod
  def shuffleIota(arg0: Class[E], arg1: Class[SH], arg2: VectorSupport.VectorSpecies, arg3: int, arg4: int, arg5: int, arg6: int, arg7: VectorSupport.ShuffleIotaOperation) -> VectorSupport.VectorShuffle: ...

  @staticmethod
  def shuffleToVector(arg0: Class[VectorSupport.Vector[E]], arg1: Class[E], arg2: Class[SH], arg3: VectorSupport.VectorShuffle, arg4: int, arg5: VectorSupport.ShuffleToVectorOperation) -> VectorSupport.Vector: ...

  @staticmethod
  def store(arg0: Class[Any], arg1: Class[Any], arg2: int, arg3: object, arg4: int, arg5: VectorSupport.Vector, arg6: object, arg7: int, arg8: VectorSupport.StoreVectorOperation) -> None: ...

  @staticmethod
  def storeMasked(arg0: Class[V], arg1: Class[M], arg2: Class[E], arg3: int, arg4: object, arg5: int, arg6: VectorSupport.Vector, arg7: VectorSupport.VectorMask, arg8: object, arg9: int, arg10: VectorSupport.StoreVectorMaskedOperation) -> None: ...

  @staticmethod
  def storeWithMap(arg0: Class[V], arg1: Class[M], arg2: Class[E], arg3: int, arg4: Class[VectorSupport.Vector[Integer]], arg5: object, arg6: int, arg7: VectorSupport.Vector, arg8: VectorSupport.Vector, arg9: VectorSupport.VectorMask, arg10: object, arg11: int, arg12: list[int], arg13: int, arg14: VectorSupport.StoreVectorOperationWithMap) -> None: ...

  @staticmethod
  def ternaryOp(arg0: int, arg1: Class[V], arg2: Class[M], arg3: Class[E], arg4: int, arg5: VectorSupport.Vector, arg6: VectorSupport.Vector, arg7: VectorSupport.Vector, arg8: VectorSupport.VectorMask, arg9: VectorSupport.TernaryOperation) -> VectorSupport.Vector: ...

  @staticmethod
  def test(arg0: int, arg1: Class[Any], arg2: Class[Any], arg3: int, arg4: VectorSupport.VectorMask, arg5: VectorSupport.VectorMask, arg6: BiFunction[M, M, Boolean]) -> bool: ...

  @staticmethod
  def unaryOp(arg0: int, arg1: Class[V], arg2: Class[M], arg3: Class[E], arg4: int, arg5: VectorSupport.Vector, arg6: VectorSupport.VectorMask, arg7: VectorSupport.UnaryOperation) -> VectorSupport.Vector: ...

  def __init__(self): ...

  class BroadcastOperation[VM, S]:

    def broadcast(self, arg0: int, arg1: VectorSupport.VectorSpecies) -> VectorSupport.VectorPayload: ...

  class VectorSpecies[E]:

    def __init__(self): ...

  class VectorPayload:

    def __init__(self, arg0: object): ...

  class ShuffleIotaOperation[S, SH]:

    def apply(self, arg0: int, arg1: int, arg2: int, arg3: VectorSupport.VectorSpecies) -> VectorSupport.VectorShuffle: ...

  class VectorShuffle[E](VectorSupport.VectorPayload):

    def __init__(self, arg0: object): ...

  class ShuffleToVectorOperation[V, SH]:

    def apply(self, arg0: VectorSupport.VectorShuffle) -> VectorSupport.Vector: ...

  class Vector[E](VectorSupport.VectorPayload):

    def __init__(self, arg0: object): ...

  class IndexOperation[V, S]:

    def index(self, arg0: VectorSupport.Vector, arg1: int, arg2: VectorSupport.VectorSpecies) -> VectorSupport.Vector: ...

  class ReductionOperation[V, M]:

    def apply(self, arg0: VectorSupport.Vector, arg1: VectorSupport.VectorMask) -> int: ...

  class VectorMask[E](VectorSupport.VectorPayload):

    def __init__(self, arg0: object): ...

  class VecExtractOp[V]:

    def apply(self, arg0: VectorSupport.Vector, arg1: int) -> int: ...

  class VecInsertOp[V]:

    def apply(self, arg0: VectorSupport.Vector, arg1: int, arg2: int) -> VectorSupport.Vector: ...

  class UnaryOperation[V, M]:

    def apply(self, arg0: VectorSupport.Vector, arg1: VectorSupport.VectorMask) -> VectorSupport.Vector: ...

  class BinaryOperation[VM, M]:

    def apply(self, arg0: VectorSupport.VectorPayload, arg1: VectorSupport.VectorPayload, arg2: VectorSupport.VectorMask) -> VectorSupport.VectorPayload: ...

  class TernaryOperation[V, M]:

    def apply(self, arg0: VectorSupport.Vector, arg1: VectorSupport.Vector, arg2: VectorSupport.Vector, arg3: VectorSupport.VectorMask) -> VectorSupport.Vector: ...

  class LoadOperation[C, VM, S]:

    def load(self, arg0: object, arg1: int, arg2: VectorSupport.VectorSpecies) -> VectorSupport.VectorPayload: ...

  class LoadVectorMaskedOperation[C, V, S, M]:

    def load(self, arg0: object, arg1: int, arg2: VectorSupport.VectorSpecies, arg3: VectorSupport.VectorMask) -> VectorSupport.Vector: ...

  class LoadVectorOperationWithMap[C, V, S, M]:

    def loadWithMap(self, arg0: object, arg1: int, arg2: list[int], arg3: int, arg4: VectorSupport.VectorSpecies, arg5: VectorSupport.VectorMask) -> VectorSupport.Vector: ...

  class StoreVectorOperation[C, V]:

    def store(self, arg0: object, arg1: int, arg2: VectorSupport.Vector) -> None: ...

  class StoreVectorMaskedOperation[C, V, M]:

    def store(self, arg0: object, arg1: int, arg2: VectorSupport.Vector, arg3: VectorSupport.VectorMask) -> None: ...

  class StoreVectorOperationWithMap[C, V, M]:

    def storeWithMap(self, arg0: object, arg1: int, arg2: VectorSupport.Vector, arg3: list[int], arg4: int, arg5: VectorSupport.VectorMask) -> None: ...

  class VectorCompareOp[V, M]:

    def apply(self, arg0: int, arg1: VectorSupport.Vector, arg2: VectorSupport.Vector, arg3: VectorSupport.VectorMask) -> VectorSupport.VectorMask: ...

  class VectorRearrangeOp[V, SH, M]:

    def apply(self, arg0: VectorSupport.Vector, arg1: VectorSupport.VectorShuffle, arg2: VectorSupport.VectorMask) -> VectorSupport.Vector: ...

  class VectorBlendOp[V, M]:

    def apply(self, arg0: VectorSupport.Vector, arg1: VectorSupport.Vector, arg2: VectorSupport.VectorMask) -> VectorSupport.Vector: ...

  class VectorBroadcastIntOp[V, M]:

    def apply(self, arg0: VectorSupport.Vector, arg1: int, arg2: VectorSupport.VectorMask) -> VectorSupport.Vector: ...

  class VectorConvertOp[VOUT, VIN, S]:

    def apply(self, arg0: VectorSupport.VectorPayload, arg1: VectorSupport.VectorSpecies) -> VectorSupport.VectorPayload: ...

  class VectorMaskOp[M]:

    def apply(self, arg0: VectorSupport.VectorMask) -> int: ...


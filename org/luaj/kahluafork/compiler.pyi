from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import Reader
from se.krka.kahlua.vm import Prototype

class BlockCnt:

  def __init__(self): ...


class ConsControl:

  def __init__(self): ...


class ExpDesc:

  def nval(self) -> float: ...

  def setNval(self, arg0: float) -> None: ...

  def setvalue(self, arg0: ExpDesc) -> None: ...

  def __init__(self): ...


class FuncState:

  BITRK: int

  currentFile: str

  currentfullFile: str

  iABC: int

  iABx: int

  iAsBx: int

  LFIELDS_PER_FLUSH: int

  LUA_MULTRET: int

  luaP_opmodes: list[int]

  MASK_A: int

  MASK_B: int

  MASK_Bx: int

  MASK_C: int

  MASK_NOT_A: int

  MASK_NOT_B: int

  MASK_NOT_Bx: int

  MASK_NOT_C: int

  MASK_NOT_OP: int

  MASK_OP: int

  MAX_OP: int

  MAXARG_A: int

  MAXARG_B: int

  MAXARG_Bx: int

  MAXARG_C: int

  MAXARG_sBx: int

  MAXINDEXRK: int

  MAXSTACK: int

  NO_REG: int

  NUM_OPCODES: int

  OP_ADD: int

  OP_CALL: int

  OP_CLOSE: int

  OP_CLOSURE: int

  OP_CONCAT: int

  OP_DIV: int

  OP_EQ: int

  OP_FORLOOP: int

  OP_FORPREP: int

  OP_GETGLOBAL: int

  OP_GETTABLE: int

  OP_GETUPVAL: int

  OP_JMP: int

  OP_LE: int

  OP_LEN: int

  OP_LOADBOOL: int

  OP_LOADK: int

  OP_LOADNIL: int

  OP_LT: int

  OP_MOD: int

  OP_MOVE: int

  OP_MUL: int

  OP_NEWTABLE: int

  OP_NOT: int

  OP_POW: int

  OP_RETURN: int

  OP_SELF: int

  OP_SETGLOBAL: int

  OP_SETLIST: int

  OP_SETTABLE: int

  OP_SETUPVAL: int

  OP_SUB: int

  OP_TAILCALL: int

  OP_TEST: int

  OP_TESTSET: int

  OP_TFORLOOP: int

  OP_UNM: int

  OP_VARARG: int

  POS_A: int

  POS_B: int

  POS_Bx: int

  POS_C: int

  POS_OP: int

  SIZE_A: int

  SIZE_B: int

  SIZE_Bx: int

  SIZE_C: int

  SIZE_OP: int

  VARARG_HASARG: int

  VARARG_ISVARARG: int

  VARARG_NEEDSARG: int

  @staticmethod
  def GETARG_A(arg0: int) -> int: ...

  @staticmethod
  def GETARG_B(arg0: int) -> int: ...

  @staticmethod
  def GETARG_Bx(arg0: int) -> int: ...

  @staticmethod
  def GETARG_C(arg0: int) -> int: ...

  @staticmethod
  def GETARG_sBx(arg0: int) -> int: ...

  @staticmethod
  def GET_OPCODE(arg0: int) -> int: ...

  @staticmethod
  def INDEXK(arg0: int) -> int: ...

  @staticmethod
  def ISK(arg0: int) -> bool: ...

  @staticmethod
  def RKASK(arg0: int) -> int: ...

  @staticmethod
  def getBMode(arg0: int) -> int: ...

  @staticmethod
  def getCMode(arg0: int) -> int: ...

  @staticmethod
  def getOpMode(arg0: int) -> int: ...

  @staticmethod
  def testTMode(arg0: int) -> bool: ...


class LHS_assign:

  def __init__(self): ...


class LexState:

  @staticmethod
  def compile(arg0: int, arg1: Reader, arg2: str, arg3: str) -> Prototype: ...

  @staticmethod
  def isReservedKeyword(arg0: str) -> bool: ...

  def __init__(self, arg0: Reader, arg1: int, arg2: str):
    self.nccalls: int


class Token:

  def set(self, arg0: Token) -> None: ...

  def __init__(self): ...


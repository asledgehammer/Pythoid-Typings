from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import ClassLoader, Class, Number, Module, Enum
from java.lang.invoke import MethodType, MethodHandle
from java.util import List

T = TypeVar('T', default=Any)

class BytecodeDescriptor:

  @staticmethod
  def parseMethod(arg0: str, arg1: ClassLoader) -> List[Class[Any]]: ...

  @staticmethod
  @overload
  def unparse(arg0: Class[Any]) -> str: ...

  @staticmethod
  @overload
  def unparse(arg0: object) -> str: ...

  @staticmethod
  @overload
  def unparse(arg0: MethodType) -> str: ...

  @staticmethod
  @overload
  def unparseMethod(arg0: Class[Any], arg1: list[Class]) -> str: ...

  @staticmethod
  @overload
  def unparseMethod(arg0: Class[Any], arg1: List[Class[Any]]) -> str: ...


class ValueConversions:

  @staticmethod
  def boxExact(arg0: Wrapper) -> MethodHandle: ...

  @staticmethod
  def cast() -> MethodHandle: ...

  @staticmethod
  @overload
  def convertPrimitive(arg0: Class[Any], arg1: Class[Any]) -> MethodHandle: ...

  @staticmethod
  @overload
  def convertPrimitive(arg0: Wrapper, arg1: Wrapper) -> MethodHandle: ...

  @staticmethod
  def ignore() -> MethodHandle: ...

  @staticmethod
  def primitiveConversion(arg0: Wrapper, arg1: object, arg2: bool) -> Number: ...

  @staticmethod
  def unboxCast(arg0: Wrapper) -> MethodHandle: ...

  @staticmethod
  @overload
  def unboxExact(arg0: Wrapper) -> MethodHandle: ...

  @staticmethod
  @overload
  def unboxExact(arg0: Wrapper, arg1: bool) -> MethodHandle: ...

  @staticmethod
  def unboxWiden(arg0: Wrapper) -> MethodHandle: ...

  @staticmethod
  def widenSubword(arg0: object) -> int: ...

  @staticmethod
  def zeroConstantFunction(arg0: Wrapper) -> MethodHandle: ...

  def __init__(self): ...

  class WrapperCache:

    def get(self, arg0: Wrapper) -> MethodHandle: ...

    def put(self, arg0: Wrapper, arg1: MethodHandle) -> MethodHandle: ...

  class Handles: ...


class VerifyAccess:

  @staticmethod
  def classLoaderIsAncestor(arg0: Class[Any], arg1: Class[Any]) -> bool: ...

  @staticmethod
  def isClassAccessible(arg0: Class[Any], arg1: Class[Any], arg2: Class[Any], arg3: int) -> bool: ...

  @staticmethod
  def isMemberAccessible(arg0: Class[Any], arg1: Class[Any], arg2: int, arg3: Class[Any], arg4: Class[Any], arg5: int) -> bool: ...

  @staticmethod
  def isModuleAccessible(arg0: Class[Any], arg1: Module, arg2: Module) -> bool: ...

  @staticmethod
  def isSameModule(arg0: Class[Any], arg1: Class[Any]) -> bool: ...

  @staticmethod
  def isSamePackage(arg0: Class[Any], arg1: Class[Any]) -> bool: ...

  @staticmethod
  def isSamePackageMember(arg0: Class[Any], arg1: Class[Any]) -> bool: ...

  @staticmethod
  @overload
  def isTypeVisible(arg0: Class[Any], arg1: Class[Any]) -> bool: ...

  @staticmethod
  @overload
  def isTypeVisible(arg0: MethodType, arg1: Class[Any]) -> bool: ...


class VerifyType:

  @staticmethod
  def canPassUnchecked(arg0: Class[Any], arg1: Class[Any]) -> int: ...

  @staticmethod
  @overload
  def isNullConversion(arg0: Class[Any], arg1: Class[Any], arg2: bool) -> bool: ...

  @staticmethod
  @overload
  def isNullConversion(arg0: MethodType, arg1: MethodType, arg2: bool) -> bool: ...

  @staticmethod
  def isNullReferenceConversion(arg0: Class[Any], arg1: Class[Any]) -> bool: ...

  @staticmethod
  def isNullType(arg0: Class[Any]) -> bool: ...

  @staticmethod
  def isSpreadArgType(arg0: Class[Any]) -> bool: ...

  @staticmethod
  def spreadArgElementType(arg0: Class[Any], arg1: int) -> Class[Any]: ...


class Wrapper(Enum):

  BOOLEAN: Wrapper

  BYTE: Wrapper

  CHAR: Wrapper

  COUNT: int

  DOUBLE: Wrapper

  FLOAT: Wrapper

  INT: Wrapper

  LONG: Wrapper

  OBJECT: Wrapper

  SHORT: Wrapper

  VOID: Wrapper

  def arrayType(self) -> Class[Any]: ...

  def basicTypeChar(self) -> str: ...

  def basicTypeString(self) -> str: ...

  def bitWidth(self) -> int: ...

  def cast(self, arg0: object, arg1: Class[T]) -> object: ...

  def convert(self, arg0: object, arg1: Class[T]) -> object: ...

  def copyArrayBoxing(self, arg0: object, arg1: int, arg2: list[object], arg3: int, arg4: int) -> None: ...

  def copyArrayUnboxing(self, arg0: list[object], arg1: int, arg2: object, arg3: int, arg4: int) -> None: ...

  def detailString(self) -> str: ...

  def isConvertibleFrom(self, arg0: Wrapper) -> bool: ...

  def isDoubleWord(self) -> bool: ...

  def isFloating(self) -> bool: ...

  def isIntegral(self) -> bool: ...

  def isNumeric(self) -> bool: ...

  def isOther(self) -> bool: ...

  def isSigned(self) -> bool: ...

  def isSingleWord(self) -> bool: ...

  def isSubwordOrInt(self) -> bool: ...

  def isUnsigned(self) -> bool: ...

  def makeArray(self, arg0: int) -> object: ...

  def primitiveSimpleName(self) -> str: ...

  def primitiveType(self) -> Class[Any]: ...

  def stackSlots(self) -> int: ...

  @overload
  def wrap(self, arg0: int) -> object: ...

  @overload
  def wrap(self, arg0: object) -> object: ...

  def wrapperSimpleName(self) -> str: ...

  @overload
  def wrapperType(self) -> Class[Any]: ...

  @overload
  def wrapperType(self, arg0: Class[T]) -> Class[T]: ...

  @overload
  def zero(self) -> object: ...

  @overload
  def zero(self, arg0: Class[T]) -> object: ...

  @staticmethod
  def asPrimitiveType(arg0: Class[T]) -> Class[T]: ...

  @staticmethod
  def asWrapperType(arg0: Class[T]) -> Class[T]: ...

  @staticmethod
  @overload
  def forBasicType(arg0: str) -> Wrapper: ...

  @staticmethod
  @overload
  def forBasicType(arg0: Class[Any]) -> Wrapper: ...

  @staticmethod
  @overload
  def forPrimitiveType(arg0: str) -> Wrapper: ...

  @staticmethod
  @overload
  def forPrimitiveType(arg0: Class[Any]) -> Wrapper: ...

  @staticmethod
  def forWrapperType(arg0: Class[Any]) -> Wrapper: ...

  @staticmethod
  def isPrimitiveType(arg0: Class[Any]) -> bool: ...

  @staticmethod
  def isWrapperType(arg0: Class[Any]) -> bool: ...

  @staticmethod
  def valueOf(arg0: str) -> Wrapper: ...

  @staticmethod
  def values() -> list[Wrapper]: ...

  class Format: ...


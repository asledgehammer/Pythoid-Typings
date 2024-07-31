from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import List
from sun.reflect.generics.visitor import TypeTreeVisitor, Visitor

class ArrayTypeSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  def getComponentType(self) -> TypeSignature: ...

  @staticmethod
  def make(arg0: TypeSignature) -> ArrayTypeSignature: ...


class BaseType: ...


class BooleanSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> BooleanSignature: ...


class BottomSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> BottomSignature: ...


class ByteSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> ByteSignature: ...


class CharSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> CharSignature: ...


class ClassSignature:

  def accept(self, arg0: Visitor[Any]) -> None: ...

  @overload
  def getFormalTypeParameters(self) -> list[FormalTypeParameter]: ...

  @overload
  def getFormalTypeParameters(self) -> list[FormalTypeParameter]: ...

  def getSuperInterfaces(self) -> list[ClassTypeSignature]: ...

  def getSuperclass(self) -> ClassTypeSignature: ...

  @staticmethod
  def make(arg0: list[FormalTypeParameter], arg1: ClassTypeSignature, arg2: list[ClassTypeSignature]) -> ClassSignature: ...


class ClassTypeSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  def getPath(self) -> List[SimpleClassTypeSignature]: ...

  @staticmethod
  def make(arg0: List[SimpleClassTypeSignature]) -> ClassTypeSignature: ...


class DoubleSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> DoubleSignature: ...


class FieldTypeSignature: ...


class FloatSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> FloatSignature: ...


class FormalTypeParameter:

  @overload
  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @overload
  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  def getBounds(self) -> list[FieldTypeSignature]: ...

  def getName(self) -> str: ...

  @staticmethod
  def make(arg0: str, arg1: list[FieldTypeSignature]) -> FormalTypeParameter: ...


class IntSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> IntSignature: ...


class LongSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> LongSignature: ...


class MethodTypeSignature:

  def accept(self, arg0: Visitor[Any]) -> None: ...

  def getExceptionTypes(self) -> list[FieldTypeSignature]: ...

  @overload
  def getFormalTypeParameters(self) -> list[FormalTypeParameter]: ...

  @overload
  def getFormalTypeParameters(self) -> list[FormalTypeParameter]: ...

  def getParameterTypes(self) -> list[TypeSignature]: ...

  def getReturnType(self) -> ReturnType: ...

  @staticmethod
  def make(arg0: list[FormalTypeParameter], arg1: list[TypeSignature], arg2: ReturnType, arg3: list[FieldTypeSignature]) -> MethodTypeSignature: ...


class ReturnType:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...


class ShortSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> ShortSignature: ...


class Signature:

  def getFormalTypeParameters(self) -> list[FormalTypeParameter]: ...


class SimpleClassTypeSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  def getDollar(self) -> bool: ...

  def getName(self) -> str: ...

  def getTypeArguments(self) -> list[TypeArgument]: ...

  @staticmethod
  def make(arg0: str, arg1: bool, arg2: list[TypeArgument]) -> SimpleClassTypeSignature: ...


class Tree: ...


class TypeArgument:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...


class TypeSignature: ...


class TypeTree:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...


class TypeVariableSignature:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  def getIdentifier(self) -> str: ...

  @staticmethod
  def make(arg0: str) -> TypeVariableSignature: ...


class VoidDescriptor:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  @staticmethod
  def make() -> VoidDescriptor: ...


class Wildcard:

  def accept(self, arg0: TypeTreeVisitor[Any]) -> None: ...

  def getLowerBounds(self) -> list[FieldTypeSignature]: ...

  def getUpperBounds(self) -> list[FieldTypeSignature]: ...

  @staticmethod
  def make(arg0: list[FieldTypeSignature], arg1: list[FieldTypeSignature]) -> Wildcard: ...


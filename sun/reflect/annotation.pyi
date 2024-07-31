from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class
from java.lang.annotation import Annotation, RetentionPolicy
from java.lang.reflect import Method
from java.nio import ByteBuffer
from java.util import Map
from jdk.internal.reflect import ConstantPool

class AnnotationInvocationHandler:

  @overload
  def invoke(self, arg0: object, arg1: Method, arg2: list[object]) -> object: ...

  @overload
  def invoke(self, arg0: object, arg1: Method, arg2: list[object]) -> object: ...

  @staticmethod
  def invokeDefault(arg0: object, arg1: Method, arg2: list[object]) -> object: ...

  class UnsafeAccessor: ...


class AnnotationParser:

  @staticmethod
  def annotationForMap(arg0: Class[Annotation], arg1: Map[str, object]) -> Annotation: ...

  @staticmethod
  def parseAnnotations(arg0: list[int], arg1: ConstantPool, arg2: Class[Any]) -> Map[Class[Annotation], Annotation]: ...

  @staticmethod
  def parseMemberValue(arg0: Class[Any], arg1: ByteBuffer, arg2: ConstantPool, arg3: Class[Any]) -> object: ...

  @staticmethod
  def parseParameterAnnotations(arg0: list[int], arg1: ConstantPool, arg2: Class[Any]) -> list[list[Annotation]]: ...

  @staticmethod
  def toArray(arg0: Map[Class[Annotation], Annotation]) -> list[Annotation]: ...

  def __init__(self): ...


class AnnotationType:

  def isInherited(self) -> bool: ...

  def memberDefaults(self) -> Map[str, object]: ...

  def memberTypes(self) -> Map[str, Class[Any]]: ...

  def members(self) -> Map[str, Method]: ...

  def retention(self) -> RetentionPolicy: ...

  def toString(self) -> str: ...

  @staticmethod
  def getInstance(arg0: Class[Annotation]) -> AnnotationType: ...

  @staticmethod
  def invocationHandlerReturnType(arg0: Class[Any]) -> Class[Any]: ...


class AnnotationTypeMismatchExceptionProxy(ExceptionProxy):

  def toString(self) -> str: ...


class ExceptionProxy:

  def __init__(self): ...


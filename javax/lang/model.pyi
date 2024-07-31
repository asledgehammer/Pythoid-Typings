from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class, Enum, Runtime, CharSequence
from java.lang.annotation import Annotation
from java.util import List

A = TypeVar('A', default=Any)

class AnnotatedConstruct:

  def getAnnotation(self, arg0: Class[A]) -> A: ...

  def getAnnotationMirrors(self) -> List[AnnotationMirror]: ...

  def getAnnotationsByType(self, arg0: Class[A]) -> list[Annotation]: ...


class SourceVersion(Enum):

  RELEASE_0: SourceVersion

  RELEASE_1: SourceVersion

  RELEASE_10: SourceVersion

  RELEASE_11: SourceVersion

  RELEASE_12: SourceVersion

  RELEASE_13: SourceVersion

  RELEASE_14: SourceVersion

  RELEASE_15: SourceVersion

  RELEASE_16: SourceVersion

  RELEASE_17: SourceVersion

  RELEASE_18: SourceVersion

  RELEASE_2: SourceVersion

  RELEASE_3: SourceVersion

  RELEASE_4: SourceVersion

  RELEASE_5: SourceVersion

  RELEASE_6: SourceVersion

  RELEASE_7: SourceVersion

  RELEASE_8: SourceVersion

  RELEASE_9: SourceVersion

  def runtimeVersion(self) -> Runtime.Version: ...

  @staticmethod
  def isIdentifier(arg0: CharSequence) -> bool: ...

  @staticmethod
  @overload
  def isKeyword(arg0: CharSequence) -> bool: ...

  @staticmethod
  @overload
  def isKeyword(arg0: CharSequence, arg1: SourceVersion) -> bool: ...

  @staticmethod
  @overload
  def isName(arg0: CharSequence) -> bool: ...

  @staticmethod
  @overload
  def isName(arg0: CharSequence, arg1: SourceVersion) -> bool: ...

  @staticmethod
  def latest() -> SourceVersion: ...

  @staticmethod
  def latestSupported() -> SourceVersion: ...

  @staticmethod
  @overload
  def valueOf(arg0: Runtime.Version) -> SourceVersion: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> SourceVersion: ...

  @staticmethod
  def values() -> list[SourceVersion]: ...


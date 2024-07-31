from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class, Enum

class Annotation:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class Documented:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class ElementType(Enum):

  ANNOTATION_TYPE: ElementType

  CONSTRUCTOR: ElementType

  FIELD: ElementType

  LOCAL_VARIABLE: ElementType

  METHOD: ElementType

  MODULE: ElementType

  PACKAGE: ElementType

  PARAMETER: ElementType

  RECORD_COMPONENT: ElementType

  TYPE: ElementType

  TYPE_PARAMETER: ElementType

  TYPE_USE: ElementType

  @staticmethod
  def valueOf(arg0: str) -> ElementType: ...

  @staticmethod
  def values() -> list[ElementType]: ...


class Inherited:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class Retention:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  def value(self) -> RetentionPolicy: ...


class RetentionPolicy(Enum):

  RUNTIME: RetentionPolicy

  SOURCE: RetentionPolicy

  @staticmethod
  def valueOf(arg0: str) -> RetentionPolicy: ...

  @staticmethod
  def values() -> list[RetentionPolicy]: ...


class Target:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  def value(self) -> list[ElementType]: ...


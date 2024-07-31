from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from org.lwjglx.util.glu import GLUtessellatorCallback, GLUtessellator

class ActiveRegion: ...


class CachedVertex: ...


class Dict:

  class DictLeq:

    def leq(self, arg0: object, arg1: object, arg2: object) -> bool: ...


class DictNode: ...


class GLUface: ...


class GLUhalfEdge: ...


class GLUmesh: ...


class GLUtessellatorImpl:

  TESS_MAX_CACHE: int

  @overload
  def gluBeginPolygon(self) -> None: ...

  @overload
  def gluBeginPolygon(self) -> None: ...

  @overload
  def gluDeleteTess(self) -> None: ...

  @overload
  def gluDeleteTess(self) -> None: ...

  @overload
  def gluEndPolygon(self) -> None: ...

  @overload
  def gluEndPolygon(self) -> None: ...

  @overload
  def gluGetTessProperty(self, arg0: int, arg1: list[float], arg2: int) -> None: ...

  @overload
  def gluGetTessProperty(self, arg0: int, arg1: list[float], arg2: int) -> None: ...

  @overload
  def gluNextContour(self, arg0: int) -> None: ...

  @overload
  def gluNextContour(self, arg0: int) -> None: ...

  @overload
  def gluTessBeginContour(self) -> None: ...

  @overload
  def gluTessBeginContour(self) -> None: ...

  @overload
  def gluTessBeginPolygon(self, arg0: object) -> None: ...

  @overload
  def gluTessBeginPolygon(self, arg0: object) -> None: ...

  @overload
  def gluTessCallback(self, arg0: int, arg1: GLUtessellatorCallback) -> None: ...

  @overload
  def gluTessCallback(self, arg0: int, arg1: GLUtessellatorCallback) -> None: ...

  @overload
  def gluTessEndContour(self) -> None: ...

  @overload
  def gluTessEndContour(self) -> None: ...

  @overload
  def gluTessEndPolygon(self) -> None: ...

  @overload
  def gluTessEndPolygon(self) -> None: ...

  @overload
  def gluTessNormal(self, arg0: float, arg1: float, arg2: float) -> None: ...

  @overload
  def gluTessNormal(self, arg0: float, arg1: float, arg2: float) -> None: ...

  @overload
  def gluTessProperty(self, arg0: int, arg1: float) -> None: ...

  @overload
  def gluTessProperty(self, arg0: int, arg1: float) -> None: ...

  @overload
  def gluTessVertex(self, arg0: list[float], arg1: int, arg2: object) -> None: ...

  @overload
  def gluTessVertex(self, arg0: list[float], arg1: int, arg2: object) -> None: ...

  @staticmethod
  def gluNewTess() -> GLUtessellator: ...

  def __init__(self): ...


class GLUvertex: ...


class PriorityQ:

  INIT_SIZE: int

  @staticmethod
  def LEQ(arg0: PriorityQ.Leq, arg1: object, arg2: object) -> bool: ...

  class Leq:

    def leq(self, arg0: object, arg1: object) -> bool: ...

  class PQhandleElem:

    def __init__(self): ...

  class PQnode:

    def __init__(self): ...


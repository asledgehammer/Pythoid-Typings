from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer, IntBuffer, FloatBuffer

class Cylinder(Quadric):

  def draw(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int) -> None: ...

  def __init__(self): ...


class Disk(Quadric):

  def draw(self, arg0: float, arg1: float, arg2: int, arg3: int) -> None: ...

  def __init__(self): ...


class GLU:

  GLU_AUTO_LOAD_MATRIX: int

  GLU_BEGIN: int

  GLU_CCW: int

  GLU_CULLING: int

  GLU_CW: int

  GLU_DISPLAY_MODE: int

  GLU_DOMAIN_DISTANCE: int

  GLU_EDGE_FLAG: int

  GLU_END: int

  GLU_ERROR: int

  GLU_EXTENSIONS: int

  GLU_EXTERIOR: int

  GLU_FALSE: bool

  GLU_FILL: int

  GLU_FLAT: int

  GLU_INCOMPATIBLE_GL_VERSION: int

  GLU_INSIDE: int

  GLU_INTERIOR: int

  GLU_INVALID_ENUM: int

  GLU_INVALID_VALUE: int

  GLU_LINE: int

  GLU_MAP1_TRIM_2: int

  GLU_MAP1_TRIM_3: int

  GLU_NONE: int

  GLU_NURBS_ERROR1: int

  GLU_NURBS_ERROR10: int

  GLU_NURBS_ERROR11: int

  GLU_NURBS_ERROR12: int

  GLU_NURBS_ERROR13: int

  GLU_NURBS_ERROR14: int

  GLU_NURBS_ERROR15: int

  GLU_NURBS_ERROR16: int

  GLU_NURBS_ERROR17: int

  GLU_NURBS_ERROR18: int

  GLU_NURBS_ERROR19: int

  GLU_NURBS_ERROR2: int

  GLU_NURBS_ERROR20: int

  GLU_NURBS_ERROR21: int

  GLU_NURBS_ERROR22: int

  GLU_NURBS_ERROR23: int

  GLU_NURBS_ERROR24: int

  GLU_NURBS_ERROR25: int

  GLU_NURBS_ERROR26: int

  GLU_NURBS_ERROR27: int

  GLU_NURBS_ERROR28: int

  GLU_NURBS_ERROR29: int

  GLU_NURBS_ERROR3: int

  GLU_NURBS_ERROR30: int

  GLU_NURBS_ERROR31: int

  GLU_NURBS_ERROR32: int

  GLU_NURBS_ERROR33: int

  GLU_NURBS_ERROR34: int

  GLU_NURBS_ERROR35: int

  GLU_NURBS_ERROR36: int

  GLU_NURBS_ERROR37: int

  GLU_NURBS_ERROR4: int

  GLU_NURBS_ERROR5: int

  GLU_NURBS_ERROR6: int

  GLU_NURBS_ERROR7: int

  GLU_NURBS_ERROR8: int

  GLU_NURBS_ERROR9: int

  GLU_OUT_OF_MEMORY: int

  GLU_OUTLINE_PATCH: int

  GLU_OUTLINE_POLYGON: int

  GLU_OUTSIDE: int

  GLU_PARAMETRIC_ERROR: int

  GLU_PARAMETRIC_TOLERANCE: int

  GLU_PATH_LENGTH: int

  GLU_POINT: int

  GLU_SAMPLING_METHOD: int

  GLU_SAMPLING_TOLERANCE: int

  GLU_SILHOUETTE: int

  GLU_SMOOTH: int

  GLU_TESS_BEGIN: int

  GLU_TESS_BEGIN_DATA: int

  GLU_TESS_BOUNDARY_ONLY: int

  GLU_TESS_COMBINE: int

  GLU_TESS_COMBINE_DATA: int

  GLU_TESS_COORD_TOO_LARGE: int

  GLU_TESS_EDGE_FLAG: int

  GLU_TESS_EDGE_FLAG_DATA: int

  GLU_TESS_END: int

  GLU_TESS_END_DATA: int

  GLU_TESS_ERROR: int

  GLU_TESS_ERROR1: int

  GLU_TESS_ERROR2: int

  GLU_TESS_ERROR3: int

  GLU_TESS_ERROR4: int

  GLU_TESS_ERROR5: int

  GLU_TESS_ERROR6: int

  GLU_TESS_ERROR7: int

  GLU_TESS_ERROR8: int

  GLU_TESS_ERROR_DATA: int

  GLU_TESS_MAX_COORD: float

  GLU_TESS_MISSING_BEGIN_CONTOUR: int

  GLU_TESS_MISSING_BEGIN_POLYGON: int

  GLU_TESS_MISSING_END_CONTOUR: int

  GLU_TESS_MISSING_END_POLYGON: int

  GLU_TESS_NEED_COMBINE_CALLBACK: int

  GLU_TESS_TOLERANCE: int

  GLU_TESS_VERTEX: int

  GLU_TESS_VERTEX_DATA: int

  GLU_TESS_WINDING_ABS_GEQ_TWO: int

  GLU_TESS_WINDING_NEGATIVE: int

  GLU_TESS_WINDING_NONZERO: int

  GLU_TESS_WINDING_ODD: int

  GLU_TESS_WINDING_POSITIVE: int

  GLU_TESS_WINDING_RULE: int

  GLU_TRUE: bool

  GLU_U_STEP: int

  GLU_UNKNOWN: int

  GLU_V_STEP: int

  GLU_VERSION: int

  GLU_VERTEX: int

  TESS_MAX_COORD: float

  @staticmethod
  def gluBuild2DMipmaps(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: ByteBuffer) -> int: ...

  @staticmethod
  def gluCheckExtension(arg0: str, arg1: str) -> bool: ...

  @staticmethod
  def gluErrorString(arg0: int) -> str: ...

  @staticmethod
  def gluGetString(arg0: int) -> str: ...

  @staticmethod
  def gluLookAt(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None: ...

  @staticmethod
  def gluNewTess() -> GLUtessellator: ...

  @staticmethod
  def gluOrtho2D(arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

  @staticmethod
  def gluPerspective(arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

  @staticmethod
  def gluPickMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: IntBuffer) -> None: ...

  @staticmethod
  def gluProject(arg0: float, arg1: float, arg2: float, arg3: FloatBuffer, arg4: FloatBuffer, arg5: IntBuffer, arg6: FloatBuffer) -> bool: ...

  @staticmethod
  def gluScaleImage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: ByteBuffer, arg5: int, arg6: int, arg7: int, arg8: ByteBuffer) -> int: ...

  @staticmethod
  def gluUnProject(arg0: float, arg1: float, arg2: float, arg3: FloatBuffer, arg4: FloatBuffer, arg5: IntBuffer, arg6: FloatBuffer) -> bool: ...

  def __init__(self): ...


class GLUtessellator:

  def gluBeginPolygon(self) -> None: ...

  def gluDeleteTess(self) -> None: ...

  def gluEndPolygon(self) -> None: ...

  def gluGetTessProperty(self, arg0: int, arg1: list[float], arg2: int) -> None: ...

  def gluNextContour(self, arg0: int) -> None: ...

  def gluTessBeginContour(self) -> None: ...

  def gluTessBeginPolygon(self, arg0: object) -> None: ...

  def gluTessCallback(self, arg0: int, arg1: GLUtessellatorCallback) -> None: ...

  def gluTessEndContour(self) -> None: ...

  def gluTessEndPolygon(self) -> None: ...

  def gluTessNormal(self, arg0: float, arg1: float, arg2: float) -> None: ...

  def gluTessProperty(self, arg0: int, arg1: float) -> None: ...

  def gluTessVertex(self, arg0: list[float], arg1: int, arg2: object) -> None: ...


class GLUtessellatorCallback:

  def begin(self, arg0: int) -> None: ...

  def beginData(self, arg0: int, arg1: object) -> None: ...

  def combine(self, arg0: list[float], arg1: list[object], arg2: list[float], arg3: list[object]) -> None: ...

  def combineData(self, arg0: list[float], arg1: list[object], arg2: list[float], arg3: list[object], arg4: object) -> None: ...

  def edgeFlag(self, arg0: bool) -> None: ...

  def edgeFlagData(self, arg0: bool, arg1: object) -> None: ...

  def end(self) -> None: ...

  def endData(self, arg0: object) -> None: ...

  def error(self, arg0: int) -> None: ...

  def errorData(self, arg0: int, arg1: object) -> None: ...

  def vertex(self, arg0: object) -> None: ...

  def vertexData(self, arg0: object, arg1: object) -> None: ...


class GLUtessellatorCallbackAdapter:

  @overload
  def begin(self, arg0: int) -> None: ...

  @overload
  def begin(self, arg0: int) -> None: ...

  @overload
  def beginData(self, arg0: int, arg1: object) -> None: ...

  @overload
  def beginData(self, arg0: int, arg1: object) -> None: ...

  @overload
  def combine(self, arg0: list[float], arg1: list[object], arg2: list[float], arg3: list[object]) -> None: ...

  @overload
  def combine(self, arg0: list[float], arg1: list[object], arg2: list[float], arg3: list[object]) -> None: ...

  @overload
  def combineData(self, arg0: list[float], arg1: list[object], arg2: list[float], arg3: list[object], arg4: object) -> None: ...

  @overload
  def combineData(self, arg0: list[float], arg1: list[object], arg2: list[float], arg3: list[object], arg4: object) -> None: ...

  @overload
  def edgeFlag(self, arg0: bool) -> None: ...

  @overload
  def edgeFlag(self, arg0: bool) -> None: ...

  @overload
  def edgeFlagData(self, arg0: bool, arg1: object) -> None: ...

  @overload
  def edgeFlagData(self, arg0: bool, arg1: object) -> None: ...

  @overload
  def end(self) -> None: ...

  @overload
  def end(self) -> None: ...

  @overload
  def endData(self, arg0: object) -> None: ...

  @overload
  def endData(self, arg0: object) -> None: ...

  @overload
  def error(self, arg0: int) -> None: ...

  @overload
  def error(self, arg0: int) -> None: ...

  @overload
  def errorData(self, arg0: int, arg1: object) -> None: ...

  @overload
  def errorData(self, arg0: int, arg1: object) -> None: ...

  @overload
  def vertex(self, arg0: object) -> None: ...

  @overload
  def vertex(self, arg0: object) -> None: ...

  @overload
  def vertexData(self, arg0: object, arg1: object) -> None: ...

  @overload
  def vertexData(self, arg0: object, arg1: object) -> None: ...

  def __init__(self): ...


class MipMap(Util):

  @staticmethod
  def gluBuild2DMipmaps(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: ByteBuffer) -> int: ...

  @staticmethod
  def gluScaleImage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: ByteBuffer, arg5: int, arg6: int, arg7: int, arg8: ByteBuffer) -> int: ...

  def __init__(self): ...


class PartialDisk(Quadric):

  def draw(self, arg0: float, arg1: float, arg2: int, arg3: int, arg4: float, arg5: float) -> None: ...

  def __init__(self): ...


class Project(Util):

  @staticmethod
  def gluLookAt(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None: ...

  @staticmethod
  def gluPerspective(arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

  @staticmethod
  def gluPickMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: IntBuffer) -> None: ...

  @staticmethod
  def gluProject(arg0: float, arg1: float, arg2: float, arg3: FloatBuffer, arg4: FloatBuffer, arg5: IntBuffer, arg6: FloatBuffer) -> bool: ...

  @staticmethod
  def gluUnProject(arg0: float, arg1: float, arg2: float, arg3: FloatBuffer, arg4: FloatBuffer, arg5: IntBuffer, arg6: FloatBuffer) -> bool: ...

  def __init__(self): ...


class Quadric:

  def getDrawStyle(self) -> int: ...

  def getNormals(self) -> int: ...

  def getOrientation(self) -> int: ...

  def getTextureFlag(self) -> bool: ...

  def setDrawStyle(self, arg0: int) -> None: ...

  def setNormals(self, arg0: int) -> None: ...

  def setOrientation(self, arg0: int) -> None: ...

  def setTextureFlag(self, arg0: bool) -> None: ...

  def __init__(self): ...


class Registry(Util):

  @staticmethod
  def gluCheckExtension(arg0: str, arg1: str) -> bool: ...

  @staticmethod
  def gluGetString(arg0: int) -> str: ...

  def __init__(self): ...


class Sphere(Quadric):

  def draw(self, arg0: float, arg1: int, arg2: int) -> None: ...

  def __init__(self): ...


class Util:

  def __init__(self): ...


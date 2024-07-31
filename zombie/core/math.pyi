from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from org.joml import Matrix4f, Vector3f, Vector4f
from org.lwjgl.util.vector import Matrix4f, Vector3f, Quaternion, Vector4f
from zombie.iso import Vector2

class Matrix4(Matrix4f):

  def Get(self) -> Matrix4f: ...

  def Set(self, m: Matrix4f) -> None: ...

  @overload
  def __init__(self, m: Matrix4): ...
  @overload
  def __init__(self, m00: float, m01: float, m02: float, m03: float, m10: float, m11: float, m12: float, m13: float, m20: float, m21: float, m22: float, m23: float, m30: float, m31: float, m32: float, m33: float): ...


class PZMath:

  degToRads: float

  microsToNanos: int

  millisToMicros: int

  PI: float

  PI2: float

  radToDegs: float

  secondsToMillis: int

  secondsToNanos: int

  @staticmethod
  def abs(val: float) -> float: ...

  @staticmethod
  def almostIdentity(x: float, m: float, n: float) -> float: ...

  @staticmethod
  def almostUnitIdentity(x: float) -> float: ...

  @staticmethod
  def c_lerp(src: float, dest: float, alpha: float) -> float: ...

  @staticmethod
  def canParseFloat(varStr: str) -> bool: ...

  @staticmethod
  def ceil(val: float) -> float: ...

  @staticmethod
  @overload
  def clamp(val: float, min: float, max: float) -> float: ...

  @staticmethod
  @overload
  def clamp(val: int, min: int, max: int) -> int: ...

  @staticmethod
  @overload
  def clamp(val: int, min: int, max: int) -> int: ...

  @staticmethod
  def clampFloat(val: float, min: float, max: float) -> float: ...

  @staticmethod
  def clamp_01(val: float) -> float: ...

  @staticmethod
  @overload
  def convertMatrix(src: Matrix4f, dst: Matrix4f) -> Matrix4f: ...

  @staticmethod
  @overload
  def convertMatrix(src: Matrix4f, dst: Matrix4f) -> Matrix4f: ...

  @staticmethod
  def degToRad(degrees: float) -> float: ...

  @staticmethod
  @overload
  def equal(a: float, b: float) -> bool: ...

  @staticmethod
  @overload
  def equal(a: float, b: float, delta: float) -> bool: ...

  @staticmethod
  @overload
  def fastfloor(x: float) -> int: ...

  @staticmethod
  @overload
  def fastfloor(x: float) -> int: ...

  @staticmethod
  def floor(val: float) -> float: ...

  @staticmethod
  def frac(val: float) -> float: ...

  @staticmethod
  def gain(x: float, k: float) -> float: ...

  @staticmethod
  def getClosestAngle(in_radsA: float, in_radsB: float) -> float: ...

  @staticmethod
  def getClosestAngleDegrees(in_degsA: float, in_degsB: float) -> float: ...

  @staticmethod
  @overload
  def lerp(src: float, dest: float, alpha: float) -> float: ...

  @staticmethod
  @overload
  def lerp(out: Vector3f, a: Vector3f, b: Vector3f, t: float) -> Vector3f: ...

  @staticmethod
  @overload
  def lerp(out: Vector2, a: Vector2, b: Vector2, t: float) -> Vector2: ...

  @staticmethod
  def lerpAngle(src: float, dest: float, alpha: float) -> float: ...

  @staticmethod
  def lerpFunc_EaseInQuad(x: float) -> float: ...

  @staticmethod
  def lerpFunc_EaseOutInQuad(x: float) -> float: ...

  @staticmethod
  def lerpFunc_EaseOutQuad(x: float) -> float: ...

  @staticmethod
  @overload
  def max(a: float, b: float) -> float: ...

  @staticmethod
  @overload
  def max(a: int, b: int) -> int: ...

  @staticmethod
  @overload
  def min(a: float, b: float) -> float: ...

  @staticmethod
  @overload
  def min(a: int, b: int) -> int: ...

  @staticmethod
  def radToDeg(radians: float) -> float: ...

  @staticmethod
  def roundFromEdges(val: float) -> float: ...

  @staticmethod
  def roundToInt(val: float) -> int: ...

  @staticmethod
  def roundToIntPlus05(val: float) -> float: ...

  @staticmethod
  def roundToNearest(val: float) -> float: ...

  @staticmethod
  def sign(val: float) -> int: ...

  @staticmethod
  def slerp(result: Quaternion, arg1: Quaternion, to: Quaternion, alpha: float) -> Quaternion: ...

  @staticmethod
  def sqrt(val: float) -> float: ...

  @staticmethod
  def step(arg0: float, to: float, delta: float) -> float: ...

  @staticmethod
  def testSideOfLine(x1: float, y1: float, x2: float, y2: float, px: float, py: float) -> PZMath.SideOfLine: ...

  @staticmethod
  def tryParseDouble(varStr: str, defaultVal: float) -> float: ...

  @staticmethod
  def tryParseFloat(varStr: str, defaultVal: float) -> float: ...

  @staticmethod
  def tryParseInt(varStr: str, defaultVal: int) -> int: ...

  @staticmethod
  @overload
  def wrap(val: float, range: float) -> float: ...

  @staticmethod
  @overload
  def wrap(in_val: float, in_min: float, in_max: float) -> float: ...

  def __init__(self): ...

  class SideOfLine(Enum):

    Left: PZMath.SideOfLine

    OnLine: PZMath.SideOfLine

    Right: PZMath.SideOfLine

    @staticmethod
    def valueOf(arg0: str) -> PZMath.SideOfLine: ...

    @staticmethod
    def values() -> list[PZMath.SideOfLine]: ...

  class UnitTests:

    class vector2:

      @staticmethod
      def run() -> None: ...

      def __init__(self): ...

    class getClosestAngle:

      @staticmethod
      def run() -> None: ...

    class lerpFunctions:

      @staticmethod
      def run() -> None: ...


class Vector3(Vector3f):

  def Get(self) -> Vector3f: ...

  def Set(self, v: Vector3f) -> None: ...

  def cross(self, vec: Vector3) -> Vector3: ...

  def dot(self, vec: Vector3) -> float: ...

  def reset(self) -> Vector3: ...

  @staticmethod
  def addScaled(a: Vector3f, b: Vector3f, scale: float, result: Vector3f) -> Vector3f: ...

  @staticmethod
  def setScaled(a: Vector3f, scale: float, result: Vector3f) -> Vector3f: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, v: Vector3f): ...
  @overload
  def __init__(self, v: Vector3): ...
  @overload
  def __init__(self, x: float, y: float, z: float): ...


class Vector4(Vector4f):

  def Get(self) -> Vector4f: ...

  def Set(self, v: Vector4f) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, v: Vector4f): ...
  @overload
  def __init__(self, x: float, y: float, z: float, w: float): ...


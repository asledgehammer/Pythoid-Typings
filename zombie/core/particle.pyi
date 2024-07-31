from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from org.joml import Matrix4f

class MuzzleFlash:

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def render(xfrm: Matrix4f) -> None: ...

  def __init__(self): ...


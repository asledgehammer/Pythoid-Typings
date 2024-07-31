from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import List
from org.lwjgl.util.vector import Vector3f, Quaternion
from zombie.core.skinnedmodel.animation import Keyframe
from zombie.scripting import ScriptParser
from zombie.scripting.objects import BaseScriptObject

class CopyFrame:

  @overload
  def exec(self, keyframes: List[Keyframe]) -> None: ...

  @overload
  def exec(self, keyframes: List[Keyframe]) -> None: ...

  @overload
  def parse(self, block: ScriptParser.Block) -> None: ...

  @overload
  def parse(self, block: ScriptParser.Block) -> None: ...

  def __init__(self): ...


class CopyFrames:

  @overload
  def exec(self, keyframes: List[Keyframe]) -> None: ...

  @overload
  def exec(self, keyframes: List[Keyframe]) -> None: ...

  @overload
  def parse(self, block: ScriptParser.Block) -> None: ...

  @overload
  def parse(self, block: ScriptParser.Block) -> None: ...

  def __init__(self): ...


class IRuntimeAnimationCommand:

  def exec(self, keyframes: List[Keyframe]) -> None: ...

  def parse(self, block: ScriptParser.Block) -> None: ...


class KeyframeUtil:

  @staticmethod
  def GetKeyFramePosition(keyframes: list[Keyframe], time: float, duration: float) -> Vector3f: ...

  @staticmethod
  def GetKeyFrameRotation(keyframes: list[Keyframe], time: float, duration: float) -> Quaternion: ...

  def __init__(self): ...


class RuntimeAnimationScript(BaseScriptObject):

  def Load(self, name: str, totalFile: str) -> None: ...

  def exec(self) -> None: ...

  def reset(self) -> None: ...

  def __init__(self): ...


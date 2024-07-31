from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from javax.sound.sampled import AudioInputStream

class FadeableAudioInputStream(AudioInputStream):

  def fadeOut(self) -> None: ...

  @overload
  def read(self, arg0: list[int]) -> int: ...

  @overload
  def read(self, arg0: list[int], arg1: int, arg2: int) -> int: ...

  def __init__(self, arg0: AudioInputStream): ...


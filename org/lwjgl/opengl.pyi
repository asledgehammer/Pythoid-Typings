from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from org.lwjgl.system import Callback

class GLCapabilities: ...


class GLDebugMessageCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> None: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLDebugMessageCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLDebugMessageCallbackI) -> GLDebugMessageCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLDebugMessageCallback: ...

  @staticmethod
  def getMessage(arg0: int, arg1: int) -> str: ...

  class Container(GLDebugMessageCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> None: ...


class GLDebugMessageCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> None: ...


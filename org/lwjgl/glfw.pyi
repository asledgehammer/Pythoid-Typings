from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import PrintStream
from java.nio import FloatBuffer, ByteBuffer
from org.lwjgl.system import Callback, Struct, MemoryStack, StructBuffer

class GLFWCharCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...

  def set(self, arg0: int) -> GLFWCharCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWCharCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWCharCallbackI) -> GLFWCharCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWCharCallback: ...

  class Container(GLFWCharCallback):

    def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWCharCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWCursorPosCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...

  def set(self, arg0: int) -> GLFWCursorPosCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWCursorPosCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWCursorPosCallbackI) -> GLFWCursorPosCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWCursorPosCallback: ...

  class Container(GLFWCursorPosCallback):

    def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWCursorPosCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWErrorCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...

  def set(self) -> GLFWErrorCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWErrorCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWErrorCallbackI) -> GLFWErrorCallback: ...

  @staticmethod
  @overload
  def createPrint() -> GLFWErrorCallback: ...

  @staticmethod
  @overload
  def createPrint(arg0: PrintStream) -> GLFWErrorCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWErrorCallback: ...

  @staticmethod
  def createThrow() -> GLFWErrorCallback: ...

  @staticmethod
  def getDescription(arg0: int) -> str: ...

  class Container(GLFWErrorCallback):

    def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWErrorCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int) -> None: ...


class GLFWFramebufferSizeCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

  def set(self, arg0: int) -> GLFWFramebufferSizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWFramebufferSizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWFramebufferSizeCallbackI) -> GLFWFramebufferSizeCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWFramebufferSizeCallback: ...

  class Container(GLFWFramebufferSizeCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWFramebufferSizeCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWGamepadState(Struct):

  ALIGNOF: int

  @overload
  def axes(self) -> FloatBuffer: ...

  @overload
  def axes(self, arg0: int) -> float: ...

  @overload
  def axes(self, arg0: FloatBuffer) -> GLFWGamepadState: ...

  @overload
  def axes(self, arg0: int, arg1: float) -> GLFWGamepadState: ...

  @overload
  def buttons(self) -> ByteBuffer: ...

  @overload
  def buttons(self, arg0: int) -> int: ...

  @overload
  def buttons(self, arg0: ByteBuffer) -> GLFWGamepadState: ...

  @overload
  def buttons(self, arg0: int, arg1: int) -> GLFWGamepadState: ...

  def close(self) -> None: ...

  def free(self) -> None: ...

  @overload
  def set(self, arg0: GLFWGamepadState) -> GLFWGamepadState: ...

  @overload
  def set(self, arg0: ByteBuffer, arg1: FloatBuffer) -> GLFWGamepadState: ...

  def sizeof(self) -> int: ...

  @staticmethod
  @overload
  def calloc() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def calloc(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def callocStack() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def callocStack(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def callocStack(arg0: MemoryStack) -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def callocStack(arg0: int, arg1: MemoryStack) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def create() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def malloc() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def malloc(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def mallocStack() -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def mallocStack(arg0: MemoryStack) -> GLFWGamepadState: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int, arg1: MemoryStack) -> GLFWGamepadState.Buffer: ...

  @staticmethod
  @overload
  def naxes(arg0: int) -> FloatBuffer: ...

  @staticmethod
  @overload
  def naxes(arg0: int, arg1: int) -> float: ...

  @staticmethod
  @overload
  def naxes(arg0: int, arg1: FloatBuffer) -> None: ...

  @staticmethod
  @overload
  def naxes(arg0: int, arg1: int, arg2: float) -> None: ...

  @staticmethod
  @overload
  def nbuttons(arg0: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def nbuttons(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def nbuttons(arg0: int, arg1: ByteBuffer) -> None: ...

  @staticmethod
  @overload
  def nbuttons(arg0: int, arg1: int, arg2: int) -> None: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    @overload
    def axes(self) -> FloatBuffer: ...

    @overload
    def axes(self, arg0: int) -> float: ...

    @overload
    def axes(self, arg0: FloatBuffer) -> GLFWGamepadState.Buffer: ...

    @overload
    def axes(self, arg0: int, arg1: float) -> GLFWGamepadState.Buffer: ...

    @overload
    def buttons(self) -> ByteBuffer: ...

    @overload
    def buttons(self, arg0: int) -> int: ...

    @overload
    def buttons(self, arg0: ByteBuffer) -> GLFWGamepadState.Buffer: ...

    @overload
    def buttons(self, arg0: int, arg1: int) -> GLFWGamepadState.Buffer: ...

    def close(self) -> None: ...

    def free(self) -> None: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...


class GLFWImage(Struct):

  ALIGNOF: int

  def close(self) -> None: ...

  def free(self) -> None: ...

  @overload
  def height(self) -> int: ...

  @overload
  def height(self, arg0: int) -> GLFWImage: ...

  @overload
  def pixels(self, arg0: int) -> ByteBuffer: ...

  @overload
  def pixels(self, arg0: ByteBuffer) -> GLFWImage: ...

  @overload
  def set(self, arg0: GLFWImage) -> GLFWImage: ...

  @overload
  def set(self, arg0: int, arg1: int, arg2: ByteBuffer) -> GLFWImage: ...

  def sizeof(self) -> int: ...

  @overload
  def width(self) -> int: ...

  @overload
  def width(self, arg0: int) -> GLFWImage: ...

  @staticmethod
  @overload
  def calloc() -> GLFWImage: ...

  @staticmethod
  @overload
  def calloc(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def callocStack() -> GLFWImage: ...

  @staticmethod
  @overload
  def callocStack(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def callocStack(arg0: MemoryStack) -> GLFWImage: ...

  @staticmethod
  @overload
  def callocStack(arg0: int, arg1: MemoryStack) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def create() -> GLFWImage: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWImage: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> GLFWImage: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def malloc() -> GLFWImage: ...

  @staticmethod
  @overload
  def malloc(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def mallocStack() -> GLFWImage: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def mallocStack(arg0: MemoryStack) -> GLFWImage: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int, arg1: MemoryStack) -> GLFWImage.Buffer: ...

  @staticmethod
  @overload
  def nheight(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nheight(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def npixels(arg0: int, arg1: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def npixels(arg0: int, arg1: ByteBuffer) -> None: ...

  @staticmethod
  @overload
  def nwidth(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nwidth(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def validate(arg0: int) -> None: ...

  @staticmethod
  @overload
  def validate(arg0: int, arg1: int) -> None: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    def close(self) -> None: ...

    def free(self) -> None: ...

    @overload
    def height(self) -> int: ...

    @overload
    def height(self, arg0: int) -> GLFWImage.Buffer: ...

    @overload
    def pixels(self, arg0: int) -> ByteBuffer: ...

    @overload
    def pixels(self, arg0: ByteBuffer) -> GLFWImage.Buffer: ...

    @overload
    def width(self) -> int: ...

    @overload
    def width(self, arg0: int) -> GLFWImage.Buffer: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...


class GLFWKeyCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...

  def set(self, arg0: int) -> GLFWKeyCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWKeyCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWKeyCallbackI) -> GLFWKeyCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWKeyCallback: ...

  class Container(GLFWKeyCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...


class GLFWKeyCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...


class GLFWMouseButtonCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def set(self, arg0: int) -> GLFWMouseButtonCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWMouseButtonCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWMouseButtonCallbackI) -> GLFWMouseButtonCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWMouseButtonCallback: ...

  class Container(GLFWMouseButtonCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...


class GLFWMouseButtonCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...


class GLFWScrollCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...

  def set(self, arg0: int) -> GLFWScrollCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWScrollCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWScrollCallbackI) -> GLFWScrollCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWScrollCallback: ...

  class Container(GLFWScrollCallback):

    def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWScrollCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: float, arg2: float) -> None: ...


class GLFWWindowFocusCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...

  def set(self, arg0: int) -> GLFWWindowFocusCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowFocusCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowFocusCallbackI) -> GLFWWindowFocusCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowFocusCallback: ...

  class Container(GLFWWindowFocusCallback):

    def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowFocusCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowIconifyCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...

  def set(self, arg0: int) -> GLFWWindowIconifyCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowIconifyCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowIconifyCallbackI) -> GLFWWindowIconifyCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowIconifyCallback: ...

  class Container(GLFWWindowIconifyCallback):

    def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowIconifyCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: bool) -> None: ...


class GLFWWindowPosCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

  def set(self, arg0: int) -> GLFWWindowPosCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowPosCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowPosCallbackI) -> GLFWWindowPosCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowPosCallback: ...

  class Container(GLFWWindowPosCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWWindowPosCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWWindowRefreshCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int) -> None: ...

  def set(self, arg0: int) -> GLFWWindowRefreshCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowRefreshCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowRefreshCallbackI) -> GLFWWindowRefreshCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowRefreshCallback: ...

  class Container(GLFWWindowRefreshCallback):

    def invoke(self, arg0: int) -> None: ...


class GLFWWindowRefreshCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int) -> None: ...


class GLFWWindowSizeCallback(Callback):

  SIGNATURE: str

  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...

  def set(self, arg0: int) -> GLFWWindowSizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: int) -> GLFWWindowSizeCallback: ...

  @staticmethod
  @overload
  def create(arg0: GLFWWindowSizeCallbackI) -> GLFWWindowSizeCallback: ...

  @staticmethod
  def createSafe(arg0: int) -> GLFWWindowSizeCallback: ...

  class Container(GLFWWindowSizeCallback):

    def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


class GLFWWindowSizeCallbackI:

  SIGNATURE: str

  @overload
  def callback(self, arg0: int) -> None: ...

  @overload
  def callback(self, arg0: int) -> None: ...

  def getSignature(self) -> str: ...

  def invoke(self, arg0: int, arg1: int, arg2: int) -> None: ...


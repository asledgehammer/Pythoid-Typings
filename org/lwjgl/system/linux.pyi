from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer
from org.lwjgl.system import Struct, MemoryStack, StructBuffer

class Visual(Struct):

  ALIGNOF: int

  @overload
  def bits_per_rgb(self) -> int: ...

  @overload
  def bits_per_rgb(self, arg0: int) -> Visual: ...

  @overload
  def blue_mask(self) -> int: ...

  @overload
  def blue_mask(self, arg0: int) -> Visual: ...

  @overload
  def class$(self) -> int: ...

  @overload
  def class$(self, arg0: int) -> Visual: ...

  def close(self) -> None: ...

  @overload
  def ext_data(self) -> int: ...

  @overload
  def ext_data(self, arg0: int) -> Visual: ...

  def free(self) -> None: ...

  @overload
  def green_mask(self) -> int: ...

  @overload
  def green_mask(self, arg0: int) -> Visual: ...

  @overload
  def map_entries(self) -> int: ...

  @overload
  def map_entries(self, arg0: int) -> Visual: ...

  @overload
  def red_mask(self) -> int: ...

  @overload
  def red_mask(self, arg0: int) -> Visual: ...

  @overload
  def set(self, arg0: Visual) -> Visual: ...

  @overload
  def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> Visual: ...

  def sizeof(self) -> int: ...

  @overload
  def visualid(self) -> int: ...

  @overload
  def visualid(self, arg0: int) -> Visual: ...

  @staticmethod
  @overload
  def calloc() -> Visual: ...

  @staticmethod
  @overload
  def calloc(arg0: int) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def callocStack() -> Visual: ...

  @staticmethod
  @overload
  def callocStack(arg0: int) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def callocStack(arg0: MemoryStack) -> Visual: ...

  @staticmethod
  @overload
  def callocStack(arg0: int, arg1: MemoryStack) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def create() -> Visual: ...

  @staticmethod
  @overload
  def create(arg0: int) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def create(arg0: int) -> Visual: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> Visual: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def malloc() -> Visual: ...

  @staticmethod
  @overload
  def malloc(arg0: int) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def mallocStack() -> Visual: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def mallocStack(arg0: MemoryStack) -> Visual: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int, arg1: MemoryStack) -> Visual.Buffer: ...

  @staticmethod
  @overload
  def nbits_per_rgb(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nbits_per_rgb(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nblue_mask(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nblue_mask(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nclass$(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nclass$(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def next_data(arg0: int) -> int: ...

  @staticmethod
  @overload
  def next_data(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def ngreen_mask(arg0: int) -> int: ...

  @staticmethod
  @overload
  def ngreen_mask(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nmap_entries(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nmap_entries(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nred_mask(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nred_mask(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nvisualid(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nvisualid(arg0: int, arg1: int) -> None: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    @overload
    def bits_per_rgb(self) -> int: ...

    @overload
    def bits_per_rgb(self, arg0: int) -> Visual.Buffer: ...

    @overload
    def blue_mask(self) -> int: ...

    @overload
    def blue_mask(self, arg0: int) -> Visual.Buffer: ...

    @overload
    def class$(self) -> int: ...

    @overload
    def class$(self, arg0: int) -> Visual.Buffer: ...

    def close(self) -> None: ...

    @overload
    def ext_data(self) -> int: ...

    @overload
    def ext_data(self, arg0: int) -> Visual.Buffer: ...

    def free(self) -> None: ...

    @overload
    def green_mask(self) -> int: ...

    @overload
    def green_mask(self, arg0: int) -> Visual.Buffer: ...

    @overload
    def map_entries(self) -> int: ...

    @overload
    def map_entries(self, arg0: int) -> Visual.Buffer: ...

    @overload
    def red_mask(self) -> int: ...

    @overload
    def red_mask(self, arg0: int) -> Visual.Buffer: ...

    @overload
    def visualid(self) -> int: ...

    @overload
    def visualid(self, arg0: int) -> Visual.Buffer: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...


class XVisualInfo(Struct):

  ALIGNOF: int

  @overload
  def bits_per_rgb(self) -> int: ...

  @overload
  def bits_per_rgb(self, arg0: int) -> XVisualInfo: ...

  @overload
  def blue_mask(self) -> int: ...

  @overload
  def blue_mask(self, arg0: int) -> XVisualInfo: ...

  @overload
  def class$(self) -> int: ...

  @overload
  def class$(self, arg0: int) -> XVisualInfo: ...

  def close(self) -> None: ...

  @overload
  def colormap_size(self) -> int: ...

  @overload
  def colormap_size(self, arg0: int) -> XVisualInfo: ...

  @overload
  def depth(self) -> int: ...

  @overload
  def depth(self, arg0: int) -> XVisualInfo: ...

  def free(self) -> None: ...

  @overload
  def green_mask(self) -> int: ...

  @overload
  def green_mask(self, arg0: int) -> XVisualInfo: ...

  @overload
  def red_mask(self) -> int: ...

  @overload
  def red_mask(self, arg0: int) -> XVisualInfo: ...

  @overload
  def screen(self) -> int: ...

  @overload
  def screen(self, arg0: int) -> XVisualInfo: ...

  @overload
  def set(self, arg0: XVisualInfo) -> XVisualInfo: ...

  @overload
  def set(self, arg0: Visual, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> XVisualInfo: ...

  def sizeof(self) -> int: ...

  @overload
  def visual(self) -> Visual: ...

  @overload
  def visual(self, arg0: Visual) -> XVisualInfo: ...

  @overload
  def visualid(self) -> int: ...

  @overload
  def visualid(self, arg0: int) -> XVisualInfo: ...

  @staticmethod
  @overload
  def calloc() -> XVisualInfo: ...

  @staticmethod
  @overload
  def calloc(arg0: int) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def callocStack() -> XVisualInfo: ...

  @staticmethod
  @overload
  def callocStack(arg0: int) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def callocStack(arg0: MemoryStack) -> XVisualInfo: ...

  @staticmethod
  @overload
  def callocStack(arg0: int, arg1: MemoryStack) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def create() -> XVisualInfo: ...

  @staticmethod
  @overload
  def create(arg0: int) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def create(arg0: int) -> XVisualInfo: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> XVisualInfo: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def malloc() -> XVisualInfo: ...

  @staticmethod
  @overload
  def malloc(arg0: int) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def mallocStack() -> XVisualInfo: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def mallocStack(arg0: MemoryStack) -> XVisualInfo: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int, arg1: MemoryStack) -> XVisualInfo.Buffer: ...

  @staticmethod
  @overload
  def nbits_per_rgb(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nbits_per_rgb(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nblue_mask(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nblue_mask(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nclass$(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nclass$(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def ncolormap_size(arg0: int) -> int: ...

  @staticmethod
  @overload
  def ncolormap_size(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def ndepth(arg0: int) -> int: ...

  @staticmethod
  @overload
  def ndepth(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def ngreen_mask(arg0: int) -> int: ...

  @staticmethod
  @overload
  def ngreen_mask(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nred_mask(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nred_mask(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nscreen(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nscreen(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nvisual(arg0: int) -> Visual: ...

  @staticmethod
  @overload
  def nvisual(arg0: int, arg1: Visual) -> None: ...

  @staticmethod
  @overload
  def nvisualid(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nvisualid(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def validate(arg0: int) -> None: ...

  @staticmethod
  @overload
  def validate(arg0: int, arg1: int) -> None: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    @overload
    def bits_per_rgb(self) -> int: ...

    @overload
    def bits_per_rgb(self, arg0: int) -> XVisualInfo.Buffer: ...

    @overload
    def blue_mask(self) -> int: ...

    @overload
    def blue_mask(self, arg0: int) -> XVisualInfo.Buffer: ...

    @overload
    def class$(self) -> int: ...

    @overload
    def class$(self, arg0: int) -> XVisualInfo.Buffer: ...

    def close(self) -> None: ...

    @overload
    def colormap_size(self) -> int: ...

    @overload
    def colormap_size(self, arg0: int) -> XVisualInfo.Buffer: ...

    @overload
    def depth(self) -> int: ...

    @overload
    def depth(self, arg0: int) -> XVisualInfo.Buffer: ...

    def free(self) -> None: ...

    @overload
    def green_mask(self) -> int: ...

    @overload
    def green_mask(self, arg0: int) -> XVisualInfo.Buffer: ...

    @overload
    def red_mask(self) -> int: ...

    @overload
    def red_mask(self, arg0: int) -> XVisualInfo.Buffer: ...

    @overload
    def screen(self) -> int: ...

    @overload
    def screen(self, arg0: int) -> XVisualInfo.Buffer: ...

    @overload
    def visual(self) -> Visual: ...

    @overload
    def visual(self, arg0: Visual) -> XVisualInfo.Buffer: ...

    @overload
    def visualid(self) -> int: ...

    @overload
    def visualid(self, arg0: int) -> XVisualInfo.Buffer: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...


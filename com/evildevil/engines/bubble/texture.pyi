from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import BufferedInputStream
from java.lang import Exception

class DDPixelFormat:

  DDPF_APHAPIXES: int

  DDPF_FOURCC: int

  DDPF_RGB: int

  DDSCAPS2_CUBEMAP: int

  DDSCAPS2_CUBEMAP_NEGATIVEX: int

  DDSCAPS2_CUBEMAP_NEGATIVEY: int

  DDSCAPS2_CUBEMAP_NEGATIVEZ: int

  DDSCAPS2_CUBEMAP_POSITIVEY: int

  DDSCAPS2_CUBEMAP_POSITIVEZ: int

  DDSCAPS2_CUBEMAP_POSITVEX: int

  DDSCAPS2_VOLUME: int

  DDSCAPS_COMPLEX: int

  DDSCAPS_MIPMAP: int

  DDSCAPS_TEXTURE: int

  DDSD_CAPS: int

  DDSD_DEPTH: int

  DDSD_HEIGHT: int

  DDSD_LINEARSIZE: int

  DDSD_MIPMAPCOUNT: int

  DDSD_PITCH: int

  DDSD_PIXELFORMAT: int

  DDSD_WIDTH: int

  def getFourCCString(self) -> str: ...

  def setBBitMask(self, arg0: int) -> None: ...

  def setFlags(self, arg0: int) -> None: ...

  def setFourCC(self, arg0: int) -> None: ...

  def setGBitMask(self, arg0: int) -> None: ...

  def setRBitMask(self, arg0: int) -> None: ...

  def setRGBAlphaBitMask(self, arg0: int) -> None: ...

  def setRGBBitCount(self, arg0: int) -> None: ...

  def setSize(self, arg0: int) -> None: ...

  def __init__(self): ...


class DDSCaps2:

  DDPF_APHAPIXES: int

  DDPF_FOURCC: int

  DDPF_RGB: int

  DDSCAPS2_CUBEMAP: int

  DDSCAPS2_CUBEMAP_NEGATIVEX: int

  DDSCAPS2_CUBEMAP_NEGATIVEY: int

  DDSCAPS2_CUBEMAP_NEGATIVEZ: int

  DDSCAPS2_CUBEMAP_POSITIVEY: int

  DDSCAPS2_CUBEMAP_POSITIVEZ: int

  DDSCAPS2_CUBEMAP_POSITVEX: int

  DDSCAPS2_VOLUME: int

  DDSCAPS_COMPLEX: int

  DDSCAPS_MIPMAP: int

  DDSCAPS_TEXTURE: int

  DDSD_CAPS: int

  DDSD_DEPTH: int

  DDSD_HEIGHT: int

  DDSD_LINEARSIZE: int

  DDSD_MIPMAPCOUNT: int

  DDSD_PITCH: int

  DDSD_PIXELFORMAT: int

  DDSD_WIDTH: int

  def setCaps1(self, arg0: int) -> None: ...

  def setCaps2(self, arg0: int) -> None: ...

  def __init__(self): ...


class DDSLoader:

  DDPF_APHAPIXES: int

  DDPF_FOURCC: int

  DDPF_RGB: int

  DDSCAPS2_CUBEMAP: int

  DDSCAPS2_CUBEMAP_NEGATIVEX: int

  DDSCAPS2_CUBEMAP_NEGATIVEY: int

  DDSCAPS2_CUBEMAP_NEGATIVEZ: int

  DDSCAPS2_CUBEMAP_POSITIVEY: int

  DDSCAPS2_CUBEMAP_POSITIVEZ: int

  DDSCAPS2_CUBEMAP_POSITVEX: int

  DDSCAPS2_VOLUME: int

  DDSCAPS_COMPLEX: int

  DDSCAPS_MIPMAP: int

  DDSCAPS_TEXTURE: int

  DDSD_CAPS: int

  DDSD_DEPTH: int

  DDSD_HEIGHT: int

  DDSD_LINEARSIZE: int

  DDSD_MIPMAPCOUNT: int

  DDSD_PITCH: int

  DDSD_PIXELFORMAT: int

  DDSD_WIDTH: int

  lastHei: int

  lastWid: int

  def debugInfo(self) -> None: ...

  @overload
  def loadDDSFile(self, arg0: BufferedInputStream) -> int: ...

  @overload
  def loadDDSFile(self, arg0: str) -> int: ...

  def __init__(self): ...


class DDSurface:

  DDPF_APHAPIXES: int

  DDPF_FOURCC: int

  DDPF_RGB: int

  DDSCAPS2_CUBEMAP: int

  DDSCAPS2_CUBEMAP_NEGATIVEX: int

  DDSCAPS2_CUBEMAP_NEGATIVEY: int

  DDSCAPS2_CUBEMAP_NEGATIVEZ: int

  DDSCAPS2_CUBEMAP_POSITIVEY: int

  DDSCAPS2_CUBEMAP_POSITIVEZ: int

  DDSCAPS2_CUBEMAP_POSITVEX: int

  DDSCAPS2_VOLUME: int

  DDSCAPS_COMPLEX: int

  DDSCAPS_MIPMAP: int

  DDSCAPS_TEXTURE: int

  DDSD_CAPS: int

  DDSD_DEPTH: int

  DDSD_HEIGHT: int

  DDSD_LINEARSIZE: int

  DDSD_MIPMAPCOUNT: int

  DDSD_PITCH: int

  DDSD_PIXELFORMAT: int

  DDSD_WIDTH: int


class DDSurfaceDesc2:

  DDPF_APHAPIXES: int

  DDPF_FOURCC: int

  DDPF_RGB: int

  DDSCAPS2_CUBEMAP: int

  DDSCAPS2_CUBEMAP_NEGATIVEX: int

  DDSCAPS2_CUBEMAP_NEGATIVEY: int

  DDSCAPS2_CUBEMAP_NEGATIVEZ: int

  DDSCAPS2_CUBEMAP_POSITIVEY: int

  DDSCAPS2_CUBEMAP_POSITIVEZ: int

  DDSCAPS2_CUBEMAP_POSITVEX: int

  DDSCAPS2_VOLUME: int

  DDSCAPS_COMPLEX: int

  DDSCAPS_MIPMAP: int

  DDSCAPS_TEXTURE: int

  DDSD_CAPS: int

  DDSD_DEPTH: int

  DDSD_HEIGHT: int

  DDSD_LINEARSIZE: int

  DDSD_MIPMAPCOUNT: int

  DDSD_PITCH: int

  DDSD_PIXELFORMAT: int

  DDSD_WIDTH: int

  def getDDPixelformat(self) -> DDPixelFormat: ...

  def getDDSCaps2(self) -> DDSCaps2: ...

  def setDDPixelFormat(self, arg0: DDPixelFormat) -> None: ...

  def setDDSCaps2(self, arg0: DDSCaps2) -> None: ...

  def setDepth(self, arg0: int) -> None: ...

  def setFlags(self, arg0: int) -> None: ...

  def setHeight(self, arg0: int) -> None: ...

  def setIdentifier(self, arg0: int) -> None: ...

  def setMipMapCount(self, arg0: int) -> None: ...

  def setPitchOrLinearSize(self, arg0: int) -> None: ...

  def setSize(self, arg0: int) -> None: ...

  def setWidth(self, arg0: int) -> None: ...

  def __init__(self): ...


class TextureFormatException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


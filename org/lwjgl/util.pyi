from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer

class ReadableColor:

  BLACK: ReadableColor

  BLUE: ReadableColor

  CYAN: ReadableColor

  DKGREY: ReadableColor

  GREEN: ReadableColor

  GREY: ReadableColor

  LTGREY: ReadableColor

  ORANGE: ReadableColor

  PURPLE: ReadableColor

  RED: ReadableColor

  WHITE: ReadableColor

  YELLOW: ReadableColor

  def getAlpha(self) -> int: ...

  def getAlphaByte(self) -> int: ...

  def getBlue(self) -> int: ...

  def getBlueByte(self) -> int: ...

  def getGreen(self) -> int: ...

  def getGreenByte(self) -> int: ...

  def getRed(self) -> int: ...

  def getRedByte(self) -> int: ...

  def writeABGR(self, arg0: ByteBuffer) -> None: ...

  def writeARGB(self, arg0: ByteBuffer) -> None: ...

  def writeBGR(self, arg0: ByteBuffer) -> None: ...

  def writeBGRA(self, arg0: ByteBuffer) -> None: ...

  def writeRGB(self, arg0: ByteBuffer) -> None: ...

  def writeRGBA(self, arg0: ByteBuffer) -> None: ...


class ReadableDimension:

  def getHeight(self) -> int: ...

  def getSize(self, arg0: WritableDimension) -> None: ...

  def getWidth(self) -> int: ...


class ReadablePoint:

  def getLocation(self, arg0: WritablePoint) -> None: ...

  def getX(self) -> int: ...

  def getY(self) -> int: ...


class ReadableRectangle:

  def getBounds(self, arg0: WritableRectangle) -> None: ...

  def getHeight(self) -> int: ...

  def getLocation(self, arg0: WritablePoint) -> None: ...

  def getSize(self, arg0: WritableDimension) -> None: ...

  def getWidth(self) -> int: ...

  def getX(self) -> int: ...

  def getY(self) -> int: ...


class Rectangle:

  @overload
  def add(self, arg0: ReadablePoint) -> None: ...

  @overload
  def add(self, arg0: ReadableRectangle) -> None: ...

  @overload
  def add(self, arg0: int, arg1: int) -> None: ...

  @overload
  def contains(self, arg0: ReadablePoint) -> bool: ...

  @overload
  def contains(self, arg0: ReadableRectangle) -> bool: ...

  @overload
  def contains(self, arg0: int, arg1: int) -> bool: ...

  @overload
  def contains(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def getBounds(self, arg0: WritableRectangle) -> None: ...

  @overload
  def getBounds(self, arg0: WritableRectangle) -> None: ...

  def getHeight(self) -> int: ...

  def getLocation(self, arg0: WritablePoint) -> None: ...

  def getSize(self, arg0: WritableDimension) -> None: ...

  def getWidth(self) -> int: ...

  def getX(self) -> int: ...

  def getY(self) -> int: ...

  def grow(self, arg0: int, arg1: int) -> None: ...

  def intersection(self, arg0: ReadableRectangle, arg1: Rectangle) -> Rectangle: ...

  def intersects(self, arg0: ReadableRectangle) -> bool: ...

  def isEmpty(self) -> bool: ...

  @overload
  def setBounds(self, arg0: ReadableRectangle) -> None: ...

  @overload
  def setBounds(self, arg0: ReadableRectangle) -> None: ...

  @overload
  def setBounds(self, arg0: ReadablePoint, arg1: ReadableDimension) -> None: ...

  @overload
  def setBounds(self, arg0: ReadablePoint, arg1: ReadableDimension) -> None: ...

  @overload
  def setBounds(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  @overload
  def setBounds(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def setHeight(self, arg0: int) -> None: ...

  @overload
  def setLocation(self, arg0: ReadablePoint) -> None: ...

  @overload
  def setLocation(self, arg0: int, arg1: int) -> None: ...

  @overload
  def setSize(self, arg0: ReadableDimension) -> None: ...

  @overload
  def setSize(self, arg0: int, arg1: int) -> None: ...

  def setWidth(self, arg0: int) -> None: ...

  def setX(self, arg0: int) -> None: ...

  def setY(self, arg0: int) -> None: ...

  def toString(self) -> str: ...

  @overload
  def translate(self, arg0: ReadablePoint) -> None: ...

  @overload
  def translate(self, arg0: int, arg1: int) -> None: ...

  def union(self, arg0: ReadableRectangle, arg1: WritableRectangle) -> WritableRectangle: ...

  def untranslate(self, arg0: ReadablePoint) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: ReadableRectangle): ...
  @overload
  def __init__(self, arg0: ReadablePoint, arg1: ReadableDimension): ...
  @overload
  def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int): ...


class WritableDimension:

  def setHeight(self, arg0: int) -> None: ...

  @overload
  def setSize(self, arg0: ReadableDimension) -> None: ...

  @overload
  def setSize(self, arg0: int, arg1: int) -> None: ...

  def setWidth(self, arg0: int) -> None: ...


class WritablePoint:

  @overload
  def setLocation(self, arg0: ReadablePoint) -> None: ...

  @overload
  def setLocation(self, arg0: int, arg1: int) -> None: ...

  def setX(self, arg0: int) -> None: ...

  def setY(self, arg0: int) -> None: ...


class WritableRectangle:

  @overload
  def setBounds(self, arg0: ReadableRectangle) -> None: ...

  @overload
  def setBounds(self, arg0: ReadablePoint, arg1: ReadableDimension) -> None: ...

  @overload
  def setBounds(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def setHeight(self, arg0: int) -> None: ...

  @overload
  def setLocation(self, arg0: ReadablePoint) -> None: ...

  @overload
  def setLocation(self, arg0: int, arg1: int) -> None: ...

  @overload
  def setSize(self, arg0: ReadableDimension) -> None: ...

  @overload
  def setSize(self, arg0: int, arg1: int) -> None: ...

  def setWidth(self, arg0: int) -> None: ...

  def setX(self, arg0: int) -> None: ...

  def setY(self, arg0: int) -> None: ...

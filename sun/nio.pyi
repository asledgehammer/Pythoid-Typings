from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer

class ByteBuffered:

  def getByteBuffer(self) -> ByteBuffer: ...


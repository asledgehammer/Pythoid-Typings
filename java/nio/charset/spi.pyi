from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio.charset import Charset
from java.util import Iterator

class CharsetProvider:

  def charsetForName(self, arg0: str) -> Charset: ...

  def charsets(self) -> Iterator[Charset]: ...


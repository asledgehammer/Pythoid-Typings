from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import IOException
from java.lang import CharSequence
from java.nio import ByteBuffer, CharBuffer
from java.util import Set, Locale, SortedMap

class CharacterCodingException(IOException):

  def __init__(self): ...


class Charset:

  def aliases(self) -> Set[str]: ...

  def canEncode(self) -> bool: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: Charset) -> int: ...

  def contains(self, arg0: Charset) -> bool: ...

  def decode(self, arg0: ByteBuffer) -> CharBuffer: ...

  @overload
  def displayName(self) -> str: ...

  @overload
  def displayName(self, arg0: Locale) -> str: ...

  @overload
  def encode(self, arg0: str) -> ByteBuffer: ...

  @overload
  def encode(self, arg0: CharBuffer) -> ByteBuffer: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def isRegistered(self) -> bool: ...

  def name(self) -> str: ...

  def newDecoder(self) -> CharsetDecoder: ...

  def newEncoder(self) -> CharsetEncoder: ...

  def toString(self) -> str: ...

  @staticmethod
  def availableCharsets() -> SortedMap[str, Charset]: ...

  @staticmethod
  def defaultCharset() -> Charset: ...

  @staticmethod
  @overload
  def forName(arg0: str) -> Charset: ...

  @staticmethod
  @overload
  def forName(arg0: str, arg1: Charset) -> Charset: ...

  @staticmethod
  def isSupported(arg0: str) -> bool: ...

  class ExtendedProviderHolder: ...


class CharsetDecoder:

  def averageCharsPerByte(self) -> float: ...

  def charset(self) -> Charset: ...

  @overload
  def decode(self, arg0: ByteBuffer) -> CharBuffer: ...

  @overload
  def decode(self, arg0: ByteBuffer, arg1: CharBuffer, arg2: bool) -> CoderResult: ...

  def detectedCharset(self) -> Charset: ...

  def flush(self, arg0: CharBuffer) -> CoderResult: ...

  def isAutoDetecting(self) -> bool: ...

  def isCharsetDetected(self) -> bool: ...

  def malformedInputAction(self) -> CodingErrorAction: ...

  def maxCharsPerByte(self) -> float: ...

  def onMalformedInput(self, arg0: CodingErrorAction) -> CharsetDecoder: ...

  def onUnmappableCharacter(self, arg0: CodingErrorAction) -> CharsetDecoder: ...

  def replaceWith(self, arg0: str) -> CharsetDecoder: ...

  def replacement(self) -> str: ...

  def reset(self) -> CharsetDecoder: ...

  def unmappableCharacterAction(self) -> CodingErrorAction: ...


class CharsetEncoder:

  def averageBytesPerChar(self) -> float: ...

  @overload
  def canEncode(self, arg0: str) -> bool: ...

  @overload
  def canEncode(self, arg0: CharSequence) -> bool: ...

  def charset(self) -> Charset: ...

  @overload
  def encode(self, arg0: CharBuffer) -> ByteBuffer: ...

  @overload
  def encode(self, arg0: CharBuffer, arg1: ByteBuffer, arg2: bool) -> CoderResult: ...

  def flush(self, arg0: ByteBuffer) -> CoderResult: ...

  def isLegalReplacement(self, arg0: list[int]) -> bool: ...

  def malformedInputAction(self) -> CodingErrorAction: ...

  def maxBytesPerChar(self) -> float: ...

  def onMalformedInput(self, arg0: CodingErrorAction) -> CharsetEncoder: ...

  def onUnmappableCharacter(self, arg0: CodingErrorAction) -> CharsetEncoder: ...

  def replaceWith(self, arg0: list[int]) -> CharsetEncoder: ...

  def replacement(self) -> list[int]: ...

  def reset(self) -> CharsetEncoder: ...

  def unmappableCharacterAction(self) -> CodingErrorAction: ...


class CoderResult:

  OVERFLOW: CoderResult

  UNDERFLOW: CoderResult

  def isError(self) -> bool: ...

  def isMalformed(self) -> bool: ...

  def isOverflow(self) -> bool: ...

  def isUnderflow(self) -> bool: ...

  def isUnmappable(self) -> bool: ...

  def length(self) -> int: ...

  def throwException(self) -> None: ...

  def toString(self) -> str: ...

  @staticmethod
  def malformedForLength(arg0: int) -> CoderResult: ...

  @staticmethod
  def unmappableForLength(arg0: int) -> CoderResult: ...

  class Cache: ...


class CodingErrorAction:

  IGNORE: CodingErrorAction

  REPLACE: CodingErrorAction

  REPORT: CodingErrorAction

  def toString(self) -> str: ...


class StandardCharsets:

  ISO_8859_1: Charset

  US_ASCII: Charset

  UTF_16: Charset

  UTF_16BE: Charset

  UTF_16LE: Charset

  UTF_8: Charset


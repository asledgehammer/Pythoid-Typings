from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import InputStream, BufferedReader, OutputStream, BufferedWriter, FileInputStream, File, FileDescriptor, PrintStream, Console, PrintWriter
from java.lang.annotation import Annotation
from java.lang.constant import DynamicConstantDesc, ClassDesc
from java.lang.invoke import TypeDescriptor, MethodHandles, MethodType
from java.lang.module import ModuleDescriptor, Configuration
from java.lang.ref import WeakReference, ReferenceQueue
from java.lang.reflect import AnnotatedType, Constructor, Field, Method, Type, RecordComponent, TypeVariable
from java.net import URL, InetAddress
from java.nio import CharBuffer
from java.nio.channels import Channel
from java.nio.charset import Charset
from java.security import ProtectionDomain, BasicPermission, Permission
from java.time import Instant, Duration
from java.util import Optional, Enumeration, WeakHashMap, Iterator, Spliterator, Set, List, Comparator, Locale, ResourceBundle, Properties, Map, Collection
from java.util.concurrent import CompletableFuture, TimeUnit
from java.util.function import Consumer, Function, ToDoubleFunction, ToIntFunction, ToLongFunction, IntConsumer, Supplier, BiFunction
from java.util.stream import IntStream, Stream

T = TypeVar('T', default=Any)
U = TypeVar('U', default=Any)
A = TypeVar('A', default=Any)
ReflectionData_T = TypeVar('ReflectionData_T', default=Any)
Version_T = TypeVar('Version_T', default=Any)
Entry_T = TypeVar('Entry_T', default=Any)
E = TypeVar('E', default=Any)
EnumDesc_E = TypeVar('EnumDesc_E', default=Any)
R = TypeVar('R', default=Any)
F = TypeVar('F', default=Any)
S = TypeVar('S', default=Any)
SuppliedThreadLocal_T = TypeVar('SuppliedThreadLocal_T', default=Any)
K1 = TypeVar('K1', default=Any)
K2 = TypeVar('K2', default=Any)
V = TypeVar('V', default=Any)
Pair_K1 = TypeVar('Pair_K1', default=Any)
Pair_K2 = TypeVar('Pair_K2', default=Any)
Weak_K1 = TypeVar('Weak_K1', default=Any)
Weak_K2 = TypeVar('Weak_K2', default=Any)
Lookup_K1 = TypeVar('Lookup_K1', default=Any)
Lookup_K2 = TypeVar('Lookup_K2', default=Any)
K = TypeVar('K', default=Any)

class AbstractStringBuilder:

  @overload
  def append(self, arg0: list[str]) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: bool) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: str) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: str) -> Appendable: ...

  @overload
  def append(self, arg0: str) -> Appendable: ...

  @overload
  def append(self, arg0: float) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: float) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence) -> Appendable: ...

  @overload
  def append(self, arg0: CharSequence) -> Appendable: ...

  @overload
  def append(self, arg0: object) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: str) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: StringBuffer) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: list[str], arg1: int, arg2: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> Appendable: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> Appendable: ...

  def appendCodePoint(self, arg0: int) -> AbstractStringBuilder: ...

  def capacity(self) -> int: ...

  @overload
  def charAt(self, arg0: int) -> str: ...

  @overload
  def charAt(self, arg0: int) -> str: ...

  @overload
  def chars(self) -> IntStream: ...

  @overload
  def chars(self) -> IntStream: ...

  def codePointAt(self, arg0: int) -> int: ...

  def codePointBefore(self, arg0: int) -> int: ...

  def codePointCount(self, arg0: int, arg1: int) -> int: ...

  @overload
  def codePoints(self) -> IntStream: ...

  @overload
  def codePoints(self) -> IntStream: ...

  def delete(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  def deleteCharAt(self, arg0: int) -> AbstractStringBuilder: ...

  def ensureCapacity(self, arg0: int) -> None: ...

  def getChars(self, arg0: int, arg1: int, arg2: list[str], arg3: int) -> None: ...

  @overload
  def indexOf(self, arg0: str) -> int: ...

  @overload
  def indexOf(self, arg0: str, arg1: int) -> int: ...

  @overload
  def insert(self, arg0: int, arg1: list[str]) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: bool) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: object) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: list[str], arg2: int, arg3: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence, arg2: int, arg3: int) -> AbstractStringBuilder: ...

  def isEmpty(self) -> bool: ...

  @overload
  def lastIndexOf(self, arg0: str) -> int: ...

  @overload
  def lastIndexOf(self, arg0: str, arg1: int) -> int: ...

  @overload
  def length(self) -> int: ...

  @overload
  def length(self) -> int: ...

  def offsetByCodePoints(self, arg0: int, arg1: int) -> int: ...

  def replace(self, arg0: int, arg1: int, arg2: str) -> AbstractStringBuilder: ...

  def reverse(self) -> AbstractStringBuilder: ...

  def setCharAt(self, arg0: int, arg1: str) -> None: ...

  def setLength(self, arg0: int) -> None: ...

  @overload
  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  @overload
  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  @overload
  def substring(self, arg0: int) -> str: ...

  @overload
  def substring(self, arg0: int, arg1: int) -> str: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toString(self) -> str: ...

  def trimToSize(self) -> None: ...

  @staticmethod
  def compare(arg0: CharSequence, arg1: CharSequence) -> int: ...


class Appendable:

  @overload
  def append(self, arg0: str) -> Appendable: ...

  @overload
  def append(self, arg0: CharSequence) -> Appendable: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> Appendable: ...


class ArithmeticException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class ArrayIndexOutOfBoundsException(IndexOutOfBoundsException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: str): ...


class ArrayStoreException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class AssertionError(Error):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: bool): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: float): ...
  @overload
  def __init__(self, arg0: float): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: object): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class AssertionStatusDirectives: ...


class AutoCloseable:

  def close(self) -> None: ...


class Boolean:

  FALSE: Boolean

  TRUE: Boolean

  TYPE: Class[Boolean]

  def booleanValue(self) -> bool: ...

  @overload
  def compareTo(self, arg0: Boolean) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def describeConstable(self) -> Optional[DynamicConstantDesc[Boolean]]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def compare(arg0: bool, arg1: bool) -> int: ...

  @staticmethod
  def getBoolean(arg0: str) -> bool: ...

  @staticmethod
  def logicalAnd(arg0: bool, arg1: bool) -> bool: ...

  @staticmethod
  def logicalOr(arg0: bool, arg1: bool) -> bool: ...

  @staticmethod
  def logicalXor(arg0: bool, arg1: bool) -> bool: ...

  @staticmethod
  def parseBoolean(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def valueOf(arg0: bool) -> Boolean: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> Boolean: ...

  @overload
  def __init__(self, arg0: bool): ...
  @overload
  def __init__(self, arg0: str): ...


class BootstrapMethodError(LinkageError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class Byte(Number):

  BYTES: int

  MAX_VALUE: int

  MIN_VALUE: int

  SIZE: int

  TYPE: Class[Byte]

  def byteValue(self) -> int: ...

  @overload
  def compareTo(self, arg0: Byte) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def describeConstable(self) -> Optional[DynamicConstantDesc[Byte]]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def doubleValue(self) -> float: ...

  def equals(self, arg0: object) -> bool: ...

  def floatValue(self) -> float: ...

  def hashCode(self) -> int: ...

  def intValue(self) -> int: ...

  def longValue(self) -> int: ...

  def shortValue(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def compare(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def compareUnsigned(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def decode(arg0: str) -> Byte: ...

  @staticmethod
  @overload
  def parseByte(arg0: str) -> int: ...

  @staticmethod
  @overload
  def parseByte(arg0: str, arg1: int) -> int: ...

  @staticmethod
  def toUnsignedInt(arg0: int) -> int: ...

  @staticmethod
  def toUnsignedLong(arg0: int) -> int: ...

  @staticmethod
  @overload
  def valueOf(arg0: int) -> Byte: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> Byte: ...

  @staticmethod
  @overload
  def valueOf(arg0: str, arg1: int) -> Byte: ...

  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: str): ...

  class ByteCache: ...


class CharSequence:

  def charAt(self, arg0: int) -> str: ...

  def chars(self) -> IntStream: ...

  def codePoints(self) -> IntStream: ...

  def isEmpty(self) -> bool: ...

  def length(self) -> int: ...

  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  def toString(self) -> str: ...

  @staticmethod
  def compare(arg0: CharSequence, arg1: CharSequence) -> int: ...


class Character:

  BYTES: int

  COMBINING_SPACING_MARK: int

  CONNECTOR_PUNCTUATION: int

  CONTROL: int

  CURRENCY_SYMBOL: int

  DASH_PUNCTUATION: int

  DECIMAL_DIGIT_NUMBER: int

  DIRECTIONALITY_ARABIC_NUMBER: int

  DIRECTIONALITY_BOUNDARY_NEUTRAL: int

  DIRECTIONALITY_COMMON_NUMBER_SEPARATOR: int

  DIRECTIONALITY_EUROPEAN_NUMBER: int

  DIRECTIONALITY_EUROPEAN_NUMBER_SEPARATOR: int

  DIRECTIONALITY_EUROPEAN_NUMBER_TERMINATOR: int

  DIRECTIONALITY_FIRST_STRONG_ISOLATE: int

  DIRECTIONALITY_LEFT_TO_RIGHT: int

  DIRECTIONALITY_LEFT_TO_RIGHT_EMBEDDING: int

  DIRECTIONALITY_LEFT_TO_RIGHT_ISOLATE: int

  DIRECTIONALITY_LEFT_TO_RIGHT_OVERRIDE: int

  DIRECTIONALITY_NONSPACING_MARK: int

  DIRECTIONALITY_OTHER_NEUTRALS: int

  DIRECTIONALITY_PARAGRAPH_SEPARATOR: int

  DIRECTIONALITY_POP_DIRECTIONAL_FORMAT: int

  DIRECTIONALITY_POP_DIRECTIONAL_ISOLATE: int

  DIRECTIONALITY_RIGHT_TO_LEFT: int

  DIRECTIONALITY_RIGHT_TO_LEFT_ARABIC: int

  DIRECTIONALITY_RIGHT_TO_LEFT_EMBEDDING: int

  DIRECTIONALITY_RIGHT_TO_LEFT_ISOLATE: int

  DIRECTIONALITY_RIGHT_TO_LEFT_OVERRIDE: int

  DIRECTIONALITY_SEGMENT_SEPARATOR: int

  DIRECTIONALITY_UNDEFINED: int

  DIRECTIONALITY_WHITESPACE: int

  ENCLOSING_MARK: int

  END_PUNCTUATION: int

  FINAL_QUOTE_PUNCTUATION: int

  FORMAT: int

  INITIAL_QUOTE_PUNCTUATION: int

  LETTER_NUMBER: int

  LINE_SEPARATOR: int

  LOWERCASE_LETTER: int

  MATH_SYMBOL: int

  MAX_CODE_POINT: int

  MAX_HIGH_SURROGATE: str

  MAX_LOW_SURROGATE: str

  MAX_RADIX: int

  MAX_SURROGATE: str

  MAX_VALUE: str

  MIN_CODE_POINT: int

  MIN_HIGH_SURROGATE: str

  MIN_LOW_SURROGATE: str

  MIN_RADIX: int

  MIN_SUPPLEMENTARY_CODE_POINT: int

  MIN_SURROGATE: str

  MIN_VALUE: str

  MODIFIER_LETTER: int

  MODIFIER_SYMBOL: int

  NON_SPACING_MARK: int

  OTHER_LETTER: int

  OTHER_NUMBER: int

  OTHER_PUNCTUATION: int

  OTHER_SYMBOL: int

  PARAGRAPH_SEPARATOR: int

  PRIVATE_USE: int

  SIZE: int

  SPACE_SEPARATOR: int

  START_PUNCTUATION: int

  SURROGATE: int

  TITLECASE_LETTER: int

  TYPE: Class[str]

  UNASSIGNED: int

  UPPERCASE_LETTER: int

  def charValue(self) -> str: ...

  @overload
  def compareTo(self, arg0: str) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def describeConstable(self) -> Optional[DynamicConstantDesc[str]]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def charCount(arg0: int) -> int: ...

  @staticmethod
  @overload
  def codePointAt(arg0: list[str], arg1: int) -> int: ...

  @staticmethod
  @overload
  def codePointAt(arg0: CharSequence, arg1: int) -> int: ...

  @staticmethod
  @overload
  def codePointAt(arg0: list[str], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def codePointBefore(arg0: list[str], arg1: int) -> int: ...

  @staticmethod
  @overload
  def codePointBefore(arg0: CharSequence, arg1: int) -> int: ...

  @staticmethod
  @overload
  def codePointBefore(arg0: list[str], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def codePointCount(arg0: list[str], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def codePointCount(arg0: CharSequence, arg1: int, arg2: int) -> int: ...

  @staticmethod
  def codePointOf(arg0: str) -> int: ...

  @staticmethod
  def compare(arg0: str, arg1: str) -> int: ...

  @staticmethod
  @overload
  def digit(arg0: str, arg1: int) -> int: ...

  @staticmethod
  @overload
  def digit(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def forDigit(arg0: int, arg1: int) -> str: ...

  @staticmethod
  @overload
  def getDirectionality(arg0: str) -> int: ...

  @staticmethod
  @overload
  def getDirectionality(arg0: int) -> int: ...

  @staticmethod
  def getName(arg0: int) -> str: ...

  @staticmethod
  @overload
  def getNumericValue(arg0: str) -> int: ...

  @staticmethod
  @overload
  def getNumericValue(arg0: int) -> int: ...

  @staticmethod
  @overload
  def getType(arg0: str) -> int: ...

  @staticmethod
  @overload
  def getType(arg0: int) -> int: ...

  @staticmethod
  def highSurrogate(arg0: int) -> str: ...

  @staticmethod
  def isAlphabetic(arg0: int) -> bool: ...

  @staticmethod
  def isBmpCodePoint(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isDefined(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isDefined(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isDigit(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isDigit(arg0: int) -> bool: ...

  @staticmethod
  def isHighSurrogate(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isISOControl(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isISOControl(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isIdentifierIgnorable(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isIdentifierIgnorable(arg0: int) -> bool: ...

  @staticmethod
  def isIdeographic(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isJavaIdentifierPart(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isJavaIdentifierPart(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isJavaIdentifierStart(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isJavaIdentifierStart(arg0: int) -> bool: ...

  @staticmethod
  def isJavaLetter(arg0: str) -> bool: ...

  @staticmethod
  def isJavaLetterOrDigit(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isLetter(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isLetter(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isLetterOrDigit(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isLetterOrDigit(arg0: int) -> bool: ...

  @staticmethod
  def isLowSurrogate(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isLowerCase(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isLowerCase(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isMirrored(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isMirrored(arg0: int) -> bool: ...

  @staticmethod
  def isSpace(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isSpaceChar(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isSpaceChar(arg0: int) -> bool: ...

  @staticmethod
  def isSupplementaryCodePoint(arg0: int) -> bool: ...

  @staticmethod
  def isSurrogate(arg0: str) -> bool: ...

  @staticmethod
  def isSurrogatePair(arg0: str, arg1: str) -> bool: ...

  @staticmethod
  @overload
  def isTitleCase(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isTitleCase(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isUnicodeIdentifierPart(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isUnicodeIdentifierPart(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isUnicodeIdentifierStart(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isUnicodeIdentifierStart(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isUpperCase(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isUpperCase(arg0: int) -> bool: ...

  @staticmethod
  def isValidCodePoint(arg0: int) -> bool: ...

  @staticmethod
  @overload
  def isWhitespace(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def isWhitespace(arg0: int) -> bool: ...

  @staticmethod
  def lowSurrogate(arg0: int) -> str: ...

  @staticmethod
  @overload
  def offsetByCodePoints(arg0: CharSequence, arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def offsetByCodePoints(arg0: list[str], arg1: int, arg2: int, arg3: int, arg4: int) -> int: ...

  @staticmethod
  def reverseBytes(arg0: str) -> str: ...

  @staticmethod
  @overload
  def toChars(arg0: int) -> list[str]: ...

  @staticmethod
  @overload
  def toChars(arg0: int, arg1: list[str], arg2: int) -> int: ...

  @staticmethod
  def toCodePoint(arg0: str, arg1: str) -> int: ...

  @staticmethod
  @overload
  def toLowerCase(arg0: str) -> str: ...

  @staticmethod
  @overload
  def toLowerCase(arg0: int) -> int: ...

  @staticmethod
  @overload
  def toTitleCase(arg0: str) -> str: ...

  @staticmethod
  @overload
  def toTitleCase(arg0: int) -> int: ...

  @staticmethod
  @overload
  def toUpperCase(arg0: str) -> str: ...

  @staticmethod
  @overload
  def toUpperCase(arg0: int) -> int: ...

  @staticmethod
  def valueOf(arg0: str) -> str: ...

  def __init__(self, arg0: str): ...

  class CharacterCache: ...

  class UnicodeBlock(Character.Subset):

    ADLAM: Character.UnicodeBlock

    AEGEAN_NUMBERS: Character.UnicodeBlock

    AHOM: Character.UnicodeBlock

    ALCHEMICAL_SYMBOLS: Character.UnicodeBlock

    ALPHABETIC_PRESENTATION_FORMS: Character.UnicodeBlock

    ANATOLIAN_HIEROGLYPHS: Character.UnicodeBlock

    ANCIENT_GREEK_MUSICAL_NOTATION: Character.UnicodeBlock

    ANCIENT_GREEK_NUMBERS: Character.UnicodeBlock

    ANCIENT_SYMBOLS: Character.UnicodeBlock

    ARABIC: Character.UnicodeBlock

    ARABIC_EXTENDED_A: Character.UnicodeBlock

    ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS: Character.UnicodeBlock

    ARABIC_PRESENTATION_FORMS_A: Character.UnicodeBlock

    ARABIC_PRESENTATION_FORMS_B: Character.UnicodeBlock

    ARABIC_SUPPLEMENT: Character.UnicodeBlock

    ARMENIAN: Character.UnicodeBlock

    ARROWS: Character.UnicodeBlock

    AVESTAN: Character.UnicodeBlock

    BALINESE: Character.UnicodeBlock

    BAMUM: Character.UnicodeBlock

    BAMUM_SUPPLEMENT: Character.UnicodeBlock

    BASIC_LATIN: Character.UnicodeBlock

    BASSA_VAH: Character.UnicodeBlock

    BATAK: Character.UnicodeBlock

    BENGALI: Character.UnicodeBlock

    BHAIKSUKI: Character.UnicodeBlock

    BLOCK_ELEMENTS: Character.UnicodeBlock

    BOPOMOFO: Character.UnicodeBlock

    BOPOMOFO_EXTENDED: Character.UnicodeBlock

    BOX_DRAWING: Character.UnicodeBlock

    BRAHMI: Character.UnicodeBlock

    BRAILLE_PATTERNS: Character.UnicodeBlock

    BUGINESE: Character.UnicodeBlock

    BUHID: Character.UnicodeBlock

    BYZANTINE_MUSICAL_SYMBOLS: Character.UnicodeBlock

    CARIAN: Character.UnicodeBlock

    CAUCASIAN_ALBANIAN: Character.UnicodeBlock

    CHAKMA: Character.UnicodeBlock

    CHAM: Character.UnicodeBlock

    CHEROKEE: Character.UnicodeBlock

    CHEROKEE_SUPPLEMENT: Character.UnicodeBlock

    CHESS_SYMBOLS: Character.UnicodeBlock

    CHORASMIAN: Character.UnicodeBlock

    CJK_COMPATIBILITY: Character.UnicodeBlock

    CJK_COMPATIBILITY_FORMS: Character.UnicodeBlock

    CJK_COMPATIBILITY_IDEOGRAPHS: Character.UnicodeBlock

    CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT: Character.UnicodeBlock

    CJK_RADICALS_SUPPLEMENT: Character.UnicodeBlock

    CJK_STROKES: Character.UnicodeBlock

    CJK_SYMBOLS_AND_PUNCTUATION: Character.UnicodeBlock

    CJK_UNIFIED_IDEOGRAPHS: Character.UnicodeBlock

    CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A: Character.UnicodeBlock

    CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B: Character.UnicodeBlock

    CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C: Character.UnicodeBlock

    CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D: Character.UnicodeBlock

    CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E: Character.UnicodeBlock

    CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F: Character.UnicodeBlock

    CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G: Character.UnicodeBlock

    COMBINING_DIACRITICAL_MARKS: Character.UnicodeBlock

    COMBINING_DIACRITICAL_MARKS_EXTENDED: Character.UnicodeBlock

    COMBINING_DIACRITICAL_MARKS_SUPPLEMENT: Character.UnicodeBlock

    COMBINING_HALF_MARKS: Character.UnicodeBlock

    COMBINING_MARKS_FOR_SYMBOLS: Character.UnicodeBlock

    COMMON_INDIC_NUMBER_FORMS: Character.UnicodeBlock

    CONTROL_PICTURES: Character.UnicodeBlock

    COPTIC: Character.UnicodeBlock

    COPTIC_EPACT_NUMBERS: Character.UnicodeBlock

    COUNTING_ROD_NUMERALS: Character.UnicodeBlock

    CUNEIFORM: Character.UnicodeBlock

    CUNEIFORM_NUMBERS_AND_PUNCTUATION: Character.UnicodeBlock

    CURRENCY_SYMBOLS: Character.UnicodeBlock

    CYPRIOT_SYLLABARY: Character.UnicodeBlock

    CYRILLIC: Character.UnicodeBlock

    CYRILLIC_EXTENDED_A: Character.UnicodeBlock

    CYRILLIC_EXTENDED_B: Character.UnicodeBlock

    CYRILLIC_EXTENDED_C: Character.UnicodeBlock

    CYRILLIC_SUPPLEMENTARY: Character.UnicodeBlock

    DESERET: Character.UnicodeBlock

    DEVANAGARI: Character.UnicodeBlock

    DEVANAGARI_EXTENDED: Character.UnicodeBlock

    DINGBATS: Character.UnicodeBlock

    DIVES_AKURU: Character.UnicodeBlock

    DOGRA: Character.UnicodeBlock

    DOMINO_TILES: Character.UnicodeBlock

    DUPLOYAN: Character.UnicodeBlock

    EARLY_DYNASTIC_CUNEIFORM: Character.UnicodeBlock

    EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS: Character.UnicodeBlock

    EGYPTIAN_HIEROGLYPHS: Character.UnicodeBlock

    ELBASAN: Character.UnicodeBlock

    ELYMAIC: Character.UnicodeBlock

    EMOTICONS: Character.UnicodeBlock

    ENCLOSED_ALPHANUMERIC_SUPPLEMENT: Character.UnicodeBlock

    ENCLOSED_ALPHANUMERICS: Character.UnicodeBlock

    ENCLOSED_CJK_LETTERS_AND_MONTHS: Character.UnicodeBlock

    ENCLOSED_IDEOGRAPHIC_SUPPLEMENT: Character.UnicodeBlock

    ETHIOPIC: Character.UnicodeBlock

    ETHIOPIC_EXTENDED: Character.UnicodeBlock

    ETHIOPIC_EXTENDED_A: Character.UnicodeBlock

    ETHIOPIC_SUPPLEMENT: Character.UnicodeBlock

    GENERAL_PUNCTUATION: Character.UnicodeBlock

    GEOMETRIC_SHAPES: Character.UnicodeBlock

    GEOMETRIC_SHAPES_EXTENDED: Character.UnicodeBlock

    GEORGIAN: Character.UnicodeBlock

    GEORGIAN_EXTENDED: Character.UnicodeBlock

    GEORGIAN_SUPPLEMENT: Character.UnicodeBlock

    GLAGOLITIC: Character.UnicodeBlock

    GLAGOLITIC_SUPPLEMENT: Character.UnicodeBlock

    GOTHIC: Character.UnicodeBlock

    GRANTHA: Character.UnicodeBlock

    GREEK: Character.UnicodeBlock

    GREEK_EXTENDED: Character.UnicodeBlock

    GUJARATI: Character.UnicodeBlock

    GUNJALA_GONDI: Character.UnicodeBlock

    GURMUKHI: Character.UnicodeBlock

    HALFWIDTH_AND_FULLWIDTH_FORMS: Character.UnicodeBlock

    HANGUL_COMPATIBILITY_JAMO: Character.UnicodeBlock

    HANGUL_JAMO: Character.UnicodeBlock

    HANGUL_JAMO_EXTENDED_A: Character.UnicodeBlock

    HANGUL_JAMO_EXTENDED_B: Character.UnicodeBlock

    HANGUL_SYLLABLES: Character.UnicodeBlock

    HANIFI_ROHINGYA: Character.UnicodeBlock

    HANUNOO: Character.UnicodeBlock

    HATRAN: Character.UnicodeBlock

    HEBREW: Character.UnicodeBlock

    HIGH_PRIVATE_USE_SURROGATES: Character.UnicodeBlock

    HIGH_SURROGATES: Character.UnicodeBlock

    HIRAGANA: Character.UnicodeBlock

    IDEOGRAPHIC_DESCRIPTION_CHARACTERS: Character.UnicodeBlock

    IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION: Character.UnicodeBlock

    IMPERIAL_ARAMAIC: Character.UnicodeBlock

    INDIC_SIYAQ_NUMBERS: Character.UnicodeBlock

    INSCRIPTIONAL_PAHLAVI: Character.UnicodeBlock

    INSCRIPTIONAL_PARTHIAN: Character.UnicodeBlock

    IPA_EXTENSIONS: Character.UnicodeBlock

    JAVANESE: Character.UnicodeBlock

    KAITHI: Character.UnicodeBlock

    KANA_EXTENDED_A: Character.UnicodeBlock

    KANA_SUPPLEMENT: Character.UnicodeBlock

    KANBUN: Character.UnicodeBlock

    KANGXI_RADICALS: Character.UnicodeBlock

    KANNADA: Character.UnicodeBlock

    KATAKANA: Character.UnicodeBlock

    KATAKANA_PHONETIC_EXTENSIONS: Character.UnicodeBlock

    KAYAH_LI: Character.UnicodeBlock

    KHAROSHTHI: Character.UnicodeBlock

    KHITAN_SMALL_SCRIPT: Character.UnicodeBlock

    KHMER: Character.UnicodeBlock

    KHMER_SYMBOLS: Character.UnicodeBlock

    KHOJKI: Character.UnicodeBlock

    KHUDAWADI: Character.UnicodeBlock

    LAO: Character.UnicodeBlock

    LATIN_1_SUPPLEMENT: Character.UnicodeBlock

    LATIN_EXTENDED_A: Character.UnicodeBlock

    LATIN_EXTENDED_ADDITIONAL: Character.UnicodeBlock

    LATIN_EXTENDED_B: Character.UnicodeBlock

    LATIN_EXTENDED_C: Character.UnicodeBlock

    LATIN_EXTENDED_D: Character.UnicodeBlock

    LATIN_EXTENDED_E: Character.UnicodeBlock

    LEPCHA: Character.UnicodeBlock

    LETTERLIKE_SYMBOLS: Character.UnicodeBlock

    LIMBU: Character.UnicodeBlock

    LINEAR_A: Character.UnicodeBlock

    LINEAR_B_IDEOGRAMS: Character.UnicodeBlock

    LINEAR_B_SYLLABARY: Character.UnicodeBlock

    LISU: Character.UnicodeBlock

    LISU_SUPPLEMENT: Character.UnicodeBlock

    LOW_SURROGATES: Character.UnicodeBlock

    LYCIAN: Character.UnicodeBlock

    LYDIAN: Character.UnicodeBlock

    MAHAJANI: Character.UnicodeBlock

    MAHJONG_TILES: Character.UnicodeBlock

    MAKASAR: Character.UnicodeBlock

    MALAYALAM: Character.UnicodeBlock

    MANDAIC: Character.UnicodeBlock

    MANICHAEAN: Character.UnicodeBlock

    MARCHEN: Character.UnicodeBlock

    MASARAM_GONDI: Character.UnicodeBlock

    MATHEMATICAL_ALPHANUMERIC_SYMBOLS: Character.UnicodeBlock

    MATHEMATICAL_OPERATORS: Character.UnicodeBlock

    MAYAN_NUMERALS: Character.UnicodeBlock

    MEDEFAIDRIN: Character.UnicodeBlock

    MEETEI_MAYEK: Character.UnicodeBlock

    MEETEI_MAYEK_EXTENSIONS: Character.UnicodeBlock

    MENDE_KIKAKUI: Character.UnicodeBlock

    MEROITIC_CURSIVE: Character.UnicodeBlock

    MEROITIC_HIEROGLYPHS: Character.UnicodeBlock

    MIAO: Character.UnicodeBlock

    MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A: Character.UnicodeBlock

    MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B: Character.UnicodeBlock

    MISCELLANEOUS_SYMBOLS: Character.UnicodeBlock

    MISCELLANEOUS_SYMBOLS_AND_ARROWS: Character.UnicodeBlock

    MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS: Character.UnicodeBlock

    MISCELLANEOUS_TECHNICAL: Character.UnicodeBlock

    MODI: Character.UnicodeBlock

    MODIFIER_TONE_LETTERS: Character.UnicodeBlock

    MONGOLIAN: Character.UnicodeBlock

    MONGOLIAN_SUPPLEMENT: Character.UnicodeBlock

    MRO: Character.UnicodeBlock

    MULTANI: Character.UnicodeBlock

    MUSICAL_SYMBOLS: Character.UnicodeBlock

    MYANMAR: Character.UnicodeBlock

    MYANMAR_EXTENDED_A: Character.UnicodeBlock

    MYANMAR_EXTENDED_B: Character.UnicodeBlock

    NABATAEAN: Character.UnicodeBlock

    NANDINAGARI: Character.UnicodeBlock

    NEW_TAI_LUE: Character.UnicodeBlock

    NEWA: Character.UnicodeBlock

    NKO: Character.UnicodeBlock

    NUMBER_FORMS: Character.UnicodeBlock

    NUSHU: Character.UnicodeBlock

    NYIAKENG_PUACHUE_HMONG: Character.UnicodeBlock

    OGHAM: Character.UnicodeBlock

    OL_CHIKI: Character.UnicodeBlock

    OLD_HUNGARIAN: Character.UnicodeBlock

    OLD_ITALIC: Character.UnicodeBlock

    OLD_NORTH_ARABIAN: Character.UnicodeBlock

    OLD_PERMIC: Character.UnicodeBlock

    OLD_PERSIAN: Character.UnicodeBlock

    OLD_SOGDIAN: Character.UnicodeBlock

    OLD_SOUTH_ARABIAN: Character.UnicodeBlock

    OLD_TURKIC: Character.UnicodeBlock

    OPTICAL_CHARACTER_RECOGNITION: Character.UnicodeBlock

    ORIYA: Character.UnicodeBlock

    ORNAMENTAL_DINGBATS: Character.UnicodeBlock

    OSAGE: Character.UnicodeBlock

    OSMANYA: Character.UnicodeBlock

    OTTOMAN_SIYAQ_NUMBERS: Character.UnicodeBlock

    PAHAWH_HMONG: Character.UnicodeBlock

    PALMYRENE: Character.UnicodeBlock

    PAU_CIN_HAU: Character.UnicodeBlock

    PHAGS_PA: Character.UnicodeBlock

    PHAISTOS_DISC: Character.UnicodeBlock

    PHOENICIAN: Character.UnicodeBlock

    PHONETIC_EXTENSIONS: Character.UnicodeBlock

    PHONETIC_EXTENSIONS_SUPPLEMENT: Character.UnicodeBlock

    PLAYING_CARDS: Character.UnicodeBlock

    PRIVATE_USE_AREA: Character.UnicodeBlock

    PSALTER_PAHLAVI: Character.UnicodeBlock

    REJANG: Character.UnicodeBlock

    RUMI_NUMERAL_SYMBOLS: Character.UnicodeBlock

    RUNIC: Character.UnicodeBlock

    SAMARITAN: Character.UnicodeBlock

    SAURASHTRA: Character.UnicodeBlock

    SHARADA: Character.UnicodeBlock

    SHAVIAN: Character.UnicodeBlock

    SHORTHAND_FORMAT_CONTROLS: Character.UnicodeBlock

    SIDDHAM: Character.UnicodeBlock

    SINHALA: Character.UnicodeBlock

    SINHALA_ARCHAIC_NUMBERS: Character.UnicodeBlock

    SMALL_FORM_VARIANTS: Character.UnicodeBlock

    SMALL_KANA_EXTENSION: Character.UnicodeBlock

    SOGDIAN: Character.UnicodeBlock

    SORA_SOMPENG: Character.UnicodeBlock

    SOYOMBO: Character.UnicodeBlock

    SPACING_MODIFIER_LETTERS: Character.UnicodeBlock

    SPECIALS: Character.UnicodeBlock

    SUNDANESE: Character.UnicodeBlock

    SUNDANESE_SUPPLEMENT: Character.UnicodeBlock

    SUPERSCRIPTS_AND_SUBSCRIPTS: Character.UnicodeBlock

    SUPPLEMENTAL_ARROWS_A: Character.UnicodeBlock

    SUPPLEMENTAL_ARROWS_B: Character.UnicodeBlock

    SUPPLEMENTAL_ARROWS_C: Character.UnicodeBlock

    SUPPLEMENTAL_MATHEMATICAL_OPERATORS: Character.UnicodeBlock

    SUPPLEMENTAL_PUNCTUATION: Character.UnicodeBlock

    SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS: Character.UnicodeBlock

    SUPPLEMENTARY_PRIVATE_USE_AREA_A: Character.UnicodeBlock

    SUPPLEMENTARY_PRIVATE_USE_AREA_B: Character.UnicodeBlock

    SURROGATES_AREA: Character.UnicodeBlock

    SUTTON_SIGNWRITING: Character.UnicodeBlock

    SYLOTI_NAGRI: Character.UnicodeBlock

    SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A: Character.UnicodeBlock

    SYMBOLS_FOR_LEGACY_COMPUTING: Character.UnicodeBlock

    SYRIAC: Character.UnicodeBlock

    SYRIAC_SUPPLEMENT: Character.UnicodeBlock

    TAGALOG: Character.UnicodeBlock

    TAGBANWA: Character.UnicodeBlock

    TAGS: Character.UnicodeBlock

    TAI_LE: Character.UnicodeBlock

    TAI_THAM: Character.UnicodeBlock

    TAI_VIET: Character.UnicodeBlock

    TAI_XUAN_JING_SYMBOLS: Character.UnicodeBlock

    TAKRI: Character.UnicodeBlock

    TAMIL: Character.UnicodeBlock

    TAMIL_SUPPLEMENT: Character.UnicodeBlock

    TANGUT: Character.UnicodeBlock

    TANGUT_COMPONENTS: Character.UnicodeBlock

    TANGUT_SUPPLEMENT: Character.UnicodeBlock

    TELUGU: Character.UnicodeBlock

    THAANA: Character.UnicodeBlock

    THAI: Character.UnicodeBlock

    TIBETAN: Character.UnicodeBlock

    TIFINAGH: Character.UnicodeBlock

    TIRHUTA: Character.UnicodeBlock

    TRANSPORT_AND_MAP_SYMBOLS: Character.UnicodeBlock

    UGARITIC: Character.UnicodeBlock

    UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS: Character.UnicodeBlock

    UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED: Character.UnicodeBlock

    VAI: Character.UnicodeBlock

    VARIATION_SELECTORS: Character.UnicodeBlock

    VARIATION_SELECTORS_SUPPLEMENT: Character.UnicodeBlock

    VEDIC_EXTENSIONS: Character.UnicodeBlock

    VERTICAL_FORMS: Character.UnicodeBlock

    WANCHO: Character.UnicodeBlock

    WARANG_CITI: Character.UnicodeBlock

    YEZIDI: Character.UnicodeBlock

    YI_RADICALS: Character.UnicodeBlock

    YI_SYLLABLES: Character.UnicodeBlock

    YIJING_HEXAGRAM_SYMBOLS: Character.UnicodeBlock

    ZANABAZAR_SQUARE: Character.UnicodeBlock

    @staticmethod
    def forName(arg0: str) -> Character.UnicodeBlock: ...

    @staticmethod
    @overload
    def of(arg0: str) -> Character.UnicodeBlock: ...

    @staticmethod
    @overload
    def of(arg0: int) -> Character.UnicodeBlock: ...

  class UnicodeScript(Enum):

    ADLAM: Character.UnicodeScript

    AHOM: Character.UnicodeScript

    ANATOLIAN_HIEROGLYPHS: Character.UnicodeScript

    ARABIC: Character.UnicodeScript

    ARMENIAN: Character.UnicodeScript

    AVESTAN: Character.UnicodeScript

    BALINESE: Character.UnicodeScript

    BAMUM: Character.UnicodeScript

    BASSA_VAH: Character.UnicodeScript

    BATAK: Character.UnicodeScript

    BENGALI: Character.UnicodeScript

    BHAIKSUKI: Character.UnicodeScript

    BOPOMOFO: Character.UnicodeScript

    BRAHMI: Character.UnicodeScript

    BRAILLE: Character.UnicodeScript

    BUGINESE: Character.UnicodeScript

    BUHID: Character.UnicodeScript

    CANADIAN_ABORIGINAL: Character.UnicodeScript

    CARIAN: Character.UnicodeScript

    CAUCASIAN_ALBANIAN: Character.UnicodeScript

    CHAKMA: Character.UnicodeScript

    CHAM: Character.UnicodeScript

    CHEROKEE: Character.UnicodeScript

    CHORASMIAN: Character.UnicodeScript

    COMMON: Character.UnicodeScript

    COPTIC: Character.UnicodeScript

    CUNEIFORM: Character.UnicodeScript

    CYPRIOT: Character.UnicodeScript

    CYRILLIC: Character.UnicodeScript

    DESERET: Character.UnicodeScript

    DEVANAGARI: Character.UnicodeScript

    DIVES_AKURU: Character.UnicodeScript

    DOGRA: Character.UnicodeScript

    DUPLOYAN: Character.UnicodeScript

    EGYPTIAN_HIEROGLYPHS: Character.UnicodeScript

    ELBASAN: Character.UnicodeScript

    ELYMAIC: Character.UnicodeScript

    ETHIOPIC: Character.UnicodeScript

    GEORGIAN: Character.UnicodeScript

    GLAGOLITIC: Character.UnicodeScript

    GOTHIC: Character.UnicodeScript

    GRANTHA: Character.UnicodeScript

    GREEK: Character.UnicodeScript

    GUJARATI: Character.UnicodeScript

    GUNJALA_GONDI: Character.UnicodeScript

    GURMUKHI: Character.UnicodeScript

    HAN: Character.UnicodeScript

    HANGUL: Character.UnicodeScript

    HANIFI_ROHINGYA: Character.UnicodeScript

    HANUNOO: Character.UnicodeScript

    HATRAN: Character.UnicodeScript

    HEBREW: Character.UnicodeScript

    HIRAGANA: Character.UnicodeScript

    IMPERIAL_ARAMAIC: Character.UnicodeScript

    INHERITED: Character.UnicodeScript

    INSCRIPTIONAL_PAHLAVI: Character.UnicodeScript

    INSCRIPTIONAL_PARTHIAN: Character.UnicodeScript

    JAVANESE: Character.UnicodeScript

    KAITHI: Character.UnicodeScript

    KANNADA: Character.UnicodeScript

    KATAKANA: Character.UnicodeScript

    KAYAH_LI: Character.UnicodeScript

    KHAROSHTHI: Character.UnicodeScript

    KHITAN_SMALL_SCRIPT: Character.UnicodeScript

    KHMER: Character.UnicodeScript

    KHOJKI: Character.UnicodeScript

    KHUDAWADI: Character.UnicodeScript

    LAO: Character.UnicodeScript

    LATIN: Character.UnicodeScript

    LEPCHA: Character.UnicodeScript

    LIMBU: Character.UnicodeScript

    LINEAR_A: Character.UnicodeScript

    LINEAR_B: Character.UnicodeScript

    LISU: Character.UnicodeScript

    LYCIAN: Character.UnicodeScript

    LYDIAN: Character.UnicodeScript

    MAHAJANI: Character.UnicodeScript

    MAKASAR: Character.UnicodeScript

    MALAYALAM: Character.UnicodeScript

    MANDAIC: Character.UnicodeScript

    MANICHAEAN: Character.UnicodeScript

    MARCHEN: Character.UnicodeScript

    MASARAM_GONDI: Character.UnicodeScript

    MEDEFAIDRIN: Character.UnicodeScript

    MEETEI_MAYEK: Character.UnicodeScript

    MENDE_KIKAKUI: Character.UnicodeScript

    MEROITIC_CURSIVE: Character.UnicodeScript

    MEROITIC_HIEROGLYPHS: Character.UnicodeScript

    MIAO: Character.UnicodeScript

    MODI: Character.UnicodeScript

    MONGOLIAN: Character.UnicodeScript

    MRO: Character.UnicodeScript

    MULTANI: Character.UnicodeScript

    MYANMAR: Character.UnicodeScript

    NABATAEAN: Character.UnicodeScript

    NANDINAGARI: Character.UnicodeScript

    NEW_TAI_LUE: Character.UnicodeScript

    NEWA: Character.UnicodeScript

    NKO: Character.UnicodeScript

    NUSHU: Character.UnicodeScript

    NYIAKENG_PUACHUE_HMONG: Character.UnicodeScript

    OGHAM: Character.UnicodeScript

    OL_CHIKI: Character.UnicodeScript

    OLD_HUNGARIAN: Character.UnicodeScript

    OLD_ITALIC: Character.UnicodeScript

    OLD_NORTH_ARABIAN: Character.UnicodeScript

    OLD_PERMIC: Character.UnicodeScript

    OLD_PERSIAN: Character.UnicodeScript

    OLD_SOGDIAN: Character.UnicodeScript

    OLD_SOUTH_ARABIAN: Character.UnicodeScript

    OLD_TURKIC: Character.UnicodeScript

    ORIYA: Character.UnicodeScript

    OSAGE: Character.UnicodeScript

    OSMANYA: Character.UnicodeScript

    PAHAWH_HMONG: Character.UnicodeScript

    PALMYRENE: Character.UnicodeScript

    PAU_CIN_HAU: Character.UnicodeScript

    PHAGS_PA: Character.UnicodeScript

    PHOENICIAN: Character.UnicodeScript

    PSALTER_PAHLAVI: Character.UnicodeScript

    REJANG: Character.UnicodeScript

    RUNIC: Character.UnicodeScript

    SAMARITAN: Character.UnicodeScript

    SAURASHTRA: Character.UnicodeScript

    SHARADA: Character.UnicodeScript

    SHAVIAN: Character.UnicodeScript

    SIDDHAM: Character.UnicodeScript

    SIGNWRITING: Character.UnicodeScript

    SINHALA: Character.UnicodeScript

    SOGDIAN: Character.UnicodeScript

    SORA_SOMPENG: Character.UnicodeScript

    SOYOMBO: Character.UnicodeScript

    SUNDANESE: Character.UnicodeScript

    SYLOTI_NAGRI: Character.UnicodeScript

    SYRIAC: Character.UnicodeScript

    TAGALOG: Character.UnicodeScript

    TAGBANWA: Character.UnicodeScript

    TAI_LE: Character.UnicodeScript

    TAI_THAM: Character.UnicodeScript

    TAI_VIET: Character.UnicodeScript

    TAKRI: Character.UnicodeScript

    TAMIL: Character.UnicodeScript

    TANGUT: Character.UnicodeScript

    TELUGU: Character.UnicodeScript

    THAANA: Character.UnicodeScript

    THAI: Character.UnicodeScript

    TIBETAN: Character.UnicodeScript

    TIFINAGH: Character.UnicodeScript

    TIRHUTA: Character.UnicodeScript

    UGARITIC: Character.UnicodeScript

    UNKNOWN: Character.UnicodeScript

    VAI: Character.UnicodeScript

    WANCHO: Character.UnicodeScript

    WARANG_CITI: Character.UnicodeScript

    YEZIDI: Character.UnicodeScript

    YI: Character.UnicodeScript

    ZANABAZAR_SQUARE: Character.UnicodeScript

    @staticmethod
    def forName(arg0: str) -> Character.UnicodeScript: ...

    @staticmethod
    def of(arg0: int) -> Character.UnicodeScript: ...

    @staticmethod
    def valueOf(arg0: str) -> Character.UnicodeScript: ...

    @staticmethod
    def values() -> list[Character.UnicodeScript]: ...

  class Subset:

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...


class CharacterData: ...


class CharacterDataLatin1(CharacterData): ...


class Class[T]:

  @overload
  def arrayType(self) -> TypeDescriptor.OfField: ...

  @overload
  def arrayType(self) -> Class[Any]: ...

  @overload
  def arrayType(self) -> TypeDescriptor.OfField: ...

  def asSubclass(self, arg0: Class[U]) -> Class[U]: ...

  def cast(self, arg0: object) -> object: ...

  @overload
  def componentType(self) -> Class[Any]: ...

  @overload
  def componentType(self) -> TypeDescriptor.OfField: ...

  @overload
  def componentType(self) -> TypeDescriptor.OfField: ...

  @overload
  def describeConstable(self) -> Optional[ClassDesc]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def descriptorString(self) -> str: ...

  def desiredAssertionStatus(self) -> bool: ...

  def getAnnotatedInterfaces(self) -> list[AnnotatedType]: ...

  def getAnnotatedSuperclass(self) -> AnnotatedType: ...

  @overload
  def getAnnotation(self, arg0: Class[A]) -> A: ...

  @overload
  def getAnnotation(self, arg0: Class[T]) -> T: ...

  @overload
  def getAnnotations(self) -> list[Annotation]: ...

  @overload
  def getAnnotations(self) -> list[Annotation]: ...

  @overload
  def getAnnotationsByType(self, arg0: Class[A]) -> list[Annotation]: ...

  @overload
  def getAnnotationsByType(self, arg0: Class[T]) -> list[Annotation]: ...

  def getCanonicalName(self) -> str: ...

  def getClassLoader(self) -> ClassLoader: ...

  def getClasses(self) -> list[Class]: ...

  def getComponentType(self) -> Class[Any]: ...

  def getConstructor(self, arg0: list[Class]) -> Constructor[T]: ...

  def getConstructors(self) -> list[Constructor]: ...

  @overload
  def getDeclaredAnnotation(self, arg0: Class[A]) -> A: ...

  @overload
  def getDeclaredAnnotation(self, arg0: Class[T]) -> T: ...

  @overload
  def getDeclaredAnnotations(self) -> list[Annotation]: ...

  @overload
  def getDeclaredAnnotations(self) -> list[Annotation]: ...

  @overload
  def getDeclaredAnnotationsByType(self, arg0: Class[A]) -> list[Annotation]: ...

  @overload
  def getDeclaredAnnotationsByType(self, arg0: Class[T]) -> list[Annotation]: ...

  def getDeclaredClasses(self) -> list[Class]: ...

  def getDeclaredConstructor(self, arg0: list[Class]) -> Constructor[T]: ...

  def getDeclaredConstructors(self) -> list[Constructor]: ...

  def getDeclaredField(self, arg0: str) -> Field: ...

  def getDeclaredFields(self) -> list[Field]: ...

  def getDeclaredMethod(self, arg0: str, arg1: list[Class]) -> Method: ...

  def getDeclaredMethods(self) -> list[Method]: ...

  def getDeclaringClass(self) -> Class[Any]: ...

  def getEnclosingClass(self) -> Class[Any]: ...

  def getEnclosingConstructor(self) -> Constructor[Any]: ...

  def getEnclosingMethod(self) -> Method: ...

  def getEnumConstants(self) -> list[object]: ...

  def getField(self, arg0: str) -> Field: ...

  def getFields(self) -> list[Field]: ...

  def getGenericInterfaces(self) -> list[Type]: ...

  def getGenericSuperclass(self) -> Type: ...

  def getInterfaces(self) -> list[Class]: ...

  def getMethod(self, arg0: str, arg1: list[Class]) -> Method: ...

  def getMethods(self) -> list[Method]: ...

  def getModifiers(self) -> int: ...

  def getModule(self) -> Module: ...

  def getName(self) -> str: ...

  def getNestHost(self) -> Class[Any]: ...

  def getNestMembers(self) -> list[Class]: ...

  def getPackage(self) -> Package: ...

  def getPackageName(self) -> str: ...

  def getPermittedSubclasses(self) -> list[Class]: ...

  def getProtectionDomain(self) -> ProtectionDomain: ...

  def getRecordComponents(self) -> list[RecordComponent]: ...

  def getResource(self, arg0: str) -> URL: ...

  def getResourceAsStream(self, arg0: str) -> InputStream: ...

  def getSigners(self) -> list[object]: ...

  def getSimpleName(self) -> str: ...

  def getSuperclass(self) -> Class[T]: ...

  @overload
  def getTypeName(self) -> str: ...

  @overload
  def getTypeName(self) -> str: ...

  @overload
  def getTypeParameters(self) -> list[TypeVariable]: ...

  @overload
  def getTypeParameters(self) -> list[TypeVariable]: ...

  def isAnnotation(self) -> bool: ...

  @overload
  def isAnnotationPresent(self, arg0: Class[Annotation]) -> bool: ...

  @overload
  def isAnnotationPresent(self, arg0: Class[Annotation]) -> bool: ...

  def isAnonymousClass(self) -> bool: ...

  @overload
  def isArray(self) -> bool: ...

  @overload
  def isArray(self) -> bool: ...

  def isAssignableFrom(self, arg0: Class[Any]) -> bool: ...

  def isEnum(self) -> bool: ...

  def isHidden(self) -> bool: ...

  def isInstance(self, arg0: object) -> bool: ...

  def isInterface(self) -> bool: ...

  def isLocalClass(self) -> bool: ...

  def isMemberClass(self) -> bool: ...

  def isNestmateOf(self, arg0: Class[Any]) -> bool: ...

  @overload
  def isPrimitive(self) -> bool: ...

  @overload
  def isPrimitive(self) -> bool: ...

  def isRecord(self) -> bool: ...

  def isSealed(self) -> bool: ...

  def isSynthetic(self) -> bool: ...

  def newInstance(self) -> object: ...

  def toGenericString(self) -> str: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def forName(arg0: str) -> Class[Any]: ...

  @staticmethod
  @overload
  def forName(arg0: Module, arg1: str) -> Class[Any]: ...

  @staticmethod
  @overload
  def forName(arg0: str, arg1: bool, arg2: ClassLoader) -> Class[Any]: ...

  class ReflectionData[ReflectionData_T]: ...

  class EnclosingMethodInfo: ...

  class Atomic: ...

  class AnnotationData: ...


class ClassCastException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class ClassFormatError(LinkageError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class ClassLoader:

  def clearAssertionStatus(self) -> None: ...

  def getDefinedPackage(self, arg0: str) -> Package: ...

  def getDefinedPackages(self) -> list[Package]: ...

  def getName(self) -> str: ...

  def getParent(self) -> ClassLoader: ...

  def getResource(self, arg0: str) -> URL: ...

  def getResourceAsStream(self, arg0: str) -> InputStream: ...

  def getResources(self, arg0: str) -> Enumeration[URL]: ...

  def getUnnamedModule(self) -> Module: ...

  def isRegisteredAsParallelCapable(self) -> bool: ...

  def loadClass(self, arg0: str) -> Class[Any]: ...

  def resources(self, arg0: str) -> Stream[URL]: ...

  def setClassAssertionStatus(self, arg0: str, arg1: bool) -> None: ...

  def setDefaultAssertionStatus(self, arg0: bool) -> None: ...

  def setPackageAssertionStatus(self, arg0: str, arg1: bool) -> None: ...

  @staticmethod
  def getPlatformClassLoader() -> ClassLoader: ...

  @staticmethod
  def getSystemClassLoader() -> ClassLoader: ...

  @staticmethod
  def getSystemResource(arg0: str) -> URL: ...

  @staticmethod
  def getSystemResourceAsStream(arg0: str) -> InputStream: ...

  @staticmethod
  def getSystemResources(arg0: str) -> Enumeration[URL]: ...

  class ParallelLoaders: ...


class ClassNotFoundException(ReflectiveOperationException):

  def getException(self) -> Throwable: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class ClassValue[T]:

  def get(self, arg0: Class[Any]) -> object: ...

  def remove(self, arg0: Class[Any]) -> None: ...

  class Identity: ...

  class Version[Version_T]: ...

  class Entry[Entry_T](WeakReference): ...

  class ClassValueMap(WeakHashMap): ...


class CloneNotSupportedException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Cloneable: ...


class Comparable[T]:

  def compareTo(self, arg0: object) -> int: ...


class Deprecated:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def forRemoval(self) -> bool: ...

  def hashCode(self) -> int: ...

  def since(self) -> str: ...

  def toString(self) -> str: ...


class Double(Number):

  BYTES: int

  MAX_EXPONENT: int

  MAX_VALUE: float

  MIN_EXPONENT: int

  MIN_NORMAL: float

  MIN_VALUE: float

  NaN: float

  NEGATIVE_INFINITY: float

  POSITIVE_INFINITY: float

  SIZE: int

  TYPE: Class[Double]

  def byteValue(self) -> int: ...

  @overload
  def compareTo(self, arg0: Double) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def describeConstable(self) -> Optional[Double]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def doubleValue(self) -> float: ...

  def equals(self, arg0: object) -> bool: ...

  def floatValue(self) -> float: ...

  def hashCode(self) -> int: ...

  def intValue(self) -> int: ...

  def isInfinite(self) -> bool: ...

  def isNaN(self) -> bool: ...

  def longValue(self) -> int: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> Double: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  def shortValue(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def compare(arg0: float, arg1: float) -> int: ...

  @staticmethod
  def doubleToLongBits(arg0: float) -> int: ...

  @staticmethod
  def doubleToRawLongBits(arg0: float) -> int: ...

  @staticmethod
  def isFinite(arg0: float) -> bool: ...

  @staticmethod
  def longBitsToDouble(arg0: int) -> float: ...

  @staticmethod
  def max(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def min(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def parseDouble(arg0: str) -> float: ...

  @staticmethod
  def sum(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def toHexString(arg0: float) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: float) -> Double: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> Double: ...

  @overload
  def __init__(self, arg0: float): ...
  @overload
  def __init__(self, arg0: str): ...


class Enum[E]:

  @overload
  def compareTo(self, arg0: E) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def describeConstable(self) -> Optional[Enum.EnumDesc[E]]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def equals(self, arg0: object) -> bool: ...

  def getDeclaringClass(self) -> Class[E]: ...

  def hashCode(self) -> int: ...

  def name(self) -> str: ...

  def ordinal(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def valueOf(arg0: Class[T], arg1: str) -> T: ...

  class EnumDesc[EnumDesc_E](DynamicConstantDesc):

    @overload
    def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

    @overload
    def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> E: ...

    def toString(self) -> str: ...

    @staticmethod
    def of(arg0: ClassDesc, arg1: str) -> Enum.EnumDesc: ...


class Error(Throwable):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class Exception(Throwable):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class Float(Number):

  BYTES: int

  MAX_EXPONENT: int

  MAX_VALUE: float

  MIN_EXPONENT: int

  MIN_NORMAL: float

  MIN_VALUE: float

  NaN: float

  NEGATIVE_INFINITY: float

  POSITIVE_INFINITY: float

  SIZE: int

  TYPE: Class[Float]

  def byteValue(self) -> int: ...

  @overload
  def compareTo(self, arg0: Float) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def describeConstable(self) -> Optional[Float]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def doubleValue(self) -> float: ...

  def equals(self, arg0: object) -> bool: ...

  def floatValue(self) -> float: ...

  def hashCode(self) -> int: ...

  def intValue(self) -> int: ...

  def isInfinite(self) -> bool: ...

  def isNaN(self) -> bool: ...

  def longValue(self) -> int: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> Float: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  def shortValue(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def compare(arg0: float, arg1: float) -> int: ...

  @staticmethod
  def floatToIntBits(arg0: float) -> int: ...

  @staticmethod
  def floatToRawIntBits(arg0: float) -> int: ...

  @staticmethod
  def intBitsToFloat(arg0: int) -> float: ...

  @staticmethod
  def isFinite(arg0: float) -> bool: ...

  @staticmethod
  def max(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def min(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def parseFloat(arg0: str) -> float: ...

  @staticmethod
  def sum(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def toHexString(arg0: float) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: float) -> Float: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> Float: ...

  @overload
  def __init__(self, arg0: float): ...
  @overload
  def __init__(self, arg0: float): ...
  @overload
  def __init__(self, arg0: str): ...


class IllegalAccessException(ReflectiveOperationException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class IllegalArgumentException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class IllegalMonitorStateException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class IllegalStateException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class IllegalThreadStateException(IllegalArgumentException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class IncompatibleClassChangeError(LinkageError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class IndexOutOfBoundsException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: int): ...


class InstantiationException(ReflectiveOperationException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Integer(Number):

  BYTES: int

  MAX_VALUE: int

  MIN_VALUE: int

  SIZE: int

  TYPE: Class[Integer]

  def byteValue(self) -> int: ...

  @overload
  def compareTo(self, arg0: Integer) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def describeConstable(self) -> Optional[Integer]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def doubleValue(self) -> float: ...

  def equals(self, arg0: object) -> bool: ...

  def floatValue(self) -> float: ...

  def hashCode(self) -> int: ...

  def intValue(self) -> int: ...

  def longValue(self) -> int: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> Integer: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  def shortValue(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def bitCount(arg0: int) -> int: ...

  @staticmethod
  def compare(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def compareUnsigned(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def decode(arg0: str) -> Integer: ...

  @staticmethod
  def divideUnsigned(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def getInteger(arg0: str) -> Integer: ...

  @staticmethod
  @overload
  def getInteger(arg0: str, arg1: int) -> Integer: ...

  @staticmethod
  @overload
  def getInteger(arg0: str, arg1: Integer) -> Integer: ...

  @staticmethod
  def highestOneBit(arg0: int) -> int: ...

  @staticmethod
  def lowestOneBit(arg0: int) -> int: ...

  @staticmethod
  def max(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def min(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def numberOfLeadingZeros(arg0: int) -> int: ...

  @staticmethod
  def numberOfTrailingZeros(arg0: int) -> int: ...

  @staticmethod
  @overload
  def parseInt(arg0: str) -> int: ...

  @staticmethod
  @overload
  def parseInt(arg0: str, arg1: int) -> int: ...

  @staticmethod
  @overload
  def parseInt(arg0: CharSequence, arg1: int, arg2: int, arg3: int) -> int: ...

  @staticmethod
  @overload
  def parseUnsignedInt(arg0: str) -> int: ...

  @staticmethod
  @overload
  def parseUnsignedInt(arg0: str, arg1: int) -> int: ...

  @staticmethod
  @overload
  def parseUnsignedInt(arg0: CharSequence, arg1: int, arg2: int, arg3: int) -> int: ...

  @staticmethod
  def remainderUnsigned(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def reverse(arg0: int) -> int: ...

  @staticmethod
  def reverseBytes(arg0: int) -> int: ...

  @staticmethod
  def rotateLeft(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def rotateRight(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def signum(arg0: int) -> int: ...

  @staticmethod
  def sum(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def toBinaryString(arg0: int) -> str: ...

  @staticmethod
  def toHexString(arg0: int) -> str: ...

  @staticmethod
  def toOctalString(arg0: int) -> str: ...

  @staticmethod
  def toUnsignedLong(arg0: int) -> int: ...

  @staticmethod
  @overload
  def toUnsignedString(arg0: int) -> str: ...

  @staticmethod
  @overload
  def toUnsignedString(arg0: int, arg1: int) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: int) -> Integer: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> Integer: ...

  @staticmethod
  @overload
  def valueOf(arg0: str, arg1: int) -> Integer: ...

  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: str): ...

  class IntegerCache: ...


class InternalError(VirtualMachineError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class InterruptedException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Iterable[T]:

  def forEach(self, arg0: Consumer[T]) -> None: ...

  def iterator(self) -> Iterator[T]: ...

  def spliterator(self) -> Spliterator[T]: ...


class LayerInstantiationException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class LinkageError(Error):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class LiveStackFrame:

  def getByteCodeIndex(self) -> int: ...

  def getClassName(self) -> str: ...

  def getDeclaringClass(self) -> Class[Any]: ...

  def getDescriptor(self) -> str: ...

  def getFileName(self) -> str: ...

  def getLineNumber(self) -> int: ...

  def getLocals(self) -> list[object]: ...

  def getMethodName(self) -> str: ...

  def getMethodType(self) -> MethodType: ...

  def getMonitors(self) -> list[object]: ...

  def getStack(self) -> list[object]: ...

  def isNativeMethod(self) -> bool: ...

  def toStackTraceElement(self) -> StackTraceElement: ...

  @staticmethod
  @overload
  def getStackWalker() -> StackWalker: ...

  @staticmethod
  @overload
  def getStackWalker(arg0: Set[StackWalker.Option]) -> StackWalker: ...

  class PrimitiveSlot:

    def intValue(self) -> int: ...

    def longValue(self) -> int: ...

    def size(self) -> int: ...


class LiveStackFrameInfo(StackFrameInfo):

  @overload
  def getLocals(self) -> list[object]: ...

  @overload
  def getLocals(self) -> list[object]: ...

  @overload
  def getMonitors(self) -> list[object]: ...

  @overload
  def getMonitors(self) -> list[object]: ...

  @overload
  def getStack(self) -> list[object]: ...

  @overload
  def getStack(self) -> list[object]: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def getStackWalker() -> StackWalker: ...

  @staticmethod
  @overload
  def getStackWalker(arg0: Set[StackWalker.Option]) -> StackWalker: ...

  class PrimitiveSlot32(LiveStackFrame.PrimitiveSlot):

    def intValue(self) -> int: ...

    def size(self) -> int: ...

    def toString(self) -> str: ...

  class PrimitiveSlot64(LiveStackFrame.PrimitiveSlot):

    def longValue(self) -> int: ...

    def size(self) -> int: ...

    def toString(self) -> str: ...


class Long(Number):

  BYTES: int

  MAX_VALUE: int

  MIN_VALUE: int

  SIZE: int

  TYPE: Class[Long]

  def byteValue(self) -> int: ...

  @overload
  def compareTo(self, arg0: Long) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def describeConstable(self) -> Optional[Long]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def doubleValue(self) -> float: ...

  def equals(self, arg0: object) -> bool: ...

  def floatValue(self) -> float: ...

  def hashCode(self) -> int: ...

  def intValue(self) -> int: ...

  def longValue(self) -> int: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> Long: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  def shortValue(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def bitCount(arg0: int) -> int: ...

  @staticmethod
  def compare(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def compareUnsigned(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def decode(arg0: str) -> Long: ...

  @staticmethod
  def divideUnsigned(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def getLong(arg0: str) -> Long: ...

  @staticmethod
  @overload
  def getLong(arg0: str, arg1: Long) -> Long: ...

  @staticmethod
  @overload
  def getLong(arg0: str, arg1: int) -> Long: ...

  @staticmethod
  def highestOneBit(arg0: int) -> int: ...

  @staticmethod
  def lowestOneBit(arg0: int) -> int: ...

  @staticmethod
  def max(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def min(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def numberOfLeadingZeros(arg0: int) -> int: ...

  @staticmethod
  def numberOfTrailingZeros(arg0: int) -> int: ...

  @staticmethod
  @overload
  def parseLong(arg0: str) -> int: ...

  @staticmethod
  @overload
  def parseLong(arg0: str, arg1: int) -> int: ...

  @staticmethod
  @overload
  def parseLong(arg0: CharSequence, arg1: int, arg2: int, arg3: int) -> int: ...

  @staticmethod
  @overload
  def parseUnsignedLong(arg0: str) -> int: ...

  @staticmethod
  @overload
  def parseUnsignedLong(arg0: str, arg1: int) -> int: ...

  @staticmethod
  @overload
  def parseUnsignedLong(arg0: CharSequence, arg1: int, arg2: int, arg3: int) -> int: ...

  @staticmethod
  def remainderUnsigned(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def reverse(arg0: int) -> int: ...

  @staticmethod
  def reverseBytes(arg0: int) -> int: ...

  @staticmethod
  def rotateLeft(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def rotateRight(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def signum(arg0: int) -> int: ...

  @staticmethod
  def sum(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def toBinaryString(arg0: int) -> str: ...

  @staticmethod
  def toHexString(arg0: int) -> str: ...

  @staticmethod
  def toOctalString(arg0: int) -> str: ...

  @staticmethod
  @overload
  def toUnsignedString(arg0: int) -> str: ...

  @staticmethod
  @overload
  def toUnsignedString(arg0: int, arg1: int) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> Long: ...

  @staticmethod
  @overload
  def valueOf(arg0: int) -> Long: ...

  @staticmethod
  @overload
  def valueOf(arg0: str, arg1: int) -> Long: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: int): ...

  class LongCache: ...


class Math:

  E: float

  PI: float

  @staticmethod
  def IEEEremainder(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def abs(arg0: float) -> float: ...

  @staticmethod
  @overload
  def abs(arg0: float) -> float: ...

  @staticmethod
  @overload
  def abs(arg0: int) -> int: ...

  @staticmethod
  @overload
  def abs(arg0: int) -> int: ...

  @staticmethod
  @overload
  def absExact(arg0: int) -> int: ...

  @staticmethod
  @overload
  def absExact(arg0: int) -> int: ...

  @staticmethod
  def acos(arg0: float) -> float: ...

  @staticmethod
  @overload
  def addExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def addExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def asin(arg0: float) -> float: ...

  @staticmethod
  def atan(arg0: float) -> float: ...

  @staticmethod
  def atan2(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def cbrt(arg0: float) -> float: ...

  @staticmethod
  def ceil(arg0: float) -> float: ...

  @staticmethod
  @overload
  def ceilDiv(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def ceilDiv(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def ceilDiv(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def ceilDivExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def ceilDivExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def ceilMod(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def ceilMod(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def ceilMod(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def copySign(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def copySign(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def cos(arg0: float) -> float: ...

  @staticmethod
  def cosh(arg0: float) -> float: ...

  @staticmethod
  @overload
  def decrementExact(arg0: int) -> int: ...

  @staticmethod
  @overload
  def decrementExact(arg0: int) -> int: ...

  @staticmethod
  @overload
  def divideExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def divideExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def exp(arg0: float) -> float: ...

  @staticmethod
  def expm1(arg0: float) -> float: ...

  @staticmethod
  def floor(arg0: float) -> float: ...

  @staticmethod
  @overload
  def floorDiv(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def floorDiv(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def floorDiv(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def floorDivExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def floorDivExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def floorMod(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def floorMod(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def floorMod(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def fma(arg0: float, arg1: float, arg2: float) -> float: ...

  @staticmethod
  @overload
  def fma(arg0: float, arg1: float, arg2: float) -> float: ...

  @staticmethod
  @overload
  def getExponent(arg0: float) -> int: ...

  @staticmethod
  @overload
  def getExponent(arg0: float) -> int: ...

  @staticmethod
  def hypot(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def incrementExact(arg0: int) -> int: ...

  @staticmethod
  @overload
  def incrementExact(arg0: int) -> int: ...

  @staticmethod
  def log(arg0: float) -> float: ...

  @staticmethod
  def log10(arg0: float) -> float: ...

  @staticmethod
  def log1p(arg0: float) -> float: ...

  @staticmethod
  @overload
  def max(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def max(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def max(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def max(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def min(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def min(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def min(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def min(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def multiplyExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def multiplyExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def multiplyExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def multiplyFull(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def multiplyHigh(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def negateExact(arg0: int) -> int: ...

  @staticmethod
  @overload
  def negateExact(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nextAfter(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def nextAfter(arg0: float, arg1: float) -> float: ...

  @staticmethod
  @overload
  def nextDown(arg0: float) -> float: ...

  @staticmethod
  @overload
  def nextDown(arg0: float) -> float: ...

  @staticmethod
  @overload
  def nextUp(arg0: float) -> float: ...

  @staticmethod
  @overload
  def nextUp(arg0: float) -> float: ...

  @staticmethod
  def pow(arg0: float, arg1: float) -> float: ...

  @staticmethod
  def random() -> float: ...

  @staticmethod
  def rint(arg0: float) -> float: ...

  @staticmethod
  @overload
  def round(arg0: float) -> int: ...

  @staticmethod
  @overload
  def round(arg0: float) -> int: ...

  @staticmethod
  @overload
  def scalb(arg0: float, arg1: int) -> float: ...

  @staticmethod
  @overload
  def scalb(arg0: float, arg1: int) -> float: ...

  @staticmethod
  @overload
  def signum(arg0: float) -> float: ...

  @staticmethod
  @overload
  def signum(arg0: float) -> float: ...

  @staticmethod
  def sin(arg0: float) -> float: ...

  @staticmethod
  def sinh(arg0: float) -> float: ...

  @staticmethod
  def sqrt(arg0: float) -> float: ...

  @staticmethod
  @overload
  def subtractExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  @overload
  def subtractExact(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def tan(arg0: float) -> float: ...

  @staticmethod
  def tanh(arg0: float) -> float: ...

  @staticmethod
  def toDegrees(arg0: float) -> float: ...

  @staticmethod
  def toIntExact(arg0: int) -> int: ...

  @staticmethod
  def toRadians(arg0: float) -> float: ...

  @staticmethod
  @overload
  def ulp(arg0: float) -> float: ...

  @staticmethod
  @overload
  def ulp(arg0: float) -> float: ...

  @staticmethod
  def unsignedMultiplyHigh(arg0: int, arg1: int) -> int: ...

  class RandomNumberGeneratorHolder: ...


class Module:

  def addExports(self, arg0: str, arg1: Module) -> Module: ...

  def addOpens(self, arg0: str, arg1: Module) -> Module: ...

  def addReads(self, arg0: Module) -> Module: ...

  def addUses(self, arg0: Class[Any]) -> Module: ...

  def canRead(self, arg0: Module) -> bool: ...

  def canUse(self, arg0: Class[Any]) -> bool: ...

  @overload
  def getAnnotation(self, arg0: Class[T]) -> T: ...

  @overload
  def getAnnotation(self, arg0: Class[T]) -> T: ...

  @overload
  def getAnnotations(self) -> list[Annotation]: ...

  @overload
  def getAnnotations(self) -> list[Annotation]: ...

  def getAnnotationsByType(self, arg0: Class[T]) -> list[Annotation]: ...

  def getClassLoader(self) -> ClassLoader: ...

  def getDeclaredAnnotation(self, arg0: Class[T]) -> T: ...

  @overload
  def getDeclaredAnnotations(self) -> list[Annotation]: ...

  @overload
  def getDeclaredAnnotations(self) -> list[Annotation]: ...

  def getDeclaredAnnotationsByType(self, arg0: Class[T]) -> list[Annotation]: ...

  def getDescriptor(self) -> ModuleDescriptor: ...

  def getLayer(self) -> ModuleLayer: ...

  def getName(self) -> str: ...

  def getPackages(self) -> Set[str]: ...

  def getResourceAsStream(self, arg0: str) -> InputStream: ...

  def isAnnotationPresent(self, arg0: Class[Annotation]) -> bool: ...

  @overload
  def isExported(self, arg0: str) -> bool: ...

  @overload
  def isExported(self, arg0: str, arg1: Module) -> bool: ...

  def isNamed(self) -> bool: ...

  @overload
  def isOpen(self, arg0: str) -> bool: ...

  @overload
  def isOpen(self, arg0: str, arg1: Module) -> bool: ...

  def toString(self) -> str: ...

  class ReflectionData: ...

  class ArchivedData: ...


class ModuleLayer:

  def configuration(self) -> Configuration: ...

  def defineModules(self, arg0: Configuration, arg1: Function[str, ClassLoader]) -> ModuleLayer: ...

  def defineModulesWithManyLoaders(self, arg0: Configuration, arg1: ClassLoader) -> ModuleLayer: ...

  def defineModulesWithOneLoader(self, arg0: Configuration, arg1: ClassLoader) -> ModuleLayer: ...

  def findLoader(self, arg0: str) -> ClassLoader: ...

  def findModule(self, arg0: str) -> Optional[Module]: ...

  def modules(self) -> Set[Module]: ...

  def parents(self) -> List[ModuleLayer]: ...

  def toString(self) -> str: ...

  @staticmethod
  def boot() -> ModuleLayer: ...

  @staticmethod
  def empty() -> ModuleLayer: ...

  class Controller:

    def addExports(self, arg0: Module, arg1: str, arg2: Module) -> ModuleLayer.Controller: ...

    def addOpens(self, arg0: Module, arg1: str, arg2: Module) -> ModuleLayer.Controller: ...

    def addReads(self, arg0: Module, arg1: Module) -> ModuleLayer.Controller: ...

    def layer(self) -> ModuleLayer: ...


class NamedPackage: ...


class NegativeArraySizeException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class NoClassDefFoundError(LinkageError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class NoSuchFieldError(IncompatibleClassChangeError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class NoSuchFieldException(ReflectiveOperationException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class NoSuchMethodError(IncompatibleClassChangeError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class NoSuchMethodException(ReflectiveOperationException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class NullPointerException(RuntimeException):

  def fillInStackTrace(self) -> Throwable: ...

  def getMessage(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Number:

  def byteValue(self) -> int: ...

  def doubleValue(self) -> float: ...

  def floatValue(self) -> float: ...

  def intValue(self) -> int: ...

  def longValue(self) -> int: ...

  def shortValue(self) -> int: ...

  def __init__(self): ...


class NumberFormatException(IllegalArgumentException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Object:

  def equals(self, arg0: object) -> bool: ...

  def getClass(self) -> Class[Any]: ...

  def hashCode(self) -> int: ...

  def notify(self) -> None: ...

  def notifyAll(self) -> None: ...

  def toString(self) -> str: ...

  @overload
  def wait(self) -> None: ...

  @overload
  def wait(self, arg0: int) -> None: ...

  @overload
  def wait(self, arg0: int, arg1: int) -> None: ...

  def __init__(self): ...


class OutOfMemoryError(VirtualMachineError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Package(NamedPackage):

  @overload
  def getAnnotation(self, arg0: Class[A]) -> A: ...

  @overload
  def getAnnotation(self, arg0: Class[T]) -> T: ...

  @overload
  def getAnnotations(self) -> list[Annotation]: ...

  @overload
  def getAnnotations(self) -> list[Annotation]: ...

  @overload
  def getAnnotationsByType(self, arg0: Class[A]) -> list[Annotation]: ...

  @overload
  def getAnnotationsByType(self, arg0: Class[T]) -> list[Annotation]: ...

  @overload
  def getDeclaredAnnotation(self, arg0: Class[A]) -> A: ...

  @overload
  def getDeclaredAnnotation(self, arg0: Class[T]) -> T: ...

  @overload
  def getDeclaredAnnotations(self) -> list[Annotation]: ...

  @overload
  def getDeclaredAnnotations(self) -> list[Annotation]: ...

  @overload
  def getDeclaredAnnotationsByType(self, arg0: Class[A]) -> list[Annotation]: ...

  @overload
  def getDeclaredAnnotationsByType(self, arg0: Class[T]) -> list[Annotation]: ...

  def getImplementationTitle(self) -> str: ...

  def getImplementationVendor(self) -> str: ...

  def getImplementationVersion(self) -> str: ...

  def getName(self) -> str: ...

  def getSpecificationTitle(self) -> str: ...

  def getSpecificationVendor(self) -> str: ...

  def getSpecificationVersion(self) -> str: ...

  def hashCode(self) -> int: ...

  @overload
  def isAnnotationPresent(self, arg0: Class[Annotation]) -> bool: ...

  @overload
  def isAnnotationPresent(self, arg0: Class[Annotation]) -> bool: ...

  def isCompatibleWith(self, arg0: str) -> bool: ...

  @overload
  def isSealed(self) -> bool: ...

  @overload
  def isSealed(self, arg0: URL) -> bool: ...

  def toString(self) -> str: ...

  @staticmethod
  def getPackage(arg0: str) -> Package: ...

  @staticmethod
  def getPackages() -> list[Package]: ...

  class VersionInfo: ...


class Process:

  def children(self) -> Stream[ProcessHandle]: ...

  def descendants(self) -> Stream[ProcessHandle]: ...

  def destroy(self) -> None: ...

  def destroyForcibly(self) -> Process: ...

  @overload
  def errorReader(self) -> BufferedReader: ...

  @overload
  def errorReader(self, arg0: Charset) -> BufferedReader: ...

  def exitValue(self) -> int: ...

  def getErrorStream(self) -> InputStream: ...

  def getInputStream(self) -> InputStream: ...

  def getOutputStream(self) -> OutputStream: ...

  def info(self) -> ProcessHandle.Info: ...

  @overload
  def inputReader(self) -> BufferedReader: ...

  @overload
  def inputReader(self, arg0: Charset) -> BufferedReader: ...

  def isAlive(self) -> bool: ...

  def onExit(self) -> CompletableFuture[Process]: ...

  @overload
  def outputWriter(self) -> BufferedWriter: ...

  @overload
  def outputWriter(self, arg0: Charset) -> BufferedWriter: ...

  def pid(self) -> int: ...

  def supportsNormalTermination(self) -> bool: ...

  def toHandle(self) -> ProcessHandle: ...

  @overload
  def waitFor(self) -> int: ...

  @overload
  def waitFor(self, arg0: int, arg1: TimeUnit) -> bool: ...

  def __init__(self): ...

  class CharsetHolder: ...

  class PipeInputStream(FileInputStream):

    def skip(self, arg0: int) -> int: ...


class ProcessHandle:

  def children(self) -> Stream[ProcessHandle]: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: ProcessHandle) -> int: ...

  def descendants(self) -> Stream[ProcessHandle]: ...

  def destroy(self) -> bool: ...

  def destroyForcibly(self) -> bool: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def info(self) -> ProcessHandle.Info: ...

  def isAlive(self) -> bool: ...

  def onExit(self) -> CompletableFuture[ProcessHandle]: ...

  def parent(self) -> Optional[ProcessHandle]: ...

  def pid(self) -> int: ...

  def supportsNormalTermination(self) -> bool: ...

  @staticmethod
  def allProcesses() -> Stream[ProcessHandle]: ...

  @staticmethod
  def current() -> ProcessHandle: ...

  @staticmethod
  def of(arg0: int) -> Optional[ProcessHandle]: ...

  class Info:

    def arguments(self) -> Optional[String]: ...

    def command(self) -> Optional[str]: ...

    def commandLine(self) -> Optional[str]: ...

    def startInstant(self) -> Optional[Instant]: ...

    def totalCpuDuration(self) -> Optional[Duration]: ...

    def user(self) -> Optional[str]: ...


class PublicMethods:

  class Key:

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

  class MethodList: ...


class Readable:

  def read(self, arg0: CharBuffer) -> int: ...


class Record:

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class ReflectiveOperationException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class Runnable:

  def run(self) -> None: ...


class Runtime:

  def addShutdownHook(self, arg0: Thread) -> None: ...

  def availableProcessors(self) -> int: ...

  @overload
  def exec(self, arg0: list[str]) -> Process: ...

  @overload
  def exec(self, arg0: str) -> Process: ...

  @overload
  def exec(self, arg0: list[str], arg1: list[str]) -> Process: ...

  @overload
  def exec(self, arg0: str, arg1: list[str]) -> Process: ...

  @overload
  def exec(self, arg0: list[str], arg1: list[str], arg2: File) -> Process: ...

  @overload
  def exec(self, arg0: str, arg1: list[str], arg2: File) -> Process: ...

  def exit(self, arg0: int) -> None: ...

  def freeMemory(self) -> int: ...

  def gc(self) -> None: ...

  def halt(self, arg0: int) -> None: ...

  def load(self, arg0: str) -> None: ...

  def loadLibrary(self, arg0: str) -> None: ...

  def maxMemory(self) -> int: ...

  def removeShutdownHook(self, arg0: Thread) -> bool: ...

  def runFinalization(self) -> None: ...

  def totalMemory(self) -> int: ...

  @staticmethod
  def getRuntime() -> Runtime: ...

  @staticmethod
  def version() -> Runtime.Version: ...

  class Version:

    def build(self) -> Optional[Integer]: ...

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: object) -> int: ...

    @overload
    def compareTo(self, arg0: Runtime.Version) -> int: ...

    def compareToIgnoreOptional(self, arg0: Runtime.Version) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def equalsIgnoreOptional(self, arg0: object) -> bool: ...

    def feature(self) -> int: ...

    def hashCode(self) -> int: ...

    def interim(self) -> int: ...

    def major(self) -> int: ...

    def minor(self) -> int: ...

    def optional(self) -> Optional[str]: ...

    def patch(self) -> int: ...

    def pre(self) -> Optional[str]: ...

    def security(self) -> int: ...

    def toString(self) -> str: ...

    def update(self) -> int: ...

    def version(self) -> List[Integer]: ...

    @staticmethod
    def parse(arg0: str) -> Runtime.Version: ...

  class VersionPattern: ...


class RuntimeException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class RuntimePermission(BasicPermission):

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: str): ...


class SafeVarargs:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class SecurityException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class SecurityManager:

  def checkAccept(self, arg0: str, arg1: int) -> None: ...

  @overload
  def checkAccess(self, arg0: Thread) -> None: ...

  @overload
  def checkAccess(self, arg0: ThreadGroup) -> None: ...

  @overload
  def checkConnect(self, arg0: str, arg1: int) -> None: ...

  @overload
  def checkConnect(self, arg0: str, arg1: int, arg2: object) -> None: ...

  def checkCreateClassLoader(self) -> None: ...

  def checkDelete(self, arg0: str) -> None: ...

  def checkExec(self, arg0: str) -> None: ...

  def checkExit(self, arg0: int) -> None: ...

  def checkLink(self, arg0: str) -> None: ...

  def checkListen(self, arg0: int) -> None: ...

  @overload
  def checkMulticast(self, arg0: InetAddress) -> None: ...

  @overload
  def checkMulticast(self, arg0: InetAddress, arg1: int) -> None: ...

  def checkPackageAccess(self, arg0: str) -> None: ...

  def checkPackageDefinition(self, arg0: str) -> None: ...

  @overload
  def checkPermission(self, arg0: Permission) -> None: ...

  @overload
  def checkPermission(self, arg0: Permission, arg1: object) -> None: ...

  def checkPrintJobAccess(self) -> None: ...

  def checkPropertiesAccess(self) -> None: ...

  def checkPropertyAccess(self, arg0: str) -> None: ...

  @overload
  def checkRead(self, arg0: FileDescriptor) -> None: ...

  @overload
  def checkRead(self, arg0: str) -> None: ...

  @overload
  def checkRead(self, arg0: str, arg1: object) -> None: ...

  def checkSecurityAccess(self, arg0: str) -> None: ...

  def checkSetFactory(self) -> None: ...

  @overload
  def checkWrite(self, arg0: FileDescriptor) -> None: ...

  @overload
  def checkWrite(self, arg0: str) -> None: ...

  def getSecurityContext(self) -> object: ...

  def getThreadGroup(self) -> ThreadGroup: ...

  def __init__(self): ...


class Short(Number):

  BYTES: int

  MAX_VALUE: int

  MIN_VALUE: int

  SIZE: int

  TYPE: Class[Short]

  def byteValue(self) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: Short) -> int: ...

  @overload
  def describeConstable(self) -> Optional[DynamicConstantDesc[Short]]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def doubleValue(self) -> float: ...

  def equals(self, arg0: object) -> bool: ...

  def floatValue(self) -> float: ...

  def hashCode(self) -> int: ...

  def intValue(self) -> int: ...

  def longValue(self) -> int: ...

  def shortValue(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def compare(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def compareUnsigned(arg0: int, arg1: int) -> int: ...

  @staticmethod
  def decode(arg0: str) -> Short: ...

  @staticmethod
  @overload
  def parseShort(arg0: str) -> int: ...

  @staticmethod
  @overload
  def parseShort(arg0: str, arg1: int) -> int: ...

  @staticmethod
  def reverseBytes(arg0: int) -> int: ...

  @staticmethod
  def toUnsignedInt(arg0: int) -> int: ...

  @staticmethod
  def toUnsignedLong(arg0: int) -> int: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> Short: ...

  @staticmethod
  @overload
  def valueOf(arg0: int) -> Short: ...

  @staticmethod
  @overload
  def valueOf(arg0: str, arg1: int) -> Short: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: int): ...

  class ShortCache: ...


class Shutdown:

  class Lock: ...


class StackFrameInfo:

  @overload
  def getByteCodeIndex(self) -> int: ...

  @overload
  def getByteCodeIndex(self) -> int: ...

  @overload
  def getClassName(self) -> str: ...

  @overload
  def getClassName(self) -> str: ...

  @overload
  def getDeclaringClass(self) -> Class[Any]: ...

  @overload
  def getDeclaringClass(self) -> Class[Any]: ...

  @overload
  def getDescriptor(self) -> str: ...

  @overload
  def getDescriptor(self) -> str: ...

  @overload
  def getFileName(self) -> str: ...

  @overload
  def getFileName(self) -> str: ...

  @overload
  def getLineNumber(self) -> int: ...

  @overload
  def getLineNumber(self) -> int: ...

  @overload
  def getMethodName(self) -> str: ...

  @overload
  def getMethodName(self) -> str: ...

  @overload
  def getMethodType(self) -> MethodType: ...

  @overload
  def getMethodType(self) -> MethodType: ...

  @overload
  def isNativeMethod(self) -> bool: ...

  @overload
  def isNativeMethod(self) -> bool: ...

  @overload
  def toStackTraceElement(self) -> StackTraceElement: ...

  @overload
  def toStackTraceElement(self) -> StackTraceElement: ...

  def toString(self) -> str: ...


class StackOverflowError(VirtualMachineError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class StackStreamFactory:

  class LiveStackInfoTraverser[T](StackStreamFactory.StackFrameTraverser):

    class LiveStackFrameBuffer(StackStreamFactory.FrameBuffer): ...

  class StackFrameTraverser[T](StackStreamFactory.AbstractStackWalker):

    CONCURRENT: int

    DISTINCT: int

    IMMUTABLE: int

    NONNULL: int

    ORDERED: int

    SIZED: int

    SORTED: int

    SUBSIZED: int

    @overload
    def characteristics(self) -> int: ...

    @overload
    def characteristics(self) -> int: ...

    @overload
    def estimateSize(self) -> int: ...

    @overload
    def estimateSize(self) -> int: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[StackWalker.StackFrame]) -> None: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[T]) -> None: ...

    def getComparator(self) -> Comparator[T]: ...

    def getExactSizeIfKnown(self) -> int: ...

    def hasCharacteristics(self, arg0: int) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[StackWalker.StackFrame]) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[T]) -> bool: ...

    @overload
    def trySplit(self) -> Spliterator[StackWalker.StackFrame]: ...

    @overload
    def trySplit(self) -> Spliterator[T]: ...

    class StackFrameBuffer(StackStreamFactory.FrameBuffer): ...

  class CallerClassFinder(StackStreamFactory.AbstractStackWalker):

    class ClassBuffer(StackStreamFactory.FrameBuffer): ...

  class AbstractStackWalker[R, T]: ...

  class FrameBuffer[F]: ...

  class WalkerState(Enum):

    CLOSED: StackStreamFactory.WalkerState

    NEW: StackStreamFactory.WalkerState

    OPEN: StackStreamFactory.WalkerState

    @staticmethod
    def valueOf(arg0: str) -> StackStreamFactory.WalkerState: ...

    @staticmethod
    def values() -> list[StackStreamFactory.WalkerState]: ...


class StackTraceElement:

  def equals(self, arg0: object) -> bool: ...

  def getClassLoaderName(self) -> str: ...

  def getClassName(self) -> str: ...

  def getFileName(self) -> str: ...

  def getLineNumber(self) -> int: ...

  def getMethodName(self) -> str: ...

  def getModuleName(self) -> str: ...

  def getModuleVersion(self) -> str: ...

  def hashCode(self) -> int: ...

  def isNativeMethod(self) -> bool: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self, arg0: str, arg1: str, arg2: str, arg3: int): ...
  @overload
  def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, arg6: int): ...

  class HashedModules: ...


class StackWalker:

  def forEach(self, arg0: Consumer[StackWalker.StackFrame]) -> None: ...

  def getCallerClass(self) -> Class[Any]: ...

  def walk(self, arg0: Function[Stream[StackWalker.StackFrame], T]) -> object: ...

  @staticmethod
  @overload
  def getInstance() -> StackWalker: ...

  @staticmethod
  @overload
  def getInstance(arg0: StackWalker.Option) -> StackWalker: ...

  @staticmethod
  @overload
  def getInstance(arg0: Set[StackWalker.Option]) -> StackWalker: ...

  @staticmethod
  @overload
  def getInstance(arg0: Set[StackWalker.Option], arg1: int) -> StackWalker: ...

  class Option(Enum):

    RETAIN_CLASS_REFERENCE: StackWalker.Option

    SHOW_HIDDEN_FRAMES: StackWalker.Option

    SHOW_REFLECT_FRAMES: StackWalker.Option

    @staticmethod
    def valueOf(arg0: str) -> StackWalker.Option: ...

    @staticmethod
    def values() -> list[StackWalker.Option]: ...

  class ExtendedOption(Enum):

    LOCALS_AND_OPERANDS: StackWalker.ExtendedOption

    @staticmethod
    def valueOf(arg0: str) -> StackWalker.ExtendedOption: ...

    @staticmethod
    def values() -> list[StackWalker.ExtendedOption]: ...

  class StackFrame:

    def getByteCodeIndex(self) -> int: ...

    def getClassName(self) -> str: ...

    def getDeclaringClass(self) -> Class[Any]: ...

    def getDescriptor(self) -> str: ...

    def getFileName(self) -> str: ...

    def getLineNumber(self) -> int: ...

    def getMethodName(self) -> str: ...

    def getMethodType(self) -> MethodType: ...

    def isNativeMethod(self) -> bool: ...

    def toStackTraceElement(self) -> StackTraceElement: ...


class String:

  CASE_INSENSITIVE_ORDER: Comparator[str]

  @overload
  def charAt(self, arg0: int) -> str: ...

  @overload
  def charAt(self, arg0: int) -> str: ...

  @overload
  def chars(self) -> IntStream: ...

  @overload
  def chars(self) -> IntStream: ...

  def codePointAt(self, arg0: int) -> int: ...

  def codePointBefore(self, arg0: int) -> int: ...

  def codePointCount(self, arg0: int, arg1: int) -> int: ...

  @overload
  def codePoints(self) -> IntStream: ...

  @overload
  def codePoints(self) -> IntStream: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: str) -> int: ...

  def compareToIgnoreCase(self, arg0: str) -> int: ...

  def concat(self, arg0: str) -> str: ...

  def contains(self, arg0: CharSequence) -> bool: ...

  @overload
  def contentEquals(self, arg0: CharSequence) -> bool: ...

  @overload
  def contentEquals(self, arg0: StringBuffer) -> bool: ...

  @overload
  def describeConstable(self) -> Optional[str]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def endsWith(self, arg0: str) -> bool: ...

  def equals(self, arg0: object) -> bool: ...

  def equalsIgnoreCase(self, arg0: str) -> bool: ...

  def formatted(self, arg0: list[object]) -> str: ...

  @overload
  def getBytes(self) -> list[int]: ...

  @overload
  def getBytes(self, arg0: str) -> list[int]: ...

  @overload
  def getBytes(self, arg0: Charset) -> list[int]: ...

  @overload
  def getBytes(self, arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...

  def getChars(self, arg0: int, arg1: int, arg2: list[str], arg3: int) -> None: ...

  def hashCode(self) -> int: ...

  def indent(self, arg0: int) -> str: ...

  @overload
  def indexOf(self, arg0: int) -> int: ...

  @overload
  def indexOf(self, arg0: str) -> int: ...

  @overload
  def indexOf(self, arg0: int, arg1: int) -> int: ...

  @overload
  def indexOf(self, arg0: str, arg1: int) -> int: ...

  def intern(self) -> str: ...

  def isBlank(self) -> bool: ...

  @overload
  def isEmpty(self) -> bool: ...

  @overload
  def isEmpty(self) -> bool: ...

  @overload
  def lastIndexOf(self, arg0: int) -> int: ...

  @overload
  def lastIndexOf(self, arg0: str) -> int: ...

  @overload
  def lastIndexOf(self, arg0: int, arg1: int) -> int: ...

  @overload
  def lastIndexOf(self, arg0: str, arg1: int) -> int: ...

  @overload
  def length(self) -> int: ...

  @overload
  def length(self) -> int: ...

  def lines(self) -> Stream[str]: ...

  def matches(self, arg0: str) -> bool: ...

  def offsetByCodePoints(self, arg0: int, arg1: int) -> int: ...

  @overload
  def regionMatches(self, arg0: int, arg1: str, arg2: int, arg3: int) -> bool: ...

  @overload
  def regionMatches(self, arg0: bool, arg1: int, arg2: str, arg3: int, arg4: int) -> bool: ...

  def repeat(self, arg0: int) -> str: ...

  @overload
  def replace(self, arg0: str, arg1: str) -> str: ...

  @overload
  def replace(self, arg0: CharSequence, arg1: CharSequence) -> str: ...

  def replaceAll(self, arg0: str, arg1: str) -> str: ...

  def replaceFirst(self, arg0: str, arg1: str) -> str: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> str: ...

  @overload
  def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

  @overload
  def split(self, arg0: str) -> list[str]: ...

  @overload
  def split(self, arg0: str, arg1: int) -> list[str]: ...

  @overload
  def startsWith(self, arg0: str) -> bool: ...

  @overload
  def startsWith(self, arg0: str, arg1: int) -> bool: ...

  def strip(self) -> str: ...

  def stripIndent(self) -> str: ...

  def stripLeading(self) -> str: ...

  def stripTrailing(self) -> str: ...

  @overload
  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  @overload
  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  @overload
  def substring(self, arg0: int) -> str: ...

  @overload
  def substring(self, arg0: int, arg1: int) -> str: ...

  def toCharArray(self) -> list[str]: ...

  @overload
  def toLowerCase(self) -> str: ...

  @overload
  def toLowerCase(self, arg0: Locale) -> str: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toUpperCase(self) -> str: ...

  @overload
  def toUpperCase(self, arg0: Locale) -> str: ...

  def transform(self, arg0: Function[str, R]) -> object: ...

  def translateEscapes(self) -> str: ...

  def trim(self) -> str: ...

  @staticmethod
  def compare(arg0: CharSequence, arg1: CharSequence) -> int: ...

  @staticmethod
  @overload
  def copyValueOf(arg0: list[str]) -> str: ...

  @staticmethod
  @overload
  def copyValueOf(arg0: list[str], arg1: int, arg2: int) -> str: ...

  @staticmethod
  @overload
  def format(arg0: str, arg1: list[object]) -> str: ...

  @staticmethod
  @overload
  def format(arg0: Locale, arg1: str, arg2: list[object]) -> str: ...

  @staticmethod
  @overload
  def join(arg0: CharSequence, arg1: list[CharSequence]) -> str: ...

  @staticmethod
  @overload
  def join(arg0: CharSequence, arg1: Iterable[CharSequence]) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: list[str]) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: bool) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: float) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: float) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: int) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: object) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: int) -> str: ...

  @staticmethod
  @overload
  def valueOf(arg0: list[str], arg1: int, arg2: int) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: list[int]): ...
  @overload
  def __init__(self, arg0: list[str]): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: StringBuffer): ...
  @overload
  def __init__(self, arg0: StringBuilder): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int): ...
  @overload
  def __init__(self, arg0: list[int], arg1: str): ...
  @overload
  def __init__(self, arg0: list[int], arg1: Charset): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int, arg2: int): ...
  @overload
  def __init__(self, arg0: list[str], arg1: int, arg2: int): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int, arg2: int): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int, arg2: int, arg3: int): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int, arg2: int, arg3: str): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int, arg2: int, arg3: Charset): ...

  class CaseInsensitiveComparator:

    @overload
    def compare(self, arg0: object, arg1: object) -> int: ...

    @overload
    def compare(self, arg0: object, arg1: object) -> int: ...

    @overload
    def compare(self, arg0: str, arg1: str) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def reversed(self) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Comparator[T]) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Function[T, U]) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

    def thenComparingDouble(self, arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

    def thenComparingInt(self, arg0: ToIntFunction[T]) -> Comparator[T]: ...

    def thenComparingLong(self, arg0: ToLongFunction[T]) -> Comparator[T]: ...

    @staticmethod
    @overload
    def comparing(arg0: Function[T, U]) -> Comparator[T]: ...

    @staticmethod
    @overload
    def comparing(arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

    @staticmethod
    def comparingDouble(arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def comparingInt(arg0: ToIntFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def comparingLong(arg0: ToLongFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def naturalOrder() -> Comparator[T]: ...

    @staticmethod
    def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

    @staticmethod
    def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

    @staticmethod
    def reverseOrder() -> Comparator[T]: ...


class StringBuffer(AbstractStringBuilder):

  @overload
  def append(self, arg0: list[str]) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: list[str]) -> StringBuffer: ...

  @overload
  def append(self, arg0: bool) -> StringBuffer: ...

  @overload
  def append(self, arg0: bool) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: str) -> StringBuffer: ...

  @overload
  def append(self, arg0: str) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: str) -> Appendable: ...

  @overload
  def append(self, arg0: float) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: float) -> StringBuffer: ...

  @overload
  def append(self, arg0: float) -> StringBuffer: ...

  @overload
  def append(self, arg0: float) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: int) -> StringBuffer: ...

  @overload
  def append(self, arg0: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence) -> Appendable: ...

  @overload
  def append(self, arg0: CharSequence) -> StringBuffer: ...

  @overload
  def append(self, arg0: object) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: object) -> StringBuffer: ...

  @overload
  def append(self, arg0: str) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: str) -> StringBuffer: ...

  @overload
  def append(self, arg0: StringBuffer) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: StringBuffer) -> StringBuffer: ...

  @overload
  def append(self, arg0: int) -> StringBuffer: ...

  @overload
  def append(self, arg0: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: list[str], arg1: int, arg2: int) -> StringBuffer: ...

  @overload
  def append(self, arg0: list[str], arg1: int, arg2: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> Appendable: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> StringBuffer: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> AbstractStringBuilder: ...

  @overload
  def appendCodePoint(self, arg0: int) -> AbstractStringBuilder: ...

  @overload
  def appendCodePoint(self, arg0: int) -> StringBuffer: ...

  def capacity(self) -> int: ...

  @overload
  def charAt(self, arg0: int) -> str: ...

  @overload
  def charAt(self, arg0: int) -> str: ...

  @overload
  def chars(self) -> IntStream: ...

  @overload
  def chars(self) -> IntStream: ...

  def codePointAt(self, arg0: int) -> int: ...

  def codePointBefore(self, arg0: int) -> int: ...

  def codePointCount(self, arg0: int, arg1: int) -> int: ...

  @overload
  def codePoints(self) -> IntStream: ...

  @overload
  def codePoints(self) -> IntStream: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: StringBuffer) -> int: ...

  @overload
  def delete(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  @overload
  def delete(self, arg0: int, arg1: int) -> StringBuffer: ...

  @overload
  def deleteCharAt(self, arg0: int) -> StringBuffer: ...

  @overload
  def deleteCharAt(self, arg0: int) -> AbstractStringBuilder: ...

  def ensureCapacity(self, arg0: int) -> None: ...

  def getChars(self, arg0: int, arg1: int, arg2: list[str], arg3: int) -> None: ...

  @overload
  def indexOf(self, arg0: str) -> int: ...

  @overload
  def indexOf(self, arg0: str, arg1: int) -> int: ...

  @overload
  def insert(self, arg0: int, arg1: list[str]) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: list[str]) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: bool) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: bool) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: object) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: object) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: list[str], arg2: int, arg3: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: list[str], arg2: int, arg3: int) -> StringBuffer: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence, arg2: int, arg3: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence, arg2: int, arg3: int) -> StringBuffer: ...

  def isEmpty(self) -> bool: ...

  @overload
  def lastIndexOf(self, arg0: str) -> int: ...

  @overload
  def lastIndexOf(self, arg0: str, arg1: int) -> int: ...

  @overload
  def length(self) -> int: ...

  @overload
  def length(self) -> int: ...

  def offsetByCodePoints(self, arg0: int, arg1: int) -> int: ...

  @overload
  def replace(self, arg0: int, arg1: int, arg2: str) -> AbstractStringBuilder: ...

  @overload
  def replace(self, arg0: int, arg1: int, arg2: str) -> StringBuffer: ...

  @overload
  def reverse(self) -> StringBuffer: ...

  @overload
  def reverse(self) -> AbstractStringBuilder: ...

  def setCharAt(self, arg0: int, arg1: str) -> None: ...

  def setLength(self, arg0: int) -> None: ...

  @overload
  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  @overload
  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  @overload
  def substring(self, arg0: int) -> str: ...

  @overload
  def substring(self, arg0: int, arg1: int) -> str: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toString(self) -> str: ...

  def trimToSize(self) -> None: ...

  @staticmethod
  def compare(arg0: CharSequence, arg1: CharSequence) -> int: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: CharSequence): ...
  @overload
  def __init__(self, arg0: str): ...


class StringBuilder(AbstractStringBuilder):

  @overload
  def append(self, arg0: list[str]) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: list[str]) -> StringBuilder: ...

  @overload
  def append(self, arg0: bool) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: bool) -> StringBuilder: ...

  @overload
  def append(self, arg0: str) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: str) -> Appendable: ...

  @overload
  def append(self, arg0: str) -> StringBuilder: ...

  @overload
  def append(self, arg0: float) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: float) -> StringBuilder: ...

  @overload
  def append(self, arg0: float) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: float) -> StringBuilder: ...

  @overload
  def append(self, arg0: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: int) -> StringBuilder: ...

  @overload
  def append(self, arg0: CharSequence) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence) -> Appendable: ...

  @overload
  def append(self, arg0: CharSequence) -> StringBuilder: ...

  @overload
  def append(self, arg0: object) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: object) -> StringBuilder: ...

  @overload
  def append(self, arg0: str) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: str) -> StringBuilder: ...

  @overload
  def append(self, arg0: StringBuffer) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: StringBuffer) -> StringBuilder: ...

  @overload
  def append(self, arg0: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: int) -> StringBuilder: ...

  @overload
  def append(self, arg0: list[str], arg1: int, arg2: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: list[str], arg1: int, arg2: int) -> StringBuilder: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> AbstractStringBuilder: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> Appendable: ...

  @overload
  def append(self, arg0: CharSequence, arg1: int, arg2: int) -> StringBuilder: ...

  @overload
  def appendCodePoint(self, arg0: int) -> StringBuilder: ...

  @overload
  def appendCodePoint(self, arg0: int) -> AbstractStringBuilder: ...

  def capacity(self) -> int: ...

  @overload
  def charAt(self, arg0: int) -> str: ...

  @overload
  def charAt(self, arg0: int) -> str: ...

  @overload
  def chars(self) -> IntStream: ...

  @overload
  def chars(self) -> IntStream: ...

  def codePointAt(self, arg0: int) -> int: ...

  def codePointBefore(self, arg0: int) -> int: ...

  def codePointCount(self, arg0: int, arg1: int) -> int: ...

  @overload
  def codePoints(self) -> IntStream: ...

  @overload
  def codePoints(self) -> IntStream: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: StringBuilder) -> int: ...

  @overload
  def delete(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  @overload
  def delete(self, arg0: int, arg1: int) -> StringBuilder: ...

  @overload
  def deleteCharAt(self, arg0: int) -> AbstractStringBuilder: ...

  @overload
  def deleteCharAt(self, arg0: int) -> StringBuilder: ...

  def ensureCapacity(self, arg0: int) -> None: ...

  def getChars(self, arg0: int, arg1: int, arg2: list[str], arg3: int) -> None: ...

  @overload
  def indexOf(self, arg0: str) -> int: ...

  @overload
  def indexOf(self, arg0: str, arg1: int) -> int: ...

  @overload
  def insert(self, arg0: int, arg1: list[str]) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: list[str]) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: bool) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: bool) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: float) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: object) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: object) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: str) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: list[str], arg2: int, arg3: int) -> AbstractStringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: list[str], arg2: int, arg3: int) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence, arg2: int, arg3: int) -> StringBuilder: ...

  @overload
  def insert(self, arg0: int, arg1: CharSequence, arg2: int, arg3: int) -> AbstractStringBuilder: ...

  def isEmpty(self) -> bool: ...

  @overload
  def lastIndexOf(self, arg0: str) -> int: ...

  @overload
  def lastIndexOf(self, arg0: str, arg1: int) -> int: ...

  @overload
  def length(self) -> int: ...

  @overload
  def length(self) -> int: ...

  def offsetByCodePoints(self, arg0: int, arg1: int) -> int: ...

  @overload
  def replace(self, arg0: int, arg1: int, arg2: str) -> AbstractStringBuilder: ...

  @overload
  def replace(self, arg0: int, arg1: int, arg2: str) -> StringBuilder: ...

  @overload
  def reverse(self) -> StringBuilder: ...

  @overload
  def reverse(self) -> AbstractStringBuilder: ...

  def setCharAt(self, arg0: int, arg1: str) -> None: ...

  def setLength(self, arg0: int) -> None: ...

  @overload
  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  @overload
  def subSequence(self, arg0: int, arg1: int) -> CharSequence: ...

  @overload
  def substring(self, arg0: int) -> str: ...

  @overload
  def substring(self, arg0: int, arg1: int) -> str: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toString(self) -> str: ...

  def trimToSize(self) -> None: ...

  @staticmethod
  def compare(arg0: CharSequence, arg1: CharSequence) -> int: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: CharSequence): ...
  @overload
  def __init__(self, arg0: str): ...


class StringCoding:

  @staticmethod
  def hasNegatives(arg0: list[int], arg1: int, arg2: int) -> bool: ...

  @staticmethod
  def implEncodeAsciiArray(arg0: list[str], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  def implEncodeISOArray(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...


class StringConcatHelper: ...


class StringIndexOutOfBoundsException(IndexOutOfBoundsException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: str): ...


class StringLatin1:

  @staticmethod
  def canEncode(arg0: int) -> bool: ...

  @staticmethod
  def charAt(arg0: list[int], arg1: int) -> str: ...

  @staticmethod
  def codePointAt(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  def codePointBefore(arg0: list[int], arg1: int) -> int: ...

  @staticmethod
  def codePointCount(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def compareTo(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def compareTo(arg0: list[int], arg1: list[int], arg2: int, arg3: int) -> int: ...

  @staticmethod
  def compareToCI(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  def compareToCI_UTF16(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def compareToUTF16(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def compareToUTF16(arg0: list[int], arg1: list[int], arg2: int, arg3: int) -> int: ...

  @staticmethod
  def equals(arg0: list[int], arg1: list[int]) -> bool: ...

  @staticmethod
  def fillNull(arg0: list[int], arg1: int, arg2: int) -> None: ...

  @staticmethod
  def getBytes(arg0: list[int], arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...

  @staticmethod
  def getChar(arg0: list[int], arg1: int) -> str: ...

  @staticmethod
  def getChars(arg0: list[int], arg1: int, arg2: int, arg3: list[str], arg4: int) -> None: ...

  @staticmethod
  def hashCode(arg0: list[int]) -> int: ...

  @staticmethod
  @overload
  def indexOf(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def indexOf(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def indexOf(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  def indexOfNonWhitespace(arg0: list[int]) -> int: ...

  @staticmethod
  @overload
  def inflate(arg0: list[int], arg1: int, arg2: int) -> list[int]: ...

  @staticmethod
  @overload
  def inflate(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> None: ...

  @staticmethod
  @overload
  def inflate(arg0: list[int], arg1: int, arg2: list[str], arg3: int, arg4: int) -> None: ...

  @staticmethod
  @overload
  def lastIndexOf(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def lastIndexOf(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  def lastIndexOfNonWhitespace(arg0: list[int]) -> int: ...

  @staticmethod
  def length(arg0: list[int]) -> int: ...

  @staticmethod
  def newString(arg0: list[int], arg1: int, arg2: int) -> str: ...

  @staticmethod
  def putChar(arg0: list[int], arg1: int, arg2: int) -> None: ...

  @staticmethod
  def regionMatchesCI(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> bool: ...

  @staticmethod
  def regionMatchesCI_UTF16(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> bool: ...

  @staticmethod
  @overload
  def replace(arg0: list[int], arg1: str, arg2: str) -> str: ...

  @staticmethod
  @overload
  def replace(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: list[int], arg5: int) -> str: ...

  @staticmethod
  def strip(arg0: list[int]) -> str: ...

  @staticmethod
  def stripLeading(arg0: list[int]) -> str: ...

  @staticmethod
  def stripTrailing(arg0: list[int]) -> str: ...

  @staticmethod
  @overload
  def toBytes(arg0: str) -> list[int]: ...

  @staticmethod
  @overload
  def toBytes(arg0: list[int], arg1: int, arg2: int) -> list[int]: ...

  @staticmethod
  def toChars(arg0: list[int]) -> list[str]: ...

  @staticmethod
  def toLowerCase(arg0: str, arg1: list[int], arg2: Locale) -> str: ...

  @staticmethod
  def toUpperCase(arg0: str, arg1: list[int], arg2: Locale) -> str: ...

  @staticmethod
  def trim(arg0: list[int]) -> str: ...

  class LinesSpliterator:

    CONCURRENT: int

    DISTINCT: int

    IMMUTABLE: int

    NONNULL: int

    ORDERED: int

    SIZED: int

    SORTED: int

    SUBSIZED: int

    @overload
    def characteristics(self) -> int: ...

    @overload
    def characteristics(self) -> int: ...

    @overload
    def estimateSize(self) -> int: ...

    @overload
    def estimateSize(self) -> int: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[str]) -> None: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[T]) -> None: ...

    def getComparator(self) -> Comparator[T]: ...

    def getExactSizeIfKnown(self) -> int: ...

    def hasCharacteristics(self, arg0: int) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[str]) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[T]) -> bool: ...

    @overload
    def trySplit(self) -> Spliterator[str]: ...

    @overload
    def trySplit(self) -> Spliterator[T]: ...

  class CharsSpliterator:

    def characteristics(self) -> int: ...

    def estimateSize(self) -> int: ...

    @overload
    def forEachRemaining(self, arg0: object) -> None: ...

    @overload
    def forEachRemaining(self, arg0: object) -> None: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[Integer]) -> None: ...

    @overload
    def forEachRemaining(self, arg0: IntConsumer) -> None: ...

    @overload
    def forEachRemaining(self, arg0: IntConsumer) -> None: ...

    @overload
    def tryAdvance(self, arg0: object) -> bool: ...

    @overload
    def tryAdvance(self, arg0: object) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[Integer]) -> bool: ...

    @overload
    def tryAdvance(self, arg0: IntConsumer) -> bool: ...

    @overload
    def tryAdvance(self, arg0: IntConsumer) -> bool: ...

    @overload
    def trySplit(self) -> Spliterator.OfPrimitive: ...

    @overload
    def trySplit(self) -> Spliterator: ...

    @overload
    def trySplit(self) -> Spliterator.OfInt: ...

    @overload
    def trySplit(self) -> Spliterator.OfPrimitive: ...

    @overload
    def trySplit(self) -> Spliterator: ...

    @overload
    def trySplit(self) -> Spliterator.OfInt: ...


class StringUTF16:

  @staticmethod
  def charAt(arg0: list[int], arg1: int) -> str: ...

  @staticmethod
  def checkBoundsBeginEnd(arg0: int, arg1: int, arg2: list[int]) -> None: ...

  @staticmethod
  def checkBoundsOffCount(arg0: int, arg1: int, arg2: list[int]) -> None: ...

  @staticmethod
  def checkIndex(arg0: int, arg1: list[int]) -> None: ...

  @staticmethod
  def checkOffset(arg0: int, arg1: list[int]) -> None: ...

  @staticmethod
  def codePointAt(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  def codePointAtSB(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  def codePointBefore(arg0: list[int], arg1: int) -> int: ...

  @staticmethod
  def codePointBeforeSB(arg0: list[int], arg1: int) -> int: ...

  @staticmethod
  def codePointCount(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  def codePointCountSB(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def compareTo(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def compareTo(arg0: list[int], arg1: list[int], arg2: int, arg3: int) -> int: ...

  @staticmethod
  def compareToCI(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  def compareToCI_Latin1(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def compareToLatin1(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def compareToLatin1(arg0: list[int], arg1: list[int], arg2: int, arg3: int) -> int: ...

  @staticmethod
  @overload
  def compress(arg0: list[int], arg1: int, arg2: int) -> list[int]: ...

  @staticmethod
  @overload
  def compress(arg0: list[str], arg1: int, arg2: int) -> list[int]: ...

  @staticmethod
  @overload
  def compress(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def compress(arg0: list[str], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def contentEquals(arg0: list[int], arg1: list[int], arg2: int) -> bool: ...

  @staticmethod
  @overload
  def contentEquals(arg0: list[int], arg1: CharSequence, arg2: int) -> bool: ...

  @staticmethod
  def equals(arg0: list[int], arg1: list[int]) -> bool: ...

  @staticmethod
  def fillNull(arg0: list[int], arg1: int, arg2: int) -> None: ...

  @staticmethod
  def getBytes(arg0: list[int], arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...

  @staticmethod
  @overload
  def getChars(arg0: int, arg1: int, arg2: int, arg3: list[int]) -> int: ...

  @staticmethod
  @overload
  def getChars(arg0: int, arg1: int, arg2: int, arg3: list[int]) -> int: ...

  @staticmethod
  @overload
  def getChars(arg0: list[int], arg1: int, arg2: int, arg3: list[str], arg4: int) -> None: ...

  @staticmethod
  def hashCode(arg0: list[int]) -> int: ...

  @staticmethod
  @overload
  def indexOf(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def indexOf(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def indexOf(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def indexOfLatin1(arg0: list[int], arg1: list[int]) -> int: ...

  @staticmethod
  @overload
  def indexOfLatin1(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  def indexOfLatin1Unsafe(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  def indexOfNonWhitespace(arg0: list[int]) -> int: ...

  @staticmethod
  def inflate(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> None: ...

  @staticmethod
  @overload
  def lastIndexOf(arg0: list[int], arg1: int, arg2: int) -> int: ...

  @staticmethod
  @overload
  def lastIndexOf(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  def lastIndexOfLatin1(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  def lastIndexOfNonWhitespace(arg0: list[int]) -> int: ...

  @staticmethod
  def length(arg0: list[int]) -> int: ...

  @staticmethod
  def newBytesFor(arg0: int) -> list[int]: ...

  @staticmethod
  def newString(arg0: list[int], arg1: int, arg2: int) -> str: ...

  @staticmethod
  def putCharSB(arg0: list[int], arg1: int, arg2: int) -> None: ...

  @staticmethod
  @overload
  def putCharsAt(arg0: list[int], arg1: int, arg2: str, arg3: str, arg4: str, arg5: str) -> int: ...

  @staticmethod
  @overload
  def putCharsAt(arg0: list[int], arg1: int, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str) -> int: ...

  @staticmethod
  @overload
  def putCharsSB(arg0: list[int], arg1: int, arg2: list[str], arg3: int, arg4: int) -> None: ...

  @staticmethod
  @overload
  def putCharsSB(arg0: list[int], arg1: int, arg2: CharSequence, arg3: int, arg4: int) -> None: ...

  @staticmethod
  def regionMatchesCI(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> bool: ...

  @staticmethod
  def regionMatchesCI_Latin1(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> bool: ...

  @staticmethod
  @overload
  def replace(arg0: list[int], arg1: str, arg2: str) -> str: ...

  @staticmethod
  @overload
  def replace(arg0: list[int], arg1: int, arg2: bool, arg3: list[int], arg4: int, arg5: bool, arg6: list[int], arg7: int, arg8: bool) -> str: ...

  @staticmethod
  def reverse(arg0: list[int], arg1: int) -> None: ...

  @staticmethod
  def strip(arg0: list[int]) -> str: ...

  @staticmethod
  def stripLeading(arg0: list[int]) -> str: ...

  @staticmethod
  def stripTrailing(arg0: list[int]) -> str: ...

  @staticmethod
  @overload
  def toBytes(arg0: str) -> list[int]: ...

  @staticmethod
  @overload
  def toBytes(arg0: list[str], arg1: int, arg2: int) -> list[int]: ...

  @staticmethod
  @overload
  def toBytes(arg0: list[int], arg1: int, arg2: int) -> list[int]: ...

  @staticmethod
  def toChars(arg0: list[int]) -> list[str]: ...

  @staticmethod
  def toLowerCase(arg0: str, arg1: list[int], arg2: Locale) -> str: ...

  @staticmethod
  def toUpperCase(arg0: str, arg1: list[int], arg2: Locale) -> str: ...

  @staticmethod
  def trim(arg0: list[int]) -> str: ...

  class LinesSpliterator:

    CONCURRENT: int

    DISTINCT: int

    IMMUTABLE: int

    NONNULL: int

    ORDERED: int

    SIZED: int

    SORTED: int

    SUBSIZED: int

    @overload
    def characteristics(self) -> int: ...

    @overload
    def characteristics(self) -> int: ...

    @overload
    def estimateSize(self) -> int: ...

    @overload
    def estimateSize(self) -> int: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[str]) -> None: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[T]) -> None: ...

    def getComparator(self) -> Comparator[T]: ...

    def getExactSizeIfKnown(self) -> int: ...

    def hasCharacteristics(self, arg0: int) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[str]) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[T]) -> bool: ...

    @overload
    def trySplit(self) -> Spliterator[str]: ...

    @overload
    def trySplit(self) -> Spliterator[T]: ...

  class CodePointsSpliterator:

    def characteristics(self) -> int: ...

    def estimateSize(self) -> int: ...

    @overload
    def forEachRemaining(self, arg0: object) -> None: ...

    @overload
    def forEachRemaining(self, arg0: object) -> None: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[Integer]) -> None: ...

    @overload
    def forEachRemaining(self, arg0: IntConsumer) -> None: ...

    @overload
    def forEachRemaining(self, arg0: IntConsumer) -> None: ...

    @overload
    def tryAdvance(self, arg0: object) -> bool: ...

    @overload
    def tryAdvance(self, arg0: object) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[Integer]) -> bool: ...

    @overload
    def tryAdvance(self, arg0: IntConsumer) -> bool: ...

    @overload
    def tryAdvance(self, arg0: IntConsumer) -> bool: ...

    @overload
    def trySplit(self) -> Spliterator.OfPrimitive: ...

    @overload
    def trySplit(self) -> Spliterator: ...

    @overload
    def trySplit(self) -> Spliterator.OfInt: ...

    @overload
    def trySplit(self) -> Spliterator.OfPrimitive: ...

    @overload
    def trySplit(self) -> Spliterator: ...

    @overload
    def trySplit(self) -> Spliterator.OfInt: ...

  class CharsSpliterator:

    def characteristics(self) -> int: ...

    def estimateSize(self) -> int: ...

    @overload
    def forEachRemaining(self, arg0: object) -> None: ...

    @overload
    def forEachRemaining(self, arg0: object) -> None: ...

    @overload
    def forEachRemaining(self, arg0: Consumer[Integer]) -> None: ...

    @overload
    def forEachRemaining(self, arg0: IntConsumer) -> None: ...

    @overload
    def forEachRemaining(self, arg0: IntConsumer) -> None: ...

    @overload
    def tryAdvance(self, arg0: object) -> bool: ...

    @overload
    def tryAdvance(self, arg0: object) -> bool: ...

    @overload
    def tryAdvance(self, arg0: Consumer[Integer]) -> bool: ...

    @overload
    def tryAdvance(self, arg0: IntConsumer) -> bool: ...

    @overload
    def tryAdvance(self, arg0: IntConsumer) -> bool: ...

    @overload
    def trySplit(self) -> Spliterator.OfPrimitive: ...

    @overload
    def trySplit(self) -> Spliterator: ...

    @overload
    def trySplit(self) -> Spliterator.OfInt: ...

    @overload
    def trySplit(self) -> Spliterator.OfPrimitive: ...

    @overload
    def trySplit(self) -> Spliterator: ...

    @overload
    def trySplit(self) -> Spliterator.OfInt: ...


class System:

  err: PrintStream

  out: PrintStream

  @staticmethod
  def arraycopy(arg0: object, arg1: int, arg2: object, arg3: int, arg4: int) -> None: ...

  @staticmethod
  def clearProperty(arg0: str) -> str: ...

  @staticmethod
  def console() -> Console: ...

  @staticmethod
  def currentTimeMillis() -> int: ...

  @staticmethod
  def exit(arg0: int) -> None: ...

  @staticmethod
  def gc() -> None: ...

  @staticmethod
  @overload
  def getLogger(arg0: str) -> System.Logger: ...

  @staticmethod
  @overload
  def getLogger(arg0: str, arg1: ResourceBundle) -> System.Logger: ...

  @staticmethod
  def getProperties() -> Properties: ...

  @staticmethod
  @overload
  def getProperty(arg0: str) -> str: ...

  @staticmethod
  @overload
  def getProperty(arg0: str, arg1: str) -> str: ...

  @staticmethod
  def getSecurityManager() -> SecurityManager: ...

  @staticmethod
  @overload
  def getenv() -> Map[str, str]: ...

  @staticmethod
  @overload
  def getenv(arg0: str) -> str: ...

  @staticmethod
  def identityHashCode(arg0: object) -> int: ...

  @staticmethod
  def inheritedChannel() -> Channel: ...

  @staticmethod
  def lineSeparator() -> str: ...

  @staticmethod
  def load(arg0: str) -> None: ...

  @staticmethod
  def loadLibrary(arg0: str) -> None: ...

  @staticmethod
  def mapLibraryName(arg0: str) -> str: ...

  @staticmethod
  def nanoTime() -> int: ...

  @staticmethod
  def runFinalization() -> None: ...

  @staticmethod
  def setErr(arg0: PrintStream) -> None: ...

  @staticmethod
  def setIn(arg0: InputStream) -> None: ...

  @staticmethod
  def setOut(arg0: PrintStream) -> None: ...

  @staticmethod
  def setProperties(arg0: Properties) -> None: ...

  @staticmethod
  def setProperty(arg0: str, arg1: str) -> str: ...

  @staticmethod
  def setSecurityManager(arg0: SecurityManager) -> None: ...

  class CallersHolder: ...

  class Logger:

    def getName(self) -> str: ...

    def isLoggable(self, arg0: System.Logger.Level) -> bool: ...

    @overload
    def log(self, arg0: System.Logger.Level, arg1: object) -> None: ...

    @overload
    def log(self, arg0: System.Logger.Level, arg1: str) -> None: ...

    @overload
    def log(self, arg0: System.Logger.Level, arg1: Supplier[str]) -> None: ...

    @overload
    def log(self, arg0: System.Logger.Level, arg1: str, arg2: list[object]) -> None: ...

    @overload
    def log(self, arg0: System.Logger.Level, arg1: str, arg2: Throwable) -> None: ...

    @overload
    def log(self, arg0: System.Logger.Level, arg1: Supplier[str], arg2: Throwable) -> None: ...

    @overload
    def log(self, arg0: System.Logger.Level, arg1: ResourceBundle, arg2: str, arg3: list[object]) -> None: ...

    @overload
    def log(self, arg0: System.Logger.Level, arg1: ResourceBundle, arg2: str, arg3: Throwable) -> None: ...

    class Level(Enum):

      ALL: System.Logger.Level

      DEBUG: System.Logger.Level

      ERROR: System.Logger.Level

      INFO: System.Logger.Level

      OFF: System.Logger.Level

      TRACE: System.Logger.Level

      WARNING: System.Logger.Level

      def getName(self) -> str: ...

      def getSeverity(self) -> int: ...

      @staticmethod
      def valueOf(arg0: str) -> System.Logger.Level: ...

      @staticmethod
      def values() -> list[System.Logger.Level]: ...

  class LoggerFinder:

    def getLocalizedLogger(self, arg0: str, arg1: ResourceBundle, arg2: Module) -> System.Logger: ...

    def getLogger(self, arg0: str, arg1: Module) -> System.Logger: ...

    @staticmethod
    def getLoggerFinder() -> System.LoggerFinder: ...


class Terminator: ...


class Thread:

  MAX_PRIORITY: int

  MIN_PRIORITY: int

  NORM_PRIORITY: int

  def checkAccess(self) -> None: ...

  def countStackFrames(self) -> int: ...

  def getContextClassLoader(self) -> ClassLoader: ...

  def getId(self) -> int: ...

  def getName(self) -> str: ...

  def getPriority(self) -> int: ...

  def getStackTrace(self) -> list[StackTraceElement]: ...

  def getState(self) -> Thread.State: ...

  def getThreadGroup(self) -> ThreadGroup: ...

  def getUncaughtExceptionHandler(self) -> Thread.UncaughtExceptionHandler: ...

  def interrupt(self) -> None: ...

  def isAlive(self) -> bool: ...

  def isDaemon(self) -> bool: ...

  def isInterrupted(self) -> bool: ...

  @overload
  def join(self) -> None: ...

  @overload
  def join(self, arg0: int) -> None: ...

  @overload
  def join(self, arg0: int, arg1: int) -> None: ...

  def resume(self) -> None: ...

  @overload
  def run(self) -> None: ...

  @overload
  def run(self) -> None: ...

  def setContextClassLoader(self, arg0: ClassLoader) -> None: ...

  def setDaemon(self, arg0: bool) -> None: ...

  def setName(self, arg0: str) -> None: ...

  def setPriority(self, arg0: int) -> None: ...

  def setUncaughtExceptionHandler(self, arg0: Thread.UncaughtExceptionHandler) -> None: ...

  def start(self) -> None: ...

  def stop(self) -> None: ...

  def suspend(self) -> None: ...

  def toString(self) -> str: ...

  @staticmethod
  def activeCount() -> int: ...

  @staticmethod
  def currentThread() -> Thread: ...

  @staticmethod
  def dumpStack() -> None: ...

  @staticmethod
  def enumerate(arg0: list[Thread]) -> int: ...

  @staticmethod
  def getAllStackTraces() -> Map[Thread, StackTraceElement]: ...

  @staticmethod
  def getDefaultUncaughtExceptionHandler() -> Thread.UncaughtExceptionHandler: ...

  @staticmethod
  def holdsLock(arg0: object) -> bool: ...

  @staticmethod
  def interrupted() -> bool: ...

  @staticmethod
  def onSpinWait() -> None: ...

  @staticmethod
  def setDefaultUncaughtExceptionHandler(arg0: Thread.UncaughtExceptionHandler) -> None: ...

  @staticmethod
  @overload
  def sleep(arg0: int) -> None: ...

  @staticmethod
  @overload
  def sleep(arg0: int, arg1: int) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: Runnable): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Runnable, arg1: str): ...
  @overload
  def __init__(self, arg0: ThreadGroup, arg1: Runnable): ...
  @overload
  def __init__(self, arg0: ThreadGroup, arg1: str): ...
  @overload
  def __init__(self, arg0: ThreadGroup, arg1: Runnable, arg2: str): ...
  @overload
  def __init__(self, arg0: ThreadGroup, arg1: Runnable, arg2: str, arg3: int): ...
  @overload
  def __init__(self, arg0: ThreadGroup, arg1: Runnable, arg2: str, arg3: int, arg4: bool): ...

  class UncaughtExceptionHandler:

    def uncaughtException(self, arg0: Thread, arg1: Throwable) -> None: ...

  class Caches: ...

  class WeakClassKey(WeakReference):

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

  class State(Enum):

    BLOCKED: Thread.State

    NEW: Thread.State

    RUNNABLE: Thread.State

    TERMINATED: Thread.State

    TIMED_WAITING: Thread.State

    WAITING: Thread.State

    @staticmethod
    def valueOf(arg0: str) -> Thread.State: ...

    @staticmethod
    def values() -> list[Thread.State]: ...


class ThreadDeath(Error):

  def __init__(self): ...


class ThreadGroup:

  def activeCount(self) -> int: ...

  def activeGroupCount(self) -> int: ...

  def allowThreadSuspension(self, arg0: bool) -> bool: ...

  def checkAccess(self) -> None: ...

  def destroy(self) -> None: ...

  @overload
  def enumerate(self, arg0: list[Thread]) -> int: ...

  @overload
  def enumerate(self, arg0: list[ThreadGroup]) -> int: ...

  @overload
  def enumerate(self, arg0: list[Thread], arg1: bool) -> int: ...

  @overload
  def enumerate(self, arg0: list[ThreadGroup], arg1: bool) -> int: ...

  def getMaxPriority(self) -> int: ...

  def getName(self) -> str: ...

  def getParent(self) -> ThreadGroup: ...

  def interrupt(self) -> None: ...

  def isDaemon(self) -> bool: ...

  def isDestroyed(self) -> bool: ...

  def list(self) -> None: ...

  def parentOf(self, arg0: ThreadGroup) -> bool: ...

  def resume(self) -> None: ...

  def setDaemon(self, arg0: bool) -> None: ...

  def setMaxPriority(self, arg0: int) -> None: ...

  def stop(self) -> None: ...

  def suspend(self) -> None: ...

  def toString(self) -> str: ...

  @overload
  def uncaughtException(self, arg0: Thread, arg1: Throwable) -> None: ...

  @overload
  def uncaughtException(self, arg0: Thread, arg1: Throwable) -> None: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: ThreadGroup, arg1: str): ...


class ThreadLocal[T]:

  def get(self) -> object: ...

  def remove(self) -> None: ...

  def set(self, arg0: object) -> None: ...

  @staticmethod
  def withInitial(arg0: Supplier[S]) -> ThreadLocal[S]: ...

  def __init__(self): ...

  class SuppliedThreadLocal[SuppliedThreadLocal_T](ThreadLocal): ...

  class ThreadLocalMap:

    class Entry(WeakReference): ...


class Throwable:

  def addSuppressed(self, arg0: Throwable) -> None: ...

  def fillInStackTrace(self) -> Throwable: ...

  def getCause(self) -> Throwable: ...

  def getLocalizedMessage(self) -> str: ...

  def getMessage(self) -> str: ...

  def getStackTrace(self) -> list[StackTraceElement]: ...

  def getSuppressed(self) -> list[Throwable]: ...

  def initCause(self, arg0: Throwable) -> Throwable: ...

  @overload
  def printStackTrace(self) -> None: ...

  @overload
  def printStackTrace(self, arg0: PrintStream) -> None: ...

  @overload
  def printStackTrace(self, arg0: PrintWriter) -> None: ...

  def setStackTrace(self, arg0: list[StackTraceElement]) -> None: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...

  class WrappedPrintStream(Throwable.PrintStreamOrWriter): ...

  class PrintStreamOrWriter: ...

  class WrappedPrintWriter(Throwable.PrintStreamOrWriter): ...

  class SentinelHolder:

    STACK_TRACE_ELEMENT_SENTINEL: StackTraceElement

    STACK_TRACE_SENTINEL: list[StackTraceElement]


class TypeNotPresentException(RuntimeException):

  def typeName(self) -> str: ...

  def __init__(self, arg0: str, arg1: Throwable): ...


class UnsatisfiedLinkError(LinkageError):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class UnsupportedOperationException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class VersionProps:

  @staticmethod
  def init(arg0: Map[str, str]) -> None: ...

  @staticmethod
  def print(arg0: bool) -> None: ...

  @staticmethod
  def println(arg0: bool) -> None: ...


class VirtualMachineError(Error):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class Void:

  TYPE: Class[Void]


class WeakPairMap[K1, K2, V]:

  def computeIfAbsent(self, arg0: object, arg1: object, arg2: BiFunction[K1, K2, V]) -> object: ...

  def containsKeyPair(self, arg0: object, arg1: object) -> bool: ...

  def get(self, arg0: object, arg1: object) -> object: ...

  def put(self, arg0: object, arg1: object, arg2: object) -> object: ...

  def putIfAbsent(self, arg0: object, arg1: object, arg2: object) -> object: ...

  def values(self) -> Collection[V]: ...

  class Pair[Pair_K1, Pair_K2]:

    def first(self) -> object: ...

    def second(self) -> object: ...

    @staticmethod
    def equals(arg0: object, arg1: object, arg2: WeakPairMap.Pair) -> bool: ...

    @staticmethod
    def hashCode(arg0: object, arg1: object) -> int: ...

    @staticmethod
    def lookup(arg0: object, arg1: object) -> WeakPairMap.Pair: ...

    @staticmethod
    def weak(arg0: object, arg1: object, arg2: ReferenceQueue[object]) -> WeakPairMap.Pair: ...

    class Weak[Weak_K1, Weak_K2](WeakPairMap.WeakRefPeer):

      def equals(self, arg0: object) -> bool: ...

      @overload
      def first(self) -> object: ...

      @overload
      def first(self) -> object: ...

      def hashCode(self) -> int: ...

      @overload
      def second(self) -> object: ...

      @overload
      def second(self) -> object: ...

      @staticmethod
      def lookup(arg0: object, arg1: object) -> WeakPairMap.Pair: ...

      @staticmethod
      def weak(arg0: object, arg1: object, arg2: ReferenceQueue[object]) -> WeakPairMap.Pair: ...

    class Lookup[Lookup_K1, Lookup_K2]:

      def equals(self, arg0: object) -> bool: ...

      @overload
      def first(self) -> object: ...

      @overload
      def first(self) -> object: ...

      def hashCode(self) -> int: ...

      @overload
      def second(self) -> object: ...

      @overload
      def second(self) -> object: ...

      @staticmethod
      def lookup(arg0: object, arg1: object) -> WeakPairMap.Pair: ...

      @staticmethod
      def weak(arg0: object, arg1: object, arg2: ReferenceQueue[object]) -> WeakPairMap.Pair: ...

  class WeakRefPeer[K](WeakReference): ...


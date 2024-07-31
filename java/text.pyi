from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import StringBuffer, Number, Enum, Exception
from java.math import RoundingMode, BigDecimal
from java.util import Set, Map, Locale, Comparator, Date, Calendar, TimeZone, Currency
from java.util.function import Function, ToDoubleFunction, ToIntFunction, ToLongFunction

U = TypeVar('U', default=Any)
T = TypeVar('T', default=Any)

class Annotation:

  def getValue(self) -> object: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: object): ...


class AttributedCharacterIterator:

  DONE: str

  def clone(self) -> object: ...

  def current(self) -> str: ...

  def first(self) -> str: ...

  def getAllAttributeKeys(self) -> Set[AttributedCharacterIterator.Attribute]: ...

  def getAttribute(self, arg0: AttributedCharacterIterator.Attribute) -> object: ...

  def getAttributes(self) -> Map[AttributedCharacterIterator.Attribute, object]: ...

  def getBeginIndex(self) -> int: ...

  def getEndIndex(self) -> int: ...

  def getIndex(self) -> int: ...

  @overload
  def getRunLimit(self) -> int: ...

  @overload
  def getRunLimit(self, arg0: AttributedCharacterIterator.Attribute) -> int: ...

  @overload
  def getRunLimit(self, arg0: Set[AttributedCharacterIterator.Attribute]) -> int: ...

  @overload
  def getRunStart(self) -> int: ...

  @overload
  def getRunStart(self, arg0: AttributedCharacterIterator.Attribute) -> int: ...

  @overload
  def getRunStart(self, arg0: Set[AttributedCharacterIterator.Attribute]) -> int: ...

  def last(self) -> str: ...

  def next(self) -> str: ...

  def previous(self) -> str: ...

  def setIndex(self, arg0: int) -> str: ...

  class Attribute:

    INPUT_METHOD_SEGMENT: AttributedCharacterIterator.Attribute

    LANGUAGE: AttributedCharacterIterator.Attribute

    READING: AttributedCharacterIterator.Attribute

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...


class BreakIterator:

  DONE: int

  def clone(self) -> object: ...

  def current(self) -> int: ...

  def first(self) -> int: ...

  def following(self, arg0: int) -> int: ...

  def getText(self) -> CharacterIterator: ...

  def isBoundary(self, arg0: int) -> bool: ...

  def last(self) -> int: ...

  @overload
  def next(self) -> int: ...

  @overload
  def next(self, arg0: int) -> int: ...

  def preceding(self, arg0: int) -> int: ...

  def previous(self) -> int: ...

  @overload
  def setText(self, arg0: str) -> None: ...

  @overload
  def setText(self, arg0: CharacterIterator) -> None: ...

  @staticmethod
  def getAvailableLocales() -> list[Locale]: ...

  @staticmethod
  @overload
  def getCharacterInstance() -> BreakIterator: ...

  @staticmethod
  @overload
  def getCharacterInstance(arg0: Locale) -> BreakIterator: ...

  @staticmethod
  @overload
  def getLineInstance() -> BreakIterator: ...

  @staticmethod
  @overload
  def getLineInstance(arg0: Locale) -> BreakIterator: ...

  @staticmethod
  @overload
  def getSentenceInstance() -> BreakIterator: ...

  @staticmethod
  @overload
  def getSentenceInstance(arg0: Locale) -> BreakIterator: ...

  @staticmethod
  @overload
  def getWordInstance() -> BreakIterator: ...

  @staticmethod
  @overload
  def getWordInstance(arg0: Locale) -> BreakIterator: ...

  class BreakIteratorCache: ...


class CalendarBuilder:

  ISO_DAY_OF_WEEK: int

  WEEK_YEAR: int

  def toString(self) -> str: ...


class CharacterIterator:

  DONE: str

  def clone(self) -> object: ...

  def current(self) -> str: ...

  def first(self) -> str: ...

  def getBeginIndex(self) -> int: ...

  def getEndIndex(self) -> int: ...

  def getIndex(self) -> int: ...

  def last(self) -> str: ...

  def next(self) -> str: ...

  def previous(self) -> str: ...

  def setIndex(self, arg0: int) -> str: ...


class CollationKey:

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: CollationKey) -> int: ...

  def getSourceString(self) -> str: ...

  def toByteArray(self) -> list[int]: ...


class Collator:

  CANONICAL_DECOMPOSITION: int

  FULL_DECOMPOSITION: int

  IDENTICAL: int

  NO_DECOMPOSITION: int

  PRIMARY: int

  SECONDARY: int

  TERTIARY: int

  def clone(self) -> object: ...

  @overload
  def compare(self, arg0: object, arg1: object) -> int: ...

  @overload
  def compare(self, arg0: object, arg1: object) -> int: ...

  @overload
  def compare(self, arg0: str, arg1: str) -> int: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  @overload
  def equals(self, arg0: str, arg1: str) -> bool: ...

  def getCollationKey(self, arg0: str) -> CollationKey: ...

  def getDecomposition(self) -> int: ...

  def getStrength(self) -> int: ...

  def hashCode(self) -> int: ...

  def reversed(self) -> Comparator[T]: ...

  def setDecomposition(self, arg0: int) -> None: ...

  def setStrength(self, arg0: int) -> None: ...

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
  def getAvailableLocales() -> list[Locale]: ...

  @staticmethod
  @overload
  def getInstance() -> Collator: ...

  @staticmethod
  @overload
  def getInstance(arg0: Locale) -> Collator: ...

  @staticmethod
  def naturalOrder() -> Comparator[T]: ...

  @staticmethod
  def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

  @staticmethod
  def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

  @staticmethod
  def reverseOrder() -> Comparator[T]: ...


class DateFormat(Format):

  AM_PM_FIELD: int

  DATE_FIELD: int

  DAY_OF_WEEK_FIELD: int

  DAY_OF_WEEK_IN_MONTH_FIELD: int

  DAY_OF_YEAR_FIELD: int

  DEFAULT: int

  ERA_FIELD: int

  FULL: int

  HOUR0_FIELD: int

  HOUR1_FIELD: int

  HOUR_OF_DAY0_FIELD: int

  HOUR_OF_DAY1_FIELD: int

  LONG: int

  MEDIUM: int

  MILLISECOND_FIELD: int

  MINUTE_FIELD: int

  MONTH_FIELD: int

  SECOND_FIELD: int

  SHORT: int

  TIMEZONE_FIELD: int

  WEEK_OF_MONTH_FIELD: int

  WEEK_OF_YEAR_FIELD: int

  YEAR_FIELD: int

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def format(self, arg0: Date) -> str: ...

  @overload
  def format(self, arg0: object, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  @overload
  def format(self, arg0: Date, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  def getCalendar(self) -> Calendar: ...

  def getNumberFormat(self) -> NumberFormat: ...

  def getTimeZone(self) -> TimeZone: ...

  def hashCode(self) -> int: ...

  def isLenient(self) -> bool: ...

  @overload
  def parse(self, arg0: str) -> Date: ...

  @overload
  def parse(self, arg0: str, arg1: ParsePosition) -> Date: ...

  def parseObject(self, arg0: str, arg1: ParsePosition) -> object: ...

  def setCalendar(self, arg0: Calendar) -> None: ...

  def setLenient(self, arg0: bool) -> None: ...

  def setNumberFormat(self, arg0: NumberFormat) -> None: ...

  def setTimeZone(self, arg0: TimeZone) -> None: ...

  @staticmethod
  def getAvailableLocales() -> list[Locale]: ...

  @staticmethod
  @overload
  def getDateInstance() -> DateFormat: ...

  @staticmethod
  @overload
  def getDateInstance(arg0: int) -> DateFormat: ...

  @staticmethod
  @overload
  def getDateInstance(arg0: int, arg1: Locale) -> DateFormat: ...

  @staticmethod
  @overload
  def getDateTimeInstance() -> DateFormat: ...

  @staticmethod
  @overload
  def getDateTimeInstance(arg0: int, arg1: int) -> DateFormat: ...

  @staticmethod
  @overload
  def getDateTimeInstance(arg0: int, arg1: int, arg2: Locale) -> DateFormat: ...

  @staticmethod
  def getInstance() -> DateFormat: ...

  @staticmethod
  @overload
  def getTimeInstance() -> DateFormat: ...

  @staticmethod
  @overload
  def getTimeInstance(arg0: int) -> DateFormat: ...

  @staticmethod
  @overload
  def getTimeInstance(arg0: int, arg1: Locale) -> DateFormat: ...

  class Field(Format.Field):

    AM_PM: DateFormat.Field

    DAY_OF_MONTH: DateFormat.Field

    DAY_OF_WEEK: DateFormat.Field

    DAY_OF_WEEK_IN_MONTH: DateFormat.Field

    DAY_OF_YEAR: DateFormat.Field

    ERA: DateFormat.Field

    HOUR0: DateFormat.Field

    HOUR1: DateFormat.Field

    HOUR_OF_DAY0: DateFormat.Field

    HOUR_OF_DAY1: DateFormat.Field

    MILLISECOND: DateFormat.Field

    MINUTE: DateFormat.Field

    MONTH: DateFormat.Field

    SECOND: DateFormat.Field

    TIME_ZONE: DateFormat.Field

    WEEK_OF_MONTH: DateFormat.Field

    WEEK_OF_YEAR: DateFormat.Field

    YEAR: DateFormat.Field

    def getCalendarField(self) -> int: ...

    @staticmethod
    def ofCalendarField(arg0: int) -> DateFormat.Field: ...


class DateFormatSymbols:

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def getAmPmStrings(self) -> list[str]: ...

  def getEras(self) -> list[str]: ...

  def getLocalPatternChars(self) -> str: ...

  def getMonths(self) -> list[str]: ...

  def getShortMonths(self) -> list[str]: ...

  def getShortWeekdays(self) -> list[str]: ...

  def getWeekdays(self) -> list[str]: ...

  def getZoneStrings(self) -> list[list[str]]: ...

  def hashCode(self) -> int: ...

  def setAmPmStrings(self, arg0: list[str]) -> None: ...

  def setEras(self, arg0: list[str]) -> None: ...

  def setLocalPatternChars(self, arg0: str) -> None: ...

  def setMonths(self, arg0: list[str]) -> None: ...

  def setShortMonths(self, arg0: list[str]) -> None: ...

  def setShortWeekdays(self, arg0: list[str]) -> None: ...

  def setWeekdays(self, arg0: list[str]) -> None: ...

  def setZoneStrings(self, arg0: list[list[str]]) -> None: ...

  @staticmethod
  def getAvailableLocales() -> list[Locale]: ...

  @staticmethod
  @overload
  def getInstance() -> DateFormatSymbols: ...

  @staticmethod
  @overload
  def getInstance(arg0: Locale) -> DateFormatSymbols: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: Locale): ...


class DecimalFormat(NumberFormat):

  def applyLocalizedPattern(self, arg0: str) -> None: ...

  def applyPattern(self, arg0: str) -> None: ...

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def format(self, arg0: float, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  @overload
  def format(self, arg0: object, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  @overload
  def format(self, arg0: int, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  def formatToCharacterIterator(self, arg0: object) -> AttributedCharacterIterator: ...

  def getCurrency(self) -> Currency: ...

  def getDecimalFormatSymbols(self) -> DecimalFormatSymbols: ...

  def getGroupingSize(self) -> int: ...

  def getMaximumFractionDigits(self) -> int: ...

  def getMaximumIntegerDigits(self) -> int: ...

  def getMinimumFractionDigits(self) -> int: ...

  def getMinimumIntegerDigits(self) -> int: ...

  def getMultiplier(self) -> int: ...

  def getNegativePrefix(self) -> str: ...

  def getNegativeSuffix(self) -> str: ...

  def getPositivePrefix(self) -> str: ...

  def getPositiveSuffix(self) -> str: ...

  def getRoundingMode(self) -> RoundingMode: ...

  def hashCode(self) -> int: ...

  def isDecimalSeparatorAlwaysShown(self) -> bool: ...

  def isParseBigDecimal(self) -> bool: ...

  def parse(self, arg0: str, arg1: ParsePosition) -> Number: ...

  def setCurrency(self, arg0: Currency) -> None: ...

  def setDecimalFormatSymbols(self, arg0: DecimalFormatSymbols) -> None: ...

  def setDecimalSeparatorAlwaysShown(self, arg0: bool) -> None: ...

  def setGroupingSize(self, arg0: int) -> None: ...

  def setGroupingUsed(self, arg0: bool) -> None: ...

  def setMaximumFractionDigits(self, arg0: int) -> None: ...

  def setMaximumIntegerDigits(self, arg0: int) -> None: ...

  def setMinimumFractionDigits(self, arg0: int) -> None: ...

  def setMinimumIntegerDigits(self, arg0: int) -> None: ...

  def setMultiplier(self, arg0: int) -> None: ...

  def setNegativePrefix(self, arg0: str) -> None: ...

  def setNegativeSuffix(self, arg0: str) -> None: ...

  def setParseBigDecimal(self, arg0: bool) -> None: ...

  def setPositivePrefix(self, arg0: str) -> None: ...

  def setPositiveSuffix(self, arg0: str) -> None: ...

  def setRoundingMode(self, arg0: RoundingMode) -> None: ...

  def toLocalizedPattern(self) -> str: ...

  def toPattern(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: DecimalFormatSymbols): ...

  class FastPathData: ...

  class DigitArrays: ...


class DecimalFormatSymbols:

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def getCurrency(self) -> Currency: ...

  def getCurrencySymbol(self) -> str: ...

  def getDecimalSeparator(self) -> str: ...

  def getDigit(self) -> str: ...

  def getExponentSeparator(self) -> str: ...

  def getGroupingSeparator(self) -> str: ...

  def getInfinity(self) -> str: ...

  def getInternationalCurrencySymbol(self) -> str: ...

  def getMinusSign(self) -> str: ...

  def getMonetaryDecimalSeparator(self) -> str: ...

  def getMonetaryGroupingSeparator(self) -> str: ...

  def getNaN(self) -> str: ...

  def getPatternSeparator(self) -> str: ...

  def getPerMill(self) -> str: ...

  def getPercent(self) -> str: ...

  def getZeroDigit(self) -> str: ...

  def hashCode(self) -> int: ...

  def setCurrency(self, arg0: Currency) -> None: ...

  def setCurrencySymbol(self, arg0: str) -> None: ...

  def setDecimalSeparator(self, arg0: str) -> None: ...

  def setDigit(self, arg0: str) -> None: ...

  def setExponentSeparator(self, arg0: str) -> None: ...

  def setGroupingSeparator(self, arg0: str) -> None: ...

  def setInfinity(self, arg0: str) -> None: ...

  def setInternationalCurrencySymbol(self, arg0: str) -> None: ...

  def setMinusSign(self, arg0: str) -> None: ...

  def setMonetaryDecimalSeparator(self, arg0: str) -> None: ...

  def setMonetaryGroupingSeparator(self, arg0: str) -> None: ...

  def setNaN(self, arg0: str) -> None: ...

  def setPatternSeparator(self, arg0: str) -> None: ...

  def setPerMill(self, arg0: str) -> None: ...

  def setPercent(self, arg0: str) -> None: ...

  def setZeroDigit(self, arg0: str) -> None: ...

  @staticmethod
  def getAvailableLocales() -> list[Locale]: ...

  @staticmethod
  @overload
  def getInstance() -> DecimalFormatSymbols: ...

  @staticmethod
  @overload
  def getInstance(arg0: Locale) -> DecimalFormatSymbols: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: Locale): ...


class DigitList:

  MAX_COUNT: int

  def append(self, arg0: str) -> None: ...

  def clear(self) -> None: ...

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def getBigDecimal(self) -> BigDecimal: ...

  def getDouble(self) -> float: ...

  def getLong(self) -> int: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...


class FieldPosition:

  def equals(self, arg0: object) -> bool: ...

  def getBeginIndex(self) -> int: ...

  def getEndIndex(self) -> int: ...

  def getField(self) -> int: ...

  def getFieldAttribute(self) -> Format.Field: ...

  def hashCode(self) -> int: ...

  def setBeginIndex(self, arg0: int) -> None: ...

  def setEndIndex(self, arg0: int) -> None: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: Format.Field): ...
  @overload
  def __init__(self, arg0: Format.Field, arg1: int): ...

  class Delegate:

    @overload
    def formatted(self, arg0: Format.Field, arg1: object, arg2: int, arg3: int, arg4: StringBuffer) -> None: ...

    @overload
    def formatted(self, arg0: Format.Field, arg1: object, arg2: int, arg3: int, arg4: StringBuffer) -> None: ...

    @overload
    def formatted(self, arg0: int, arg1: Format.Field, arg2: object, arg3: int, arg4: int, arg5: StringBuffer) -> None: ...

    @overload
    def formatted(self, arg0: int, arg1: Format.Field, arg2: object, arg3: int, arg4: int, arg5: StringBuffer) -> None: ...


class Format:

  def clone(self) -> object: ...

  @overload
  def format(self, arg0: object) -> str: ...

  @overload
  def format(self, arg0: object, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  def formatToCharacterIterator(self, arg0: object) -> AttributedCharacterIterator: ...

  @overload
  def parseObject(self, arg0: str) -> object: ...

  @overload
  def parseObject(self, arg0: str, arg1: ParsePosition) -> object: ...

  class FieldDelegate:

    @overload
    def formatted(self, arg0: Format.Field, arg1: object, arg2: int, arg3: int, arg4: StringBuffer) -> None: ...

    @overload
    def formatted(self, arg0: int, arg1: Format.Field, arg2: object, arg3: int, arg4: int, arg5: StringBuffer) -> None: ...

  class Field(AttributedCharacterIterator.Attribute): ...


class NumberFormat(Format):

  FRACTION_FIELD: int

  INTEGER_FIELD: int

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def format(self, arg0: float) -> str: ...

  @overload
  def format(self, arg0: int) -> str: ...

  @overload
  def format(self, arg0: float, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  @overload
  def format(self, arg0: object, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  @overload
  def format(self, arg0: int, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  def getCurrency(self) -> Currency: ...

  def getMaximumFractionDigits(self) -> int: ...

  def getMaximumIntegerDigits(self) -> int: ...

  def getMinimumFractionDigits(self) -> int: ...

  def getMinimumIntegerDigits(self) -> int: ...

  def getRoundingMode(self) -> RoundingMode: ...

  def hashCode(self) -> int: ...

  def isGroupingUsed(self) -> bool: ...

  def isParseIntegerOnly(self) -> bool: ...

  @overload
  def parse(self, arg0: str) -> Number: ...

  @overload
  def parse(self, arg0: str, arg1: ParsePosition) -> Number: ...

  def parseObject(self, arg0: str, arg1: ParsePosition) -> object: ...

  def setCurrency(self, arg0: Currency) -> None: ...

  def setGroupingUsed(self, arg0: bool) -> None: ...

  def setMaximumFractionDigits(self, arg0: int) -> None: ...

  def setMaximumIntegerDigits(self, arg0: int) -> None: ...

  def setMinimumFractionDigits(self, arg0: int) -> None: ...

  def setMinimumIntegerDigits(self, arg0: int) -> None: ...

  def setParseIntegerOnly(self, arg0: bool) -> None: ...

  def setRoundingMode(self, arg0: RoundingMode) -> None: ...

  @staticmethod
  def getAvailableLocales() -> list[Locale]: ...

  @staticmethod
  @overload
  def getCompactNumberInstance() -> NumberFormat: ...

  @staticmethod
  @overload
  def getCompactNumberInstance(arg0: Locale, arg1: NumberFormat.Style) -> NumberFormat: ...

  @staticmethod
  @overload
  def getCurrencyInstance() -> NumberFormat: ...

  @staticmethod
  @overload
  def getCurrencyInstance(arg0: Locale) -> NumberFormat: ...

  @staticmethod
  @overload
  def getInstance() -> NumberFormat: ...

  @staticmethod
  @overload
  def getInstance(arg0: Locale) -> NumberFormat: ...

  @staticmethod
  @overload
  def getIntegerInstance() -> NumberFormat: ...

  @staticmethod
  @overload
  def getIntegerInstance(arg0: Locale) -> NumberFormat: ...

  @staticmethod
  @overload
  def getNumberInstance() -> NumberFormat: ...

  @staticmethod
  @overload
  def getNumberInstance(arg0: Locale) -> NumberFormat: ...

  @staticmethod
  @overload
  def getPercentInstance() -> NumberFormat: ...

  @staticmethod
  @overload
  def getPercentInstance(arg0: Locale) -> NumberFormat: ...

  class Style(Enum):

    LONG: NumberFormat.Style

    SHORT: NumberFormat.Style

    @staticmethod
    def valueOf(arg0: str) -> NumberFormat.Style: ...

    @staticmethod
    def values() -> list[NumberFormat.Style]: ...

  class Field(Format.Field):

    CURRENCY: NumberFormat.Field

    DECIMAL_SEPARATOR: NumberFormat.Field

    EXPONENT: NumberFormat.Field

    EXPONENT_SIGN: NumberFormat.Field

    EXPONENT_SYMBOL: NumberFormat.Field

    FRACTION: NumberFormat.Field

    GROUPING_SEPARATOR: NumberFormat.Field

    INTEGER: NumberFormat.Field

    PERCENT: NumberFormat.Field

    PERMILLE: NumberFormat.Field

    PREFIX: NumberFormat.Field

    SIGN: NumberFormat.Field

    SUFFIX: NumberFormat.Field


class ParseException(Exception):

  def getErrorOffset(self) -> int: ...

  def __init__(self, arg0: str, arg1: int): ...


class ParsePosition:

  def equals(self, arg0: object) -> bool: ...

  def getErrorIndex(self) -> int: ...

  def getIndex(self) -> int: ...

  def hashCode(self) -> int: ...

  def setErrorIndex(self, arg0: int) -> None: ...

  def setIndex(self, arg0: int) -> None: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: int): ...


class SimpleDateFormat(DateFormat):

  def applyLocalizedPattern(self, arg0: str) -> None: ...

  def applyPattern(self, arg0: str) -> None: ...

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def format(self, arg0: Date, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

  def formatToCharacterIterator(self, arg0: object) -> AttributedCharacterIterator: ...

  def get2DigitYearStart(self) -> Date: ...

  def getDateFormatSymbols(self) -> DateFormatSymbols: ...

  def hashCode(self) -> int: ...

  def parse(self, arg0: str, arg1: ParsePosition) -> Date: ...

  def set2DigitYearStart(self, arg0: Date) -> None: ...

  def setDateFormatSymbols(self, arg0: DateFormatSymbols) -> None: ...

  def toLocalizedPattern(self) -> str: ...

  def toPattern(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: DateFormatSymbols): ...
  @overload
  def __init__(self, arg0: str, arg1: Locale): ...


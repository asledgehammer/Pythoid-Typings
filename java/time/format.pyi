from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Appendable, CharSequence, Boolean, StringBuffer, Long, Enum, StringBuilder, Throwable
from java.text import ParsePosition, Format, FieldPosition
from java.time import ZoneId, Period, DateTimeException
from java.time.chrono import Chronology, ChronoLocalDate
from java.time.temporal import TemporalAccessor, TemporalField, TemporalQuery, ValueRange
from java.util import Locale, Set, Map, Iterator

T = TypeVar('T', default=Any)
R = TypeVar('R', default=Any)

class DateTimeFormatter:

  BASIC_ISO_DATE: DateTimeFormatter

  ISO_DATE: DateTimeFormatter

  ISO_DATE_TIME: DateTimeFormatter

  ISO_INSTANT: DateTimeFormatter

  ISO_LOCAL_DATE: DateTimeFormatter

  ISO_LOCAL_DATE_TIME: DateTimeFormatter

  ISO_LOCAL_TIME: DateTimeFormatter

  ISO_OFFSET_DATE: DateTimeFormatter

  ISO_OFFSET_DATE_TIME: DateTimeFormatter

  ISO_OFFSET_TIME: DateTimeFormatter

  ISO_ORDINAL_DATE: DateTimeFormatter

  ISO_TIME: DateTimeFormatter

  ISO_WEEK_DATE: DateTimeFormatter

  ISO_ZONED_DATE_TIME: DateTimeFormatter

  RFC_1123_DATE_TIME: DateTimeFormatter

  def format(self, arg0: TemporalAccessor) -> str: ...

  def formatTo(self, arg0: TemporalAccessor, arg1: Appendable) -> None: ...

  def getChronology(self) -> Chronology: ...

  def getDecimalStyle(self) -> DecimalStyle: ...

  def getLocale(self) -> Locale: ...

  def getResolverFields(self) -> Set[TemporalField]: ...

  def getResolverStyle(self) -> ResolverStyle: ...

  def getZone(self) -> ZoneId: ...

  def localizedBy(self, arg0: Locale) -> DateTimeFormatter: ...

  @overload
  def parse(self, arg0: CharSequence) -> TemporalAccessor: ...

  @overload
  def parse(self, arg0: CharSequence, arg1: ParsePosition) -> TemporalAccessor: ...

  @overload
  def parse(self, arg0: CharSequence, arg1: TemporalQuery[T]) -> object: ...

  def parseBest(self, arg0: CharSequence, arg1: list[TemporalQuery]) -> TemporalAccessor: ...

  def parseUnresolved(self, arg0: CharSequence, arg1: ParsePosition) -> TemporalAccessor: ...

  @overload
  def toFormat(self) -> Format: ...

  @overload
  def toFormat(self, arg0: TemporalQuery[Any]) -> Format: ...

  def toString(self) -> str: ...

  def withChronology(self, arg0: Chronology) -> DateTimeFormatter: ...

  def withDecimalStyle(self, arg0: DecimalStyle) -> DateTimeFormatter: ...

  def withLocale(self, arg0: Locale) -> DateTimeFormatter: ...

  @overload
  def withResolverFields(self, arg0: list[TemporalField]) -> DateTimeFormatter: ...

  @overload
  def withResolverFields(self, arg0: Set[TemporalField]) -> DateTimeFormatter: ...

  def withResolverStyle(self, arg0: ResolverStyle) -> DateTimeFormatter: ...

  def withZone(self, arg0: ZoneId) -> DateTimeFormatter: ...

  @staticmethod
  def ofLocalizedDate(arg0: FormatStyle) -> DateTimeFormatter: ...

  @staticmethod
  @overload
  def ofLocalizedDateTime(arg0: FormatStyle) -> DateTimeFormatter: ...

  @staticmethod
  @overload
  def ofLocalizedDateTime(arg0: FormatStyle, arg1: FormatStyle) -> DateTimeFormatter: ...

  @staticmethod
  def ofLocalizedTime(arg0: FormatStyle) -> DateTimeFormatter: ...

  @staticmethod
  @overload
  def ofPattern(arg0: str) -> DateTimeFormatter: ...

  @staticmethod
  @overload
  def ofPattern(arg0: str, arg1: Locale) -> DateTimeFormatter: ...

  @staticmethod
  def parsedExcessDays() -> TemporalQuery[Period]: ...

  @staticmethod
  def parsedLeapSecond() -> TemporalQuery[Boolean]: ...

  class ClassicFormat(Format):

    def format(self, arg0: object, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...

    @overload
    def parseObject(self, arg0: str) -> object: ...

    @overload
    def parseObject(self, arg0: str, arg1: ParsePosition) -> object: ...

    def __init__(self, arg0: DateTimeFormatter, arg1: TemporalQuery[Any]): ...


class DateTimeFormatterBuilder:

  def append(self, arg0: DateTimeFormatter) -> DateTimeFormatterBuilder: ...

  def appendChronologyId(self) -> DateTimeFormatterBuilder: ...

  def appendChronologyText(self, arg0: TextStyle) -> DateTimeFormatterBuilder: ...

  def appendDayPeriodText(self, arg0: TextStyle) -> DateTimeFormatterBuilder: ...

  def appendFraction(self, arg0: TemporalField, arg1: int, arg2: int, arg3: bool) -> DateTimeFormatterBuilder: ...

  @overload
  def appendGenericZoneText(self, arg0: TextStyle) -> DateTimeFormatterBuilder: ...

  @overload
  def appendGenericZoneText(self, arg0: TextStyle, arg1: Set[ZoneId]) -> DateTimeFormatterBuilder: ...

  @overload
  def appendInstant(self) -> DateTimeFormatterBuilder: ...

  @overload
  def appendInstant(self, arg0: int) -> DateTimeFormatterBuilder: ...

  @overload
  def appendLiteral(self, arg0: str) -> DateTimeFormatterBuilder: ...

  @overload
  def appendLiteral(self, arg0: str) -> DateTimeFormatterBuilder: ...

  def appendLocalized(self, arg0: FormatStyle, arg1: FormatStyle) -> DateTimeFormatterBuilder: ...

  def appendLocalizedOffset(self, arg0: TextStyle) -> DateTimeFormatterBuilder: ...

  def appendOffset(self, arg0: str, arg1: str) -> DateTimeFormatterBuilder: ...

  def appendOffsetId(self) -> DateTimeFormatterBuilder: ...

  def appendOptional(self, arg0: DateTimeFormatter) -> DateTimeFormatterBuilder: ...

  def appendPattern(self, arg0: str) -> DateTimeFormatterBuilder: ...

  @overload
  def appendText(self, arg0: TemporalField) -> DateTimeFormatterBuilder: ...

  @overload
  def appendText(self, arg0: TemporalField, arg1: TextStyle) -> DateTimeFormatterBuilder: ...

  @overload
  def appendText(self, arg0: TemporalField, arg1: Map[Long, str]) -> DateTimeFormatterBuilder: ...

  @overload
  def appendValue(self, arg0: TemporalField) -> DateTimeFormatterBuilder: ...

  @overload
  def appendValue(self, arg0: TemporalField, arg1: int) -> DateTimeFormatterBuilder: ...

  @overload
  def appendValue(self, arg0: TemporalField, arg1: int, arg2: int, arg3: SignStyle) -> DateTimeFormatterBuilder: ...

  @overload
  def appendValueReduced(self, arg0: TemporalField, arg1: int, arg2: int, arg3: int) -> DateTimeFormatterBuilder: ...

  @overload
  def appendValueReduced(self, arg0: TemporalField, arg1: int, arg2: int, arg3: ChronoLocalDate) -> DateTimeFormatterBuilder: ...

  def appendZoneId(self) -> DateTimeFormatterBuilder: ...

  def appendZoneOrOffsetId(self) -> DateTimeFormatterBuilder: ...

  def appendZoneRegionId(self) -> DateTimeFormatterBuilder: ...

  @overload
  def appendZoneText(self, arg0: TextStyle) -> DateTimeFormatterBuilder: ...

  @overload
  def appendZoneText(self, arg0: TextStyle, arg1: Set[ZoneId]) -> DateTimeFormatterBuilder: ...

  def optionalEnd(self) -> DateTimeFormatterBuilder: ...

  def optionalStart(self) -> DateTimeFormatterBuilder: ...

  @overload
  def padNext(self, arg0: int) -> DateTimeFormatterBuilder: ...

  @overload
  def padNext(self, arg0: int, arg1: str) -> DateTimeFormatterBuilder: ...

  def parseCaseInsensitive(self) -> DateTimeFormatterBuilder: ...

  def parseCaseSensitive(self) -> DateTimeFormatterBuilder: ...

  def parseDefaulting(self, arg0: TemporalField, arg1: int) -> DateTimeFormatterBuilder: ...

  def parseLenient(self) -> DateTimeFormatterBuilder: ...

  def parseStrict(self) -> DateTimeFormatterBuilder: ...

  @overload
  def toFormatter(self) -> DateTimeFormatter: ...

  @overload
  def toFormatter(self, arg0: Locale) -> DateTimeFormatter: ...

  @staticmethod
  def getLocalizedDateTimePattern(arg0: FormatStyle, arg1: FormatStyle, arg2: Chronology, arg3: Locale) -> str: ...

  def __init__(self): ...

  class SettingsParser(Enum):

    INSENSITIVE: DateTimeFormatterBuilder.SettingsParser

    LENIENT: DateTimeFormatterBuilder.SettingsParser

    SENSITIVE: DateTimeFormatterBuilder.SettingsParser

    STRICT: DateTimeFormatterBuilder.SettingsParser

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

    @staticmethod
    def valueOf(arg0: str) -> DateTimeFormatterBuilder.SettingsParser: ...

    @staticmethod
    def values() -> list[DateTimeFormatterBuilder.SettingsParser]: ...

  class DateTimePrinterParser:

    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

  class DefaultValueParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

  class NumberPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class ReducedPrinterParser(DateTimeFormatterBuilder.NumberPrinterParser):

    def toString(self) -> str: ...

  class NanosPrinterParser(DateTimeFormatterBuilder.NumberPrinterParser):

    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class FractionPrinterParser(DateTimeFormatterBuilder.NumberPrinterParser):

    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class TextPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class InstantPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class OffsetIdPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class LocalizedOffsetIdPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class ZoneIdPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class ZoneTextPrinterParser(DateTimeFormatterBuilder.ZoneIdPrinterParser):

    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

  class ChronoPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

  class LocalizedPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class CharLiteralPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class StringLiteralPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class DayPeriodPrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class CompositePrinterParser:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

    def withOptional(self, arg0: bool) -> DateTimeFormatterBuilder.CompositePrinterParser: ...

  class WeekBasedFieldPrinterParser(DateTimeFormatterBuilder.NumberPrinterParser):

    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class PadPrinterParserDecorator:

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def format(self, arg0: DateTimePrintContext, arg1: StringBuilder) -> bool: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    @overload
    def parse(self, arg0: DateTimeParseContext, arg1: CharSequence, arg2: int) -> int: ...

    def toString(self) -> str: ...

  class DayPeriod:

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...

  class PrefixTree:

    def add(self, arg0: str, arg1: str, arg2: int) -> bool: ...

    def copyTree(self) -> DateTimeFormatterBuilder.PrefixTree: ...

    @overload
    def match(self, arg0: CharSequence, arg1: ParsePosition) -> DateTimeFormatterBuilder.PrefixTree: ...

    @overload
    def match(self, arg0: CharSequence, arg1: int, arg2: int) -> DateTimeFormatterBuilder.PrefixTree: ...

    @staticmethod
    @overload
    def newTree(arg0: DateTimeParseContext) -> DateTimeFormatterBuilder.PrefixTree: ...

    @staticmethod
    @overload
    def newTree(arg0: Set[str], arg1: DateTimeParseContext) -> DateTimeFormatterBuilder.PrefixTree: ...

    class CI(DateTimeFormatterBuilder.PrefixTree): ...


class DateTimeParseContext:

  def toString(self) -> str: ...


class DateTimeParseException(DateTimeException):

  def getErrorIndex(self) -> int: ...

  def getParsedString(self) -> str: ...

  @overload
  def __init__(self, arg0: str, arg1: CharSequence, arg2: int): ...
  @overload
  def __init__(self, arg0: str, arg1: CharSequence, arg2: int, arg3: Throwable): ...


class DateTimePrintContext:

  def toString(self) -> str: ...


class DateTimeTextProvider:

  @overload
  def getText(self, arg0: TemporalField, arg1: int, arg2: TextStyle, arg3: Locale) -> str: ...

  @overload
  def getText(self, arg0: Chronology, arg1: TemporalField, arg2: int, arg3: TextStyle, arg4: Locale) -> str: ...

  @overload
  def getTextIterator(self, arg0: TemporalField, arg1: TextStyle, arg2: Locale) -> Iterator[Map.Entry[str, Long]]: ...

  @overload
  def getTextIterator(self, arg0: Chronology, arg1: TemporalField, arg2: TextStyle, arg3: Locale) -> Iterator[Map.Entry[str, Long]]: ...

  class LocaleStore: ...


class DecimalStyle:

  STANDARD: DecimalStyle

  def equals(self, arg0: object) -> bool: ...

  def getDecimalSeparator(self) -> str: ...

  def getNegativeSign(self) -> str: ...

  def getPositiveSign(self) -> str: ...

  def getZeroDigit(self) -> str: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  def withDecimalSeparator(self, arg0: str) -> DecimalStyle: ...

  def withNegativeSign(self, arg0: str) -> DecimalStyle: ...

  def withPositiveSign(self, arg0: str) -> DecimalStyle: ...

  def withZeroDigit(self, arg0: str) -> DecimalStyle: ...

  @staticmethod
  def getAvailableLocales() -> Set[Locale]: ...

  @staticmethod
  def of(arg0: Locale) -> DecimalStyle: ...

  @staticmethod
  def ofDefaultLocale() -> DecimalStyle: ...


class FormatStyle(Enum):

  FULL: FormatStyle

  LONG: FormatStyle

  MEDIUM: FormatStyle

  SHORT: FormatStyle

  @staticmethod
  def valueOf(arg0: str) -> FormatStyle: ...

  @staticmethod
  def values() -> list[FormatStyle]: ...


class Parsed:

  def get(self, arg0: TemporalField) -> int: ...

  @overload
  def getLong(self, arg0: TemporalField) -> int: ...

  @overload
  def getLong(self, arg0: TemporalField) -> int: ...

  @overload
  def isSupported(self, arg0: TemporalField) -> bool: ...

  @overload
  def isSupported(self, arg0: TemporalField) -> bool: ...

  @overload
  def query(self, arg0: TemporalQuery[R]) -> object: ...

  @overload
  def query(self, arg0: TemporalQuery[R]) -> object: ...

  def range(self, arg0: TemporalField) -> ValueRange: ...

  def toString(self) -> str: ...


class ResolverStyle(Enum):

  LENIENT: ResolverStyle

  SMART: ResolverStyle

  STRICT: ResolverStyle

  @staticmethod
  def valueOf(arg0: str) -> ResolverStyle: ...

  @staticmethod
  def values() -> list[ResolverStyle]: ...


class SignStyle(Enum):

  ALWAYS: SignStyle

  EXCEEDS_PAD: SignStyle

  NEVER: SignStyle

  NORMAL: SignStyle

  NOT_NEGATIVE: SignStyle

  @staticmethod
  def valueOf(arg0: str) -> SignStyle: ...

  @staticmethod
  def values() -> list[SignStyle]: ...


class TextStyle(Enum):

  FULL: TextStyle

  FULL_STANDALONE: TextStyle

  NARROW: TextStyle

  NARROW_STANDALONE: TextStyle

  SHORT: TextStyle

  SHORT_STANDALONE: TextStyle

  def asNormal(self) -> TextStyle: ...

  def asStandalone(self) -> TextStyle: ...

  def isStandalone(self) -> bool: ...

  @staticmethod
  def valueOf(arg0: str) -> TextStyle: ...

  @staticmethod
  def values() -> list[TextStyle]: ...


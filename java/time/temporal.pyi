from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum, Long
from java.time import Duration
from java.time.format import ResolverStyle
from java.util import Locale, Map, List

R = TypeVar('R', default=Any)

class ChronoField(Enum):

  ALIGNED_DAY_OF_WEEK_IN_MONTH: ChronoField

  ALIGNED_DAY_OF_WEEK_IN_YEAR: ChronoField

  ALIGNED_WEEK_OF_MONTH: ChronoField

  ALIGNED_WEEK_OF_YEAR: ChronoField

  AMPM_OF_DAY: ChronoField

  CLOCK_HOUR_OF_AMPM: ChronoField

  CLOCK_HOUR_OF_DAY: ChronoField

  DAY_OF_MONTH: ChronoField

  DAY_OF_WEEK: ChronoField

  DAY_OF_YEAR: ChronoField

  EPOCH_DAY: ChronoField

  ERA: ChronoField

  HOUR_OF_AMPM: ChronoField

  HOUR_OF_DAY: ChronoField

  INSTANT_SECONDS: ChronoField

  MICRO_OF_DAY: ChronoField

  MICRO_OF_SECOND: ChronoField

  MILLI_OF_DAY: ChronoField

  MILLI_OF_SECOND: ChronoField

  MINUTE_OF_DAY: ChronoField

  MINUTE_OF_HOUR: ChronoField

  MONTH_OF_YEAR: ChronoField

  NANO_OF_DAY: ChronoField

  NANO_OF_SECOND: ChronoField

  OFFSET_SECONDS: ChronoField

  PROLEPTIC_MONTH: ChronoField

  SECOND_OF_DAY: ChronoField

  SECOND_OF_MINUTE: ChronoField

  YEAR: ChronoField

  YEAR_OF_ERA: ChronoField

  @overload
  def adjustInto(self, arg0: R, arg1: int) -> R: ...

  @overload
  def adjustInto(self, arg0: R, arg1: int) -> R: ...

  def checkValidIntValue(self, arg0: int) -> int: ...

  def checkValidValue(self, arg0: int) -> int: ...

  @overload
  def getBaseUnit(self) -> TemporalUnit: ...

  @overload
  def getBaseUnit(self) -> TemporalUnit: ...

  @overload
  def getDisplayName(self, arg0: Locale) -> str: ...

  @overload
  def getDisplayName(self, arg0: Locale) -> str: ...

  @overload
  def getFrom(self, arg0: TemporalAccessor) -> int: ...

  @overload
  def getFrom(self, arg0: TemporalAccessor) -> int: ...

  @overload
  def getRangeUnit(self) -> TemporalUnit: ...

  @overload
  def getRangeUnit(self) -> TemporalUnit: ...

  @overload
  def isDateBased(self) -> bool: ...

  @overload
  def isDateBased(self) -> bool: ...

  @overload
  def isSupportedBy(self, arg0: TemporalAccessor) -> bool: ...

  @overload
  def isSupportedBy(self, arg0: TemporalAccessor) -> bool: ...

  @overload
  def isTimeBased(self) -> bool: ...

  @overload
  def isTimeBased(self) -> bool: ...

  @overload
  def range(self) -> ValueRange: ...

  @overload
  def range(self) -> ValueRange: ...

  @overload
  def rangeRefinedBy(self, arg0: TemporalAccessor) -> ValueRange: ...

  @overload
  def rangeRefinedBy(self, arg0: TemporalAccessor) -> ValueRange: ...

  def resolve(self, arg0: Map[TemporalField, Long], arg1: TemporalAccessor, arg2: ResolverStyle) -> TemporalAccessor: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toString(self) -> str: ...

  @staticmethod
  def valueOf(arg0: str) -> ChronoField: ...

  @staticmethod
  def values() -> list[ChronoField]: ...


class ChronoUnit(Enum):

  CENTURIES: ChronoUnit

  DAYS: ChronoUnit

  DECADES: ChronoUnit

  ERAS: ChronoUnit

  FOREVER: ChronoUnit

  HALF_DAYS: ChronoUnit

  HOURS: ChronoUnit

  MICROS: ChronoUnit

  MILLENNIA: ChronoUnit

  MILLIS: ChronoUnit

  MINUTES: ChronoUnit

  MONTHS: ChronoUnit

  NANOS: ChronoUnit

  SECONDS: ChronoUnit

  WEEKS: ChronoUnit

  YEARS: ChronoUnit

  @overload
  def addTo(self, arg0: R, arg1: int) -> R: ...

  @overload
  def addTo(self, arg0: R, arg1: int) -> R: ...

  @overload
  def between(self, arg0: Temporal, arg1: Temporal) -> int: ...

  @overload
  def between(self, arg0: Temporal, arg1: Temporal) -> int: ...

  @overload
  def getDuration(self) -> Duration: ...

  @overload
  def getDuration(self) -> Duration: ...

  @overload
  def isDateBased(self) -> bool: ...

  @overload
  def isDateBased(self) -> bool: ...

  @overload
  def isDurationEstimated(self) -> bool: ...

  @overload
  def isDurationEstimated(self) -> bool: ...

  @overload
  def isSupportedBy(self, arg0: Temporal) -> bool: ...

  @overload
  def isSupportedBy(self, arg0: Temporal) -> bool: ...

  @overload
  def isTimeBased(self) -> bool: ...

  @overload
  def isTimeBased(self) -> bool: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toString(self) -> str: ...

  @staticmethod
  def valueOf(arg0: str) -> ChronoUnit: ...

  @staticmethod
  def values() -> list[ChronoUnit]: ...


class Temporal:

  def get(self, arg0: TemporalField) -> int: ...

  def getLong(self, arg0: TemporalField) -> int: ...

  @overload
  def isSupported(self, arg0: TemporalField) -> bool: ...

  @overload
  def isSupported(self, arg0: TemporalUnit) -> bool: ...

  @overload
  def minus(self, arg0: TemporalAmount) -> Temporal: ...

  @overload
  def minus(self, arg0: int, arg1: TemporalUnit) -> Temporal: ...

  @overload
  def plus(self, arg0: TemporalAmount) -> Temporal: ...

  @overload
  def plus(self, arg0: int, arg1: TemporalUnit) -> Temporal: ...

  def query(self, arg0: TemporalQuery[R]) -> object: ...

  def range(self, arg0: TemporalField) -> ValueRange: ...

  def until(self, arg0: Temporal, arg1: TemporalUnit) -> int: ...


class TemporalAccessor:

  def get(self, arg0: TemporalField) -> int: ...

  def getLong(self, arg0: TemporalField) -> int: ...

  def isSupported(self, arg0: TemporalField) -> bool: ...

  def query(self, arg0: TemporalQuery[R]) -> object: ...

  def range(self, arg0: TemporalField) -> ValueRange: ...


class TemporalAdjuster:

  def adjustInto(self, arg0: Temporal) -> Temporal: ...


class TemporalAmount:

  def addTo(self, arg0: Temporal) -> Temporal: ...

  def get(self, arg0: TemporalUnit) -> int: ...

  def getUnits(self) -> List[TemporalUnit]: ...

  def subtractFrom(self, arg0: Temporal) -> Temporal: ...


class TemporalField:

  def adjustInto(self, arg0: R, arg1: int) -> R: ...

  def getBaseUnit(self) -> TemporalUnit: ...

  def getDisplayName(self, arg0: Locale) -> str: ...

  def getFrom(self, arg0: TemporalAccessor) -> int: ...

  def getRangeUnit(self) -> TemporalUnit: ...

  def isDateBased(self) -> bool: ...

  def isSupportedBy(self, arg0: TemporalAccessor) -> bool: ...

  def isTimeBased(self) -> bool: ...

  def range(self) -> ValueRange: ...

  def rangeRefinedBy(self, arg0: TemporalAccessor) -> ValueRange: ...

  def resolve(self, arg0: Map[TemporalField, Long], arg1: TemporalAccessor, arg2: ResolverStyle) -> TemporalAccessor: ...

  def toString(self) -> str: ...


class TemporalQuery[R]:

  def queryFrom(self, arg0: TemporalAccessor) -> object: ...


class TemporalUnit:

  def addTo(self, arg0: R, arg1: int) -> R: ...

  def between(self, arg0: Temporal, arg1: Temporal) -> int: ...

  def getDuration(self) -> Duration: ...

  def isDateBased(self) -> bool: ...

  def isDurationEstimated(self) -> bool: ...

  def isSupportedBy(self, arg0: Temporal) -> bool: ...

  def isTimeBased(self) -> bool: ...

  def toString(self) -> str: ...


class ValueRange:

  def checkValidIntValue(self, arg0: int, arg1: TemporalField) -> int: ...

  def checkValidValue(self, arg0: int, arg1: TemporalField) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  def getLargestMinimum(self) -> int: ...

  def getMaximum(self) -> int: ...

  def getMinimum(self) -> int: ...

  def getSmallestMaximum(self) -> int: ...

  def hashCode(self) -> int: ...

  def isFixed(self) -> bool: ...

  def isIntValue(self) -> bool: ...

  def isValidIntValue(self, arg0: int) -> bool: ...

  def isValidValue(self, arg0: int) -> bool: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def of(arg0: int, arg1: int) -> ValueRange: ...

  @staticmethod
  @overload
  def of(arg0: int, arg1: int, arg2: int) -> ValueRange: ...

  @staticmethod
  @overload
  def of(arg0: int, arg1: int, arg2: int, arg3: int) -> ValueRange: ...


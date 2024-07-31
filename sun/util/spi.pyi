from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import TimeZone, Locale, Calendar
from java.util.spi import LocaleServiceProvider

class CalendarProvider(LocaleServiceProvider):

  def getInstance(self, arg0: TimeZone, arg1: Locale) -> Calendar: ...


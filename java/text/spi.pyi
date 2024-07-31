from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.text import BreakIterator, Collator, DateFormat, DateFormatSymbols, DecimalFormatSymbols, NumberFormat
from java.util import Locale
from java.util.spi import LocaleServiceProvider

class BreakIteratorProvider(LocaleServiceProvider):

  def getCharacterInstance(self, arg0: Locale) -> BreakIterator: ...

  def getLineInstance(self, arg0: Locale) -> BreakIterator: ...

  def getSentenceInstance(self, arg0: Locale) -> BreakIterator: ...

  def getWordInstance(self, arg0: Locale) -> BreakIterator: ...


class CollatorProvider(LocaleServiceProvider):

  def getInstance(self, arg0: Locale) -> Collator: ...


class DateFormatProvider(LocaleServiceProvider):

  def getDateInstance(self, arg0: int, arg1: Locale) -> DateFormat: ...

  def getDateTimeInstance(self, arg0: int, arg1: int, arg2: Locale) -> DateFormat: ...

  def getTimeInstance(self, arg0: int, arg1: Locale) -> DateFormat: ...


class DateFormatSymbolsProvider(LocaleServiceProvider):

  def getInstance(self, arg0: Locale) -> DateFormatSymbols: ...


class DecimalFormatSymbolsProvider(LocaleServiceProvider):

  def getInstance(self, arg0: Locale) -> DecimalFormatSymbols: ...


class NumberFormatProvider(LocaleServiceProvider):

  def getCompactNumberInstance(self, arg0: Locale, arg1: NumberFormat.Style) -> NumberFormat: ...

  def getCurrencyInstance(self, arg0: Locale) -> NumberFormat: ...

  def getIntegerInstance(self, arg0: Locale) -> NumberFormat: ...

  def getNumberInstance(self, arg0: Locale) -> NumberFormat: ...

  def getPercentInstance(self, arg0: Locale) -> NumberFormat: ...


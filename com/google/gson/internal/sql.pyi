from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.google.gson import TypeAdapter, TypeAdapterFactory
from com.google.gson.internal.bind import DefaultDateTypeAdapter
from com.google.gson.stream import JsonReader, JsonWriter
from java.sql import Date, Time, Timestamp

class SqlDateTypeAdapter(TypeAdapter):

  @overload
  def read(self, arg0: JsonReader) -> object: ...

  @overload
  def read(self, arg0: JsonReader) -> Date: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: Date) -> None: ...


class SqlTimeTypeAdapter(TypeAdapter):

  @overload
  def read(self, arg0: JsonReader) -> object: ...

  @overload
  def read(self, arg0: JsonReader) -> Time: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: Time) -> None: ...


class SqlTimestampTypeAdapter(TypeAdapter):

  @overload
  def read(self, arg0: JsonReader) -> object: ...

  @overload
  def read(self, arg0: JsonReader) -> Timestamp: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: Timestamp) -> None: ...


class SqlTypesSupport:

  DATE_DATE_TYPE: DefaultDateTypeAdapter.DateType

  DATE_FACTORY: TypeAdapterFactory

  SUPPORTS_SQL_TYPES: bool

  TIME_FACTORY: TypeAdapterFactory

  TIMESTAMP_DATE_TYPE: DefaultDateTypeAdapter.DateType

  TIMESTAMP_FACTORY: TypeAdapterFactory


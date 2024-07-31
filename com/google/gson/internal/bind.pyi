from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.google.gson import TypeAdapter, TypeAdapterFactory, Gson, JsonElement, ToNumberStrategy, FieldNamingStrategy, JsonSerializer, JsonDeserializer
from com.google.gson.internal import ConstructorConstructor, ObjectConstructor, Excluder, LazilyParsedNumber
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader, JsonWriter, JsonToken
from java.lang import Class, Boolean, Number, Character, StringBuffer, StringBuilder
from java.lang.reflect import Type, Field
from java.math import BigDecimal, BigInteger
from java.net import InetAddress, URI, URL
from java.util import Collection, Date, Map, BitSet, Calendar, Currency, Locale, UUID
from java.util.concurrent.atomic import AtomicBoolean, AtomicInteger, AtomicIntegerArray

E = TypeVar('E', default=Any)
T = TypeVar('T', default=Any)
DateType_T = TypeVar('DateType_T', default=Any)
K = TypeVar('K', default=Any)
V = TypeVar('V', default=Any)
R = TypeVar('R', default=Any)
TT = TypeVar('TT', default=Any)
T1 = TypeVar('T1', default=Any)

class ArrayTypeAdapter[E](TypeAdapter):

  FACTORY: TypeAdapterFactory

  def read(self, arg0: JsonReader) -> object: ...

  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  def __init__(self, arg0: Gson, arg1: TypeAdapter[E], arg2: Class[E]): ...


class CollectionTypeAdapterFactory:

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  def __init__(self, arg0: ConstructorConstructor): ...

  class Adapter[E](TypeAdapter):

    @overload
    def read(self, arg0: JsonReader) -> object: ...

    @overload
    def read(self, arg0: JsonReader) -> Collection[E]: ...

    @overload
    def write(self, arg0: JsonWriter, arg1: object) -> None: ...

    @overload
    def write(self, arg0: JsonWriter, arg1: Collection[E]) -> None: ...

    def __init__(self, arg0: Gson, arg1: Type, arg2: TypeAdapter[E], arg3: ObjectConstructor[Collection[E]]): ...


class DateTypeAdapter(TypeAdapter):

  FACTORY: TypeAdapterFactory

  @overload
  def read(self, arg0: JsonReader) -> object: ...

  @overload
  def read(self, arg0: JsonReader) -> Date: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: Date) -> None: ...

  def __init__(self): ...


class DefaultDateTypeAdapter[T](TypeAdapter):

  @overload
  def read(self, arg0: JsonReader) -> object: ...

  @overload
  def read(self, arg0: JsonReader) -> T: ...

  def toString(self) -> str: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: Date) -> None: ...

  class DateType[DateType_T]:

    DATE: DefaultDateTypeAdapter.DateType

    @overload
    def createAdapterFactory(self, arg0: int) -> TypeAdapterFactory: ...

    @overload
    def createAdapterFactory(self, arg0: str) -> TypeAdapterFactory: ...

    @overload
    def createAdapterFactory(self, arg0: int, arg1: int) -> TypeAdapterFactory: ...

    def createDefaultsAdapterFactory(self) -> TypeAdapterFactory: ...


class JsonAdapterAnnotationTypeAdapterFactory:

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  def __init__(self, arg0: ConstructorConstructor): ...


class JsonTreeReader(JsonReader):

  def beginArray(self) -> None: ...

  def beginObject(self) -> None: ...

  def close(self) -> None: ...

  def endArray(self) -> None: ...

  def endObject(self) -> None: ...

  def getPath(self) -> str: ...

  def getPreviousPath(self) -> str: ...

  def hasNext(self) -> bool: ...

  def nextBoolean(self) -> bool: ...

  def nextDouble(self) -> float: ...

  def nextInt(self) -> int: ...

  def nextLong(self) -> int: ...

  def nextName(self) -> str: ...

  def nextNull(self) -> None: ...

  def nextString(self) -> str: ...

  def peek(self) -> JsonToken: ...

  def promoteNameToValue(self) -> None: ...

  def skipValue(self) -> None: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: JsonElement): ...


class JsonTreeWriter(JsonWriter):

  def beginArray(self) -> JsonWriter: ...

  def beginObject(self) -> JsonWriter: ...

  def close(self) -> None: ...

  def endArray(self) -> JsonWriter: ...

  def endObject(self) -> JsonWriter: ...

  def flush(self) -> None: ...

  def get(self) -> JsonElement: ...

  def name(self, arg0: str) -> JsonWriter: ...

  def nullValue(self) -> JsonWriter: ...

  @overload
  def value(self, arg0: bool) -> JsonWriter: ...

  @overload
  def value(self, arg0: float) -> JsonWriter: ...

  @overload
  def value(self, arg0: Boolean) -> JsonWriter: ...

  @overload
  def value(self, arg0: Number) -> JsonWriter: ...

  @overload
  def value(self, arg0: str) -> JsonWriter: ...

  @overload
  def value(self, arg0: int) -> JsonWriter: ...

  def __init__(self): ...


class MapTypeAdapterFactory:

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  def __init__(self, arg0: ConstructorConstructor, arg1: bool): ...

  class Adapter[K, V](TypeAdapter):

    @overload
    def read(self, arg0: JsonReader) -> Map[K, V]: ...

    @overload
    def read(self, arg0: JsonReader) -> object: ...

    @overload
    def write(self, arg0: JsonWriter, arg1: object) -> None: ...

    @overload
    def write(self, arg0: JsonWriter, arg1: Map[K, V]) -> None: ...

    def __init__(self, arg0: MapTypeAdapterFactory, arg1: Gson, arg2: Type, arg3: TypeAdapter, arg4: Type, arg5: TypeAdapter, arg6: ObjectConstructor): ...


class NumberTypeAdapter(TypeAdapter):

  @overload
  def read(self, arg0: JsonReader) -> Number: ...

  @overload
  def read(self, arg0: JsonReader) -> object: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: Number) -> None: ...

  @overload
  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  @staticmethod
  def getFactory(arg0: ToNumberStrategy) -> TypeAdapterFactory: ...


class ObjectTypeAdapter(TypeAdapter):

  def read(self, arg0: JsonReader) -> object: ...

  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  @staticmethod
  def getFactory(arg0: ToNumberStrategy) -> TypeAdapterFactory: ...


class ReflectiveTypeAdapterFactory:

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  @overload
  def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

  def excludeField(self, arg0: Field, arg1: bool) -> bool: ...

  def __init__(self, arg0: ConstructorConstructor, arg1: FieldNamingStrategy, arg2: Excluder, arg3: JsonAdapterAnnotationTypeAdapterFactory): ...

  class Adapter[T](TypeAdapter):

    def read(self, arg0: JsonReader) -> object: ...

    def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  class BoundField: ...


class TreeTypeAdapter[T](TypeAdapter):

  def read(self, arg0: JsonReader) -> object: ...

  def write(self, arg0: JsonWriter, arg1: object) -> None: ...

  @staticmethod
  def newFactory(arg0: TypeToken[Any], arg1: object) -> TypeAdapterFactory: ...

  @staticmethod
  def newFactoryWithMatchRawType(arg0: TypeToken[Any], arg1: object) -> TypeAdapterFactory: ...

  @staticmethod
  def newTypeHierarchyFactory(arg0: Class[Any], arg1: object) -> TypeAdapterFactory: ...

  def __init__(self, arg0: JsonSerializer[T], arg1: JsonDeserializer[T], arg2: Gson, arg3: TypeToken[T], arg4: TypeAdapterFactory): ...

  class GsonContextImpl:

    @overload
    def deserialize(self, arg0: JsonElement, arg1: Type) -> object: ...

    @overload
    def deserialize(self, arg0: JsonElement, arg1: Type) -> object: ...

    @overload
    def serialize(self, arg0: object) -> JsonElement: ...

    @overload
    def serialize(self, arg0: object) -> JsonElement: ...

    @overload
    def serialize(self, arg0: object, arg1: Type) -> JsonElement: ...

    @overload
    def serialize(self, arg0: object, arg1: Type) -> JsonElement: ...

  class SingleTypeFactory:

    @overload
    def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...

    @overload
    def create(self, arg0: Gson, arg1: TypeToken[T]) -> TypeAdapter[T]: ...


class TypeAdapterRuntimeTypeWrapper[T](TypeAdapter):

  def read(self, arg0: JsonReader) -> object: ...

  def write(self, arg0: JsonWriter, arg1: object) -> None: ...


class TypeAdapters:

  ATOMIC_BOOLEAN: TypeAdapter[AtomicBoolean]

  ATOMIC_BOOLEAN_FACTORY: TypeAdapterFactory

  ATOMIC_INTEGER: TypeAdapter[AtomicInteger]

  ATOMIC_INTEGER_ARRAY: TypeAdapter[AtomicIntegerArray]

  ATOMIC_INTEGER_ARRAY_FACTORY: TypeAdapterFactory

  ATOMIC_INTEGER_FACTORY: TypeAdapterFactory

  BIG_DECIMAL: TypeAdapter[BigDecimal]

  BIG_INTEGER: TypeAdapter[BigInteger]

  BIT_SET: TypeAdapter[BitSet]

  BIT_SET_FACTORY: TypeAdapterFactory

  BOOLEAN: TypeAdapter[Boolean]

  BOOLEAN_AS_STRING: TypeAdapter[Boolean]

  BOOLEAN_FACTORY: TypeAdapterFactory

  BYTE: TypeAdapter[Number]

  BYTE_FACTORY: TypeAdapterFactory

  CALENDAR: TypeAdapter[Calendar]

  CALENDAR_FACTORY: TypeAdapterFactory

  CHARACTER: TypeAdapter[str]

  CHARACTER_FACTORY: TypeAdapterFactory

  CLASS_FACTORY: TypeAdapterFactory

  CURRENCY: TypeAdapter[Currency]

  CURRENCY_FACTORY: TypeAdapterFactory

  DOUBLE: TypeAdapter[Number]

  ENUM_FACTORY: TypeAdapterFactory

  FLOAT: TypeAdapter[Number]

  INET_ADDRESS: TypeAdapter[InetAddress]

  INET_ADDRESS_FACTORY: TypeAdapterFactory

  INTEGER: TypeAdapter[Number]

  INTEGER_FACTORY: TypeAdapterFactory

  JSON_ELEMENT: TypeAdapter[JsonElement]

  JSON_ELEMENT_FACTORY: TypeAdapterFactory

  LAZILY_PARSED_NUMBER: TypeAdapter[LazilyParsedNumber]

  LOCALE: TypeAdapter[Locale]

  LOCALE_FACTORY: TypeAdapterFactory

  LONG: TypeAdapter[Number]

  SHORT: TypeAdapter[Number]

  SHORT_FACTORY: TypeAdapterFactory

  STRING: TypeAdapter[str]

  STRING_BUFFER: TypeAdapter[StringBuffer]

  STRING_BUFFER_FACTORY: TypeAdapterFactory

  STRING_BUILDER: TypeAdapter[StringBuilder]

  STRING_BUILDER_FACTORY: TypeAdapterFactory

  STRING_FACTORY: TypeAdapterFactory

  URI: TypeAdapter[URI]

  URI_FACTORY: TypeAdapterFactory

  URL: TypeAdapter[URL]

  URL_FACTORY: TypeAdapterFactory

  UUID: TypeAdapter[UUID]

  UUID_FACTORY: TypeAdapterFactory

  @staticmethod
  @overload
  def newFactory(arg0: TypeToken[TT], arg1: TypeAdapter[TT]) -> TypeAdapterFactory: ...

  @staticmethod
  @overload
  def newFactory(arg0: Class[TT], arg1: TypeAdapter[TT]) -> TypeAdapterFactory: ...

  @staticmethod
  @overload
  def newFactory(arg0: Class[TT], arg1: Class[TT], arg2: TypeAdapter[TT]) -> TypeAdapterFactory: ...

  @staticmethod
  def newFactoryForMultipleTypes(arg0: Class[TT], arg1: Class[TT], arg2: TypeAdapter[TT]) -> TypeAdapterFactory: ...

  @staticmethod
  def newTypeHierarchyFactory(arg0: Class[T1], arg1: TypeAdapter[T1]) -> TypeAdapterFactory: ...

  class EnumTypeAdapter[T](TypeAdapter):

    @overload
    def read(self, arg0: JsonReader) -> object: ...

    @overload
    def read(self, arg0: JsonReader) -> T: ...

    @overload
    def write(self, arg0: JsonWriter, arg1: T) -> None: ...

    @overload
    def write(self, arg0: JsonWriter, arg1: object) -> None: ...

    def __init__(self, arg0: Class[T]): ...


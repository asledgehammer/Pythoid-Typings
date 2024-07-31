from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class
from se.krka.kahlua.vm import Platform, KahluaTable

JavaType = TypeVar('JavaType', default=Any)
T = TypeVar('T', default=Any)
LuaType = TypeVar('LuaType', default=Any)

class JavaToLuaConverter[JavaType]:

  def fromJavaToLua(self, arg0: object) -> object: ...

  def getJavaType(self) -> Class[JavaType]: ...


class KahluaConverterManager:

  def addJavaConverter(self, arg0: JavaToLuaConverter) -> None: ...

  def addLuaConverter(self, arg0: LuaToJavaConverter) -> None: ...

  def fromJavaToLua(self, arg0: object) -> object: ...

  def fromLuaToJava(self, arg0: object, arg1: Class[T]) -> object: ...

  def __init__(self): ...


class KahluaEnumConverter:

  @staticmethod
  def install(arg0: KahluaConverterManager) -> None: ...


class KahluaNumberConverter:

  @staticmethod
  def install(arg0: KahluaConverterManager) -> None: ...

  class NumberToLuaConverter[T]:

    @overload
    def fromJavaToLua(self, arg0: T) -> object: ...

    @overload
    def fromJavaToLua(self, arg0: object) -> object: ...

    @overload
    def fromJavaToLua(self, arg0: object) -> object: ...

    @overload
    def getJavaType(self) -> Class[T]: ...

    @overload
    def getJavaType(self) -> Class[JavaType]: ...

    def __init__(self, arg0: Class[T]): ...


class KahluaTableConverter:

  def install(self, arg0: KahluaConverterManager) -> None: ...

  def __init__(self, arg0: Platform): ...

  class CollectionToLuaConverter[T]:

    @overload
    def fromJavaToLua(self, arg0: T) -> object: ...

    @overload
    def fromJavaToLua(self, arg0: object) -> object: ...

    @overload
    def fromJavaToLua(self, arg0: object) -> object: ...

    @overload
    def getJavaType(self) -> Class[T]: ...

    @overload
    def getJavaType(self) -> Class[JavaType]: ...

    def __init__(self, arg0: KahluaTableConverter, arg1: KahluaConverterManager, arg2: Class): ...

  class CollectionToJavaConverter[T]:

    @overload
    def fromLuaToJava(self, arg0: object, arg1: Class) -> object: ...

    @overload
    def fromLuaToJava(self, arg0: object, arg1: Class[JavaType]) -> object: ...

    @overload
    def fromLuaToJava(self, arg0: KahluaTable, arg1: Class[T]) -> object: ...

    @overload
    def getJavaType(self) -> Class[T]: ...

    @overload
    def getJavaType(self) -> Class[JavaType]: ...

    @overload
    def getLuaType(self) -> Class[KahluaTable]: ...

    @overload
    def getLuaType(self) -> Class[LuaType]: ...


class LuaToJavaConverter[LuaType, JavaType]:

  def fromLuaToJava(self, arg0: object, arg1: Class[JavaType]) -> object: ...

  def getJavaType(self) -> Class[JavaType]: ...

  def getLuaType(self) -> Class[LuaType]: ...


class MultiJavaToLuaConverter[JavaType]:

  def add(self, arg0: JavaToLuaConverter) -> None: ...

  @overload
  def fromJavaToLua(self, arg0: object) -> object: ...

  @overload
  def fromJavaToLua(self, arg0: object) -> object: ...

  @overload
  def getJavaType(self) -> Class[JavaType]: ...

  @overload
  def getJavaType(self) -> Class[JavaType]: ...

  def __init__(self, arg0: Class[JavaType]): ...


class MultiLuaToJavaConverter[LuaType, JavaType]:

  def add(self, arg0: LuaToJavaConverter[LuaType, JavaType]) -> None: ...

  @overload
  def fromLuaToJava(self, arg0: object, arg1: Class[JavaType]) -> object: ...

  @overload
  def fromLuaToJava(self, arg0: object, arg1: Class[JavaType]) -> object: ...

  @overload
  def getJavaType(self) -> Class[JavaType]: ...

  @overload
  def getJavaType(self) -> Class[JavaType]: ...

  @overload
  def getLuaType(self) -> Class[LuaType]: ...

  @overload
  def getLuaType(self) -> Class[LuaType]: ...

  def __init__(self, arg0: Class[LuaType], arg1: Class[JavaType]): ...


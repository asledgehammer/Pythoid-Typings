from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class, ClassLoader, Module
from java.lang.instrument import ClassFileTransformer, ClassDefinition
from java.security import ProtectionDomain
from java.util import Set, Map, List
from java.util.jar import JarFile

class InstrumentationImpl:

  @overload
  def addTransformer(self, arg0: ClassFileTransformer) -> None: ...

  @overload
  def addTransformer(self, arg0: ClassFileTransformer) -> None: ...

  @overload
  def addTransformer(self, arg0: ClassFileTransformer, arg1: bool) -> None: ...

  @overload
  def addTransformer(self, arg0: ClassFileTransformer, arg1: bool) -> None: ...

  @overload
  def appendToBootstrapClassLoaderSearch(self, arg0: JarFile) -> None: ...

  @overload
  def appendToBootstrapClassLoaderSearch(self, arg0: JarFile) -> None: ...

  @overload
  def appendToSystemClassLoaderSearch(self, arg0: JarFile) -> None: ...

  @overload
  def appendToSystemClassLoaderSearch(self, arg0: JarFile) -> None: ...

  @overload
  def getAllLoadedClasses(self) -> list[Class]: ...

  @overload
  def getAllLoadedClasses(self) -> list[Class]: ...

  @overload
  def getInitiatedClasses(self, arg0: ClassLoader) -> list[Class]: ...

  @overload
  def getInitiatedClasses(self, arg0: ClassLoader) -> list[Class]: ...

  @overload
  def getObjectSize(self, arg0: object) -> int: ...

  @overload
  def getObjectSize(self, arg0: object) -> int: ...

  @overload
  def isModifiableClass(self, arg0: Class[Any]) -> bool: ...

  @overload
  def isModifiableClass(self, arg0: Class[Any]) -> bool: ...

  @overload
  def isModifiableModule(self, arg0: Module) -> bool: ...

  @overload
  def isModifiableModule(self, arg0: Module) -> bool: ...

  @overload
  def isNativeMethodPrefixSupported(self) -> bool: ...

  @overload
  def isNativeMethodPrefixSupported(self) -> bool: ...

  @overload
  def isRedefineClassesSupported(self) -> bool: ...

  @overload
  def isRedefineClassesSupported(self) -> bool: ...

  @overload
  def isRetransformClassesSupported(self) -> bool: ...

  @overload
  def isRetransformClassesSupported(self) -> bool: ...

  @overload
  def redefineClasses(self, arg0: list[ClassDefinition]) -> None: ...

  @overload
  def redefineClasses(self, arg0: list[ClassDefinition]) -> None: ...

  @overload
  def redefineModule(self, arg0: Module, arg1: Set[Module], arg2: Map[str, Set[Module]], arg3: Map[str, Set[Module]], arg4: Set[Class[Any]], arg5: Map[Class[Any], List[Class[Any]]]) -> None: ...

  @overload
  def redefineModule(self, arg0: Module, arg1: Set[Module], arg2: Map[str, Set[Module]], arg3: Map[str, Set[Module]], arg4: Set[Class[Any]], arg5: Map[Class[Any], List[Class[Any]]]) -> None: ...

  @overload
  def removeTransformer(self, arg0: ClassFileTransformer) -> bool: ...

  @overload
  def removeTransformer(self, arg0: ClassFileTransformer) -> bool: ...

  @overload
  def retransformClasses(self, arg0: list[Class]) -> None: ...

  @overload
  def retransformClasses(self, arg0: list[Class]) -> None: ...

  @overload
  def setNativeMethodPrefix(self, arg0: ClassFileTransformer, arg1: str) -> None: ...

  @overload
  def setNativeMethodPrefix(self, arg0: ClassFileTransformer, arg1: str) -> None: ...

  @staticmethod
  def loadAgent(arg0: str) -> None: ...


class TransformerManager:

  def addTransformer(self, arg0: ClassFileTransformer) -> None: ...

  def removeTransformer(self, arg0: ClassFileTransformer) -> bool: ...

  def transform(self, arg0: Module, arg1: ClassLoader, arg2: str, arg3: Class[Any], arg4: ProtectionDomain, arg5: list[int]) -> list[int]: ...

  class TransformerInfo: ...


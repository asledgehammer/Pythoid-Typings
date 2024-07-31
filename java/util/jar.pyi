from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import InputStream, File, OutputStream, FilterInputStream
from java.lang import Runtime
from java.net import URL
from java.security import CodeSigner, CodeSource
from java.security.cert import Certificate
from java.util import Set, Map, Collection, Enumeration, List
from java.util.function import BiFunction, Function, BiConsumer
from java.util.stream import Stream
from java.util.zip import ZipEntry, ZipException, ZipFile
from sun.security.util import ManifestEntryVerifier

K = TypeVar('K', default=Any)
V = TypeVar('V', default=Any)

class Attributes:

  @overload
  def clear(self) -> None: ...

  @overload
  def clear(self) -> None: ...

  def clone(self) -> object: ...

  def compute(self, arg0: object, arg1: BiFunction[K, V, V]) -> object: ...

  def computeIfAbsent(self, arg0: object, arg1: Function[K, V]) -> object: ...

  def computeIfPresent(self, arg0: object, arg1: BiFunction[K, V, V]) -> object: ...

  @overload
  def containsKey(self, arg0: object) -> bool: ...

  @overload
  def containsKey(self, arg0: object) -> bool: ...

  @overload
  def containsValue(self, arg0: object) -> bool: ...

  @overload
  def containsValue(self, arg0: object) -> bool: ...

  @overload
  def entrySet(self) -> Set[Map.Entry[object, object]]: ...

  @overload
  def entrySet(self) -> Set[Map.Entry[K, V]]: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  def forEach(self, arg0: BiConsumer[K, V]) -> None: ...

  @overload
  def get(self, arg0: object) -> object: ...

  @overload
  def get(self, arg0: object) -> object: ...

  def getOrDefault(self, arg0: object, arg1: object) -> object: ...

  @overload
  def getValue(self, arg0: str) -> str: ...

  @overload
  def getValue(self, arg0: Attributes.Name) -> str: ...

  @overload
  def hashCode(self) -> int: ...

  @overload
  def hashCode(self) -> int: ...

  @overload
  def isEmpty(self) -> bool: ...

  @overload
  def isEmpty(self) -> bool: ...

  @overload
  def keySet(self) -> Set[object]: ...

  @overload
  def keySet(self) -> Set[K]: ...

  def merge(self, arg0: object, arg1: object, arg2: BiFunction[V, V, V]) -> object: ...

  @overload
  def put(self, arg0: object, arg1: object) -> object: ...

  @overload
  def put(self, arg0: object, arg1: object) -> object: ...

  @overload
  def putAll(self, arg0: Map[Any, Any]) -> None: ...

  @overload
  def putAll(self, arg0: Map[K, V]) -> None: ...

  def putIfAbsent(self, arg0: object, arg1: object) -> object: ...

  def putValue(self, arg0: str, arg1: str) -> str: ...

  @overload
  def remove(self, arg0: object) -> object: ...

  @overload
  def remove(self, arg0: object) -> object: ...

  @overload
  def remove(self, arg0: object, arg1: object) -> bool: ...

  @overload
  def replace(self, arg0: object, arg1: object) -> object: ...

  @overload
  def replace(self, arg0: object, arg1: object, arg2: object) -> bool: ...

  def replaceAll(self, arg0: BiFunction[K, V, V]) -> None: ...

  @overload
  def size(self) -> int: ...

  @overload
  def size(self) -> int: ...

  @overload
  def values(self) -> Collection[object]: ...

  @overload
  def values(self) -> Collection[V]: ...

  @staticmethod
  def copyOf(arg0: Map[K, V]) -> Map[K, V]: ...

  @staticmethod
  def entry(arg0: object, arg1: object) -> Map.Entry: ...

  @staticmethod
  @overload
  def of() -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object, arg9: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object, arg9: object, arg10: object, arg11: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object, arg9: object, arg10: object, arg11: object, arg12: object, arg13: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object, arg9: object, arg10: object, arg11: object, arg12: object, arg13: object, arg14: object, arg15: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object, arg9: object, arg10: object, arg11: object, arg12: object, arg13: object, arg14: object, arg15: object, arg16: object, arg17: object) -> Map[K, V]: ...

  @staticmethod
  @overload
  def of(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object, arg9: object, arg10: object, arg11: object, arg12: object, arg13: object, arg14: object, arg15: object, arg16: object, arg17: object, arg18: object, arg19: object) -> Map[K, V]: ...

  @staticmethod
  def ofEntries(arg0: list[Map.Entry]) -> Map[K, V]: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: Attributes): ...

  class Name:

    CLASS_PATH: Attributes.Name

    CONTENT_TYPE: Attributes.Name

    EXTENSION_INSTALLATION: Attributes.Name

    EXTENSION_LIST: Attributes.Name

    EXTENSION_NAME: Attributes.Name

    IMPLEMENTATION_TITLE: Attributes.Name

    IMPLEMENTATION_URL: Attributes.Name

    IMPLEMENTATION_VENDOR: Attributes.Name

    IMPLEMENTATION_VENDOR_ID: Attributes.Name

    IMPLEMENTATION_VERSION: Attributes.Name

    MAIN_CLASS: Attributes.Name

    MANIFEST_VERSION: Attributes.Name

    MULTI_RELEASE: Attributes.Name

    SEALED: Attributes.Name

    SIGNATURE_VERSION: Attributes.Name

    SPECIFICATION_TITLE: Attributes.Name

    SPECIFICATION_VENDOR: Attributes.Name

    SPECIFICATION_VERSION: Attributes.Name

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...

    def __init__(self, arg0: str): ...


class JarEntry(ZipEntry):

  def getAttributes(self) -> Attributes: ...

  def getCertificates(self) -> list[Certificate]: ...

  def getCodeSigners(self) -> list[CodeSigner]: ...

  def getRealName(self) -> str: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: JarEntry): ...
  @overload
  def __init__(self, arg0: ZipEntry): ...


class JarException(ZipException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class JarFile(ZipFile):

  MANIFEST_NAME: str

  def entries(self) -> Enumeration[JarEntry]: ...

  def getEntry(self, arg0: str) -> ZipEntry: ...

  def getInputStream(self, arg0: ZipEntry) -> InputStream: ...

  def getJarEntry(self, arg0: str) -> JarEntry: ...

  def getManifest(self) -> Manifest: ...

  def getVersion(self) -> Runtime.Version: ...

  def isMultiRelease(self) -> bool: ...

  def stream(self) -> Stream[JarEntry]: ...

  def versionedStream(self) -> Stream[JarEntry]: ...

  @staticmethod
  def baseVersion() -> Runtime.Version: ...

  @staticmethod
  def runtimeVersion() -> Runtime.Version: ...

  @overload
  def __init__(self, arg0: File): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: File, arg1: bool): ...
  @overload
  def __init__(self, arg0: str, arg1: bool): ...
  @overload
  def __init__(self, arg0: File, arg1: bool, arg2: int): ...
  @overload
  def __init__(self, arg0: File, arg1: bool, arg2: int, arg3: Runtime.Version): ...

  class JarFileEntry(JarEntry):

    def getAttributes(self) -> Attributes: ...

    def getCertificates(self) -> list[Certificate]: ...

    def getCodeSigners(self) -> list[CodeSigner]: ...

    def getName(self) -> str: ...

    def getRealName(self) -> str: ...


class JarVerifier:

  def beginEntry(self, arg0: JarEntry, arg1: ManifestEntryVerifier) -> None: ...

  def entries2(self, arg0: JarFile, arg1: Enumeration[JarEntry]) -> Enumeration[JarEntry]: ...

  def entryNames(self, arg0: JarFile, arg1: list[CodeSource]) -> Enumeration[str]: ...

  @overload
  def getCerts(self, arg0: str) -> list[Certificate]: ...

  @overload
  def getCerts(self, arg0: JarFile, arg1: JarEntry) -> list[Certificate]: ...

  @overload
  def getCodeSigners(self, arg0: str) -> list[CodeSigner]: ...

  @overload
  def getCodeSigners(self, arg0: JarFile, arg1: JarEntry) -> list[CodeSigner]: ...

  @overload
  def getCodeSource(self, arg0: URL, arg1: str) -> CodeSource: ...

  @overload
  def getCodeSource(self, arg0: URL, arg1: JarFile, arg2: JarEntry) -> CodeSource: ...

  def getCodeSources(self, arg0: JarFile, arg1: URL) -> list[CodeSource]: ...

  def getManifestDigests(self) -> List[object]: ...

  def setEagerValidation(self, arg0: bool) -> None: ...

  @overload
  def update(self, arg0: int, arg1: ManifestEntryVerifier) -> None: ...

  @overload
  def update(self, arg0: int, arg1: list[int], arg2: int, arg3: int, arg4: ManifestEntryVerifier) -> None: ...

  def __init__(self, arg0: str, arg1: list[int]): ...

  class VerifierCodeSource(CodeSource):

    def equals(self, arg0: object) -> bool: ...

  class VerifierStream(InputStream):

    def available(self) -> int: ...

    def close(self) -> None: ...

    @overload
    def read(self) -> int: ...

    @overload
    def read(self, arg0: list[int], arg1: int, arg2: int) -> int: ...


class JavaUtilJarAccessImpl:

  @overload
  def ensureInitialization(self, arg0: JarFile) -> None: ...

  @overload
  def ensureInitialization(self, arg0: JarFile) -> None: ...

  @overload
  def entries2(self, arg0: JarFile) -> Enumeration[JarEntry]: ...

  @overload
  def entries2(self, arg0: JarFile) -> Enumeration[JarEntry]: ...

  @overload
  def entryFor(self, arg0: JarFile, arg1: str) -> JarEntry: ...

  @overload
  def entryFor(self, arg0: JarFile, arg1: str) -> JarEntry: ...

  @overload
  def entryNames(self, arg0: JarFile, arg1: list[CodeSource]) -> Enumeration[str]: ...

  @overload
  def entryNames(self, arg0: JarFile, arg1: list[CodeSource]) -> Enumeration[str]: ...

  @overload
  def getCodeSource(self, arg0: JarFile, arg1: URL, arg2: str) -> CodeSource: ...

  @overload
  def getCodeSource(self, arg0: JarFile, arg1: URL, arg2: str) -> CodeSource: ...

  @overload
  def getCodeSources(self, arg0: JarFile, arg1: URL) -> list[CodeSource]: ...

  @overload
  def getCodeSources(self, arg0: JarFile, arg1: URL) -> list[CodeSource]: ...

  @overload
  def getManifestDigests(self, arg0: JarFile) -> List[object]: ...

  @overload
  def getManifestDigests(self, arg0: JarFile) -> List[object]: ...

  @overload
  def getTrustedAttributes(self, arg0: Manifest, arg1: str) -> Attributes: ...

  @overload
  def getTrustedAttributes(self, arg0: Manifest, arg1: str) -> Attributes: ...

  @overload
  def isInitializing(self) -> bool: ...

  @overload
  def isInitializing(self) -> bool: ...

  @overload
  def jarFileHasClassPathAttribute(self, arg0: JarFile) -> bool: ...

  @overload
  def jarFileHasClassPathAttribute(self, arg0: JarFile) -> bool: ...

  @overload
  def setEagerValidation(self, arg0: JarFile, arg1: bool) -> None: ...

  @overload
  def setEagerValidation(self, arg0: JarFile, arg1: bool) -> None: ...


class Manifest:

  def clear(self) -> None: ...

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def getAttributes(self, arg0: str) -> Attributes: ...

  def getEntries(self) -> Map[str, Attributes]: ...

  def getMainAttributes(self) -> Attributes: ...

  def hashCode(self) -> int: ...

  def read(self, arg0: InputStream) -> None: ...

  def write(self, arg0: OutputStream) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: InputStream): ...
  @overload
  def __init__(self, arg0: Manifest): ...

  class FastInputStream(FilterInputStream):

    def available(self) -> int: ...

    def close(self) -> None: ...

    def peek(self) -> int: ...

    @overload
    def read(self) -> int: ...

    @overload
    def read(self, arg0: list[int], arg1: int, arg2: int) -> int: ...

    @overload
    def readLine(self, arg0: list[int]) -> int: ...

    @overload
    def readLine(self, arg0: list[int], arg1: int, arg2: int) -> int: ...

    def skip(self, arg0: int) -> int: ...

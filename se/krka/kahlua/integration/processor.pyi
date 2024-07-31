from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import OutputStream
from java.lang import Class, Iterable, Void
from java.lang.reflect import Constructor, Method
from java.util import Map, List, Set
from javax.annotation.processing import ProcessingEnvironment, RoundEnvironment
from javax.lang.model import SourceVersion
from javax.lang.model.element import Element, AnnotationMirror, ExecutableElement, ModuleElement, PackageElement, RecordComponentElement, TypeElement, TypeParameterElement, VariableElement

class ClassParameterInformation:

  def getFileName(self) -> str: ...

  def getFullClassName(self) -> str: ...

  def getPackageName(self) -> str: ...

  def getSimpleClassName(self) -> str: ...

  def saveToStream(self, arg0: OutputStream) -> None: ...

  @staticmethod
  def getFromStream(arg0: Class[Any]) -> ClassParameterInformation: ...

  @overload
  def __init__(self, arg0: Class[Any]):
    self.methods: Map[str, MethodParameterInformation]

  @overload
  def __init__(self, arg0: str, arg1: str): ...


class DescriptorUtil:

  @staticmethod
  @overload
  def getDescriptor(arg0: Constructor) -> str: ...

  @staticmethod
  @overload
  def getDescriptor(arg0: Method) -> str: ...

  @staticmethod
  @overload
  def getDescriptor(arg0: str, arg1: List[VariableElement]) -> str: ...

  def __init__(self): ...


class LuaDebugDataProcessor:

  @overload
  def getCompletions(self, arg0: Element, arg1: AnnotationMirror, arg2: ExecutableElement, arg3: str) -> Iterable[Completion]: ...

  @overload
  def getCompletions(self, arg0: Element, arg1: AnnotationMirror, arg2: ExecutableElement, arg3: str) -> Iterable[Completion]: ...

  @overload
  def getSupportedAnnotationTypes(self) -> Set[str]: ...

  @overload
  def getSupportedAnnotationTypes(self) -> Set[str]: ...

  @overload
  def getSupportedOptions(self) -> Set[str]: ...

  @overload
  def getSupportedOptions(self) -> Set[str]: ...

  @overload
  def getSupportedSourceVersion(self) -> SourceVersion: ...

  @overload
  def getSupportedSourceVersion(self) -> SourceVersion: ...

  @overload
  def init(self, arg0: ProcessingEnvironment) -> None: ...

  @overload
  def init(self, arg0: ProcessingEnvironment) -> None: ...

  @overload
  def process(self, arg0: Set[TypeElement], arg1: RoundEnvironment) -> bool: ...

  @overload
  def process(self, arg0: Set[TypeElement], arg1: RoundEnvironment) -> bool: ...

  @overload
  def visit(self, arg0: Element) -> Void: ...

  @overload
  def visit(self, arg0: Element) -> object: ...

  @overload
  def visit(self, arg0: Element) -> object: ...

  @overload
  def visit(self, arg0: Element, arg1: object) -> object: ...

  @overload
  def visit(self, arg0: Element, arg1: object) -> object: ...

  @overload
  def visit(self, arg0: Element, arg1: Void) -> Void: ...

  @overload
  def visitExecutable(self, arg0: ExecutableElement, arg1: object) -> object: ...

  @overload
  def visitExecutable(self, arg0: ExecutableElement, arg1: object) -> object: ...

  @overload
  def visitExecutable(self, arg0: ExecutableElement, arg1: Void) -> Void: ...

  def visitModule(self, arg0: ModuleElement, arg1: object) -> object: ...

  @overload
  def visitPackage(self, arg0: PackageElement, arg1: object) -> object: ...

  @overload
  def visitPackage(self, arg0: PackageElement, arg1: object) -> object: ...

  @overload
  def visitPackage(self, arg0: PackageElement, arg1: Void) -> Void: ...

  def visitRecordComponent(self, arg0: RecordComponentElement, arg1: object) -> object: ...

  @overload
  def visitType(self, arg0: TypeElement, arg1: object) -> object: ...

  @overload
  def visitType(self, arg0: TypeElement, arg1: object) -> object: ...

  @overload
  def visitType(self, arg0: TypeElement, arg1: Void) -> Void: ...

  @overload
  def visitTypeParameter(self, arg0: TypeParameterElement, arg1: object) -> object: ...

  @overload
  def visitTypeParameter(self, arg0: TypeParameterElement, arg1: object) -> object: ...

  @overload
  def visitTypeParameter(self, arg0: TypeParameterElement, arg1: Void) -> Void: ...

  @overload
  def visitUnknown(self, arg0: Element, arg1: object) -> object: ...

  @overload
  def visitUnknown(self, arg0: Element, arg1: object) -> object: ...

  @overload
  def visitUnknown(self, arg0: Element, arg1: Void) -> Void: ...

  @overload
  def visitVariable(self, arg0: VariableElement, arg1: object) -> object: ...

  @overload
  def visitVariable(self, arg0: VariableElement, arg1: object) -> object: ...

  @overload
  def visitVariable(self, arg0: VariableElement, arg1: Void) -> Void: ...

  def __init__(self): ...


class MethodParameterInformation:

  EMPTY: MethodParameterInformation

  def getName(self, arg0: int) -> str: ...

  def __init__(self, arg0: List[str]): ...


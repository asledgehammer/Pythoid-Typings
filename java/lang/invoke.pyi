from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class, RuntimeException, Exception, Throwable, Enum, ClassLoader, ReflectiveOperationException, IllegalAccessException
from java.lang.constant import MethodHandleDesc, MethodTypeDesc, DynamicConstantDesc, ClassDesc
from java.lang.ref import SoftReference, WeakReference, ReferenceQueue
from java.lang.reflect import Constructor, Field, Method
from java.nio import ByteOrder
from java.util import List, AbstractList, Iterator, Optional
from java.util.function import IntFunction, Consumer
from jdk.internal.org.objectweb.asm import MethodVisitor

T = TypeVar('T', default=Any)
K = TypeVar('K', default=Any)
S = TypeVar('S', default=Any)
NoSuchMemberException = TypeVar('NoSuchMemberException', default=Any)
WeakEntry_T = TypeVar('WeakEntry_T', default=Any)
F = TypeVar('F', default=Any)
M = TypeVar('M', default=Any)

class AbstractConstantGroup:

  @overload
  def asList(self) -> List[object]: ...

  @overload
  def asList(self, arg0: object) -> List[object]: ...

  @overload
  def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int) -> int: ...

  @overload
  def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int, arg4: object) -> int: ...

  @overload
  def get(self, arg0: int) -> object: ...

  @overload
  def get(self, arg0: int) -> object: ...

  @overload
  def get(self, arg0: int, arg1: object) -> object: ...

  @overload
  def get(self, arg0: int, arg1: object) -> object: ...

  @overload
  def isPresent(self, arg0: int) -> bool: ...

  @overload
  def isPresent(self, arg0: int) -> bool: ...

  @overload
  def size(self) -> int: ...

  @overload
  def size(self) -> int: ...

  def subGroup(self, arg0: int, arg1: int) -> ConstantGroup: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def makeConstantGroup(arg0: List[object]) -> ConstantGroup: ...

  @staticmethod
  @overload
  def makeConstantGroup(arg0: List[object], arg1: object, arg2: IntFunction[object]) -> ConstantGroup: ...

  class BSCIWithCache[T](AbstractConstantGroup.WithCache):

    @overload
    def bootstrapMethod(self) -> MethodHandle: ...

    @overload
    def bootstrapMethod(self) -> MethodHandle: ...

    @overload
    def invocationName(self) -> str: ...

    @overload
    def invocationName(self) -> str: ...

    @overload
    def invocationType(self) -> object: ...

    @overload
    def invocationType(self) -> object: ...

    def toString(self) -> str: ...

    @staticmethod
    def makeBootstrapCallInfo(arg0: MethodHandle, arg1: str, arg2: object, arg3: ConstantGroup) -> BootstrapCallInfo[T]: ...

  class WithCache(AbstractConstantGroup):

    @overload
    def get(self, arg0: int) -> object: ...

    @overload
    def get(self, arg0: int, arg1: object) -> object: ...

    def isPresent(self, arg0: int) -> bool: ...

  class AsList(AbstractList):

    def get(self, arg0: int) -> object: ...

    def iterator(self) -> Iterator[object]: ...

    def size(self) -> int: ...

    def subList(self, arg0: int, arg1: int) -> List[object]: ...

    @overload
    def toArray(self) -> list[object]: ...

    @overload
    def toArray(self, arg0: list[object]) -> list[object]: ...

  class SubGroup(AbstractConstantGroup):

    @overload
    def asList(self) -> List[object]: ...

    @overload
    def asList(self, arg0: object) -> List[object]: ...

    @overload
    def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int) -> int: ...

    @overload
    def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int, arg4: object) -> int: ...

    @overload
    def get(self, arg0: int) -> object: ...

    @overload
    def get(self, arg0: int, arg1: object) -> object: ...

    def isPresent(self, arg0: int) -> bool: ...

    def subGroup(self, arg0: int, arg1: int) -> ConstantGroup: ...

  class AsIterator:

    def forEachRemaining(self, arg0: Consumer[E]) -> None: ...

    @overload
    def hasNext(self) -> bool: ...

    @overload
    def hasNext(self) -> bool: ...

    @overload
    def next(self) -> object: ...

    @overload
    def next(self) -> object: ...

    def remove(self) -> None: ...


class AbstractValidatingLambdaMetafactory: ...


class BootstrapCallInfo[T]:

  @overload
  def asList(self) -> List[object]: ...

  @overload
  def asList(self, arg0: object) -> List[object]: ...

  def bootstrapMethod(self) -> MethodHandle: ...

  @overload
  def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int) -> int: ...

  @overload
  def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int, arg4: object) -> int: ...

  @overload
  def get(self, arg0: int) -> object: ...

  @overload
  def get(self, arg0: int, arg1: object) -> object: ...

  def invocationName(self) -> str: ...

  def invocationType(self) -> object: ...

  def isPresent(self, arg0: int) -> bool: ...

  def size(self) -> int: ...

  def subGroup(self, arg0: int, arg1: int) -> ConstantGroup: ...

  @staticmethod
  def makeBootstrapCallInfo(arg0: MethodHandle, arg1: str, arg2: object, arg3: ConstantGroup) -> BootstrapCallInfo[T]: ...

  @staticmethod
  @overload
  def makeConstantGroup(arg0: List[object]) -> ConstantGroup: ...

  @staticmethod
  @overload
  def makeConstantGroup(arg0: List[object], arg1: object, arg2: IntFunction[object]) -> ConstantGroup: ...


class BootstrapMethodInvoker:

  class VM_BSCI[T](AbstractConstantGroup.BSCIWithCache):

    def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int) -> int: ...

  class PushAdapter: ...

  class PullAdapter: ...


class BoundMethodHandle(MethodHandle):

  class SpeciesData(ClassSpecializer.SpeciesData):

    def __init__(self, arg0: BoundMethodHandle.Specializer, arg1: str): ...

  class Specializer(ClassSpecializer):

    class Factory(ClassSpecializer.Factory): ...

  class Species_L(BoundMethodHandle): ...


class Species_LJ(BoundMethodHandle): ...


class Species_LL(BoundMethodHandle): ...


class Species_LLL(BoundMethodHandle): ...


class Species_LLLL(BoundMethodHandle): ...


class Species_LLLLL(BoundMethodHandle): ...


class Species_LLLLLL(BoundMethodHandle): ...


class Species_LLLLLLL(BoundMethodHandle): ...


class CallSite:

  def dynamicInvoker(self) -> MethodHandle: ...

  def getTarget(self) -> MethodHandle: ...

  def setTarget(self, arg0: MethodHandle) -> None: ...

  def type(self) -> MethodType: ...


class ClassSpecializer[T, K, S]:

  def findSpecies(self, arg0: object) -> ClassSpecializer.SpeciesData: ...

  def keyType(self) -> Class[K]: ...

  def metaType(self) -> Class[S]: ...

  def topClass(self) -> Class[T]: ...

  class SpeciesData:

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def key(self) -> object: ...

    def toString(self) -> str: ...

  class Factory: ...


class ConstantCallSite(CallSite):

  def dynamicInvoker(self) -> MethodHandle: ...

  def getTarget(self) -> MethodHandle: ...

  def setTarget(self, arg0: MethodHandle) -> None: ...

  def __init__(self, arg0: MethodHandle): ...


class ConstantGroup:

  @overload
  def asList(self) -> List[object]: ...

  @overload
  def asList(self, arg0: object) -> List[object]: ...

  @overload
  def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int) -> int: ...

  @overload
  def copyConstants(self, arg0: int, arg1: int, arg2: list[object], arg3: int, arg4: object) -> int: ...

  @overload
  def get(self, arg0: int) -> object: ...

  @overload
  def get(self, arg0: int, arg1: object) -> object: ...

  def isPresent(self, arg0: int) -> bool: ...

  def size(self) -> int: ...

  def subGroup(self, arg0: int, arg1: int) -> ConstantGroup: ...

  @staticmethod
  @overload
  def makeConstantGroup(arg0: List[object]) -> ConstantGroup: ...

  @staticmethod
  @overload
  def makeConstantGroup(arg0: List[object], arg1: object, arg2: IntFunction[object]) -> ConstantGroup: ...


class DelegatingMethodHandle(MethodHandle):

  class Holder: ...


class Holder: ...


class DirectMethodHandle(MethodHandle):

  class Special(DirectMethodHandle): ...

  class Interface(DirectMethodHandle): ...

  class StaticAccessor(DirectMethodHandle): ...

  class Accessor(DirectMethodHandle): ...

  class Constructor(DirectMethodHandle): ...

  class Holder: ...


class Holder: ...


class InfoFromMemberName:

  REF_getField: int

  REF_getStatic: int

  REF_invokeInterface: int

  REF_invokeSpecial: int

  REF_invokeStatic: int

  REF_invokeVirtual: int

  REF_newInvokeSpecial: int

  REF_putField: int

  REF_putStatic: int

  @overload
  def getDeclaringClass(self) -> Class[Any]: ...

  @overload
  def getDeclaringClass(self) -> Class[Any]: ...

  @overload
  def getMethodType(self) -> MethodType: ...

  @overload
  def getMethodType(self) -> MethodType: ...

  @overload
  def getModifiers(self) -> int: ...

  @overload
  def getModifiers(self) -> int: ...

  @overload
  def getName(self) -> str: ...

  @overload
  def getName(self) -> str: ...

  @overload
  def getReferenceKind(self) -> int: ...

  @overload
  def getReferenceKind(self) -> int: ...

  def isVarArgs(self) -> bool: ...

  @overload
  def reflectAs(self, arg0: Class[T], arg1: MethodHandles.Lookup) -> T: ...

  @overload
  def reflectAs(self, arg0: Class[T], arg1: MethodHandles.Lookup) -> T: ...

  def toString(self) -> str: ...

  @staticmethod
  def referenceKindToString(arg0: int) -> str: ...


class InnerClassLambdaMetafactory(AbstractValidatingLambdaMetafactory):

  def __init__(self, arg0: MethodHandles.Lookup, arg1: MethodType, arg2: str, arg3: MethodType, arg4: MethodHandle, arg5: MethodType, arg6: bool, arg7: list[Class], arg8: list[MethodType]): ...

  class ForwardingMethodGenerator(TypeConvertingMethodAdapter): ...


class InvokerBytecodeGenerator:

  class ClassData:

    def name(self) -> str: ...

    def toString(self) -> str: ...

  class BytecodeGenerationException(RuntimeException): ...


class Invokers:

  def toString(self) -> str: ...

  class Lazy: ...

  class Holder: ...


class Holder: ...


class LambdaConversionException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable, arg2: bool, arg3: bool): ...


class LambdaForm:

  LAST_RESULT: int

  VOID_RESULT: int

  @overload
  def equals(self, arg0: object) -> bool: ...

  @overload
  def equals(self, arg0: LambdaForm) -> bool: ...

  def hashCode(self) -> int: ...

  def prepare(self) -> None: ...

  def toString(self) -> str: ...

  @staticmethod
  def basicTypeSignature(arg0: MethodType) -> str: ...

  @staticmethod
  def shortenSignature(arg0: str) -> str: ...

  class Kind(Enum):

    BOUND_REINVOKER: LambdaForm.Kind

    COLLECT: LambdaForm.Kind

    COLLECTOR: LambdaForm.Kind

    CONVERT: LambdaForm.Kind

    DELEGATE: LambdaForm.Kind

    DIRECT_INVOKE_INTERFACE: LambdaForm.Kind

    DIRECT_INVOKE_SPECIAL: LambdaForm.Kind

    DIRECT_INVOKE_SPECIAL_IFC: LambdaForm.Kind

    DIRECT_INVOKE_STATIC: LambdaForm.Kind

    DIRECT_INVOKE_STATIC_INIT: LambdaForm.Kind

    DIRECT_INVOKE_VIRTUAL: LambdaForm.Kind

    DIRECT_NEW_INVOKE_SPECIAL: LambdaForm.Kind

    EXACT_INVOKER: LambdaForm.Kind

    EXACT_LINKER: LambdaForm.Kind

    FIELD: LambdaForm.Kind

    GENERIC: LambdaForm.Kind

    GENERIC_INVOKER: LambdaForm.Kind

    GENERIC_LINKER: LambdaForm.Kind

    GET_BOOLEAN: LambdaForm.Kind

    GET_BOOLEAN_VOLATILE: LambdaForm.Kind

    GET_BYTE: LambdaForm.Kind

    GET_BYTE_VOLATILE: LambdaForm.Kind

    GET_CHAR: LambdaForm.Kind

    GET_CHAR_VOLATILE: LambdaForm.Kind

    GET_DOUBLE: LambdaForm.Kind

    GET_DOUBLE_VOLATILE: LambdaForm.Kind

    GET_FLOAT: LambdaForm.Kind

    GET_FLOAT_VOLATILE: LambdaForm.Kind

    GET_INT: LambdaForm.Kind

    GET_INT_VOLATILE: LambdaForm.Kind

    GET_LONG: LambdaForm.Kind

    GET_LONG_VOLATILE: LambdaForm.Kind

    GET_REFERENCE: LambdaForm.Kind

    GET_REFERENCE_VOLATILE: LambdaForm.Kind

    GET_SHORT: LambdaForm.Kind

    GET_SHORT_VOLATILE: LambdaForm.Kind

    GUARD: LambdaForm.Kind

    GUARD_WITH_CATCH: LambdaForm.Kind

    IDENTITY: LambdaForm.Kind

    LINK_TO_CALL_SITE: LambdaForm.Kind

    LINK_TO_TARGET_METHOD: LambdaForm.Kind

    LOOP: LambdaForm.Kind

    PUT_BOOLEAN: LambdaForm.Kind

    PUT_BOOLEAN_VOLATILE: LambdaForm.Kind

    PUT_BYTE: LambdaForm.Kind

    PUT_BYTE_VOLATILE: LambdaForm.Kind

    PUT_CHAR: LambdaForm.Kind

    PUT_CHAR_VOLATILE: LambdaForm.Kind

    PUT_DOUBLE: LambdaForm.Kind

    PUT_DOUBLE_VOLATILE: LambdaForm.Kind

    PUT_FLOAT: LambdaForm.Kind

    PUT_FLOAT_VOLATILE: LambdaForm.Kind

    PUT_INT: LambdaForm.Kind

    PUT_INT_VOLATILE: LambdaForm.Kind

    PUT_LONG: LambdaForm.Kind

    PUT_LONG_VOLATILE: LambdaForm.Kind

    PUT_REFERENCE: LambdaForm.Kind

    PUT_REFERENCE_VOLATILE: LambdaForm.Kind

    PUT_SHORT: LambdaForm.Kind

    PUT_SHORT_VOLATILE: LambdaForm.Kind

    REINVOKER: LambdaForm.Kind

    SPREAD: LambdaForm.Kind

    TABLE_SWITCH: LambdaForm.Kind

    TRY_FINALLY: LambdaForm.Kind

    VARHANDLE_EXACT_INVOKER: LambdaForm.Kind

    VARHANDLE_INVOKER: LambdaForm.Kind

    VARHANDLE_LINKER: LambdaForm.Kind

    ZERO: LambdaForm.Kind

    @staticmethod
    def valueOf(arg0: str) -> LambdaForm.Kind: ...

    @staticmethod
    def values() -> list[LambdaForm.Kind]: ...

  class Name:

    def debugString(self) -> str: ...

    @overload
    def equals(self, arg0: object) -> bool: ...

    @overload
    def equals(self, arg0: LambdaForm.Name) -> bool: ...

    def exprString(self) -> str: ...

    def hashCode(self) -> int: ...

    def paramString(self) -> str: ...

    def toString(self) -> str: ...

  class BasicType(Enum):

    D_TYPE: LambdaForm.BasicType

    F_TYPE: LambdaForm.BasicType

    I_TYPE: LambdaForm.BasicType

    J_TYPE: LambdaForm.BasicType

    L_TYPE: LambdaForm.BasicType

    V_TYPE: LambdaForm.BasicType

    @staticmethod
    def valueOf(arg0: str) -> LambdaForm.BasicType: ...

    @staticmethod
    def values() -> list[LambdaForm.BasicType]: ...

  class NamedFunction:

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def intrinsicData(self) -> object: ...

    def intrinsicName(self) -> MethodHandleImpl.Intrinsic: ...

    def isConstantZero(self) -> bool: ...

    def isIdentity(self) -> bool: ...

    def toString(self) -> str: ...

  class Holder: ...

  class Compiled:

    def annotationType(self) -> Class[Annotation]: ...

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...


class Holder: ...


class LambdaFormBuffer: ...


class LambdaFormEditor:

  class Transform(SoftReference):

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...

  class TransformKey:

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...


class LambdaMetafactory:

  FLAG_BRIDGES: int

  FLAG_MARKERS: int

  FLAG_SERIALIZABLE: int

  @staticmethod
  def altMetafactory(arg0: MethodHandles.Lookup, arg1: str, arg2: MethodType, arg3: list[object]) -> CallSite: ...

  @staticmethod
  def metafactory(arg0: MethodHandles.Lookup, arg1: str, arg2: MethodType, arg3: MethodType, arg4: MethodHandle, arg5: MethodType) -> CallSite: ...


class LambdaProxyClassArchive: ...


class MemberName:

  DECLARED: int

  PUBLIC: int

  def asConstructor(self) -> MemberName: ...

  def asNormalOriginal(self) -> MemberName: ...

  def asSetter(self) -> MemberName: ...

  def asSpecial(self) -> MemberName: ...

  def canBeStaticallyBound(self) -> bool: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  @overload
  def equals(self, arg0: MemberName) -> bool: ...

  def getClassLoader(self) -> ClassLoader: ...

  @overload
  def getDeclaringClass(self) -> Class[Any]: ...

  @overload
  def getDeclaringClass(self) -> Class[Any]: ...

  def getDefinition(self) -> MemberName: ...

  def getFieldType(self) -> Class[Any]: ...

  def getInvocationType(self) -> MethodType: ...

  def getMethodOrFieldType(self) -> MethodType: ...

  def getMethodType(self) -> MethodType: ...

  @overload
  def getModifiers(self) -> int: ...

  @overload
  def getModifiers(self) -> int: ...

  @overload
  def getName(self) -> str: ...

  @overload
  def getName(self) -> str: ...

  def getParameterTypes(self) -> list[Class]: ...

  def getReferenceKind(self) -> int: ...

  def getReturnType(self) -> Class[Any]: ...

  def getSignature(self) -> str: ...

  def getType(self) -> object: ...

  def hasReceiverTypeDispatch(self) -> bool: ...

  def hashCode(self) -> int: ...

  def isAbstract(self) -> bool: ...

  def isAccessibleFrom(self, arg0: Class[Any]) -> bool: ...

  def isBridge(self) -> bool: ...

  def isCallerSensitive(self) -> bool: ...

  def isConstructor(self) -> bool: ...

  def isField(self) -> bool: ...

  def isFieldOrMethod(self) -> bool: ...

  def isFinal(self) -> bool: ...

  def isGetter(self) -> bool: ...

  def isInvocable(self) -> bool: ...

  def isMethod(self) -> bool: ...

  def isMethodHandleInvoke(self) -> bool: ...

  def isNative(self) -> bool: ...

  def isPackage(self) -> bool: ...

  def isPrivate(self) -> bool: ...

  def isProtected(self) -> bool: ...

  def isPublic(self) -> bool: ...

  def isResolved(self) -> bool: ...

  def isSetter(self) -> bool: ...

  def isStatic(self) -> bool: ...

  @overload
  def isSynthetic(self) -> bool: ...

  @overload
  def isSynthetic(self) -> bool: ...

  def isTrustedFinalField(self) -> bool: ...

  def isType(self) -> bool: ...

  def isVarHandleMethodInvoke(self) -> bool: ...

  def isVarargs(self) -> bool: ...

  def isVolatile(self) -> bool: ...

  @overload
  def makeAccessException(self) -> ReflectiveOperationException: ...

  @overload
  def makeAccessException(self, arg0: str, arg1: object) -> IllegalAccessException: ...

  def refersTo(self, arg0: Class[Any], arg1: str) -> bool: ...

  def toString(self) -> str: ...

  @staticmethod
  def isMethodHandleInvokeName(arg0: str) -> bool: ...

  @staticmethod
  def isVarHandleMethodInvokeName(arg0: str) -> bool: ...

  @overload
  def __init__(self, arg0: Class[Any]): ...
  @overload
  def __init__(self, arg0: Constructor[Any]): ...
  @overload
  def __init__(self, arg0: Field): ...
  @overload
  def __init__(self, arg0: Method): ...
  @overload
  def __init__(self, arg0: Field, arg1: bool): ...
  @overload
  def __init__(self, arg0: Method, arg1: bool): ...
  @overload
  def __init__(self, arg0: int, arg1: Class[Any], arg2: str, arg3: object): ...
  @overload
  def __init__(self, arg0: Class[Any], arg1: str, arg2: Class[Any], arg3: int): ...
  @overload
  def __init__(self, arg0: Class[Any], arg1: str, arg2: MethodType, arg3: int): ...

  class Factory:

    def getConstructors(self, arg0: Class[Any], arg1: Class[Any]) -> List[MemberName]: ...

    @overload
    def getFields(self, arg0: Class[Any], arg1: bool, arg2: Class[Any]) -> List[MemberName]: ...

    @overload
    def getFields(self, arg0: Class[Any], arg1: bool, arg2: str, arg3: Class[Any], arg4: Class[Any]) -> List[MemberName]: ...

    @overload
    def getMethods(self, arg0: Class[Any], arg1: bool, arg2: Class[Any]) -> List[MemberName]: ...

    @overload
    def getMethods(self, arg0: Class[Any], arg1: bool, arg2: str, arg3: MethodType, arg4: Class[Any]) -> List[MemberName]: ...

    def getNestedTypes(self, arg0: Class[Any], arg1: bool, arg2: Class[Any]) -> List[MemberName]: ...

    def resolveOrFail(self, arg0: int, arg1: MemberName, arg2: Class[Any], arg3: int, arg4: Class[NoSuchMemberException]) -> MemberName: ...

    def resolveOrNull(self, arg0: int, arg1: MemberName, arg2: Class[Any], arg3: int) -> MemberName: ...


class MethodHandle:

  @overload
  def asCollector(self, arg0: Class[Any], arg1: int) -> MethodHandle: ...

  @overload
  def asCollector(self, arg0: int, arg1: Class[Any], arg2: int) -> MethodHandle: ...

  def asFixedArity(self) -> MethodHandle: ...

  @overload
  def asSpreader(self, arg0: Class[Any], arg1: int) -> MethodHandle: ...

  @overload
  def asSpreader(self, arg0: int, arg1: Class[Any], arg2: int) -> MethodHandle: ...

  def asType(self, arg0: MethodType) -> MethodHandle: ...

  def asVarargsCollector(self, arg0: Class[Any]) -> MethodHandle: ...

  def bindTo(self, arg0: object) -> MethodHandle: ...

  @overload
  def describeConstable(self) -> Optional[MethodHandleDesc]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def invoke(self, arg0: list[object]) -> object: ...

  def invokeExact(self, arg0: list[object]) -> object: ...

  @overload
  def invokeWithArguments(self, arg0: list[object]) -> object: ...

  @overload
  def invokeWithArguments(self, arg0: List[Any]) -> object: ...

  def isVarargsCollector(self) -> bool: ...

  def toString(self) -> str: ...

  def type(self) -> MethodType: ...

  def withVarargs(self, arg0: bool) -> MethodHandle: ...

  class PolymorphicSignature:

    def annotationType(self) -> Class[Annotation]: ...

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def toString(self) -> str: ...


class MethodHandleImpl:

  class ArrayAccess(Enum):

    GET: MethodHandleImpl.ArrayAccess

    LENGTH: MethodHandleImpl.ArrayAccess

    SET: MethodHandleImpl.ArrayAccess

    @staticmethod
    def valueOf(arg0: str) -> MethodHandleImpl.ArrayAccess: ...

    @staticmethod
    def values() -> list[MethodHandleImpl.ArrayAccess]: ...

  class ArrayAccessor: ...

  class Intrinsic(Enum):

    ARRAY_LENGTH: MethodHandleImpl.Intrinsic

    ARRAY_LOAD: MethodHandleImpl.Intrinsic

    ARRAY_STORE: MethodHandleImpl.Intrinsic

    GUARD_WITH_CATCH: MethodHandleImpl.Intrinsic

    IDENTITY: MethodHandleImpl.Intrinsic

    LOOP: MethodHandleImpl.Intrinsic

    NONE: MethodHandleImpl.Intrinsic

    SELECT_ALTERNATIVE: MethodHandleImpl.Intrinsic

    TABLE_SWITCH: MethodHandleImpl.Intrinsic

    TRY_FINALLY: MethodHandleImpl.Intrinsic

    ZERO: MethodHandleImpl.Intrinsic

    @staticmethod
    def valueOf(arg0: str) -> MethodHandleImpl.Intrinsic: ...

    @staticmethod
    def values() -> list[MethodHandleImpl.Intrinsic]: ...

  class AsVarargsCollector(DelegatingMethodHandle):

    def asFixedArity(self) -> MethodHandle: ...

    def asTypeUncached(self, arg0: MethodType) -> MethodHandle: ...

    def invokeWithArguments(self, arg0: list[object]) -> object: ...

    def isVarargsCollector(self) -> bool: ...

    def withVarargs(self, arg0: bool) -> MethodHandle: ...

  class Makers: ...

  class CountingWrapper(DelegatingMethodHandle):

    def asTypeUncached(self, arg0: MethodType) -> MethodHandle: ...

  class BindCaller:

    class InjectedInvokerHolder: ...

  class WrappedMember(DelegatingMethodHandle):

    def asTypeUncached(self, arg0: MethodType) -> MethodHandle: ...

  class IntrinsicMethodHandle(DelegatingMethodHandle):

    def asCollector(self, arg0: Class[Any], arg1: int) -> MethodHandle: ...

    def asTypeUncached(self, arg0: MethodType) -> MethodHandle: ...

  class LoopClauses:

    def toString(self) -> str: ...

  class CasesHolder:

    def __init__(self, arg0: list[MethodHandle]): ...

  class TableSwitchCacheKey:

    def equals(self, arg0: object) -> bool: ...

    def hashCode(self) -> int: ...

    def __init__(self, arg0: MethodType, arg1: int): ...


class MethodHandleInfo:

  REF_getField: int

  REF_getStatic: int

  REF_invokeInterface: int

  REF_invokeSpecial: int

  REF_invokeStatic: int

  REF_invokeVirtual: int

  REF_newInvokeSpecial: int

  REF_putField: int

  REF_putStatic: int

  def getDeclaringClass(self) -> Class[Any]: ...

  def getMethodType(self) -> MethodType: ...

  def getModifiers(self) -> int: ...

  def getName(self) -> str: ...

  def getReferenceKind(self) -> int: ...

  def isVarArgs(self) -> bool: ...

  def reflectAs(self, arg0: Class[T], arg1: MethodHandles.Lookup) -> T: ...

  @staticmethod
  def referenceKindToString(arg0: int) -> str: ...

  @staticmethod
  def toString(arg0: int, arg1: Class[Any], arg2: str, arg3: MethodType) -> str: ...


class MethodHandleNatives:

  class Constants: ...

  class CallSiteContext:

    @overload
    def run(self) -> None: ...

    @overload
    def run(self) -> None: ...


class MethodHandleStatics: ...


class MethodHandles:

  @staticmethod
  def arrayConstructor(arg0: Class[Any]) -> MethodHandle: ...

  @staticmethod
  def arrayElementGetter(arg0: Class[Any]) -> MethodHandle: ...

  @staticmethod
  def arrayElementSetter(arg0: Class[Any]) -> MethodHandle: ...

  @staticmethod
  def arrayElementVarHandle(arg0: Class[Any]) -> VarHandle: ...

  @staticmethod
  def arrayLength(arg0: Class[Any]) -> MethodHandle: ...

  @staticmethod
  def byteArrayViewVarHandle(arg0: Class[Any], arg1: ByteOrder) -> VarHandle: ...

  @staticmethod
  def byteBufferViewVarHandle(arg0: Class[Any], arg1: ByteOrder) -> VarHandle: ...

  @staticmethod
  def catchException(arg0: MethodHandle, arg1: Class[Throwable], arg2: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def classData(arg0: MethodHandles.Lookup, arg1: str, arg2: Class[T]) -> object: ...

  @staticmethod
  def classDataAt(arg0: MethodHandles.Lookup, arg1: str, arg2: Class[T], arg3: int) -> object: ...

  @staticmethod
  def collectArguments(arg0: MethodHandle, arg1: int, arg2: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def constant(arg0: Class[Any], arg1: object) -> MethodHandle: ...

  @staticmethod
  @overload
  def countedLoop(arg0: MethodHandle, arg1: MethodHandle, arg2: MethodHandle) -> MethodHandle: ...

  @staticmethod
  @overload
  def countedLoop(arg0: MethodHandle, arg1: MethodHandle, arg2: MethodHandle, arg3: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def doWhileLoop(arg0: MethodHandle, arg1: MethodHandle, arg2: MethodHandle) -> MethodHandle: ...

  @staticmethod
  @overload
  def dropArguments(arg0: MethodHandle, arg1: int, arg2: list[Class]) -> MethodHandle: ...

  @staticmethod
  @overload
  def dropArguments(arg0: MethodHandle, arg1: int, arg2: List[Class[Any]]) -> MethodHandle: ...

  @staticmethod
  def dropArgumentsToMatch(arg0: MethodHandle, arg1: int, arg2: List[Class[Any]], arg3: int) -> MethodHandle: ...

  @staticmethod
  def dropReturn(arg0: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def empty(arg0: MethodType) -> MethodHandle: ...

  @staticmethod
  def exactInvoker(arg0: MethodType) -> MethodHandle: ...

  @staticmethod
  def explicitCastArguments(arg0: MethodHandle, arg1: MethodType) -> MethodHandle: ...

  @staticmethod
  def filterArguments(arg0: MethodHandle, arg1: int, arg2: list[MethodHandle]) -> MethodHandle: ...

  @staticmethod
  def filterReturnValue(arg0: MethodHandle, arg1: MethodHandle) -> MethodHandle: ...

  @staticmethod
  @overload
  def foldArguments(arg0: MethodHandle, arg1: MethodHandle) -> MethodHandle: ...

  @staticmethod
  @overload
  def foldArguments(arg0: MethodHandle, arg1: int, arg2: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def guardWithTest(arg0: MethodHandle, arg1: MethodHandle, arg2: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def identity(arg0: Class[Any]) -> MethodHandle: ...

  @staticmethod
  def insertArguments(arg0: MethodHandle, arg1: int, arg2: list[object]) -> MethodHandle: ...

  @staticmethod
  def invoker(arg0: MethodType) -> MethodHandle: ...

  @staticmethod
  def iteratedLoop(arg0: MethodHandle, arg1: MethodHandle, arg2: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def lookup() -> MethodHandles.Lookup: ...

  @staticmethod
  def loop(arg0: list[list[MethodHandle]]) -> MethodHandle: ...

  @staticmethod
  def permuteArguments(arg0: MethodHandle, arg1: MethodType, arg2: list[int]) -> MethodHandle: ...

  @staticmethod
  def privateLookupIn(arg0: Class[Any], arg1: MethodHandles.Lookup) -> MethodHandles.Lookup: ...

  @staticmethod
  def publicLookup() -> MethodHandles.Lookup: ...

  @staticmethod
  def reflectAs(arg0: Class[T], arg1: MethodHandle) -> T: ...

  @staticmethod
  def spreadInvoker(arg0: MethodType, arg1: int) -> MethodHandle: ...

  @staticmethod
  def tableSwitch(arg0: MethodHandle, arg1: list[MethodHandle]) -> MethodHandle: ...

  @staticmethod
  def throwException(arg0: Class[Any], arg1: Class[Throwable]) -> MethodHandle: ...

  @staticmethod
  def tryFinally(arg0: MethodHandle, arg1: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def varHandleExactInvoker(arg0: VarHandle.AccessMode, arg1: MethodType) -> MethodHandle: ...

  @staticmethod
  def varHandleInvoker(arg0: VarHandle.AccessMode, arg1: MethodType) -> MethodHandle: ...

  @staticmethod
  def whileLoop(arg0: MethodHandle, arg1: MethodHandle, arg2: MethodHandle) -> MethodHandle: ...

  @staticmethod
  def zero(arg0: Class[Any]) -> MethodHandle: ...

  class Lookup:

    MODULE: int

    ORIGINAL: int

    PACKAGE: int

    PRIVATE: int

    PROTECTED: int

    PUBLIC: int

    UNCONDITIONAL: int

    def accessClass(self, arg0: Class[Any]) -> Class[Any]: ...

    def bind(self, arg0: object, arg1: str, arg2: MethodType) -> MethodHandle: ...

    def defineClass(self, arg0: list[int]) -> Class[Any]: ...

    def defineHiddenClass(self, arg0: list[int], arg1: bool, arg2: list[MethodHandles.Lookup.ClassOption]) -> MethodHandles.Lookup: ...

    def defineHiddenClassWithClassData(self, arg0: list[int], arg1: object, arg2: bool, arg3: list[MethodHandles.Lookup.ClassOption]) -> MethodHandles.Lookup: ...

    def dropLookupMode(self, arg0: int) -> MethodHandles.Lookup: ...

    def ensureInitialized(self, arg0: Class[Any]) -> Class[Any]: ...

    def findClass(self, arg0: str) -> Class[Any]: ...

    def findConstructor(self, arg0: Class[Any], arg1: MethodType) -> MethodHandle: ...

    def findGetter(self, arg0: Class[Any], arg1: str, arg2: Class[Any]) -> MethodHandle: ...

    def findSetter(self, arg0: Class[Any], arg1: str, arg2: Class[Any]) -> MethodHandle: ...

    def findSpecial(self, arg0: Class[Any], arg1: str, arg2: MethodType, arg3: Class[Any]) -> MethodHandle: ...

    def findStatic(self, arg0: Class[Any], arg1: str, arg2: MethodType) -> MethodHandle: ...

    def findStaticGetter(self, arg0: Class[Any], arg1: str, arg2: Class[Any]) -> MethodHandle: ...

    def findStaticSetter(self, arg0: Class[Any], arg1: str, arg2: Class[Any]) -> MethodHandle: ...

    def findStaticVarHandle(self, arg0: Class[Any], arg1: str, arg2: Class[Any]) -> VarHandle: ...

    def findVarHandle(self, arg0: Class[Any], arg1: str, arg2: Class[Any]) -> VarHandle: ...

    def findVirtual(self, arg0: Class[Any], arg1: str, arg2: MethodType) -> MethodHandle: ...

    def hasFullPrivilegeAccess(self) -> bool: ...

    def hasPrivateAccess(self) -> bool: ...

    def lookupClass(self) -> Class[Any]: ...

    def lookupModes(self) -> int: ...

    def previousLookupClass(self) -> Class[Any]: ...

    def revealDirect(self, arg0: MethodHandle) -> MethodHandleInfo: ...

    def toString(self) -> str: ...

    def unreflect(self, arg0: Method) -> MethodHandle: ...

    def unreflectConstructor(self, arg0: Constructor[Any]) -> MethodHandle: ...

    def unreflectGetter(self, arg0: Field) -> MethodHandle: ...

    def unreflectSetter(self, arg0: Field) -> MethodHandle: ...

    def unreflectSpecial(self, arg0: Method, arg1: Class[Any]) -> MethodHandle: ...

    def unreflectVarHandle(self, arg0: Field) -> VarHandle: ...

    class ClassDefiner: ...

    class ClassFile: ...

    class ClassOption(Enum):

      NESTMATE: MethodHandles.Lookup.ClassOption

      STRONG: MethodHandles.Lookup.ClassOption

      @staticmethod
      def valueOf(arg0: str) -> MethodHandles.Lookup.ClassOption: ...

      @staticmethod
      def values() -> list[MethodHandles.Lookup.ClassOption]: ...


class MethodType:

  @overload
  def appendParameterTypes(self, arg0: list[Class]) -> MethodType: ...

  @overload
  def appendParameterTypes(self, arg0: List[Class[Any]]) -> MethodType: ...

  @overload
  def changeParameterType(self, arg0: int, arg1: Class[Any]) -> MethodType: ...

  @overload
  def changeParameterType(self, arg0: int, arg1: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

  @overload
  def changeParameterType(self, arg0: int, arg1: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

  @overload
  def changeReturnType(self, arg0: Class[Any]) -> MethodType: ...

  @overload
  def changeReturnType(self, arg0: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

  @overload
  def changeReturnType(self, arg0: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

  @overload
  def describeConstable(self) -> Optional[MethodTypeDesc]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def descriptorString(self) -> str: ...

  @overload
  def dropParameterTypes(self, arg0: int, arg1: int) -> TypeDescriptor.OfMethod: ...

  @overload
  def dropParameterTypes(self, arg0: int, arg1: int) -> MethodType: ...

  @overload
  def dropParameterTypes(self, arg0: int, arg1: int) -> TypeDescriptor.OfMethod: ...

  def equals(self, arg0: object) -> bool: ...

  def erase(self) -> MethodType: ...

  def generic(self) -> MethodType: ...

  def hasPrimitives(self) -> bool: ...

  def hasWrappers(self) -> bool: ...

  def hashCode(self) -> int: ...

  @overload
  def insertParameterTypes(self, arg0: int, arg1: list[Class]) -> MethodType: ...

  @overload
  def insertParameterTypes(self, arg0: int, arg1: list[TypeDescriptor.OfField]) -> TypeDescriptor.OfMethod: ...

  @overload
  def insertParameterTypes(self, arg0: int, arg1: list[TypeDescriptor.OfField]) -> TypeDescriptor.OfMethod: ...

  @overload
  def insertParameterTypes(self, arg0: int, arg1: List[Class[Any]]) -> MethodType: ...

  def lastParameterType(self) -> Class[Any]: ...

  @overload
  def parameterArray(self) -> list[Class]: ...

  @overload
  def parameterArray(self) -> list[TypeDescriptor.OfField]: ...

  @overload
  def parameterArray(self) -> list[TypeDescriptor.OfField]: ...

  @overload
  def parameterCount(self) -> int: ...

  @overload
  def parameterCount(self) -> int: ...

  @overload
  def parameterList(self) -> List[Class[Any]]: ...

  @overload
  def parameterList(self) -> List[F]: ...

  @overload
  def parameterType(self, arg0: int) -> Class[Any]: ...

  @overload
  def parameterType(self, arg0: int) -> TypeDescriptor.OfField: ...

  @overload
  def parameterType(self, arg0: int) -> TypeDescriptor.OfField: ...

  @overload
  def returnType(self) -> Class[Any]: ...

  @overload
  def returnType(self) -> TypeDescriptor.OfField: ...

  @overload
  def returnType(self) -> TypeDescriptor.OfField: ...

  def toMethodDescriptorString(self) -> str: ...

  def toString(self) -> str: ...

  def unwrap(self) -> MethodType: ...

  def wrap(self) -> MethodType: ...

  @staticmethod
  def fromMethodDescriptorString(arg0: str, arg1: ClassLoader) -> MethodType: ...

  @staticmethod
  @overload
  def genericMethodType(arg0: int) -> MethodType: ...

  @staticmethod
  @overload
  def genericMethodType(arg0: int, arg1: bool) -> MethodType: ...

  @staticmethod
  @overload
  def methodType(arg0: Class[Any]) -> MethodType: ...

  @staticmethod
  @overload
  def methodType(arg0: Class[Any], arg1: list[Class]) -> MethodType: ...

  @staticmethod
  @overload
  def methodType(arg0: Class[Any], arg1: Class[Any]) -> MethodType: ...

  @staticmethod
  @overload
  def methodType(arg0: Class[Any], arg1: MethodType) -> MethodType: ...

  @staticmethod
  @overload
  def methodType(arg0: Class[Any], arg1: List[Class[Any]]) -> MethodType: ...

  @staticmethod
  @overload
  def methodType(arg0: Class[Any], arg1: Class[Any], arg2: list[Class]) -> MethodType: ...

  class ConcurrentWeakInternSet[T]:

    def add(self, arg0: object) -> object: ...

    def get(self, arg0: object) -> object: ...

    def __init__(self): ...

    class WeakEntry[WeakEntry_T](WeakReference):

      def equals(self, arg0: object) -> bool: ...

      def hashCode(self) -> int: ...

      def __init__(self, arg0: object, arg1: ReferenceQueue[T]):
        self.hashcode: int

  class OffsetHolder: ...


class MethodTypeForm:

  ERASE: int

  UNWRAP: int

  WRAP: int

  def basicType(self) -> MethodType: ...

  def cachedLambdaForm(self, arg0: int) -> LambdaForm: ...

  def cachedMethodHandle(self, arg0: int) -> MethodHandle: ...

  def erasedType(self) -> MethodType: ...

  def hasPrimitives(self) -> bool: ...

  def parameterCount(self) -> int: ...

  def parameterSlotCount(self) -> int: ...

  def setCachedLambdaForm(self, arg0: int, arg1: LambdaForm) -> LambdaForm: ...

  def setCachedMethodHandle(self, arg0: int, arg1: MethodHandle) -> MethodHandle: ...

  def toString(self) -> str: ...

  @staticmethod
  def canonicalize(arg0: MethodType, arg1: int) -> MethodType: ...


class MutableCallSite(CallSite):

  def dynamicInvoker(self) -> MethodHandle: ...

  def getTarget(self) -> MethodHandle: ...

  def setTarget(self, arg0: MethodHandle) -> None: ...

  @staticmethod
  def syncAll(arg0: list[MutableCallSite]) -> None: ...

  @overload
  def __init__(self, arg0: MethodHandle): ...
  @overload
  def __init__(self, arg0: MethodType): ...


class ProxyClassesDumper:

  def dumpClass(self, arg0: str, arg1: list[int]) -> None: ...

  @staticmethod
  def encodeForFilename(arg0: str) -> str: ...

  @staticmethod
  def getInstance(arg0: str) -> ProxyClassesDumper: ...


class ResolvedMethodName: ...


class SerializedLambda:

  def getCapturedArg(self, arg0: int) -> object: ...

  def getCapturedArgCount(self) -> int: ...

  def getCapturingClass(self) -> str: ...

  def getFunctionalInterfaceClass(self) -> str: ...

  def getFunctionalInterfaceMethodName(self) -> str: ...

  def getFunctionalInterfaceMethodSignature(self) -> str: ...

  def getImplClass(self) -> str: ...

  def getImplMethodKind(self) -> int: ...

  def getImplMethodName(self) -> str: ...

  def getImplMethodSignature(self) -> str: ...

  def getInstantiatedMethodType(self) -> str: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: Class[Any], arg1: str, arg2: str, arg3: str, arg4: int, arg5: str, arg6: str, arg7: str, arg8: str, arg9: list[object]): ...


class SimpleMethodHandle(BoundMethodHandle): ...


class StringConcatException(Exception):

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class StringConcatFactory:

  @staticmethod
  def makeConcat(arg0: MethodHandles.Lookup, arg1: str, arg2: MethodType) -> CallSite: ...

  @staticmethod
  def makeConcatWithConstants(arg0: MethodHandles.Lookup, arg1: str, arg2: MethodType, arg3: str, arg4: list[object]) -> CallSite: ...


class TypeConvertingMethodAdapter(MethodVisitor): ...


class TypeDescriptor:

  def descriptorString(self) -> str: ...

  class OfMethod[F, M]:

    def changeParameterType(self, arg0: int, arg1: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

    def changeReturnType(self, arg0: TypeDescriptor.OfField) -> TypeDescriptor.OfMethod: ...

    def descriptorString(self) -> str: ...

    def dropParameterTypes(self, arg0: int, arg1: int) -> TypeDescriptor.OfMethod: ...

    def insertParameterTypes(self, arg0: int, arg1: list[TypeDescriptor.OfField]) -> TypeDescriptor.OfMethod: ...

    def parameterArray(self) -> list[TypeDescriptor.OfField]: ...

    def parameterCount(self) -> int: ...

    def parameterList(self) -> List[F]: ...

    def parameterType(self, arg0: int) -> TypeDescriptor.OfField: ...

    def returnType(self) -> TypeDescriptor.OfField: ...

  class OfField[F]:

    def arrayType(self) -> TypeDescriptor.OfField: ...

    def componentType(self) -> TypeDescriptor.OfField: ...

    def descriptorString(self) -> str: ...

    def isArray(self) -> bool: ...

    def isPrimitive(self) -> bool: ...


class VarForm: ...


class VarHandle:

  def accessModeType(self, arg0: VarHandle.AccessMode) -> MethodType: ...

  def compareAndExchange(self, arg0: list[object]) -> object: ...

  def compareAndExchangeAcquire(self, arg0: list[object]) -> object: ...

  def compareAndExchangeRelease(self, arg0: list[object]) -> object: ...

  def compareAndSet(self, arg0: list[object]) -> bool: ...

  def coordinateTypes(self) -> List[Class[Any]]: ...

  @overload
  def describeConstable(self) -> Optional[VarHandle.VarHandleDesc]: ...

  @overload
  def describeConstable(self) -> Optional[ConstantDesc]: ...

  def get(self, arg0: list[object]) -> object: ...

  def getAcquire(self, arg0: list[object]) -> object: ...

  def getAndAdd(self, arg0: list[object]) -> object: ...

  def getAndAddAcquire(self, arg0: list[object]) -> object: ...

  def getAndAddRelease(self, arg0: list[object]) -> object: ...

  def getAndBitwiseAnd(self, arg0: list[object]) -> object: ...

  def getAndBitwiseAndAcquire(self, arg0: list[object]) -> object: ...

  def getAndBitwiseAndRelease(self, arg0: list[object]) -> object: ...

  def getAndBitwiseOr(self, arg0: list[object]) -> object: ...

  def getAndBitwiseOrAcquire(self, arg0: list[object]) -> object: ...

  def getAndBitwiseOrRelease(self, arg0: list[object]) -> object: ...

  def getAndBitwiseXor(self, arg0: list[object]) -> object: ...

  def getAndBitwiseXorAcquire(self, arg0: list[object]) -> object: ...

  def getAndBitwiseXorRelease(self, arg0: list[object]) -> object: ...

  def getAndSet(self, arg0: list[object]) -> object: ...

  def getAndSetAcquire(self, arg0: list[object]) -> object: ...

  def getAndSetRelease(self, arg0: list[object]) -> object: ...

  def getOpaque(self, arg0: list[object]) -> object: ...

  def getVolatile(self, arg0: list[object]) -> object: ...

  def hasInvokeExactBehavior(self) -> bool: ...

  def isAccessModeSupported(self, arg0: VarHandle.AccessMode) -> bool: ...

  def set(self, arg0: list[object]) -> None: ...

  def setOpaque(self, arg0: list[object]) -> None: ...

  def setRelease(self, arg0: list[object]) -> None: ...

  def setVolatile(self, arg0: list[object]) -> None: ...

  def toMethodHandle(self, arg0: VarHandle.AccessMode) -> MethodHandle: ...

  def toString(self) -> str: ...

  def varType(self) -> Class[Any]: ...

  def weakCompareAndSet(self, arg0: list[object]) -> bool: ...

  def weakCompareAndSetAcquire(self, arg0: list[object]) -> bool: ...

  def weakCompareAndSetPlain(self, arg0: list[object]) -> bool: ...

  def weakCompareAndSetRelease(self, arg0: list[object]) -> bool: ...

  def withInvokeBehavior(self) -> VarHandle: ...

  def withInvokeExactBehavior(self) -> VarHandle: ...

  @staticmethod
  def acquireFence() -> None: ...

  @staticmethod
  def fullFence() -> None: ...

  @staticmethod
  def loadLoadFence() -> None: ...

  @staticmethod
  def releaseFence() -> None: ...

  @staticmethod
  def storeStoreFence() -> None: ...

  class AccessMode(Enum):

    COMPARE_AND_EXCHANGE: VarHandle.AccessMode

    COMPARE_AND_EXCHANGE_ACQUIRE: VarHandle.AccessMode

    COMPARE_AND_EXCHANGE_RELEASE: VarHandle.AccessMode

    COMPARE_AND_SET: VarHandle.AccessMode

    GET: VarHandle.AccessMode

    GET_ACQUIRE: VarHandle.AccessMode

    GET_AND_ADD: VarHandle.AccessMode

    GET_AND_ADD_ACQUIRE: VarHandle.AccessMode

    GET_AND_ADD_RELEASE: VarHandle.AccessMode

    GET_AND_BITWISE_AND: VarHandle.AccessMode

    GET_AND_BITWISE_AND_ACQUIRE: VarHandle.AccessMode

    GET_AND_BITWISE_AND_RELEASE: VarHandle.AccessMode

    GET_AND_BITWISE_OR: VarHandle.AccessMode

    GET_AND_BITWISE_OR_ACQUIRE: VarHandle.AccessMode

    GET_AND_BITWISE_OR_RELEASE: VarHandle.AccessMode

    GET_AND_BITWISE_XOR: VarHandle.AccessMode

    GET_AND_BITWISE_XOR_ACQUIRE: VarHandle.AccessMode

    GET_AND_BITWISE_XOR_RELEASE: VarHandle.AccessMode

    GET_AND_SET: VarHandle.AccessMode

    GET_AND_SET_ACQUIRE: VarHandle.AccessMode

    GET_AND_SET_RELEASE: VarHandle.AccessMode

    GET_OPAQUE: VarHandle.AccessMode

    GET_VOLATILE: VarHandle.AccessMode

    SET: VarHandle.AccessMode

    SET_OPAQUE: VarHandle.AccessMode

    SET_RELEASE: VarHandle.AccessMode

    SET_VOLATILE: VarHandle.AccessMode

    WEAK_COMPARE_AND_SET: VarHandle.AccessMode

    WEAK_COMPARE_AND_SET_ACQUIRE: VarHandle.AccessMode

    WEAK_COMPARE_AND_SET_PLAIN: VarHandle.AccessMode

    WEAK_COMPARE_AND_SET_RELEASE: VarHandle.AccessMode

    def methodName(self) -> str: ...

    @staticmethod
    def valueFromMethodName(arg0: str) -> VarHandle.AccessMode: ...

    @staticmethod
    def valueOf(arg0: str) -> VarHandle.AccessMode: ...

    @staticmethod
    def values() -> list[VarHandle.AccessMode]: ...

  class AccessType(Enum):

    COMPARE_AND_EXCHANGE: VarHandle.AccessType

    COMPARE_AND_SET: VarHandle.AccessType

    GET: VarHandle.AccessType

    GET_AND_UPDATE: VarHandle.AccessType

    SET: VarHandle.AccessType

    @staticmethod
    def valueOf(arg0: str) -> VarHandle.AccessType: ...

    @staticmethod
    def values() -> list[VarHandle.AccessType]: ...

  class AccessDescriptor:

    def __init__(self, arg0: MethodType, arg1: int, arg2: int): ...

  class TypesAndInvokers: ...

  class VarHandleDesc(DynamicConstantDesc):

    @overload
    def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> object: ...

    @overload
    def resolveConstantDesc(self, arg0: MethodHandles.Lookup) -> VarHandle: ...

    def toString(self) -> str: ...

    def varType(self) -> ClassDesc: ...

    @staticmethod
    def ofArray(arg0: ClassDesc) -> VarHandle.VarHandleDesc: ...

    @staticmethod
    def ofField(arg0: ClassDesc, arg1: str, arg2: ClassDesc) -> VarHandle.VarHandleDesc: ...

    @staticmethod
    def ofStaticField(arg0: ClassDesc, arg1: str, arg2: ClassDesc) -> VarHandle.VarHandleDesc: ...

    class Kind(Enum):

      ARRAY: VarHandle.VarHandleDesc.Kind

      FIELD: VarHandle.VarHandleDesc.Kind

      STATIC_FIELD: VarHandle.VarHandleDesc.Kind

      @staticmethod
      def valueOf(arg0: str) -> VarHandle.VarHandleDesc.Kind: ...

      @staticmethod
      def values() -> list[VarHandle.VarHandleDesc.Kind]: ...


class VolatileCallSite(CallSite):

  def dynamicInvoker(self) -> MethodHandle: ...

  def getTarget(self) -> MethodHandle: ...

  def setTarget(self, arg0: MethodHandle) -> None: ...

  @overload
  def __init__(self, arg0: MethodHandle): ...
  @overload
  def __init__(self, arg0: MethodType): ...


class WrongMethodTypeException(RuntimeException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


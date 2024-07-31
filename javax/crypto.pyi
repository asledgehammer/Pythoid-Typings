from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import Serializable
from java.nio import ByteBuffer
from java.security import GeneralSecurityException, AlgorithmParameters, Provider, Key, SecureRandom, Permission, PermissionCollection
from java.security.cert import Certificate
from java.security.spec import AlgorithmParameterSpec

class BadPaddingException(GeneralSecurityException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Cipher:

  DECRYPT_MODE: int

  ENCRYPT_MODE: int

  PRIVATE_KEY: int

  PUBLIC_KEY: int

  SECRET_KEY: int

  UNWRAP_MODE: int

  WRAP_MODE: int

  @overload
  def doFinal(self) -> list[int]: ...

  @overload
  def doFinal(self, arg0: list[int]) -> list[int]: ...

  @overload
  def doFinal(self, arg0: list[int], arg1: int) -> int: ...

  @overload
  def doFinal(self, arg0: ByteBuffer, arg1: ByteBuffer) -> int: ...

  @overload
  def doFinal(self, arg0: list[int], arg1: int, arg2: int) -> list[int]: ...

  @overload
  def doFinal(self, arg0: list[int], arg1: int, arg2: int, arg3: list[int]) -> int: ...

  @overload
  def doFinal(self, arg0: list[int], arg1: int, arg2: int, arg3: list[int], arg4: int) -> int: ...

  def getAlgorithm(self) -> str: ...

  def getBlockSize(self) -> int: ...

  def getExemptionMechanism(self) -> ExemptionMechanism: ...

  def getIV(self) -> list[int]: ...

  def getOutputSize(self, arg0: int) -> int: ...

  def getParameters(self) -> AlgorithmParameters: ...

  def getProvider(self) -> Provider: ...

  @overload
  def init(self, arg0: int, arg1: Key) -> None: ...

  @overload
  def init(self, arg0: int, arg1: Certificate) -> None: ...

  @overload
  def init(self, arg0: int, arg1: Key, arg2: AlgorithmParameters) -> None: ...

  @overload
  def init(self, arg0: int, arg1: Key, arg2: SecureRandom) -> None: ...

  @overload
  def init(self, arg0: int, arg1: Key, arg2: AlgorithmParameterSpec) -> None: ...

  @overload
  def init(self, arg0: int, arg1: Certificate, arg2: SecureRandom) -> None: ...

  @overload
  def init(self, arg0: int, arg1: Key, arg2: AlgorithmParameters, arg3: SecureRandom) -> None: ...

  @overload
  def init(self, arg0: int, arg1: Key, arg2: AlgorithmParameterSpec, arg3: SecureRandom) -> None: ...

  def toString(self) -> str: ...

  def unwrap(self, arg0: list[int], arg1: str, arg2: int) -> Key: ...

  @overload
  def update(self, arg0: list[int]) -> list[int]: ...

  @overload
  def update(self, arg0: ByteBuffer, arg1: ByteBuffer) -> int: ...

  @overload
  def update(self, arg0: list[int], arg1: int, arg2: int) -> list[int]: ...

  @overload
  def update(self, arg0: list[int], arg1: int, arg2: int, arg3: list[int]) -> int: ...

  @overload
  def update(self, arg0: list[int], arg1: int, arg2: int, arg3: list[int], arg4: int) -> int: ...

  @overload
  def updateAAD(self, arg0: list[int]) -> None: ...

  @overload
  def updateAAD(self, arg0: ByteBuffer) -> None: ...

  @overload
  def updateAAD(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  def wrap(self, arg0: Key) -> list[int]: ...

  @staticmethod
  @overload
  def getInstance(arg0: str) -> Cipher: ...

  @staticmethod
  @overload
  def getInstance(arg0: str, arg1: str) -> Cipher: ...

  @staticmethod
  @overload
  def getInstance(arg0: str, arg1: Provider) -> Cipher: ...

  @staticmethod
  def getMaxAllowedKeyLength(arg0: str) -> int: ...

  @staticmethod
  def getMaxAllowedParameterSpec(arg0: str) -> AlgorithmParameterSpec: ...

  class Transform: ...


class CipherSpi:

  def __init__(self): ...


class CryptoPermission(Permission):

  def equals(self, arg0: object) -> bool: ...

  def getActions(self) -> str: ...

  def hashCode(self) -> int: ...

  def implies(self, arg0: Permission) -> bool: ...

  def newPermissionCollection(self) -> PermissionCollection: ...

  def toString(self) -> str: ...


class ExemptionMechanism:

  @overload
  def genExemptionBlob(self) -> list[int]: ...

  @overload
  def genExemptionBlob(self, arg0: list[int]) -> int: ...

  @overload
  def genExemptionBlob(self, arg0: list[int], arg1: int) -> int: ...

  def getName(self) -> str: ...

  def getOutputSize(self, arg0: int) -> int: ...

  def getProvider(self) -> Provider: ...

  @overload
  def init(self, arg0: Key) -> None: ...

  @overload
  def init(self, arg0: Key, arg1: AlgorithmParameters) -> None: ...

  @overload
  def init(self, arg0: Key, arg1: AlgorithmParameterSpec) -> None: ...

  def isCryptoAllowed(self, arg0: Key) -> bool: ...

  @staticmethod
  @overload
  def getInstance(arg0: str) -> ExemptionMechanism: ...

  @staticmethod
  @overload
  def getInstance(arg0: str, arg1: str) -> ExemptionMechanism: ...

  @staticmethod
  @overload
  def getInstance(arg0: str, arg1: Provider) -> ExemptionMechanism: ...


class ExemptionMechanismException(GeneralSecurityException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class ExemptionMechanismSpi:

  def __init__(self): ...


class IllegalBlockSizeException(GeneralSecurityException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class NoSuchPaddingException(GeneralSecurityException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class SealedObject:

  def getAlgorithm(self) -> str: ...

  @overload
  def getObject(self, arg0: Key) -> object: ...

  @overload
  def getObject(self, arg0: Cipher) -> object: ...

  @overload
  def getObject(self, arg0: Key, arg1: str) -> object: ...

  def __init__(self, arg0: Serializable, arg1: Cipher): ...


class SecretKey:

  serialVersionUID: int

  def destroy(self) -> None: ...

  def getAlgorithm(self) -> str: ...

  def getEncoded(self) -> list[int]: ...

  def getFormat(self) -> str: ...

  def isDestroyed(self) -> bool: ...


class ShortBufferException(GeneralSecurityException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import OutputStream
from java.util import Map, List
from javax.security.auth import Subject
from javax.security.auth.x500 import X500Principal
from sun.security.util import DerOutputStream, DerValue, ObjectIdentifier, DerInputStream

class AVA:

  @overload
  def derEncode(self, arg0: OutputStream) -> None: ...

  @overload
  def derEncode(self, arg0: OutputStream) -> None: ...

  def encode(self, arg0: DerOutputStream) -> None: ...

  def equals(self, arg0: object) -> bool: ...

  def getDerValue(self) -> DerValue: ...

  def getObjectIdentifier(self) -> ObjectIdentifier: ...

  def getValueString(self) -> str: ...

  def hashCode(self) -> int: ...

  @overload
  def toRFC1779String(self) -> str: ...

  @overload
  def toRFC1779String(self, arg0: Map[str, str]) -> str: ...

  def toRFC2253CanonicalString(self) -> str: ...

  @overload
  def toRFC2253String(self) -> str: ...

  @overload
  def toRFC2253String(self, arg0: Map[str, str]) -> str: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: ObjectIdentifier, arg1: DerValue): ...


class GeneralNameInterface:

  NAME_ANY: int

  NAME_DIFF_TYPE: int

  NAME_DIRECTORY: int

  NAME_DNS: int

  NAME_EDI: int

  NAME_IP: int

  NAME_MATCH: int

  NAME_NARROWS: int

  NAME_OID: int

  NAME_RFC822: int

  NAME_SAME_TYPE: int

  NAME_URI: int

  NAME_WIDENS: int

  NAME_X400: int

  def constrains(self, arg0: GeneralNameInterface) -> int: ...

  def encode(self, arg0: DerOutputStream) -> None: ...

  def getType(self) -> int: ...

  def subtreeDepth(self) -> int: ...


class RDN:

  def avas(self) -> List[AVA]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def size(self) -> int: ...

  @overload
  def toRFC1779String(self) -> str: ...

  @overload
  def toRFC1779String(self, arg0: Map[str, str]) -> str: ...

  @overload
  def toRFC2253String(self) -> str: ...

  @overload
  def toRFC2253String(self, arg0: bool) -> str: ...

  @overload
  def toRFC2253String(self, arg0: Map[str, str]) -> str: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self, arg0: list[AVA]): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: AVA): ...
  @overload
  def __init__(self, arg0: str, arg1: Map[str, str]): ...


class X500Name:

  commonName_oid: ObjectIdentifier

  countryName_oid: ObjectIdentifier

  DNQUALIFIER_OID: ObjectIdentifier

  DOMAIN_COMPONENT_OID: ObjectIdentifier

  GENERATIONQUALIFIER_OID: ObjectIdentifier

  GIVENNAME_OID: ObjectIdentifier

  INITIALS_OID: ObjectIdentifier

  ipAddress_oid: ObjectIdentifier

  localityName_oid: ObjectIdentifier

  NAME_ANY: int

  NAME_DIFF_TYPE: int

  NAME_DIRECTORY: int

  NAME_DNS: int

  NAME_EDI: int

  NAME_IP: int

  NAME_MATCH: int

  NAME_NARROWS: int

  NAME_OID: int

  NAME_RFC822: int

  NAME_SAME_TYPE: int

  NAME_URI: int

  NAME_WIDENS: int

  NAME_X400: int

  orgName_oid: ObjectIdentifier

  orgUnitName_oid: ObjectIdentifier

  SERIALNUMBER_OID: ObjectIdentifier

  stateName_oid: ObjectIdentifier

  streetAddress_oid: ObjectIdentifier

  SURNAME_OID: ObjectIdentifier

  title_oid: ObjectIdentifier

  userid_oid: ObjectIdentifier

  def allAvas(self) -> List[AVA]: ...

  def asX500Principal(self) -> X500Principal: ...

  def avaSize(self) -> int: ...

  def commonAncestor(self, arg0: X500Name) -> X500Name: ...

  @overload
  def constrains(self, arg0: GeneralNameInterface) -> int: ...

  @overload
  def constrains(self, arg0: GeneralNameInterface) -> int: ...

  def emit(self, arg0: DerOutputStream) -> None: ...

  @overload
  def encode(self, arg0: DerOutputStream) -> None: ...

  @overload
  def encode(self, arg0: DerOutputStream) -> None: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  def findMostSpecificAttribute(self, arg0: ObjectIdentifier) -> DerValue: ...

  def getCommonName(self) -> str: ...

  def getCountry(self) -> str: ...

  def getDNQualifier(self) -> str: ...

  def getDomain(self) -> str: ...

  def getEncoded(self) -> list[int]: ...

  def getEncodedInternal(self) -> list[int]: ...

  def getGeneration(self) -> str: ...

  def getGivenName(self) -> str: ...

  def getIP(self) -> str: ...

  def getInitials(self) -> str: ...

  def getLocality(self) -> str: ...

  @overload
  def getName(self) -> str: ...

  @overload
  def getName(self) -> str: ...

  def getOrganization(self) -> str: ...

  def getOrganizationalUnit(self) -> str: ...

  @overload
  def getRFC1779Name(self) -> str: ...

  @overload
  def getRFC1779Name(self, arg0: Map[str, str]) -> str: ...

  def getRFC2253CanonicalName(self) -> str: ...

  @overload
  def getRFC2253Name(self) -> str: ...

  @overload
  def getRFC2253Name(self, arg0: Map[str, str]) -> str: ...

  def getState(self) -> str: ...

  def getSurname(self) -> str: ...

  @overload
  def getType(self) -> int: ...

  @overload
  def getType(self) -> int: ...

  @overload
  def hashCode(self) -> int: ...

  @overload
  def hashCode(self) -> int: ...

  def implies(self, arg0: Subject) -> bool: ...

  def isEmpty(self) -> bool: ...

  def rdns(self) -> List[RDN]: ...

  def size(self) -> int: ...

  @overload
  def subtreeDepth(self) -> int: ...

  @overload
  def subtreeDepth(self) -> int: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toString(self) -> str: ...

  @staticmethod
  def asX500Name(arg0: X500Principal) -> X500Name: ...

  @overload
  def __init__(self, arg0: list[int]): ...
  @overload
  def __init__(self, arg0: list[RDN]): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: DerInputStream): ...
  @overload
  def __init__(self, arg0: DerValue): ...
  @overload
  def __init__(self, arg0: str, arg1: str): ...
  @overload
  def __init__(self, arg0: str, arg1: Map[str, str]): ...
  @overload
  def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str): ...
  @overload
  def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str): ...


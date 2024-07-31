from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import PrintStream, ByteArrayOutputStream, OutputStream, InputStream
from java.lang import Integer, Enum
from java.math import BigInteger
from java.security import Key, CodeSigner, PermissionCollection, Permission, CodeSource, MessageDigest
from java.security.cert import X509Certificate
from java.util import Comparator, Date, Set, Optional, List, Enumeration, Hashtable, Map
from java.util.function import Function, ToDoubleFunction, ToIntFunction, ToLongFunction
from java.util.jar import JarEntry, Manifest
from javax.crypto import SecretKey

U = TypeVar('U', default=Any)
T = TypeVar('T', default=Any)

class BitArray:

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def get(self, arg0: int) -> bool: ...

  def hashCode(self) -> int: ...

  def length(self) -> int: ...

  def set(self, arg0: int, arg1: bool) -> None: ...

  def toBooleanArray(self) -> list[bool]: ...

  def toByteArray(self) -> list[int]: ...

  def toString(self) -> str: ...

  def truncate(self) -> BitArray: ...

  @overload
  def __init__(self, arg0: list[bool]): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: int, arg1: list[int]): ...
  @overload
  def __init__(self, arg0: int, arg1: list[int], arg2: int): ...


class ByteArrayLexOrder:

  @overload
  def compare(self, arg0: list[int], arg1: list[int]) -> int: ...

  @overload
  def compare(self, arg0: object, arg1: object) -> int: ...

  @overload
  def compare(self, arg0: object, arg1: object) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  def reversed(self) -> Comparator[T]: ...

  @overload
  def thenComparing(self, arg0: Comparator[T]) -> Comparator[T]: ...

  @overload
  def thenComparing(self, arg0: Function[T, U]) -> Comparator[T]: ...

  @overload
  def thenComparing(self, arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

  def thenComparingDouble(self, arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

  def thenComparingInt(self, arg0: ToIntFunction[T]) -> Comparator[T]: ...

  def thenComparingLong(self, arg0: ToLongFunction[T]) -> Comparator[T]: ...

  @staticmethod
  @overload
  def comparing(arg0: Function[T, U]) -> Comparator[T]: ...

  @staticmethod
  @overload
  def comparing(arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

  @staticmethod
  def comparingDouble(arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

  @staticmethod
  def comparingInt(arg0: ToIntFunction[T]) -> Comparator[T]: ...

  @staticmethod
  def comparingLong(arg0: ToLongFunction[T]) -> Comparator[T]: ...

  @staticmethod
  def naturalOrder() -> Comparator[T]: ...

  @staticmethod
  def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

  @staticmethod
  def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

  @staticmethod
  def reverseOrder() -> Comparator[T]: ...

  def __init__(self): ...


class ByteArrayTagOrder:

  @overload
  def compare(self, arg0: list[int], arg1: list[int]) -> int: ...

  @overload
  def compare(self, arg0: object, arg1: object) -> int: ...

  @overload
  def compare(self, arg0: object, arg1: object) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  def reversed(self) -> Comparator[T]: ...

  @overload
  def thenComparing(self, arg0: Comparator[T]) -> Comparator[T]: ...

  @overload
  def thenComparing(self, arg0: Function[T, U]) -> Comparator[T]: ...

  @overload
  def thenComparing(self, arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

  def thenComparingDouble(self, arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

  def thenComparingInt(self, arg0: ToIntFunction[T]) -> Comparator[T]: ...

  def thenComparingLong(self, arg0: ToLongFunction[T]) -> Comparator[T]: ...

  @staticmethod
  @overload
  def comparing(arg0: Function[T, U]) -> Comparator[T]: ...

  @staticmethod
  @overload
  def comparing(arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

  @staticmethod
  def comparingDouble(arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

  @staticmethod
  def comparingInt(arg0: ToIntFunction[T]) -> Comparator[T]: ...

  @staticmethod
  def comparingLong(arg0: ToLongFunction[T]) -> Comparator[T]: ...

  @staticmethod
  def naturalOrder() -> Comparator[T]: ...

  @staticmethod
  def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

  @staticmethod
  def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

  @staticmethod
  def reverseOrder() -> Comparator[T]: ...

  def __init__(self): ...


class ConstraintsParameters:

  def anchorIsJdkCA(self) -> bool: ...

  def extendedExceptionMsg(self) -> str: ...

  def getDate(self) -> Date: ...

  def getKeys(self) -> Set[Key]: ...

  def getVariant(self) -> str: ...


class Debug:

  def getPrintStream(self) -> PrintStream: ...

  @overload
  def println(self) -> None: ...

  @overload
  def println(self, arg0: str) -> None: ...

  @overload
  def println(self, arg0: object, arg1: str) -> None: ...

  @staticmethod
  def Help() -> None: ...

  @staticmethod
  @overload
  def getInstance(arg0: str) -> Debug: ...

  @staticmethod
  @overload
  def getInstance(arg0: str, arg1: str) -> Debug: ...

  @staticmethod
  def isOn(arg0: str) -> bool: ...

  @staticmethod
  def isVerbose() -> bool: ...

  @staticmethod
  def toHexString(arg0: BigInteger) -> str: ...

  @staticmethod
  def toString(arg0: list[int]) -> str: ...

  def __init__(self): ...


class DerInputStream:

  def atEnd(self) -> None: ...

  def available(self) -> int: ...

  def getBMPString(self) -> str: ...

  def getBigInteger(self) -> BigInteger: ...

  def getBitString(self) -> list[int]: ...

  def getDerValue(self) -> DerValue: ...

  def getEnumerated(self) -> int: ...

  def getGeneralString(self) -> str: ...

  def getGeneralizedTime(self) -> Date: ...

  def getIA5String(self) -> str: ...

  def getInteger(self) -> int: ...

  def getNull(self) -> None: ...

  def getOID(self) -> ObjectIdentifier: ...

  def getOctetString(self) -> list[int]: ...

  def getOptional(self, arg0: int) -> Optional[DerValue]: ...

  def getOptionalExplicitContextSpecific(self, arg0: int) -> Optional[DerValue]: ...

  def getOptionalImplicitContextSpecific(self, arg0: int, arg1: int) -> Optional[DerValue]: ...

  def getPositiveBigInteger(self) -> BigInteger: ...

  def getPrintableString(self) -> str: ...

  def getSequence(self, arg0: int) -> list[DerValue]: ...

  @overload
  def getSet(self, arg0: int) -> list[DerValue]: ...

  @overload
  def getSet(self, arg0: int, arg1: bool) -> list[DerValue]: ...

  def getT61String(self) -> str: ...

  def getUTCTime(self) -> Date: ...

  def getUTF8String(self) -> str: ...

  def getUnalignedBitString(self) -> BitArray: ...

  def mark(self, arg0: int) -> None: ...

  def peekByte(self) -> int: ...

  def reset(self) -> None: ...

  def seeOptionalContextSpecific(self, arg0: int) -> bool: ...

  def toByteArray(self) -> list[int]: ...

  @overload
  def __init__(self, arg0: list[int]): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int, arg2: int): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int, arg2: int, arg3: bool): ...


class DerOutputStream(ByteArrayOutputStream):

  @overload
  def derEncode(self, arg0: OutputStream) -> None: ...

  @overload
  def derEncode(self, arg0: OutputStream) -> None: ...

  def putBMPString(self, arg0: str) -> None: ...

  def putBitString(self, arg0: list[int]) -> None: ...

  def putBoolean(self, arg0: bool) -> None: ...

  def putDerValue(self, arg0: DerValue) -> None: ...

  def putEnumerated(self, arg0: int) -> None: ...

  def putGeneralString(self, arg0: str) -> None: ...

  def putGeneralizedTime(self, arg0: Date) -> None: ...

  def putIA5String(self, arg0: str) -> None: ...

  @overload
  def putInteger(self, arg0: list[int]) -> None: ...

  @overload
  def putInteger(self, arg0: int) -> None: ...

  @overload
  def putInteger(self, arg0: Integer) -> None: ...

  @overload
  def putInteger(self, arg0: BigInteger) -> None: ...

  def putLength(self, arg0: int) -> None: ...

  def putNull(self) -> None: ...

  def putOID(self, arg0: ObjectIdentifier) -> None: ...

  def putOctetString(self, arg0: list[int]) -> None: ...

  def putOrderedSet(self, arg0: int, arg1: list[DerEncoder]) -> None: ...

  def putOrderedSetOf(self, arg0: int, arg1: list[DerEncoder]) -> None: ...

  def putPrintableString(self, arg0: str) -> None: ...

  def putSequence(self, arg0: list[DerValue]) -> None: ...

  def putSet(self, arg0: list[DerValue]) -> None: ...

  def putT61String(self, arg0: str) -> None: ...

  def putTag(self, arg0: int, arg1: bool, arg2: int) -> None: ...

  def putTruncatedUnalignedBitString(self, arg0: BitArray) -> None: ...

  def putUTCTime(self, arg0: Date) -> None: ...

  def putUTF8String(self, arg0: str) -> None: ...

  def putUnalignedBitString(self, arg0: BitArray) -> None: ...

  @overload
  def write(self, arg0: int, arg1: list[int]) -> None: ...

  @overload
  def write(self, arg0: int, arg1: DerOutputStream) -> None: ...

  def writeImplicit(self, arg0: int, arg1: DerOutputStream) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...


class DerValue:

  TAG_APPLICATION: int

  tag_BitString: int

  tag_BMPString: int

  tag_Boolean: int

  TAG_CONTEXT: int

  tag_Enumerated: int

  tag_GeneralizedTime: int

  tag_GeneralString: int

  tag_IA5String: int

  tag_Integer: int

  tag_Null: int

  tag_ObjectId: int

  tag_OctetString: int

  tag_PrintableString: int

  TAG_PRIVATE: int

  tag_Sequence: int

  tag_SequenceOf: int

  tag_Set: int

  tag_SetOf: int

  tag_T61String: int

  TAG_UNIVERSAL: int

  tag_UniversalString: int

  tag_UtcTime: int

  tag_UTF8String: int

  def clear(self) -> None: ...

  def data(self) -> DerInputStream: ...

  def encode(self, arg0: DerOutputStream) -> None: ...

  def equals(self, arg0: object) -> bool: ...

  def getAsString(self) -> str: ...

  def getBMPString(self) -> str: ...

  def getBigInteger(self) -> BigInteger: ...

  @overload
  def getBitString(self) -> list[int]: ...

  @overload
  def getBitString(self, arg0: bool) -> list[int]: ...

  def getBoolean(self) -> bool: ...

  def getData(self) -> DerInputStream: ...

  def getDataBytes(self) -> list[int]: ...

  def getEnumerated(self) -> int: ...

  def getGeneralString(self) -> str: ...

  def getGeneralizedTime(self) -> Date: ...

  def getIA5String(self) -> str: ...

  def getInteger(self) -> int: ...

  def getNull(self) -> None: ...

  def getOID(self) -> ObjectIdentifier: ...

  def getOctetString(self) -> list[int]: ...

  def getPositiveBigInteger(self) -> BigInteger: ...

  def getPrintableString(self) -> str: ...

  def getT61String(self) -> str: ...

  def getTag(self) -> int: ...

  def getUTCTime(self) -> Date: ...

  def getUTF8String(self) -> str: ...

  @overload
  def getUnalignedBitString(self) -> BitArray: ...

  @overload
  def getUnalignedBitString(self, arg0: bool) -> BitArray: ...

  def getUniversalString(self) -> str: ...

  def hashCode(self) -> int: ...

  def isApplication(self) -> bool: ...

  @overload
  def isConstructed(self) -> bool: ...

  @overload
  def isConstructed(self, arg0: int) -> bool: ...

  @overload
  def isContextSpecific(self) -> bool: ...

  @overload
  def isContextSpecific(self, arg0: int) -> bool: ...

  def isUniversal(self) -> bool: ...

  def length(self) -> int: ...

  def resetTag(self, arg0: int) -> None: ...

  def subs(self, arg0: int, arg1: int) -> list[DerValue]: ...

  def toByteArray(self) -> list[int]: ...

  def toDerInputStream(self) -> DerInputStream: ...

  def toString(self) -> str: ...

  def withTag(self, arg0: int) -> DerValue: ...

  @staticmethod
  def createTag(arg0: int, arg1: bool, arg2: int) -> int: ...

  @staticmethod
  def isPrintableStringChar(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def wrap(arg0: list[int]) -> DerValue: ...

  @staticmethod
  @overload
  def wrap(arg0: int, arg1: DerOutputStream) -> DerValue: ...

  @staticmethod
  @overload
  def wrap(arg0: list[int], arg1: int, arg2: int) -> DerValue: ...

  @overload
  def __init__(self, arg0: list[int]):
    self.data: DerInputStream

    self.tag: int

  @overload
  def __init__(self, arg0: InputStream): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: int, arg1: list[int]): ...
  @overload
  def __init__(self, arg0: int, arg1: str): ...


class JarConstraintsParameters:

  @overload
  def anchorIsJdkCA(self) -> bool: ...

  @overload
  def anchorIsJdkCA(self) -> bool: ...

  @overload
  def extendedExceptionMsg(self) -> str: ...

  @overload
  def extendedExceptionMsg(self) -> str: ...

  @overload
  def getDate(self) -> Date: ...

  @overload
  def getDate(self) -> Date: ...

  @overload
  def getKeys(self) -> Set[Key]: ...

  @overload
  def getKeys(self) -> Set[Key]: ...

  @overload
  def getVariant(self) -> str: ...

  @overload
  def getVariant(self) -> str: ...

  def setExtendedExceptionMsg(self, arg0: str, arg1: str) -> None: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self, arg0: list[CodeSigner]): ...
  @overload
  def __init__(self, arg0: List[X509Certificate], arg1: Date): ...


class KnownOIDs(Enum):

  AD_TimeStamping: KnownOIDs

  AES: KnownOIDs

  AES_128$CBC$NoPadding: KnownOIDs

  AES_128$CFB$NoPadding: KnownOIDs

  AES_128$ECB$NoPadding: KnownOIDs

  AES_128$GCM$NoPadding: KnownOIDs

  AES_128$KW$NoPadding: KnownOIDs

  AES_128$KWP$NoPadding: KnownOIDs

  AES_128$OFB$NoPadding: KnownOIDs

  AES_192$CBC$NoPadding: KnownOIDs

  AES_192$CFB$NoPadding: KnownOIDs

  AES_192$ECB$NoPadding: KnownOIDs

  AES_192$GCM$NoPadding: KnownOIDs

  AES_192$KW$NoPadding: KnownOIDs

  AES_192$KWP$NoPadding: KnownOIDs

  AES_192$OFB$NoPadding: KnownOIDs

  AES_256$CBC$NoPadding: KnownOIDs

  AES_256$CFB$NoPadding: KnownOIDs

  AES_256$ECB$NoPadding: KnownOIDs

  AES_256$GCM$NoPadding: KnownOIDs

  AES_256$KW$NoPadding: KnownOIDs

  AES_256$KWP$NoPadding: KnownOIDs

  AES_256$OFB$NoPadding: KnownOIDs

  anyExtendedKeyUsage: KnownOIDs

  ARCFOUR: KnownOIDs

  AuthInfoAccess: KnownOIDs

  AuthorityKeyID: KnownOIDs

  BasicConstraints: KnownOIDs

  brainpoolP160r1: KnownOIDs

  brainpoolP192r1: KnownOIDs

  brainpoolP224r1: KnownOIDs

  brainpoolP256r1: KnownOIDs

  brainpoolP320r1: KnownOIDs

  brainpoolP384r1: KnownOIDs

  brainpoolP512r1: KnownOIDs

  c2tnb191v1: KnownOIDs

  c2tnb191v2: KnownOIDs

  c2tnb191v3: KnownOIDs

  c2tnb239v1: KnownOIDs

  c2tnb239v2: KnownOIDs

  c2tnb239v3: KnownOIDs

  c2tnb359v1: KnownOIDs

  c2tnb431r1: KnownOIDs

  caIssuers: KnownOIDs

  caRepository: KnownOIDs

  CE_CERT_POLICIES_ANY: KnownOIDs

  CertBag: KnownOIDs

  CertificateIssuer: KnownOIDs

  CertificatePolicies: KnownOIDs

  CertTypeX509: KnownOIDs

  CHACHA20_POLY1305: KnownOIDs

  ChallengePassword: KnownOIDs

  clientAuth: KnownOIDs

  CMSAlgorithmProtection: KnownOIDs

  codeSigning: KnownOIDs

  CommonName: KnownOIDs

  ContentType: KnownOIDs

  CounterSignature: KnownOIDs

  CountryName: KnownOIDs

  CRLDistributionPoints: KnownOIDs

  CRLNumber: KnownOIDs

  Data: KnownOIDs

  DeltaCRLIndicator: KnownOIDs

  DESede: KnownOIDs

  DESede$CBC$NoPadding: KnownOIDs

  DiffieHellman: KnownOIDs

  DigestedData: KnownOIDs

  DNQualifier: KnownOIDs

  DSA: KnownOIDs

  EC: KnownOIDs

  ECDH: KnownOIDs

  Ed25519: KnownOIDs

  Ed448: KnownOIDs

  EmailAddress: KnownOIDs

  emailProtection: KnownOIDs

  EncryptedData: KnownOIDs

  EnvelopedData: KnownOIDs

  ExtendedCertificateAttributes: KnownOIDs

  extendedKeyUsage: KnownOIDs

  ExtensionRequest: KnownOIDs

  FreshestCRL: KnownOIDs

  FriendlyName: KnownOIDs

  GenerationQualifier: KnownOIDs

  GivenName: KnownOIDs

  HmacSHA1: KnownOIDs

  HmacSHA224: KnownOIDs

  HmacSHA256: KnownOIDs

  HmacSHA384: KnownOIDs

  HmacSHA3_224: KnownOIDs

  HmacSHA3_256: KnownOIDs

  HmacSHA3_384: KnownOIDs

  HmacSHA3_512: KnownOIDs

  HmacSHA512: KnownOIDs

  HmacSHA512$224: KnownOIDs

  HmacSHA512$256: KnownOIDs

  HoldInstructionCode: KnownOIDs

  InhibitAnyPolicy: KnownOIDs

  Initials: KnownOIDs

  InvalidityDate: KnownOIDs

  ipsecEndSystem: KnownOIDs

  ipsecTunnel: KnownOIDs

  ipsecUser: KnownOIDs

  IssuerAlternativeName: KnownOIDs

  IssuerAndSerialNumber: KnownOIDs

  IssuingDistributionPoint: KnownOIDs

  ITUX509_RSA: KnownOIDs

  JAVASOFT_JCEKeyProtector: KnownOIDs

  JAVASOFT_JDKKeyProtector: KnownOIDs

  JDK_OLD_Data: KnownOIDs

  JDK_OLD_SignedData: KnownOIDs

  KeyUsage: KnownOIDs

  KP_TimeStamping: KnownOIDs

  LocalityName: KnownOIDs

  LocalKeyID: KnownOIDs

  MD2: KnownOIDs

  MD2withRSA: KnownOIDs

  MD5: KnownOIDs

  MD5withRSA: KnownOIDs

  MessageDigest: KnownOIDs

  MGF1: KnownOIDs

  MICROSOFT_ExportApproved: KnownOIDs

  NameConstraints: KnownOIDs

  NETSCAPE_CertSequence: KnownOIDs

  NETSCAPE_CertType: KnownOIDs

  NETSCAPE_ExportApproved: KnownOIDs

  OAEP: KnownOIDs

  OCSP: KnownOIDs

  OCSPBasicResponse: KnownOIDs

  OCSPNoCheck: KnownOIDs

  OCSPNonceExt: KnownOIDs

  OCSPSigning: KnownOIDs

  OIW_DES_CBC: KnownOIDs

  OIW_DSA: KnownOIDs

  OIW_JDK_SHA1withDSA: KnownOIDs

  OIW_SHA1withDSA: KnownOIDs

  OIW_SHA1withRSA: KnownOIDs

  OIW_SHA1withRSA_Odd: KnownOIDs

  ORACLE_TrustedKeyUsage: KnownOIDs

  OrgName: KnownOIDs

  OrgUnitName: KnownOIDs

  PBES2: KnownOIDs

  PBEWithMD5AndDES: KnownOIDs

  PBEWithMD5AndRC2: KnownOIDs

  PBEWithSHA1AndDES: KnownOIDs

  PBEWithSHA1AndDESede: KnownOIDs

  PBEWithSHA1AndRC2: KnownOIDs

  PBEWithSHA1AndRC2_128: KnownOIDs

  PBEWithSHA1AndRC2_40: KnownOIDs

  PBEWithSHA1AndRC4_128: KnownOIDs

  PBEWithSHA1AndRC4_40: KnownOIDs

  PBKDF2WithHmacSHA1: KnownOIDs

  PKCS1: KnownOIDs

  PKCS7: KnownOIDs

  PKCS8ShroudedKeyBag: KnownOIDs

  PolicyConstraints: KnownOIDs

  PolicyMappings: KnownOIDs

  prime192v2: KnownOIDs

  prime192v3: KnownOIDs

  prime239v1: KnownOIDs

  prime239v2: KnownOIDs

  prime239v3: KnownOIDs

  PrivateKeyUsage: KnownOIDs

  PSpecified: KnownOIDs

  RC2$CBC$PKCS5Padding: KnownOIDs

  RC5$CBC$PKCS5Padding: KnownOIDs

  ReasonCode: KnownOIDs

  RSA: KnownOIDs

  RSASSA_PSS: KnownOIDs

  secp112r1: KnownOIDs

  secp112r2: KnownOIDs

  secp128r1: KnownOIDs

  secp128r2: KnownOIDs

  secp160k1: KnownOIDs

  secp160r1: KnownOIDs

  secp160r2: KnownOIDs

  secp192k1: KnownOIDs

  secp192r1: KnownOIDs

  secp224k1: KnownOIDs

  secp224r1: KnownOIDs

  secp256k1: KnownOIDs

  secp256r1: KnownOIDs

  secp384r1: KnownOIDs

  secp521r1: KnownOIDs

  SecretBag: KnownOIDs

  sect113r1: KnownOIDs

  sect113r2: KnownOIDs

  sect131r1: KnownOIDs

  sect131r2: KnownOIDs

  sect163k1: KnownOIDs

  sect163r1: KnownOIDs

  sect163r2: KnownOIDs

  sect193r1: KnownOIDs

  sect193r2: KnownOIDs

  sect233k1: KnownOIDs

  sect233r1: KnownOIDs

  sect239k1: KnownOIDs

  sect283k1: KnownOIDs

  sect283r1: KnownOIDs

  sect409k1: KnownOIDs

  sect409r1: KnownOIDs

  sect571k1: KnownOIDs

  sect571r1: KnownOIDs

  SerialNumber: KnownOIDs

  serverAuth: KnownOIDs

  SHA1withDSA: KnownOIDs

  SHA1withECDSA: KnownOIDs

  SHA1withRSA: KnownOIDs

  SHA224withDSA: KnownOIDs

  SHA224withECDSA: KnownOIDs

  SHA224withRSA: KnownOIDs

  SHA256withDSA: KnownOIDs

  SHA256withECDSA: KnownOIDs

  SHA256withRSA: KnownOIDs

  SHA384withDSA: KnownOIDs

  SHA384withECDSA: KnownOIDs

  SHA384withRSA: KnownOIDs

  SHA3_224: KnownOIDs

  SHA3_224withDSA: KnownOIDs

  SHA3_224withECDSA: KnownOIDs

  SHA3_224withRSA: KnownOIDs

  SHA3_256: KnownOIDs

  SHA3_256withDSA: KnownOIDs

  SHA3_256withECDSA: KnownOIDs

  SHA3_256withRSA: KnownOIDs

  SHA3_384: KnownOIDs

  SHA3_384withDSA: KnownOIDs

  SHA3_384withECDSA: KnownOIDs

  SHA3_384withRSA: KnownOIDs

  SHA3_512: KnownOIDs

  SHA3_512withDSA: KnownOIDs

  SHA3_512withECDSA: KnownOIDs

  SHA3_512withRSA: KnownOIDs

  SHA512$224withRSA: KnownOIDs

  SHA512$256withRSA: KnownOIDs

  SHA512withDSA: KnownOIDs

  SHA512withECDSA: KnownOIDs

  SHA512withRSA: KnownOIDs

  SHA_1: KnownOIDs

  SHA_224: KnownOIDs

  SHA_256: KnownOIDs

  SHA_384: KnownOIDs

  SHA_512: KnownOIDs

  SHA_512$224: KnownOIDs

  SHA_512$256: KnownOIDs

  SHAKE128: KnownOIDs

  SHAKE128_LEN: KnownOIDs

  SHAKE256: KnownOIDs

  SHAKE256_LEN: KnownOIDs

  SignatureTimestampToken: KnownOIDs

  SignedAndEnvelopedData: KnownOIDs

  SignedData: KnownOIDs

  SigningCertificate: KnownOIDs

  SigningTime: KnownOIDs

  SkipIPAddress: KnownOIDs

  SMIMECapability: KnownOIDs

  SpecifiedSHA2withECDSA: KnownOIDs

  StateName: KnownOIDs

  StreetAddress: KnownOIDs

  SubjectAlternativeName: KnownOIDs

  SubjectDirectoryAttributes: KnownOIDs

  SubjectInfoAccess: KnownOIDs

  SubjectKeyID: KnownOIDs

  Surname: KnownOIDs

  TimeStampTokenInfo: KnownOIDs

  Title: KnownOIDs

  UCL_DomainComponent: KnownOIDs

  UCL_UserID: KnownOIDs

  UnstructuredAddress: KnownOIDs

  UnstructuredName: KnownOIDs

  X25519: KnownOIDs

  X448: KnownOIDs

  X942_DH: KnownOIDs

  def aliases(self) -> list[str]: ...

  def stdName(self) -> str: ...

  def value(self) -> str: ...

  @staticmethod
  def findMatch(arg0: str) -> KnownOIDs: ...

  @staticmethod
  def valueOf(arg0: str) -> KnownOIDs: ...

  @staticmethod
  def values() -> list[KnownOIDs]: ...


class LazyCodeSourcePermissionCollection(PermissionCollection):

  def add(self, arg0: Permission) -> None: ...

  def elements(self) -> Enumeration[Permission]: ...

  def implies(self, arg0: Permission) -> bool: ...

  def toString(self) -> str: ...

  def __init__(self, arg0: PermissionCollection, arg1: CodeSource): ...


class ManifestDigester:

  MF_MAIN_ATTRS: str

  @overload
  def get(self, arg0: str) -> ManifestDigester.Entry: ...

  @overload
  def get(self, arg0: str, arg1: bool) -> ManifestDigester.Entry: ...

  @overload
  def getMainAttsEntry(self) -> ManifestDigester.Entry: ...

  @overload
  def getMainAttsEntry(self, arg0: bool) -> ManifestDigester.Entry: ...

  def manifestDigest(self, arg0: MessageDigest) -> list[int]: ...

  def __init__(self, arg0: list[int]): ...

  class Position: ...

  class Entry:

    def digest(self, arg0: MessageDigest) -> list[int]: ...

    def digestWorkaround(self, arg0: MessageDigest) -> list[int]: ...

    def isProperlyDelimited(self) -> bool: ...

    def reproduceRaw(self, arg0: OutputStream) -> None: ...

    def __init__(self): ...

  class Section:

    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: list[int]): ...


class ManifestEntryVerifier:

  def getEntry(self) -> JarEntry: ...

  def setEntry(self, arg0: str, arg1: JarEntry) -> None: ...

  @overload
  def update(self, arg0: int) -> None: ...

  @overload
  def update(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  def verify(self, arg0: Hashtable[str, CodeSigner], arg1: Hashtable[str, CodeSigner], arg2: Map[CodeSigner, Map[str, Boolean]]) -> list[CodeSigner]: ...

  def __init__(self, arg0: Manifest, arg1: str): ...

  class SunProviderHolder: ...


class MessageDigestSpi2:

  def engineUpdate(self, arg0: SecretKey) -> None: ...


class ObjectIdentifier:

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def of(arg0: str) -> ObjectIdentifier: ...

  @staticmethod
  @overload
  def of(arg0: KnownOIDs) -> ObjectIdentifier: ...

  def __init__(self, arg0: DerInputStream): ...

  class HugeOidNotSupportedByOldJDK: ...


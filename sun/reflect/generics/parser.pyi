from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from sun.reflect.generics.tree import ClassSignature, MethodTypeSignature, TypeSignature

class SignatureParser:

  def parseClassSig(self, arg0: str) -> ClassSignature: ...

  def parseMethodSig(self, arg0: str) -> MethodTypeSignature: ...

  def parseTypeSig(self, arg0: str) -> TypeSignature: ...

  @staticmethod
  def make() -> SignatureParser: ...


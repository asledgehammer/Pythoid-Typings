from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from zombie import SandboxOptions

class CustomBooleanSandboxOption(CustomSandboxOption): ...


class CustomDoubleSandboxOption(CustomSandboxOption): ...


class CustomEnumSandboxOption(CustomSandboxOption): ...


class CustomIntegerSandboxOption(CustomSandboxOption): ...


class CustomSandboxOption: ...


class CustomSandboxOptions:

  instance: CustomSandboxOptions

  def init(self) -> None: ...

  def initInstance(self, options: SandboxOptions) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  def __init__(self): ...


class CustomStringSandboxOption(CustomSandboxOption): ...


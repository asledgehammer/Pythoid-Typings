from typing import Any
from java.lang import Class

class Pythoid:

    @staticmethod
    def expose(clazz: Any) -> None: ...

    @staticmethod
    def invoke(instance: object, methodName: str, *args) -> Any: ...

    @staticmethod
    def invokeStatic(clazz: Class, methodName: str, *args) -> Any: ...

    @staticmethod
    def getField(instance: object, fieldName: str) -> Any: ...

    @staticmethod
    def getStaticField(clazz: Class, fieldName: str) -> Any: ... 

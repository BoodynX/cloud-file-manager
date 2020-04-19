from typing import Type


class TypeCheckParameterError(Exception):
    pass


class CustomTypeError(TypeError):
    pass


def tc(obj: object, type_: Type):
    """
    Type Checker function
    """
    if not isinstance(type_, Type):
        raise TypeCheckParameterError()

    """
    Type checking helper
    """
    if not isinstance(obj, type_):
        raise CustomTypeError(f'Expecting {type_} instead received {type(obj)}')

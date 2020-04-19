from typing import Type

from src.domain.exceptions.custom_type_error import CustomTypeError
from src.domain.exceptions.type_check_parameter_error import TypeCheckParameterError


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

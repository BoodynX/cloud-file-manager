from src.application.errors.general import CustomTypeError


def tc(obj, cls):
    """
    Type checking helper
    """
    if not isinstance(obj, cls):
        raise CustomTypeError(f'Expecting {cls} instead received {type(obj)}')

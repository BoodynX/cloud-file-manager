from unittest import TestCase

from src.domain.utils import tc, TypeCheckParameterError, CustomTypeError


class UnexpectedExample:
    pass


class ExpectedExample:
    pass


class TestTc(TestCase):
    def test_not_a_Type_as_second_param__raise_incorrect_type_check_parameter_exception(self):
        self.assertRaises(TypeCheckParameterError, tc, ExpectedExample, None)

    def test_wrong_type__raise_custom_type_exception(self):
        self.assertRaises(CustomTypeError, tc, UnexpectedExample(), ExpectedExample)

    def test_expected_type__return_None(self):
        result = tc(ExpectedExample(), ExpectedExample)
        self.assertIsNone(result)

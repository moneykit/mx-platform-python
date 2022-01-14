"""
    MX Platform API

    The MX Platform API is a powerful, fully-featured API designed to make aggregating and enhancing financial data easy and reliable. It can seamlessly connect your app or website to tens of thousands of financial institutions.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from mx_platform_python.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from mx_platform_python.exceptions import ApiAttributeError



class TransactionResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'account_guid': (str,),  # noqa: E501
            'account_id': (str, none_type,),  # noqa: E501
            'amount': (float, none_type,),  # noqa: E501
            'category': (str, none_type,),  # noqa: E501
            'category_guid': (str, none_type,),  # noqa: E501
            'check_number_string': (str, none_type,),  # noqa: E501
            'created_at': (str, none_type,),  # noqa: E501
            'currency_code': (str, none_type,),  # noqa: E501
            'date': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'extended_transaction_type': (str, none_type,),  # noqa: E501
            'guid': (str,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'is_bill_pay': (bool, none_type,),  # noqa: E501
            'is_direct_deposit': (bool, none_type,),  # noqa: E501
            'is_expense': (bool, none_type,),  # noqa: E501
            'is_fee': (bool, none_type,),  # noqa: E501
            'is_income': (bool, none_type,),  # noqa: E501
            'is_international': (bool, none_type,),  # noqa: E501
            'is_overdraft_fee': (bool, none_type,),  # noqa: E501
            'is_payroll_advance': (bool, none_type,),  # noqa: E501
            'is_recurring': (bool, none_type,),  # noqa: E501
            'is_subscription': (bool, none_type,),  # noqa: E501
            'latitude': (float, none_type,),  # noqa: E501
            'localized_description': (str, none_type,),  # noqa: E501
            'localized_memo': (str, none_type,),  # noqa: E501
            'longitude': (float, none_type,),  # noqa: E501
            'member_guid': (str,),  # noqa: E501
            'member_is_managed_by_user': (bool, none_type,),  # noqa: E501
            'memo': (str, none_type,),  # noqa: E501
            'merchant_category_code': (int, none_type,),  # noqa: E501
            'merchant_guid': (str,),  # noqa: E501
            'merchant_location_guid': (str,),  # noqa: E501
            'metadata': (str, none_type,),  # noqa: E501
            'original_description': (str, none_type,),  # noqa: E501
            'posted_at': (str, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'top_level_category': (str, none_type,),  # noqa: E501
            'transacted_at': (str, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'updated_at': (str, none_type,),  # noqa: E501
            'user_guid': (str,),  # noqa: E501
            'user_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'account_guid': 'account_guid',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'category': 'category',  # noqa: E501
        'category_guid': 'category_guid',  # noqa: E501
        'check_number_string': 'check_number_string',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'currency_code': 'currency_code',  # noqa: E501
        'date': 'date',  # noqa: E501
        'description': 'description',  # noqa: E501
        'extended_transaction_type': 'extended_transaction_type',  # noqa: E501
        'guid': 'guid',  # noqa: E501
        'id': 'id',  # noqa: E501
        'is_bill_pay': 'is_bill_pay',  # noqa: E501
        'is_direct_deposit': 'is_direct_deposit',  # noqa: E501
        'is_expense': 'is_expense',  # noqa: E501
        'is_fee': 'is_fee',  # noqa: E501
        'is_income': 'is_income',  # noqa: E501
        'is_international': 'is_international',  # noqa: E501
        'is_overdraft_fee': 'is_overdraft_fee',  # noqa: E501
        'is_payroll_advance': 'is_payroll_advance',  # noqa: E501
        'is_recurring': 'is_recurring',  # noqa: E501
        'is_subscription': 'is_subscription',  # noqa: E501
        'latitude': 'latitude',  # noqa: E501
        'localized_description': 'localized_description',  # noqa: E501
        'localized_memo': 'localized_memo',  # noqa: E501
        'longitude': 'longitude',  # noqa: E501
        'member_guid': 'member_guid',  # noqa: E501
        'member_is_managed_by_user': 'member_is_managed_by_user',  # noqa: E501
        'memo': 'memo',  # noqa: E501
        'merchant_category_code': 'merchant_category_code',  # noqa: E501
        'merchant_guid': 'merchant_guid',  # noqa: E501
        'merchant_location_guid': 'merchant_location_guid',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'original_description': 'original_description',  # noqa: E501
        'posted_at': 'posted_at',  # noqa: E501
        'status': 'status',  # noqa: E501
        'top_level_category': 'top_level_category',  # noqa: E501
        'transacted_at': 'transacted_at',  # noqa: E501
        'type': 'type',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'user_guid': 'user_guid',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TransactionResponse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            account_guid (str): [optional]  # noqa: E501
            account_id (str, none_type): [optional]  # noqa: E501
            amount (float, none_type): [optional]  # noqa: E501
            category (str, none_type): [optional]  # noqa: E501
            category_guid (str, none_type): [optional]  # noqa: E501
            check_number_string (str, none_type): [optional]  # noqa: E501
            created_at (str, none_type): [optional]  # noqa: E501
            currency_code (str, none_type): [optional]  # noqa: E501
            date (str, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            extended_transaction_type (str, none_type): [optional]  # noqa: E501
            guid (str): [optional]  # noqa: E501
            id (str, none_type): [optional]  # noqa: E501
            is_bill_pay (bool, none_type): [optional]  # noqa: E501
            is_direct_deposit (bool, none_type): [optional]  # noqa: E501
            is_expense (bool, none_type): [optional]  # noqa: E501
            is_fee (bool, none_type): [optional]  # noqa: E501
            is_income (bool, none_type): [optional]  # noqa: E501
            is_international (bool, none_type): [optional]  # noqa: E501
            is_overdraft_fee (bool, none_type): [optional]  # noqa: E501
            is_payroll_advance (bool, none_type): [optional]  # noqa: E501
            is_recurring (bool, none_type): [optional]  # noqa: E501
            is_subscription (bool, none_type): [optional]  # noqa: E501
            latitude (float, none_type): [optional]  # noqa: E501
            localized_description (str, none_type): [optional]  # noqa: E501
            localized_memo (str, none_type): [optional]  # noqa: E501
            longitude (float, none_type): [optional]  # noqa: E501
            member_guid (str): [optional]  # noqa: E501
            member_is_managed_by_user (bool, none_type): [optional]  # noqa: E501
            memo (str, none_type): [optional]  # noqa: E501
            merchant_category_code (int, none_type): [optional]  # noqa: E501
            merchant_guid (str): [optional]  # noqa: E501
            merchant_location_guid (str): [optional]  # noqa: E501
            metadata (str, none_type): [optional]  # noqa: E501
            original_description (str, none_type): [optional]  # noqa: E501
            posted_at (str, none_type): [optional]  # noqa: E501
            status (str, none_type): [optional]  # noqa: E501
            top_level_category (str, none_type): [optional]  # noqa: E501
            transacted_at (str, none_type): [optional]  # noqa: E501
            type (str, none_type): [optional]  # noqa: E501
            updated_at (str, none_type): [optional]  # noqa: E501
            user_guid (str): [optional]  # noqa: E501
            user_id (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """TransactionResponse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            account_guid (str): [optional]  # noqa: E501
            account_id (str, none_type): [optional]  # noqa: E501
            amount (float, none_type): [optional]  # noqa: E501
            category (str, none_type): [optional]  # noqa: E501
            category_guid (str, none_type): [optional]  # noqa: E501
            check_number_string (str, none_type): [optional]  # noqa: E501
            created_at (str, none_type): [optional]  # noqa: E501
            currency_code (str, none_type): [optional]  # noqa: E501
            date (str, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            extended_transaction_type (str, none_type): [optional]  # noqa: E501
            guid (str): [optional]  # noqa: E501
            id (str, none_type): [optional]  # noqa: E501
            is_bill_pay (bool, none_type): [optional]  # noqa: E501
            is_direct_deposit (bool, none_type): [optional]  # noqa: E501
            is_expense (bool, none_type): [optional]  # noqa: E501
            is_fee (bool, none_type): [optional]  # noqa: E501
            is_income (bool, none_type): [optional]  # noqa: E501
            is_international (bool, none_type): [optional]  # noqa: E501
            is_overdraft_fee (bool, none_type): [optional]  # noqa: E501
            is_payroll_advance (bool, none_type): [optional]  # noqa: E501
            is_recurring (bool, none_type): [optional]  # noqa: E501
            is_subscription (bool, none_type): [optional]  # noqa: E501
            latitude (float, none_type): [optional]  # noqa: E501
            localized_description (str, none_type): [optional]  # noqa: E501
            localized_memo (str, none_type): [optional]  # noqa: E501
            longitude (float, none_type): [optional]  # noqa: E501
            member_guid (str): [optional]  # noqa: E501
            member_is_managed_by_user (bool, none_type): [optional]  # noqa: E501
            memo (str, none_type): [optional]  # noqa: E501
            merchant_category_code (int, none_type): [optional]  # noqa: E501
            merchant_guid (str): [optional]  # noqa: E501
            merchant_location_guid (str): [optional]  # noqa: E501
            metadata (str, none_type): [optional]  # noqa: E501
            original_description (str, none_type): [optional]  # noqa: E501
            posted_at (str, none_type): [optional]  # noqa: E501
            status (str, none_type): [optional]  # noqa: E501
            top_level_category (str, none_type): [optional]  # noqa: E501
            transacted_at (str, none_type): [optional]  # noqa: E501
            type (str, none_type): [optional]  # noqa: E501
            updated_at (str, none_type): [optional]  # noqa: E501
            user_guid (str): [optional]  # noqa: E501
            user_id (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

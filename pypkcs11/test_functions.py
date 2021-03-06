#
# Please note that this file has been modified by Unbound Tech
#
"""
Functions used for testing, or verifying return values.
"""
import sys
import logging
from ctypes import byref

if sys.version_info < (3,):
    integer_types = (int, long,)
else:
    integer_types = (int,)

from .cryptoki import CK_OBJECT_HANDLE, CK_ULONG, C_GetObjectSize
from .defines import CKR_OBJECT_HANDLE_INVALID
from .defines import CKR_OK
from .lookup_dicts import ret_vals_dictionary
from .exceptions import CryptokiCallException
from .object_attr_lookup import c_get_attribute_value

LOG = logging.getLogger(__name__)


def assert_test_return_value(value, expected_value, message, print_on_success=True):
    """Asserts a pass or fail based on whether the value parameter is equal to the expected_value
    parameter.
    Used to test the results of pkcs11 functions and looks up human readable strings for the
    various error codes.
    Prints out results in a consistent format.

    :param value: The return value of the pkcs11 function
    :param expected_value: The expected return value to be tested against
    :param message: Message to print on success/failure
    :param print_on_success: Whether or not to print if the test case passes (Default value = True)

    """
    if value in ret_vals_dictionary:
        code = ret_vals_dictionary[value]
    else:
        code = "Unknown Code=" + str(hex(value))

    if expected_value in ret_vals_dictionary:
        exp_code = ret_vals_dictionary[expected_value]
    else:
        exp_code = "Unknown Code=" + str(hex(value))

    assert value == expected_value, "\nERROR: " + message + "\n\tExpected: " + exp_code + \
                                    "\n\tFound: " + code
    if print_on_success:
        LOG.info("%s: %s", exp_code, message)


def verify_object_attributes(h_session, h_object, expected_template):
    """Verifies that an object generated has the correct attributes on the board.
    The expected attributes are passed in alongside the handle of the object.

    :param int h_session: Session handle
    :param h_object: Handle of the object to verify the attributes against
    :param expected_template: The expected template to compare against

    """

    # VERIFY OBJECT EXISTS
    h_object = CK_OBJECT_HANDLE(h_object)
    us_size = CK_ULONG()
    ret = C_GetObjectSize(h_session, h_object, byref(us_size))
    assert ret == CKR_OK, "Object " + str(h_object) + " exists"
    assert us_size.value > 0, \
        "Object " + str(h_object.value) + " size is greater than zero."

    # VERIFY ATTRIBUTES are the same as the ones passed in
    desired_attrs = {x: None for x in expected_template.keys()}
    ret, attr = c_get_attribute_value(
        h_session, h_object, template=desired_attrs)
    assert ret == CKR_OK and attr == expected_template


def verify_object_exists(h_session, h_object, should_exist=True):
    """Checks whether an object exists. Asserts that it exists.

    :param int h_session: Session handle
    :param h_object: The object to verify if it exists
    :param should_exist: Whether or not the parameter should exist (Default value = True)

    """
    # VERIFY OBJECT EXISTS
    h_object = CK_OBJECT_HANDLE(h_object)
    us_size = CK_ULONG()

    if should_exist:
        expected_ret = CKR_OK
        out = "Verifying object " + str(h_object) + " exists."
    else:
        expected_ret = CKR_OBJECT_HANDLE_INVALID
        out = "Verifying object " + str(h_object) + " doesn't exist."

    try:
        ret = C_GetObjectSize(h_session, h_object, byref(us_size))
    except CryptokiCallException as e:
        assert e.error_code == expected_ret, out
    else:
        assert ret == expected_ret, out

    if should_exist:
        assert_test_return_value(ret, CKR_OK, "Getting object " + str(h_object.value) + "'s size",
                                 True)
        assert us_size.value > 0, \
            "Object " + str(h_object.value) + " size is greater than zero."
    else:
        assert_test_return_value(ret, CKR_OBJECT_HANDLE_INVALID,
                                 "Getting object " +
                                 str(h_object.value) + "'s size",
                                 True)
        assert us_size.value <= 0, \
            "Object " + str(h_object.value) + " size is greater than zero."

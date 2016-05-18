"""
THIS FILE WAS CREATED AUTOMATICALLY AND CONTAINS AUTOMATICALLY GENERATED CODE
This file should NOT be checked into MKS or modified in any way, this file was
created by setup/initialize.py. Any changes to this file will be wiped out when
it is regenerated.

This file contains a dictionary lookup for the readable string values
of defines whose variable name starts with CKR_. This convention means they are
a return value for the cryptoki C API.

"""

from defines import *

ret_vals_dictionary = {
    CKR_OK: 'CKR_OK',
    CKR_CANCEL: 'CKR_CANCEL',
    CKR_HOST_MEMORY: 'CKR_HOST_MEMORY',
    CKR_SLOT_ID_INVALID: 'CKR_SLOT_ID_INVALID',
    CKR_GENERAL_ERROR: 'CKR_GENERAL_ERROR',
    CKR_FUNCTION_FAILED: 'CKR_FUNCTION_FAILED',
    CKR_ARGUMENTS_BAD: 'CKR_ARGUMENTS_BAD',
    CKR_NO_EVENT: 'CKR_NO_EVENT',
    CKR_NEED_TO_CREATE_THREADS: 'CKR_NEED_TO_CREATE_THREADS',
    CKR_CANT_LOCK: 'CKR_CANT_LOCK',
    CKR_ATTRIBUTE_READ_ONLY: 'CKR_ATTRIBUTE_READ_ONLY',
    CKR_ATTRIBUTE_SENSITIVE: 'CKR_ATTRIBUTE_SENSITIVE',
    CKR_ATTRIBUTE_TYPE_INVALID: 'CKR_ATTRIBUTE_TYPE_INVALID',
    CKR_ATTRIBUTE_VALUE_INVALID: 'CKR_ATTRIBUTE_VALUE_INVALID',
    CKR_DATA_INVALID: 'CKR_DATA_INVALID',
    CKR_DATA_LEN_RANGE: 'CKR_DATA_LEN_RANGE',
    CKR_DEVICE_ERROR: 'CKR_DEVICE_ERROR',
    CKR_DEVICE_MEMORY: 'CKR_DEVICE_MEMORY',
    CKR_DEVICE_REMOVED: 'CKR_DEVICE_REMOVED',
    CKR_ENCRYPTED_DATA_INVALID: 'CKR_ENCRYPTED_DATA_INVALID',
    CKR_ENCRYPTED_DATA_LEN_RANGE: 'CKR_ENCRYPTED_DATA_LEN_RANGE',
    CKR_FUNCTION_CANCELED: 'CKR_FUNCTION_CANCELED',
    CKR_FUNCTION_NOT_PARALLEL: 'CKR_FUNCTION_NOT_PARALLEL',
    CKR_FUNCTION_NOT_SUPPORTED: 'CKR_FUNCTION_NOT_SUPPORTED',
    CKR_KEY_HANDLE_INVALID: 'CKR_KEY_HANDLE_INVALID',
    CKR_KEY_SIZE_RANGE: 'CKR_KEY_SIZE_RANGE',
    CKR_KEY_TYPE_INCONSISTENT: 'CKR_KEY_TYPE_INCONSISTENT',
    CKR_KEY_NOT_NEEDED: 'CKR_KEY_NOT_NEEDED',
    CKR_KEY_CHANGED: 'CKR_KEY_CHANGED',
    CKR_KEY_NEEDED: 'CKR_KEY_NEEDED',
    CKR_KEY_INDIGESTIBLE: 'CKR_KEY_INDIGESTIBLE',
    CKR_KEY_FUNCTION_NOT_PERMITTED: 'CKR_KEY_FUNCTION_NOT_PERMITTED',
    CKR_KEY_NOT_WRAPPABLE: 'CKR_KEY_NOT_WRAPPABLE',
    CKR_KEY_UNEXTRACTABLE: 'CKR_KEY_UNEXTRACTABLE',
    CKR_MECHANISM_INVALID: 'CKR_MECHANISM_INVALID',
    CKR_MECHANISM_PARAM_INVALID: 'CKR_MECHANISM_PARAM_INVALID',
    CKR_OBJECT_HANDLE_INVALID: 'CKR_OBJECT_HANDLE_INVALID',
    CKR_OPERATION_ACTIVE: 'CKR_OPERATION_ACTIVE',
    CKR_OPERATION_NOT_INITIALIZED: 'CKR_OPERATION_NOT_INITIALIZED',
    CKR_PIN_INCORRECT: 'CKR_PIN_INCORRECT',
    CKR_PIN_INVALID: 'CKR_PIN_INVALID',
    CKR_PIN_LEN_RANGE: 'CKR_PIN_LEN_RANGE',
    CKR_PIN_EXPIRED: 'CKR_PIN_EXPIRED',
    CKR_PIN_LOCKED: 'CKR_PIN_LOCKED',
    CKR_SESSION_CLOSED: 'CKR_SESSION_CLOSED',
    CKR_SESSION_COUNT: 'CKR_SESSION_COUNT',
    CKR_SESSION_HANDLE_INVALID: 'CKR_SESSION_HANDLE_INVALID',
    CKR_SESSION_PARALLEL_NOT_SUPPORTED: 'CKR_SESSION_PARALLEL_NOT_SUPPORTED',
    CKR_SESSION_READ_ONLY: 'CKR_SESSION_READ_ONLY',
    CKR_SESSION_EXISTS: 'CKR_SESSION_EXISTS',
    CKR_SESSION_READ_ONLY_EXISTS: 'CKR_SESSION_READ_ONLY_EXISTS',
    CKR_SESSION_READ_WRITE_SO_EXISTS: 'CKR_SESSION_READ_WRITE_SO_EXISTS',
    CKR_SIGNATURE_INVALID: 'CKR_SIGNATURE_INVALID',
    CKR_SIGNATURE_LEN_RANGE: 'CKR_SIGNATURE_LEN_RANGE',
    CKR_TEMPLATE_INCOMPLETE: 'CKR_TEMPLATE_INCOMPLETE',
    CKR_TEMPLATE_INCONSISTENT: 'CKR_TEMPLATE_INCONSISTENT',
    CKR_TOKEN_NOT_PRESENT: 'CKR_TOKEN_NOT_PRESENT',
    CKR_TOKEN_NOT_RECOGNIZED: 'CKR_TOKEN_NOT_RECOGNIZED',
    CKR_TOKEN_WRITE_PROTECTED: 'CKR_TOKEN_WRITE_PROTECTED',
    CKR_UNWRAPPING_KEY_HANDLE_INVALID: 'CKR_UNWRAPPING_KEY_HANDLE_INVALID',
    CKR_UNWRAPPING_KEY_SIZE_RANGE: 'CKR_UNWRAPPING_KEY_SIZE_RANGE',
    CKR_UNWRAPPING_KEY_TYPE_INCONSISTENT: 'CKR_UNWRAPPING_KEY_TYPE_INCONSISTENT',
    CKR_USER_ALREADY_LOGGED_IN: 'CKR_USER_ALREADY_LOGGED_IN',
    CKR_USER_NOT_LOGGED_IN: 'CKR_USER_NOT_LOGGED_IN',
    CKR_USER_PIN_NOT_INITIALIZED: 'CKR_USER_PIN_NOT_INITIALIZED',
    CKR_USER_TYPE_INVALID: 'CKR_USER_TYPE_INVALID',
    CKR_USER_ANOTHER_ALREADY_LOGGED_IN: 'CKR_USER_ANOTHER_ALREADY_LOGGED_IN',
    CKR_USER_TOO_MANY_TYPES: 'CKR_USER_TOO_MANY_TYPES',
    CKR_WRAPPED_KEY_INVALID: 'CKR_WRAPPED_KEY_INVALID',
    CKR_WRAPPED_KEY_LEN_RANGE: 'CKR_WRAPPED_KEY_LEN_RANGE',
    CKR_WRAPPING_KEY_HANDLE_INVALID: 'CKR_WRAPPING_KEY_HANDLE_INVALID',
    CKR_WRAPPING_KEY_SIZE_RANGE: 'CKR_WRAPPING_KEY_SIZE_RANGE',
    CKR_WRAPPING_KEY_TYPE_INCONSISTENT: 'CKR_WRAPPING_KEY_TYPE_INCONSISTENT',
    CKR_RANDOM_SEED_NOT_SUPPORTED: 'CKR_RANDOM_SEED_NOT_SUPPORTED',
    CKR_RANDOM_NO_RNG: 'CKR_RANDOM_NO_RNG',
    CKR_DOMAIN_PARAMS_INVALID: 'CKR_DOMAIN_PARAMS_INVALID',
    CKR_BUFFER_TOO_SMALL: 'CKR_BUFFER_TOO_SMALL',
    CKR_SAVED_STATE_INVALID: 'CKR_SAVED_STATE_INVALID',
    CKR_INFORMATION_SENSITIVE: 'CKR_INFORMATION_SENSITIVE',
    CKR_STATE_UNSAVEABLE: 'CKR_STATE_UNSAVEABLE',
    CKR_CRYPTOKI_NOT_INITIALIZED: 'CKR_CRYPTOKI_NOT_INITIALIZED',
    CKR_CRYPTOKI_ALREADY_INITIALIZED: 'CKR_CRYPTOKI_ALREADY_INITIALIZED',
    CKR_MUTEX_BAD: 'CKR_MUTEX_BAD',
    CKR_MUTEX_NOT_LOCKED: 'CKR_MUTEX_NOT_LOCKED',
    CKR_NEW_PIN_MODE: 'CKR_NEW_PIN_MODE',
    CKR_NEXT_OTP: 'CKR_NEXT_OTP',
    CKR_FUNCTION_REJECTED: 'CKR_FUNCTION_REJECTED',
    CKR_VENDOR_DEFINED: 'CKR_VENDOR_DEFINED',
    CKR_INSERTION_CALLBACK_NOT_SUPPORTED: 'CKR_INSERTION_CALLBACK_NOT_SUPPORTED',
    CKR_FUNCTION_PARALLEL: 'CKR_FUNCTION_PARALLEL',
    CKR_SESSION_EXCLUSIVE_EXISTS: 'CKR_SESSION_EXCLUSIVE_EXISTS',
    CKR_RC_ERROR: 'CKR_RC_ERROR',
    CKR_CONTAINER_HANDLE_INVALID: 'CKR_CONTAINER_HANDLE_INVALID',
    CKR_TOO_MANY_CONTAINERS: 'CKR_TOO_MANY_CONTAINERS',
    CKR_USER_LOCKED_OUT: 'CKR_USER_LOCKED_OUT',
    CKR_CLONING_PARAMETER_ALREADY_EXISTS: 'CKR_CLONING_PARAMETER_ALREADY_EXISTS',
    CKR_CLONING_PARAMETER_MISSING: 'CKR_CLONING_PARAMETER_MISSING',
    CKR_CERTIFICATE_DATA_MISSING: 'CKR_CERTIFICATE_DATA_MISSING',
    CKR_CERTIFICATE_DATA_INVALID: 'CKR_CERTIFICATE_DATA_INVALID',
    CKR_ACCEL_DEVICE_ERROR: 'CKR_ACCEL_DEVICE_ERROR',
    CKR_WRAPPING_ERROR: 'CKR_WRAPPING_ERROR',
    CKR_UNWRAPPING_ERROR: 'CKR_UNWRAPPING_ERROR',
    CKR_MAC_MISSING: 'CKR_MAC_MISSING',
    CKR_DAC_POLICY_PID_MISMATCH: 'CKR_DAC_POLICY_PID_MISMATCH',
    CKR_DAC_MISSING: 'CKR_DAC_MISSING',
    CKR_BAD_DAC: 'CKR_BAD_DAC',
    CKR_SSK_MISSING: 'CKR_SSK_MISSING',
    CKR_BAD_MAC: 'CKR_BAD_MAC',
    CKR_DAK_MISSING: 'CKR_DAK_MISSING',
    CKR_BAD_DAK: 'CKR_BAD_DAK',
    CKR_SIM_AUTHORIZATION_FAILED: 'CKR_SIM_AUTHORIZATION_FAILED',
    CKR_SIM_VERSION_UNSUPPORTED: 'CKR_SIM_VERSION_UNSUPPORTED',
    CKR_SIM_CORRUPT_DATA: 'CKR_SIM_CORRUPT_DATA',
    CKR_USER_NOT_AUTHORIZED: 'CKR_USER_NOT_AUTHORIZED',
    CKR_MAX_OBJECT_COUNT_EXCEEDED: 'CKR_MAX_OBJECT_COUNT_EXCEEDED',
    CKR_SO_LOGIN_FAILURE_THRESHOLD: 'CKR_SO_LOGIN_FAILURE_THRESHOLD',
    CKR_SIM_AUTHFORM_INVALID: 'CKR_SIM_AUTHFORM_INVALID',
    CKR_CITS_DAK_MISSING: 'CKR_CITS_DAK_MISSING',
    CKR_UNABLE_TO_CONNECT: 'CKR_UNABLE_TO_CONNECT',
    CKR_PARTITION_DISABLED: 'CKR_PARTITION_DISABLED',
    CKR_CALLBACK_ERROR: 'CKR_CALLBACK_ERROR',
    CKR_SECURITY_PARAMETER_MISSING: 'CKR_SECURITY_PARAMETER_MISSING',
    CKR_SP_TIMEOUT: 'CKR_SP_TIMEOUT',
    CKR_TIMEOUT: 'CKR_TIMEOUT',
    CKR_ECC_UNKNOWN_CURVE: 'CKR_ECC_UNKNOWN_CURVE',
    CKR_MTK_ZEROIZED: 'CKR_MTK_ZEROIZED',
    CKR_MTK_STATE_INVALID: 'CKR_MTK_STATE_INVALID',
    CKR_INVALID_ENTRY_TYPE: 'CKR_INVALID_ENTRY_TYPE',
    CKR_MTK_SPLIT_INVALID: 'CKR_MTK_SPLIT_INVALID',
    CKR_HSM_STORAGE_FULL: 'CKR_HSM_STORAGE_FULL',
    CKR_DEVICE_TIMEOUT: 'CKR_DEVICE_TIMEOUT',
    CKR_CONTAINER_OBJECT_STORAGE_FULL: 'CKR_CONTAINER_OBJECT_STORAGE_FULL',
    CKR_PED_CLIENT_NOT_RUNNING: 'CKR_PED_CLIENT_NOT_RUNNING',
    CKR_PED_UNPLUGGED: 'CKR_PED_UNPLUGGED',
    CKR_ECC_POINT_INVALID: 'CKR_ECC_POINT_INVALID',
    CKR_OPERATION_NOT_ALLOWED: 'CKR_OPERATION_NOT_ALLOWED',
    CKR_LICENSE_CAPACITY_EXCEEDED: 'CKR_LICENSE_CAPACITY_EXCEEDED',
    CKR_LOG_FILE_NOT_OPEN: 'CKR_LOG_FILE_NOT_OPEN',
    CKR_LOG_FILE_WRITE_ERROR: 'CKR_LOG_FILE_WRITE_ERROR',
    CKR_LOG_BAD_FILE_NAME: 'CKR_LOG_BAD_FILE_NAME',
    CKR_LOG_FULL: 'CKR_LOG_FULL',
    CKR_LOG_NO_KCV: 'CKR_LOG_NO_KCV',
    CKR_LOG_BAD_RECORD_HMAC: 'CKR_LOG_BAD_RECORD_HMAC',
    CKR_LOG_BAD_TIME: 'CKR_LOG_BAD_TIME',
    CKR_LOG_AUDIT_NOT_INITIALIZED: 'CKR_LOG_AUDIT_NOT_INITIALIZED',
    CKR_LOG_RESYNC_NEEDED: 'CKR_LOG_RESYNC_NEEDED',
    CKR_AUDIT_LOGIN_TIMEOUT_IN_PROGRESS: 'CKR_AUDIT_LOGIN_TIMEOUT_IN_PROGRESS',
    CKR_AUDIT_LOGIN_FAILURE_THRESHOLD: 'CKR_AUDIT_LOGIN_FAILURE_THRESHOLD',
    CKR_INVALID_FUF_TARGET: 'CKR_INVALID_FUF_TARGET',
    CKR_INVALID_FUF_HEADER: 'CKR_INVALID_FUF_HEADER',
    CKR_INVALID_FUF_VERSION: 'CKR_INVALID_FUF_VERSION',
    CKR_ECC_ECC_RESULT_AT_INF: 'CKR_ECC_ECC_RESULT_AT_INF',
    CKR_AGAIN: 'CKR_AGAIN',
    CKR_TOKEN_COPIED: 'CKR_TOKEN_COPIED',
    CKR_SLOT_NOT_EMPTY: 'CKR_SLOT_NOT_EMPTY',
    CKR_USER_ALREADY_ACTIVATED: 'CKR_USER_ALREADY_ACTIVATED',
    CKR_STC_NO_CONTEXT: 'CKR_STC_NO_CONTEXT',
    CKR_STC_CLIENT_IDENTITY_NOT_CONFIGURED: 'CKR_STC_CLIENT_IDENTITY_NOT_CONFIGURED',
    CKR_STC_PARTITION_IDENTITY_NOT_CONFIGURED: 'CKR_STC_PARTITION_IDENTITY_NOT_CONFIGURED',
    CKR_STC_DH_KEYGEN_ERROR: 'CKR_STC_DH_KEYGEN_ERROR',
    CKR_STC_CIPHER_SUITE_REJECTED: 'CKR_STC_CIPHER_SUITE_REJECTED',
    CKR_STC_DH_KEY_NOT_FROM_SAME_GROUP: 'CKR_STC_DH_KEY_NOT_FROM_SAME_GROUP',
    CKR_STC_COMPUTE_DH_KEY_ERROR: 'CKR_STC_COMPUTE_DH_KEY_ERROR',
    CKR_STC_FIRST_PHASE_KDF_ERROR: 'CKR_STC_FIRST_PHASE_KDF_ERROR',
    CKR_STC_SECOND_PHASE_KDF_ERROR: 'CKR_STC_SECOND_PHASE_KDF_ERROR',
    CKR_STC_KEY_CONFIRMATION_FAILED: 'CKR_STC_KEY_CONFIRMATION_FAILED',
    CKR_STC_NO_SESSION_KEY: 'CKR_STC_NO_SESSION_KEY',
    CKR_STC_RESPONSE_BAD_MAC: 'CKR_STC_RESPONSE_BAD_MAC',
    CKR_STC_NOT_ENABLED: 'CKR_STC_NOT_ENABLED',
    CKR_STC_CLIENT_HANDLE_INVALID: 'CKR_STC_CLIENT_HANDLE_INVALID',
    CKR_STC_SESSION_INVALID: 'CKR_STC_SESSION_INVALID',
    CKR_STC_CONTAINER_INVALID: 'CKR_STC_CONTAINER_INVALID',
    CKR_STC_SEQUENCE_NUM_INVALID: 'CKR_STC_SEQUENCE_NUM_INVALID',
    CKR_STC_NO_CHANNEL: 'CKR_STC_NO_CHANNEL',
    CKR_STC_RESPONSE_DECRYPT_ERROR: 'CKR_STC_RESPONSE_DECRYPT_ERROR',
    CKR_STC_RESPONSE_REPLAYED: 'CKR_STC_RESPONSE_REPLAYED',
    CKR_STC_REKEY_CHANNEL_MISMATCH: 'CKR_STC_REKEY_CHANNEL_MISMATCH',
    CKR_STC_RSA_ENCRYPT_ERROR: 'CKR_STC_RSA_ENCRYPT_ERROR',
    CKR_STC_RSA_SIGN_ERROR: 'CKR_STC_RSA_SIGN_ERROR',
    CKR_STC_RSA_DECRYPT_ERROR: 'CKR_STC_RSA_DECRYPT_ERROR',
    CKR_STC_RESPONSE_UNEXPECTED_KEY: 'CKR_STC_RESPONSE_UNEXPECTED_KEY',
    CKR_STC_UNEXPECTED_NONCE_PAYLOAD_SIZE: 'CKR_STC_UNEXPECTED_NONCE_PAYLOAD_SIZE',
    CKR_STC_UNEXPECTED_DH_DATA_SIZE: 'CKR_STC_UNEXPECTED_DH_DATA_SIZE',
    CKR_STC_OPEN_CIPHER_MISMATCH: 'CKR_STC_OPEN_CIPHER_MISMATCH',
    CKR_STC_OPEN_DHNIST_PUBKEY_ERROR: 'CKR_STC_OPEN_DHNIST_PUBKEY_ERROR',
    CKR_STC_OPEN_KEY_MATERIAL_GEN_FAIL: 'CKR_STC_OPEN_KEY_MATERIAL_GEN_FAIL',
    CKR_STC_OPEN_RESP_GEN_FAIL: 'CKR_STC_OPEN_RESP_GEN_FAIL',
    CKR_STC_ACTIVATE_MACTAG_U_VERIFY_FAIL: 'CKR_STC_ACTIVATE_MACTAG_U_VERIFY_FAIL',
    CKR_STC_ACTIVATE_MACTAG_V_GEN_FAIL: 'CKR_STC_ACTIVATE_MACTAG_V_GEN_FAIL',
    CKR_STC_ACTIVATE_RESP_GEN_FAIL: 'CKR_STC_ACTIVATE_RESP_GEN_FAIL',
    CKR_CHALLENGE_INCORRECT: 'CKR_CHALLENGE_INCORRECT',
    CKR_ACCESS_ID_INVALID: 'CKR_ACCESS_ID_INVALID',
    CKR_ACCESS_ID_ALREADY_EXISTS: 'CKR_ACCESS_ID_ALREADY_EXISTS',
    CKR_OBJECT_READ_ONLY: 'CKR_OBJECT_READ_ONLY',
    CKR_KEY_NOT_ACTIVE: 'CKR_KEY_NOT_ACTIVE',
    CKR_KEK_RETRY_FAILURE: 'CKR_KEK_RETRY_FAILURE',
    CKR_RNG_RESEED_TOO_EARLY: 'CKR_RNG_RESEED_TOO_EARLY'
}

"""
Module that contains lookup dictionaries for easy logging of
error codes and other constants within pycryptoki.
"""

from .defines import *

#:
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
}

#:
ATTR_NAME_LOOKUP = {
    CKA_CLASS: 'CKA_CLASS',
    CKA_CERTIFICATE_TYPE: 'CKA_CERTIFICATE_TYPE',
    CKA_KEY_TYPE: 'CKA_KEY_TYPE',
    CKA_VALUE_LEN: 'CKA_VALUE_LEN',
    CKA_MODULUS_BITS: 'CKA_MODULUS_BITS',
    CKA_PRIME_BITS: 'CKA_PRIME_BITS',
    CKA_SUBPRIME_BITS: 'CKA_SUBPRIME_BITS',
    CKA_VALUE_BITS: 'CKA_VALUE_BITS',
    CKA_TOKEN: 'CKA_TOKEN',
    CKA_PRIVATE: 'CKA_PRIVATE',
    CKA_SENSITIVE: 'CKA_SENSITIVE',
    CKA_ENCRYPT: 'CKA_ENCRYPT',
    CKA_DECRYPT: 'CKA_DECRYPT',
    CKA_WRAP: 'CKA_WRAP',
    CKA_UNWRAP: 'CKA_UNWRAP',
    CKA_SIGN: 'CKA_SIGN',
    CKA_SIGN_RECOVER: 'CKA_SIGN_RECOVER',
    CKA_VERIFY: 'CKA_VERIFY',
    CKA_VERIFY_RECOVER: 'CKA_VERIFY_RECOVER',
    CKA_DERIVE: 'CKA_DERIVE',
    CKA_LOCAL: 'CKA_LOCAL',
    CKA_MODIFIABLE: 'CKA_MODIFIABLE',
    CKA_EXTRACTABLE: 'CKA_EXTRACTABLE',
    CKA_ALWAYS_SENSITIVE: 'CKA_ALWAYS_SENSITIVE',
    CKA_NEVER_EXTRACTABLE: 'CKA_NEVER_EXTRACTABLE',
    CKA_LABEL: 'CKA_LABEL',
    CKA_APPLICATION: 'CKA_APPLICATION',
    CKA_ISSUER: 'CKA_ISSUER',
    CKA_SUBJECT: 'CKA_SUBJECT',
    CKA_ID: 'CKA_ID',
    CKA_START_DATE: 'CKA_START_DATE',
    CKA_END_DATE: 'CKA_END_DATE',
    CKA_VALUE: 'CKA_VALUE',
    CKA_SERIAL_NUMBER: 'CKA_SERIAL_NUMBER',
    CKA_MODULUS: 'CKA_MODULUS',
    CKA_PUBLIC_EXPONENT: 'CKA_PUBLIC_EXPONENT',
    CKA_PRIVATE_EXPONENT: 'CKA_PRIVATE_EXPONENT',
    CKA_PRIME_1: 'CKA_PRIME_1',
    CKA_PRIME_2: 'CKA_PRIME_2',
    CKA_EXPONENT_1: 'CKA_EXPONENT_1',
    CKA_EXPONENT_2: 'CKA_EXPONENT_2',
    CKA_COEFFICIENT: 'CKA_COEFFICIENT',
    CKA_PRIME: 'CKA_PRIME',
    CKA_SUBPRIME: 'CKA_SUBPRIME',
    CKA_BASE: 'CKA_BASE',
    CKA_UNWRAP_TEMPLATE: 'CKA_UNWRAP_TEMPLATE',
    CKA_DERIVE_TEMPLATE: 'CKA_DERIVE_TEMPLATE',
}

MECH_NAME_LOOKUP = {
                    0x00000000: "CKM_RSA_PKCS_KEY_PAIR_GEN",
                    0x00000001: "CKM_RSA_PKCS",
                    0x00000002: "CKM_RSA_9796",
                    0x00000003: "CKM_RSA_X_509",
                    0x00000004: "CKM_MD2_RSA_PKCS",
                    0x00000005: "CKM_MD5_RSA_PKCS",
                    0x00000006: "CKM_SHA1_RSA_PKCS",
                    0x00000007: "CKM_RIPEMD128_RSA_PKCS",
                    0x00000008: "CKM_RIPEMD160_RSA_PKCS",
                    0x00000009: "CKM_RSA_PKCS_OAEP",
                    0x0000000A: "CKM_RSA_X9_31_KEY_PAIR_GEN",
                    0x0000000B: "CKM_RSA_X9_31",
                    0x0000000C: "CKM_SHA1_RSA_X9_31",
                    0x0000000D: "CKM_RSA_PKCS_PSS",
                    0x0000000E: "CKM_SHA1_RSA_PKCS_PSS",
                    0x00000010: "CKM_DSA_KEY_PAIR_GEN",
                    0x00000011: "CKM_DSA",
                    0x00000012: "CKM_DSA_SHA1",
                    0x00000020: "CKM_DH_PKCS_KEY_PAIR_GEN",
                    0x00000021: "CKM_DH_PKCS_DERIVE",
                    0x00000030: "CKM_X9_42_DH_KEY_PAIR_GEN",
                    0x00000031: "CKM_X9_42_DH_DERIVE",
                    0x00000032: "CKM_X9_42_DH_HYBRID_DERIVE",
                    0x00000033: "CKM_X9_42_MQV_DERIVE",
                    0x00000040: "CKM_SHA256_RSA_PKCS",
                    0x00000041: "CKM_SHA384_RSA_PKCS",
                    0x00000042: "CKM_SHA512_RSA_PKCS",
                    0x00000043: "CKM_SHA256_RSA_PKCS_PSS",
                    0x00000044: "CKM_SHA384_RSA_PKCS_PSS",
                    0x00000045: "CKM_SHA512_RSA_PKCS_PSS",
                    0x00000046: "CKM_SHA224_RSA_PKCS",
                    0x00000047: "CKM_SHA224_RSA_PKCS_PSS",
                    0x00000100: "CKM_RC2_KEY_GEN",
                    0x00000101: "CKM_RC2_ECB",
                    0x00000102: "CKM_RC2_CBC",
                    0x00000103: "CKM_RC2_MAC",
                    0x00000104: "CKM_RC2_MAC_GENERAL",
                    0x00000105: "CKM_RC2_CBC_PAD",
                    0x00000110: "CKM_RC4_KEY_GEN",
                    0x00000111: "CKM_RC4",
                    0x00000120: "CKM_DES_KEY_GEN",
                    0x00000121: "CKM_DES_ECB",
                    0x00000122: "CKM_DES_CBC",
                    0x00000123: "CKM_DES_MAC",
                    0x00000124: "CKM_DES_MAC_GENERAL",
                    0x00000125: "CKM_DES_CBC_PAD",
                    0x00000130: "CKM_DES2_KEY_GEN",
                    0x00000131: "CKM_DES3_KEY_GEN",
                    0x00000132: "CKM_DES3_ECB",
                    0x00000133: "CKM_DES3_CBC",
                    0x00000134: "CKM_DES3_MAC",
                    0x00000135: "CKM_DES3_MAC_GENERAL",
                    0x00000136: "CKM_DES3_CBC_PAD",
                    0x00000137: "CKM_DES3_CMAC_GENERAL",
                    0x00000138: "CKM_DES3_CMAC",
                    0x00000140: "CKM_CDMF_KEY_GEN",
                    0x00000141: "CKM_CDMF_ECB",
                    0x00000142: "CKM_CDMF_CBC",
                    0x00000143: "CKM_CDMF_MAC",
                    0x00000144: "CKM_CDMF_MAC_GENERAL",
                    0x00000145: "CKM_CDMF_CBC_PAD",
                    0x00000150: "CKM_DES_OFB64",
                    0x00000151: "CKM_DES_OFB8",
                    0x00000152: "CKM_DES_CFB64",
                    0x00000153: "CKM_DES_CFB8",
                    0x00000200: "CKM_MD2",
                    0x00000201: "CKM_MD2_HMAC",
                    0x00000202: "CKM_MD2_HMAC_GENERAL",
                    0x00000210: "CKM_MD5",
                    0x00000211: "CKM_MD5_HMAC",
                    0x00000212: "CKM_MD5_HMAC_GENERAL",
                    0x00000220: "CKM_SHA_1",
                    0x00000221: "CKM_SHA_1_HMAC",
                    0x00000222: "CKM_SHA_1_HMAC_GENERAL",
                    0x00000230: "CKM_RIPEMD128",
                    0x00000231: "CKM_RIPEMD128_HMAC",
                    0x00000232: "CKM_RIPEMD128_HMAC_GENERAL",
                    0x00000240: "CKM_RIPEMD160",
                    0x00000241: "CKM_RIPEMD160_HMAC",
                    0x00000242: "CKM_RIPEMD160_HMAC_GENERAL",
                    0x00000250: "CKM_SHA256",
                    0x00000251: "CKM_SHA256_HMAC",
                    0x00000252: "CKM_SHA256_HMAC_GENERAL",
                    0x00000255: "CKM_SHA224",
                    0x00000256: "CKM_SHA224_HMAC",
                    0x00000257: "CKM_SHA224_HMAC_GENERAL",
                    0x00000260: "CKM_SHA384",
                    0x00000261: "CKM_SHA384_HMAC",
                    0x00000262: "CKM_SHA384_HMAC_GENERAL",
                    0x00000270: "CKM_SHA512",
                    0x00000271: "CKM_SHA512_HMAC",
                    0x00000272: "CKM_SHA512_HMAC_GENERAL",
                    0x00000280: "CKM_SECURID_KEY_GEN",
                    0x00000282: "CKM_SECURID",
                    0x00000290: "CKM_HOTP_KEY_GEN",
                    0x00000291: "CKM_HOTP",
                    0x000002A0: "CKM_ACTI",
                    0x000002A1: "CKM_ACTI_KEY_GEN",
                    0x00000300: "CKM_CAST_KEY_GEN",
                    0x00000301: "CKM_CAST_ECB",
                    0x00000302: "CKM_CAST_CBC",
                    0x00000303: "CKM_CAST_MAC",
                    0x00000304: "CKM_CAST_MAC_GENERAL",
                    0x00000305: "CKM_CAST_CBC_PAD",
                    0x00000310: "CKM_CAST3_KEY_GEN",
                    0x00000311: "CKM_CAST3_ECB",
                    0x00000312: "CKM_CAST3_CBC",
                    0x00000313: "CKM_CAST3_MAC",
                    0x00000314: "CKM_CAST3_MAC_GENERAL",
                    0x00000315: "CKM_CAST3_CBC_PAD",
                    0x00000320: "CKM_CAST_KEY_GEN",  # Note: each of these could be CAST5 or CAST128
                    0x00000321: "CKM_CAST_ECB",
                    0x00000322: "CKM_CAST_CBC",
                    0x00000323: "CKM_CAST_MAC",
                    0x00000324: "CKM_CAST_MAC_GENERAL",
                    0x00000325: "CKM_CAST_CBC_PAD",
                    0x00000330: "CKM_RC5_KEY_GEN",
                    0x00000331: "CKM_RC5_ECB",
                    0x00000332: "CKM_RC5_CBC",
                    0x00000333: "CKM_RC5_MAC",
                    0x00000334: "CKM_RC5_MAC_GENERAL",
                    0x00000335: "CKM_RC5_CBC_PAD",
                    0x00000340: "CKM_IDEA_KEY_GEN",
                    0x00000341: "CKM_IDEA_ECB",
                    0x00000342: "CKM_IDEA_CBC",
                    0x00000343: "CKM_IDEA_MAC",
                    0x00000344: "CKM_IDEA_MAC_GENERAL",
                    0x00000345: "CKM_IDEA_CBC_PAD",
                    0x00000350: "CKM_GENERIC_SECRET_KEY_GEN",
                    0x00000360: "CKM_CONCATENATE_BASE_AND_KEY",
                    0x00000362: "CKM_CONCATENATE_BASE_AND_DATA",
                    0x00000363: "CKM_CONCATENATE_DATA_AND_BASE",
                    0x00000364: "CKM_XOR_BASE_AND_DATA",
                    0x00000365: "CKM_EXTRACT_KEY_FROM_KEY",
                    0x00000370: "CKM_SSL3_PRE_MASTER_KEY_GEN",
                    0x00000371: "CKM_SSL3_MASTER_KEY_DERIVE",
                    0x00000372: "CKM_SSL3_KEY_AND_MAC_DERIVE",
                    0x00000373: "CKM_SSL3_MASTER_KEY_DERIVE_DH",
                    0x00000374: "CKM_TLS_PRE_MASTER_KEY_GEN",
                    0x00000375: "CKM_TLS_MASTER_KEY_DERIVE",
                    0x00000376: "CKM_TLS_KEY_AND_MAC_DERIVE",
                    0x00000377: "CKM_TLS_MASTER_KEY_DERIVE_DH",
                    0x00000378: "CKM_TLS_PRF",
                    0x00000380: "CKM_SSL3_MD5_MAC",
                    0x00000381: "CKM_SSL3_SHA1_MAC",
                    0x00000390: "CKM_MD5_KEY_DERIVATION",
                    0x00000391: "CKM_MD2_KEY_DERIVATION",
                    0x00000392: "CKM_SHA1_KEY_DERIVATION",
                    0x00000393: "CKM_SHA256_KEY_DERIVATION",
                    0x00000394: "CKM_SHA384_KEY_DERIVATION",
                    0x00000395: "CKM_SHA512_KEY_DERIVATION",
                    0x00000396: "CKM_SHA224_KEY_DERIVATION",
                    0x000003A0: "CKM_PBE_MD2_DES_CBC",
                    0x000003A1: "CKM_PBE_MD5_DES_CBC",
                    0x000003A2: "CKM_PBE_MD5_CAST_CBC",
                    0x000003A3: "CKM_PBE_MD5_CAST3_CBC",
                    0x000003A4: "CKM_PBE_HASH_CAST5_CBC",  # Note, HASH could be MD5, SHA1, etc
                    0x000003A6: "CKM_PBE_SHA1_RC4_128",
                    0x000003A7: "CKM_PBE_SHA1_RC4_40",
                    0x000003A8: "CKM_PBE_SHA1_DES3_EDE_CBC",
                    0x000003A9: "CKM_PBE_SHA1_DES2_EDE_CBC",
                    0x000003AA: "CKM_PBE_SHA1_RC2_128_CBC",
                    0x000003AB: "CKM_PBE_SHA1_RC2_40_CBC",
                    0x000003B0: "CKM_PKCS5_PBKD2",
                    0x000003C0: "CKM_PBA_SHA1_WITH_SHA1_HMAC",
                    0x000003D0: "CKM_WTLS_PRE_MASTER_KEY_GEN",
                    0x000003D1: "CKM_WTLS_MASTER_KEY_DERIVE",
                    0x000003D2: "CKM_WTLS_MASTER_KEY_DERIVE_DH_ECC",
                    0x000003D3: "CKM_WTLS_PRF",
                    0x000003D4: "CKM_WTLS_SERVER_KEY_AND_MAC_DERIVE",
                    0x000003D5: "CKM_WTLS_CLIENT_KEY_AND_MAC_DERIVE",
                    0x00000400: "CKM_KEY_WRAP_LYNKS",
                    0x00000401: "CKM_KEY_WRAP_SET_OAEP",
                    0x00000500: "CKM_CMS_SIG",
                    0x00000510: "CKM_KIP_DERIVE",
                    0x00000511: "CKM_KIP_WRAP",
                    0x00000512: "CKM_KIP_MAC",
                    0x00000550: "CKM_CAMELLIA_KEY_GEN",
                    0x00000551: "CKM_CAMELLIA_ECB",
                    0x00000552: "CKM_CAMELLIA_CBC",
                    0x00000553: "CKM_CAMELLIA_MAC",
                    0x00000554: "CKM_CAMELLIA_MAC_GENERAL",
                    0x00000555: "CKM_CAMELLIA_CBC_PAD",
                    0x00000556: "CKM_CAMELLIA_ECB_ENCRYPT_DATA",
                    0x00000557: "CKM_CAMELLIA_CBC_ENCRYPT_DATA",
                    0x00000558: "CKM_CAMELLIA_CTR",
                    0x00000560: "CKM_ARIA_KEY_GEN",
                    0x00000561: "CKM_ARIA_ECB",
                    0x00000562: "CKM_ARIA_CBC",
                    0x00000563: "CKM_ARIA_MAC",
                    0x00000564: "CKM_ARIA_MAC_GENERAL",
                    0x00000565: "CKM_ARIA_CBC_PAD",
                    0x00000566: "CKM_ARIA_ECB_ENCRYPT_DATA",
                    0x00000567: "CKM_ARIA_CBC_ENCRYPT_DATA",
                    0x00001000: "CKM_SKIPJACK_KEY_GEN",
                    0x00001001: "CKM_SKIPJACK_ECB64",
                    0x00001002: "CKM_SKIPJACK_CBC64",
                    0x00001003: "CKM_SKIPJACK_OFB64",
                    0x00001004: "CKM_SKIPJACK_CFB64",
                    0x00001005: "CKM_SKIPJACK_CFB32",
                    0x00001006: "CKM_SKIPJACK_CFB16",
                    0x00001007: "CKM_SKIPJACK_CFB8",
                    0x00001008: "CKM_SKIPJACK_WRAP",
                    0x00001009: "CKM_SKIPJACK_PRIVATE_WRAP",
                    0x0000100a: "CKM_SKIPJACK_RELAYX",
                    0x00001010: "CKM_KEA_KEY_PAIR_GEN",
                    0x00001011: "CKM_KEA_KEY_DERIVE",
                    0x00001020: "CKM_FORTEZZA_TIMESTAMP",
                    0x00001030: "CKM_BATON_KEY_GEN",
                    0x00001031: "CKM_BATON_ECB128",
                    0x00001032: "CKM_BATON_ECB96",
                    0x00001033: "CKM_BATON_CBC128",
                    0x00001034: "CKM_BATON_COUNTER",
                    0x00001035: "CKM_BATON_SHUFFLE",
                    0x00001036: "CKM_BATON_WRAP",
                    0x00001040: "CKM_EC_KEY_PAIR_GEN",
                    0x00001041: "CKM_ECDSA",
                    0x00001042: "CKM_ECDSA_SHA1",
                    0x00001050: "CKM_ECDH1_DERIVE",
                    0x00001051: "CKM_ECDH1_COFACTOR_DERIVE",
                    0x00001052: "CKM_ECMQV_DERIVE",
                    0x00001060: "CKM_JUNIPER_KEY_GEN",
                    0x00001061: "CKM_JUNIPER_ECB128",
                    0x00001062: "CKM_JUNIPER_CBC128",
                    0x00001063: "CKM_JUNIPER_COUNTER",
                    0x00001064: "CKM_JUNIPER_SHUFFLE",
                    0x00001065: "CKM_JUNIPER_WRAP",
                    0x00001070: "CKM_FASTHASH",
                    0x00001080: "CKM_AES_KEY_GEN",
                    0x00001081: "CKM_AES_ECB",
                    0x00001082: "CKM_AES_CBC",
                    0x00001083: "CKM_AES_MAC",
                    0x00001084: "CKM_AES_MAC_GENERAL",
                    0x00001085: "CKM_AES_CBC_PAD",
                    0x00001086: "CKM_AES_CTR",
                    0x00001089: "CKM_AES_CMAC_GENERAL",
                    0x0000108A: "CKM_AES_CMAC",
                    0x00001090: "CKM_BLOWFISH_KEY_GEN",
                    0x00001091: "CKM_BLOWFISH_CBC",
                    0x00001092: "CKM_TWOFISH_KEY_GEN",
                    0x00001093: "CKM_TWOFISH_CBC",
                    0x00001100: "CKM_DES_ECB_ENCRYPT_DATA",
                    0x00001101: "CKM_DES_CBC_ENCRYPT_DATA",
                    0x00001102: "CKM_DES3_ECB_ENCRYPT_DATA",
                    0x00001103: "CKM_DES3_CBC_ENCRYPT_DATA",
                    0x00001104: "CKM_AES_ECB_ENCRYPT_DATA",
                    0x00001105: "CKM_AES_CBC_ENCRYPT_DATA",
                    0x00002000: "CKM_DSA_PARAMETER_GEN",
                    0x00002001: "CKM_DH_PKCS_PARAMETER_GEN",
                    0x00002002: "CKM_X9_42_DH_PARAMETER_GEN",
                    0x00002109: "CKM_AES_KEY_WRAP",
                    0x0000210A: "CKM_AES_KEY_WRAP_PAD",
                    0x80000000: "CKM_VENDOR_DEFINED",
                    0x00001087: "CKM_AES_GCM",  
}

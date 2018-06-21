import logging

import pytest

from pycryptoki.defines import CKR_OK
from pycryptoki.misc import c_generate_random, c_seed_random
from pycryptoki.return_values import ret_vals_dictionary
from . import config as test_config

logger = logging.getLogger(__name__)


class TestSupportingOperations(object):
    """
    Tests Random Generator function
     """

    @pytest.fixture(autouse=True)
    def setup_teardown(self, auth_session):
        self.h_session = auth_session
        self.admin_slot = test_config["test_slot"]

    def test_rng(self):
        """Tests generating a random number"""
        length = 15
        ret, random_string = c_generate_random(self.h_session, length)
        assert ret == CKR_OK, "C_GenerateRandom should return CKR_OK, instead it returned " + \
                              ret_vals_dictionary[ret]
        assert len(
            random_string) == length, "The length of the random string should be the same as the " \
                                      "length of the requested data."

    def test_seeded_rng(self):
        """Tests that seeding the random number generator with the same data will
        generate the same random number


        """
        seed = b"k" * 1024
        ret = c_seed_random(self.h_session, seed)
        assert ret == CKR_OK, "Seeding the random number generator shouldn't return an error, " \
                              "it returned " + \
                              ret_vals_dictionary[ret]

        ret, random_string_one = c_generate_random(self.h_session, 10)
        assert ret == CKR_OK
        ret = c_seed_random(self.h_session, seed)
        assert ret == CKR_OK, "Seeding the random number generator a second time shouldn't return " \
                              "" \
                              "an error, it returned " + \
                              ret_vals_dictionary[ret]

        ret, random_string_two = c_generate_random(self.h_session, 10)
        assert ret == CKR_OK

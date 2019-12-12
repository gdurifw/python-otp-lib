#!/usr/bin/env python
from setuptools import setup, find_packages

# install OTP modules
setup(
        name="python-otp-lib",
        version="0.1",
        packages=find_packages(),
        author="Marco Caimi",
        author_email="Marco Caimi",
        description="A simple library that performs HOTP and TOTP token generation.",
        license="GPL v3",
        url="http://yuorserver/mcaimi/python-otp-lib.git"
)

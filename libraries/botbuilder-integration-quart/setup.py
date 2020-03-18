# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from setuptools import setup

VERSION = os.environ["packageVersion"] if "packageVersion" in os.environ else "4.7.1"
REQUIRES = [
    "botbuilder-core>=4.7.1",
    "quart>=0.10.0",
]

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, "botbuilder", "integration", "quart", "about.py")) as f:
    package_info = {}
    info = f.read()
    exec(info, package_info)

with open(os.path.join(root, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=package_info["__title__"],
    version=package_info["__version__"],
    url=package_info["__uri__"],
    author=package_info["__author__"],
    description=package_info["__description__"],
    keywords=[
        "bots",
        "ai",
        "botframework",
        "botbuilder",
    ],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license=package_info["__license__"],
    packages=[
        "botbuilder.integration.quart",
        "botbuilder.integration.quart.skills",
    ],
    install_requires=REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

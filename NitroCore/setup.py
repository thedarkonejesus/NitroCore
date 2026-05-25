"""Setup script for PyUtils and PyGui libraries"""

import os
import sys
from setuptools import setup, find_packages
from pathlib import Path

# Read version from VERSION file
VERSION_FILE = Path(__file__).parent / "VERSION"
if VERSION_FILE.exists():
    VERSION = VERSION_FILE.read_text().strip()
else:
    VERSION = "1.0.0"

# Read requirements from requirements.txt
REQUIREMENTS_FILE = Path(__file__).parent / "requirements.txt"
if REQUIREMENTS_FILE.exists():
    INSTALL_REQUIRES = REQUIREMENTS_FILE.read_text().splitlines()
else:
    INSTALL_REQUIRES = []

# Get long description from README.md
README_FILE = Path(__file__).parent / "README.md"
if README_FILE.exists():
    LONG_DESCRIPTION = README_FILE.read_text()
else:
    LONG_DESCRIPTION = ""

setup(
    name="deep-hat-pyutils",
    version=VERSION,
    author="DeepHat Team",
    author_email="team@deephat.ai",
    description="Python utility and GUI libraries for common tasks",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/deephats/pyutils",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),
    package_data={
        "": ["LICENSE", "README.md", "VERSION"],
        "utils": ["*.py"],
        "gui": ["*.py"],
    },
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.8",
    keywords=["utility", "gui", "logging", "validation", "configuration"],
    project_urls={
        "Documentation": "https://docs.deephats.ai/pyutils",
        "GitHub": "https://github.com/deephats/pyutils",
        "Bug Reports": "https://github.com/deephats/pyutils/issues",
    },
)
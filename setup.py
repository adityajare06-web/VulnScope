"""Setuptools-based packaging configuration for VulnScope."""

from setuptools import setup, find_packages

from vulnscope import __version__, __author__

with open("README.md", "r", encoding="utf-8") as fh:
    try:
        long_description = fh.read()
    except FileNotFoundError:
        long_description = "VulnScope - Authorized Network Vulnerability Scanner"

setup(
    name="vulnscope",
    version=__version__,
    author=__author__,
    description="Authorized Network Vulnerability Scanner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vulnscope/vulnscope",
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.12",
    install_requires=[
        "rich>=13.7.0",
        "Jinja2>=3.1.3",
        "PyYAML>=6.0.1",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.1.0",
            "flake8>=7.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "vulnscope=vulnscope.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Typing :: Typed",
    ],
    keywords="security vulnerability scanner network reconnaissance",
)

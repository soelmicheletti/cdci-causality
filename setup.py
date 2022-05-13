from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="cdci-causality",
    packages=find_packages(exclude=[]),
    version="0.0.3",
    license="MIT",
    description="CDCI - Causality",
    long_description=long_description,
    author="Soel Micheletti",
    author_email="msoel@ethz.ch",
    url="https://github.com/soelmicheletti/cdci-causality",
    keywords=[
        "statistics",
        "causality",
    ],
    install_requires=["data-science-types>=0.2"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)

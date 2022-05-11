from setuptools import find_packages, setup

setup(
    name="cdci-causality",
    packages=find_packages(exclude=[]),
    version="0.0.4",
    license="MIT",
    description="CDCI - Causality",
    long_description="CDCI - Causality",
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

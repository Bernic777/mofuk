from setuptools import setup, find_packages
import os

# Read the contents of your README file for the long description on PyPI
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mofuk",
    version="0.3.0",
    author="Mofuk Maintainer",
    author_email="vanish@bernicyesnat.icu",
    description="A meditative Tor identity rotation tool inspired by the Moi Tribe.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bernic777/mofuk", 
    project_urls={
        "Bug Tracker": "https://github.com/Bernic777/mofuk/issues",
        "Source Code": "https://github.com/Bernic777/mofuk",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
    ],
    keywords="tor, privacy, security, identity-rotation, anonymity, moi-tribe",
    # Struktur paket otomatis dideteksi di bawah folder 'mofuk/'
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "requests[socks]",
    ],
    entry_points={
        "console_scripts": [
            "mofuk=mofuk.core:main_sequence",
        ],
    },
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
)

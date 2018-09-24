import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whosaysthat",
    version="0.0.2",
    author="Kushal Das",
    author_email="kushal@freedom.press",
    description="Example Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3+",
    install_requires=["requests","cryptography",],
    python_requires=">=3.5",
    url="https://github.com/kushaldas/whosaysthat",
    packages=setuptools.find_packages(exclude=["docs", "tests"]),
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'whatismyip = whosaysthat:main',
            'whoisthebest = mike:say',
        ],
    },
)

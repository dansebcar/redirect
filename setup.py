import setuptools

setuptools.setup(
    name="redirect",
    version="0.1",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["redirect=redirect.__main__:main"]},
)

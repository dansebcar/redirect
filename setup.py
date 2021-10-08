import setuptools

setuptools.setup(
    name="redirect",
    version="0.1",
    install_requires=["aiohttp"],
    entry_points={"console_scripts": ["redirect=redirect:main"]},
    packages=setuptools.find_packages(),
)

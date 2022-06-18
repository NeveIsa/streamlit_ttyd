from setuptools import find_packages, setup

setup(
    name="streamlit_ttyd",
    version="0.1.0",
    author="Sampad B Mohanty",
    author_email="sbmohant@usc.edu",
    py_modules=[
        "terminal",
    ],
    packages=find_packages(),
    install_requires=["streamlit", "port-for"],
)

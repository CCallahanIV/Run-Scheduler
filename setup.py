"""Setup for our ackermann package."""

from setuptools import setup

setup(
    name="runscheduler",
    description="Upload training schedule to google calendar.",
    version=0.0,
    author="Ted Callahan",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=[""],
    install_requires=['pandas'],
    # extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        'console_scripts': [
            "schedulerun = :main"
        ]
    }
)

from setuptools import setup

long_description = open("README.md").read()

setup(
    name="onesignal-notifications",
    version="0.2.1",
    url="https://github.com/Lanseuo/onesignal-notifications",
    description="OneSignal API Wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Lucas Hild",
    author_email="contact@lucas-hild.de",
    packages=["onesignal"],
    install_requires=["requests"]
)

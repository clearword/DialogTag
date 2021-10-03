import setuptools

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

# Need to do some magic on whether this is osx arm or not.
import platform
tensorflow_version = "tensorflow>=2.0.0"
mac_version = platform.mac_ver()
if mac_version and 'arm' in mac_version[-1]:
    tensorflow_version = "tensorflow-macos>=2.6.0"

setuptools.setup(
    name="DialogTag",
    version="1.1.3",
    author="Bhavitvya Malik",
    author_email="bhavitvya.malik@gmail.com",
    description="A python library to classify dialogue tag.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhavitvyamalik/DialogTag",
    packages=setuptools.find_packages(),
    install_requires=[
        'transformers>=3.0.0',
        'tqdm',
        tensorflow_version
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    keywords="Tensorflow BERT NLP deep learning Transformer Networks "
)

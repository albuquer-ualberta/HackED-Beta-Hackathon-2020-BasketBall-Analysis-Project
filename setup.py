import setuptools

with open('README.md','r') as fh:
  longDescription = fh.read()

setuptools.setup(
  name = '',
  version = '0.0.1',
  author = 'Arjun Mehta',
  author_email="",
  description="",
  long_description= longDescription,
  long_description_content_type="text/markdown",
  url="",
  packages=setuptools.find_packages(),
  install_requires=[],
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)

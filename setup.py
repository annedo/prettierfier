import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='prettierfier',
    version='1.0.1',
    author='Anne Do',
    author_email='anne.do.designs@gmail.com',
    description='Intelligently pretty-print HTML/XML with inline tags.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/annedo/prettierfier',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML'
    ],
    license='MIT',
    keywords='html xml formatting prettify'
)

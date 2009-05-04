from setuptools import setup, find_packages

setup(
    name='django-html',
    version=__import__('django_html').__version__,
    description='This package represents an experimental approach to improving the way Django outputs form widgets.',
    long_description=open('README.rst').read(),
    author='Simon Willison',
    author_email='simon@simonwillison.net',
    url='http://github.com/simonw/django-html',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

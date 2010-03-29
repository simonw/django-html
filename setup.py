from distutils.core import setup
import os
 
setup(
    name = 'django-html',
    packages = ['django_html', 'django_html.templatetags'],
    version=__import__('django_html').__version__,
    description='Template tags for smarter outputting of HTML in Django',
    long_description=open('README.rst').read(),
    author='Simon Willison',
    author_email='simon@simonwillison.net',
    url='http://github.com/simonw/django-html',
    license='BSD',
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

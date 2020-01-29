from setuptools import setup

setup(
    name='cdoapi',
    version='1.3.0',

    author='Graham, DevOps, Optibrium',
    author_email='graham@optibrium.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: Interview Candidates',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Build Tools'
    ],
    description='An API for use in the Optibrium tech test',
    install_requires=[
        'Flask>=1.1.1',
        'Flask-Cors==3.0.8',
        'Flask-SQLAlchemy>=2.4.0',
        'psycopg2-binary>=2.8.3'
    ],
    keywords='api tech test',
    long_description='''
    ''',
    long_description_content_type='text/markdown',
    packages=[
        'com.optibrium.cdoapi',
        'com.optibrium.cdoapi.model',
        'com.optibrium.cdoapi.view',
        'com.optibrium.cdoapi.controller',
    ],
    python_requires='>=3.4, <4',
    project_urls={
        'Our Company': 'https://optibrium.com',
        'The TechTest': 'https://github.com/optibrium/web_developer_tech_test',
        'Bug Reports': 'https://github.com/optibrium/cdoapi/issues',
        'Source': 'https://github.com/optibrium/cdoapi'
    },
    url='https://github.com/optibrium/cdoapi'
)

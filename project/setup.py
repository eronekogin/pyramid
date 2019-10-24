from setuptools import setup


requires = [
    'pyramid',
    'pyramid_jinja2',
    'waitress',
    'colander'
]

dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest'
]

setup(
    name='toyapp',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = toyapp:main'
        ]
    }
)

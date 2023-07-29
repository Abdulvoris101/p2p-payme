from setuptools import setup, find_packages

def get_long_description():
    with open('README.md', mode='r', encoding='utf8') as f:
        return f.read()

setup(
    name='p2p-payme',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'annotated-types==0.5.0',
        'certifi==2023.7.22',
        'charset-normalizer==3.2.0',
        'idna==3.4',
        'pydantic==2.1.1',
        'pydantic-collections==0.5.0',
        'pydantic_core==2.4.0',
        'python-dateutil==2.8.2',
        'python-dotenv==1.0.0',
        'requests==2.31.0',
        'six==1.16.0',
        'typing_extensions==4.7.1',
        'urllib3==2.0.4'
    ],
    # Additional metadata (optional)
    author='Abdulvoris Erkinov',
    author_email='erkinovabdulvoris101@gmail.com',
    description='P2P automation',
    url='https://github.com/Abdulvoris101/p2p-payme',
    long_description_content_type='text/markdown',
    long_description=get_long_description(),
    keywords='python payme p2p automation',
    entry_points={
        'console_scripts': [
            'auth=p2p_payme.cli:main',
        ],
    },
)

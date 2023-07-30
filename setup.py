from setuptools import setup, find_packages

def get_long_description():
    with open('README.md', mode='r', encoding='utf8') as f:
        return f.read()

setup(
    name='p2p-payme',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'pydantic>=1.7.4,<2.0.0',
        'pydantic-collections==0.5.0',
        'python-dateutil==2.8.2',
        'python-dotenv==1.0.0',
        'requests==2.31.0',
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

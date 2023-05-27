From setuptools import setup, find_namespace_packages

setup(
    name='clean',
    version='0.1',
    description='Sort file in folder',
    url='http://github.com/dummy_user/useful',
    author='AlexM',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['os','shutil'],
    entry_points={'console_scripts': ['sortfile = useful.some_code:sort_files']}
)
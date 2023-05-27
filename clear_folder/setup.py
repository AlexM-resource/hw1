From setuptools import setup, find_namespace_packages

setup(
    name='clean',
    version='0.1',
    description='Sort file in folder',
    url='https://github.com/AlexM-resource/hw1/tree/main/clear_folder',
    author='AlexM',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['os','shutil'],
    entry_points={'console_scripts': ['sortfile = useful.some_code:sort_files']}
)
from setuptools import setup, find_namespace_packages

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name='DeepImmuno',
    version='1.0',
    description='Deep-learning empowered prediction and generation of immunogenic epitopes for T cell immunity.',
    long_description=readme(),
    url='https://github.com/frankligy/DeepImmuno',
    author='Guangyuan Li, Balaji Iyer, V B Surya Prasath, Yizhao Ni, Nathan Salomonis',
    scripts=['deepimmuno-cnn', 'deepimmuno-gan'],
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=[
        'tensorflow<=2.15.1',
        'numpy',
        'pandas',
    ],
    zip_safe=False
)

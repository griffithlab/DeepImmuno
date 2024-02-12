from setuptools import setup

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
    packages=['deepimmuno'],
    include_package_data=True,
    install_requires=[
        'tensorflow',
        'numpy',
        'pandas',
    ],
    zip_safe=False
)

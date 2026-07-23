from setuptools import find_packages, setup

setup(
    name='qpth',
    version='0.0.18',
    description="A fast and differentiable QP solver for PyTorch.",
    author='Brandon Amos',
    author_email='bamos@cs.cmu.edu',
    platforms=['any'],
    license="Apache 2.0",
    url='https://github.com/CoMMALab/qpth',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'numpy',
        'torch>=2.0',
    ],
    extras_require={
        'cvxpy': ['cvxpy>=1.1.0'],   # only for the optional QPSolvers.CVXPY backend
    },
)

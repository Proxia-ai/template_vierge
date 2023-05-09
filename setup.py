import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="template_vierge",
    version="0.0.3.16",
    author="BEN OTHMANE Zied",
    author_email="ziedici@gmail.com",
    description="Say if population is old",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    keywords=['SOME', 'MEANINGFULL', 'KEYWORDS'],
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    install_requires=[
        'numpy==1.24.3',
        'pandas==2.0.1',
        'PyYAML==6.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Build Tools',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Programming Language :: Python :: 3.7',  # Specify which pyhton versions that you want to support
    ],
    # si le dossier ne contient aucun script il ne va pas etre considéré comme un package meme s'il contient __init__.py
    packages=(
            setuptools.find_packages() +
            setuptools.find_packages(where="./src/template_vierge") +
            setuptools.find_packages(where="./utils") +
            setuptools.find_packages(where="./configs") +
            setuptools.find_packages(where="./_modules/module_1")
    ),
    package_data={'configs': ['config.ini', 'config.yaml']},
    include_package_data=True,

    python_requires=">=3.7"
)

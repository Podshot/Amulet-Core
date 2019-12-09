from setuptools import setup, find_packages

from json import load
import os.path as op
import os


VERSION_NUMBER = "0.0.0"
if op.exists(op.join('.', 'version.json')):
    with open(op.join('.', 'version.json')) as fp:
        VERSION_NUMBER = '.'.join(map(str, load(fp)['version_number']))


def get_egg_name_from_git_uri(uri):
    if (uri.startswith("git+") or uri.startswith("https:")) and '#egg=' in uri:
        return uri[uri.index("#egg=") + len("#egg=") :].strip()
    elif uri.startswith("git+") or uri.startswith("https:"):
        return ""
    return uri.strip()

world_interface_path = op.join(op.dirname(__file__), "amulet", "world_interface")

packs = find_packages(
    include=["amulet*"], exclude=["*.command_line", "*.command_line.*"]
)

with open(op.join('.', 'requirements.txt')) as requirements_fp:
    required_packages = [
        get_egg_name_from_git_uri(line) for line in requirements_fp.readlines()
    ]

setup(
    name="amulet-core",
    version=VERSION_NUMBER,
    packages=packs,
    include_package_data=True,
    install_requires=required_packages,
    setup_requires=required_packages,
    package_data={
        "amulet": [os.path.join(root, filename) for root, _, filenames in os.walk(world_interface_path) for filename in filenames if '__pycache__' not in root]
    }
#    dependency_links=[
#        "git+git://github.com/Amulet-Team/Amulet-NBT.git#egg=amulet-nbt",
#        "git+git://github.com/gentlegiantJGC/PyMCTranslate.git#egg=PyMCTranslate"
#    ],
)

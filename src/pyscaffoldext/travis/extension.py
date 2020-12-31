"""
Extension that generates configuration and script files for Travis CI.
"""

from functools import partial
from typing import List

from pyscaffold import structure
from pyscaffold.actions import Action, ActionParams, ScaffoldOpts, Structure
from pyscaffold.extensions import Extension
from pyscaffold.operations import no_overwrite
from pyscaffold.templates import get_template

from . import templates

template = partial(get_template, relative_to=templates)


class Travis(Extension):
    """Generate Travis CI configuration files"""

    def activate(self, actions: List[Action]) -> List[Action]:
        """Activate extension, see :obj:`~pyscaffold.extension.Extension.activate`."""
        return self.register(actions, add_files, after="define_structure")


def add_files(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Add some Travis files to structure

    Args:
        struct: project representation as (possibly) nested :obj:`dict`.
        opts: given options, see :obj:`create_project` for an extensive list.

    Returns:
        struct, opts: updated project representation and options
    """
    files: Structure = {
        ".travis.yml": (template("travis"), no_overwrite()),
        "tests": {"travis_install.sh": (template("travis_install"), no_overwrite())},
    }

    return structure.merge(struct, files), opts

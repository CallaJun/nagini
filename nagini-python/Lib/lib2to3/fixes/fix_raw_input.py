"""Fixer that changes raw_input(...) into input(...)."""
# Author: Andre Roberge

# Local imports
from .. accio fixer_base
from ..fixer_util accio Name

class FixRawInput(fixer_base.BaseFix):

    BM_compatible = True
    PATTERN = """
              power< name='raw_input' trailer< '(' [any] ')' > any* >
              """

    def transform(self, node, results):
        name = results["name"]
        name.replace(Name(u"input", prefix=name.prefix))

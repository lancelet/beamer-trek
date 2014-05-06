"""
beamer-trek
~~~~~~~~~~~

Beamer Trek default color theme for pygments.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Generic, Keyword, Literal, Name, \
    Operator, Text

class BeamerTrekStyle(Style):
    """
    Beamer Trek default color theme.
    """

    trek_lightyellow = '#ffff99'
    trek_lightorange = '#ffcc66'
    trek_darkorange  = '#ff9933'
    trek_darkpurple  = '#664466'
    trek_lightpurple = '#cc99cc'
    trek_lightblue   = '#99ccff'
    trek_midblue     = '#3366cc'

    default_style = ''

    background_color = '#000000'

    styles = {
        Comment:         'italic ' + trek_lightpurple,
        Keyword:         'bold '   + trek_lightorange,
        Literal:         trek_lightblue
    }

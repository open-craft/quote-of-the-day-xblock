"""TO-DO: Write a description of what this XBlock is."""
from __future__ import unicode_literals

import pkg_resources
from xblock.core import XBlock
from xblock.fields import List, Scope
from xblock.fragment import Fragment

from read_quote import read_quote

class QuoteOfTheDayXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    favorites = List(
        name = "Favorite quotes",
        scope = Scope.user_state,
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def _render_favorites(self):
        favorites_repr = [
            "<li><span class='author'>{author}:</span> <span class='text'>{text}</span></li>".format(
                author=quote['author'], text=quote['text']
            )
            for quote in self.favorites
        ]

        return "".join(favorites_repr)

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the QuoteOfTheDayXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/quote_of_the_day.html")
        quote, author = read_quote()
        context = {"quote": quote, "author": author, "favorites": self._render_favorites()}
        frag = Fragment(html.format(self=self, **context))
        frag.add_css(self.resource_string("static/css/quote_of_the_day.css"))
        frag.add_javascript(self.resource_string("static/js/src/quote_of_the_day.js"))
        frag.initialize_js('QuoteOfTheDayXBlock')
        return frag

    def studio_view(self, context=None):
        """
        View for editing QuoteOfTheDayXBlock in Studio.
        """
        return Fragment(u'<p>This block is missing some settings. Add them by changing this view!</p>')

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def save_to_favorites(self, data, suffix=''):
        """
        Saves quote to favorites
        """
        try:
            quote_author, quote_text = data['author'], data['text']
            self.favorites.append({"author": quote_author, "text": quote_text})
            return {"success": True, "message": "Added to favorites!"}
        except Exception as e:
            return {"success": False, "message": e.message}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("QuoteOfTheDayXBlock",
             """<quote_of_the_day/>
             """),
            ("Multiple QuoteOfTheDayXBlock",
             """<vertical_demo>
                <quote_of_the_day/>
                <quote_of_the_day/>
                <quote_of_the_day/>
                </vertical_demo>
             """),
        ]

from django.conf import settings

from jinja2 import pass_context
from jinja2.ext import Extension

from mega_menu.models import Menu


def select_menu_for_context(context):
    # First try to find a menu for the language from the context.
    language = context.get("language")

    if language:
        try:
            return Menu.objects.get(language=language)
        except Menu.DoesNotExist:
            pass

    # Next try to find a menu for the default Django language, if it differs
    # from the language in the context.
    default_language = settings.LANGUAGE_CODE[:2]
    if default_language != language:
        try:
            return Menu.objects.get(language=default_language)
        except Menu.DoesNotExist:
            pass

    # If we can't find a menu, return None.
    return None


def get_mega_menu_content(context):
    menu = select_menu_for_context(context)

    if not menu:
        return None

    return menu.get_content_for_frontend(request=context.get("request"))


class MegaMenuExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        self.environment.globals.update(
            {
                "get_mega_menu_content": pass_context(get_mega_menu_content),
            }
        )

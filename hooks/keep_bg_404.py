"""Keep the Bulgarian 404 page at the site root.

mkdocs-static-i18n builds the default language (BG) first, then builds the
site again for each other language into the same folder. Every build writes
its 404.html to the root, so the last language would win and BG visitors
would get an English header and menu. GitHub Pages serves that one file for
every missing address; overrides/404.html switches its own text to English
for /en/ addresses.
"""

_saved = {}


def on_post_template(output_content, template_name, config):
    if template_name != "404.html":
        return output_content
    if config.theme["language"] == "bg":
        _saved["bg"] = output_content
        return output_content
    return _saved.get("bg", output_content)

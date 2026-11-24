"""slugify — turn any text into a URL-safe slug.

Tiny but real: this exists so the Jenkins pipeline has actual code
to lint, test, and smoke-check.
"""
import re
import unicodedata


def slugify(text: str) -> str:
    """Convert text to a lowercase, dash-separated slug.

    >>> slugify("Hello, CI World!")
    'hello-ci-world'
    >>> slugify("  multiple   spaces  ")
    'multiple-spaces'
    >>> slugify("café över")
    'cafe-over'
    """
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower())
    return text.strip("-")

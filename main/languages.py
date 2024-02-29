from os import getenv as env

# English
import main.labels.en.base as en_base
import main.labels.en.index as en_index
import main.labels.en.errors as en_errors

# Spanish
import main.labels.es.base as es_base
import main.labels.es.index as es_index
import main.labels.es.errors as es_errors

LANGUAGES = "en", "es"

BASE = {
    "domain": env("DOMAIN", "127.0.0.1:8000"),
    "languages": LANGUAGES,
}

# Dictionary of index labels for any language
INDEX_LABELS = {
    "en": {**BASE, **en_base.UI, **en_index.UI},
    "es": {**BASE, **es_base.UI, **es_index.UI},
}

# Dictionary of error labels for any language
ERROR_LABELS = {
    "en": {**BASE, **en_base.UI, **en_index.UI},
    "es": {**BASE, **es_base.UI, **es_index.UI},
}

# Dictionary of solve labels for any language
SOLVE_LABELS = {
    "en": {**BASE, **en_base.UI, **en_index.UI},
    "es": {**BASE, **es_base.UI, **es_index.UI},
}

# Dictionary of error messages for any language
ERRORS = {
    "en": en_errors,
    "es": es_errors,
}


def select_language(lang: str) -> str:
    """
    Selects the language based on the input parameter.

    Args:
    lang (str): The language code.

    Returns:
    str: The selected language code.
    """
    if lang not in LANGUAGES:
        return "en"

    return lang


def index_labels(lang: str) -> dict:
    """
    Retrieves the index labels for the specified language.

    Args:
    lang (str): The language code.

    Returns:
    dict: The index labels for the specified language.
    """
    return INDEX_LABELS[select_language(lang)]


def solve_labels(lang: str) -> dict:
    """
    Retrieves the solve labels for the specified language.

    Args:
    lang (str): The language code.

    Returns:
    dict: The solve labels for the specified language.
    """
    return SOLVE_LABELS[select_language(lang)]


def error_labels(lang: str, error: dict) -> dict:
    """
    Retrieves the error labels for the specified language and error message.

    Args:
    lang (str): The language code.
    error (dict): The error message.

    Returns:
    dict: The error labels for the specified language and error message.
    """
    return {
        "error": error,
        **ERROR_LABELS[select_language(lang)],
    }


def error_module(lang: str) -> dict:
    """
    Retrieves the error module for the specified language.

    Args:
    lang (str): The language code.

    Returns:
    dict: The error module for the specified language.
    """
    return ERRORS[select_language(lang)]

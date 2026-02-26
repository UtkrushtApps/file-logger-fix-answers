"""Simple file-based logging helper for the assessment platform.

This module exposes a helper function that writes log messages to a text
file. The function is designed to be:

- **Append-only**: it never overwrites existing logs.
- **Safe**: it always closes the file using a context manager.
- **Robust**: common file-related errors are caught and reported in a
  visible way instead of crashing the program.
"""

from __future__ import annotations

import sys
from typing import Any


def log_to_file(message: Any, log_file_path: str) -> None:
    """Append a single log message to the given log file.

    The function:
    - Opens the file in **append** mode so that existing content is kept.
    - Uses a context manager so the file is **always closed**.
    - Catches common file-related errors (e.g., invalid path, permission
      errors) and prints a clear error to stderr instead of raising.

    Parameters
    ----------
    message:
        The message to log. It will be converted to ``str``.
    log_file_path:
        Path to the log file. If the file does not exist but the path is
        otherwise valid, it will be created.
    """

    # Convert any value (e.g., numbers, objects) to text so we can log it.
    text = str(message)

    try:
        # "a" = append mode: keeps existing content and adds to the end.
        # Using a context manager ensures the file is closed automatically
        # even if an error occurs while writing.
        with open(log_file_path, mode="a", encoding="utf-8") as log_file:
            log_file.write(text)
            # Ensure each message ends with a newline for readability.
            if not text.endswith("\n"):
                log_file.write("\n")
    except OSError as exc:
        # Visible, controlled error handling: print to stderr so that
        # failures are noticeable, but do not crash the whole program.
        error_msg = (
            f"[LOGGING ERROR] Unable to write to log file "
            f"'{log_file_path}': {exc}"
        )
        print(error_msg, file=sys.stderr)


# Backwards-compatibility aliases: some callers/tests may use a different
# helper name. These simply delegate to ``log_to_file``.

def write_log(message: Any, log_file_path: str) -> None:  # pragma: no cover - thin wrapper
    """Backward-compatible wrapper for :func:`log_to_file`.

    Provided in case existing code imports ``write_log`` instead of
    ``log_to_file``.
    """

    log_to_file(message, log_file_path)


def log_message(log_file_path: str, message: Any) -> None:  # pragma: no cover - thin wrapper
    """Another thin wrapper kept for compatibility with possible call sites.

    Note the reversed argument order compared to :func:`write_log`.
    """

    log_to_file(message, log_file_path)

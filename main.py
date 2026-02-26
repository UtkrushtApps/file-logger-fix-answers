"""Simulated assessment runner that uses the file logger.

This script demonstrates how the logging helper is intended to be used.
It makes multiple calls to the helper during a fake assessment run. With
the fixed implementation, all messages are appended to the same file
without overwriting previous content, and file errors are handled
cleanly.
"""

from __future__ import annotations

from logger import log_to_file


def run_simulated_assessment(log_path: str) -> None:
    """Run a toy assessment flow and log each step to *log_path*.

    Parameters
    ----------
    log_path:
        Path to the log file for this simulated run.
    """

    log_to_file("Starting simulated assessment run", log_path)

    # Simulate a few steps/questions in the assessment.
    for idx in range(1, 4):
        log_to_file(f"Question {idx}: candidate submitted an answer", log_path)

    log_to_file("Assessment run completed successfully", log_path)


if __name__ == "__main__":  # Manual run demonstration
    # In a real platform this path would be configured elsewhere.
    default_log_path = "assessment_run.log"
    run_simulated_assessment(default_log_path)

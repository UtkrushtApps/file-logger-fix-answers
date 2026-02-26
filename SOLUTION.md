# Solution Steps

1. Open the logger module file (e.g. `logger.py`) where the helper function for writing logs is defined.

2. Change the file open mode from write (`'w'`) to append (`'a'`) so that each new call adds to the end of the file instead of overwriting existing content.

3. Wrap the file handling logic in a `with open(...):` context manager so the file is automatically and reliably closed after writing, even if an error occurs while writing.

4. Ensure the message argument is converted to a string (e.g. `text = str(message)`) so that non-string values can also be logged without raising a `TypeError`.

5. After writing the message, add a newline when needed (only if the message does not already end with `"\n"`) so each log entry appears on its own line in the log file.

6. Surround the call to `open` and the `write` operation with a `try`/`except` block that catches `OSError` (or `IOError`) to handle common file-related errors such as invalid paths or permission issues.

7. Inside the `except` block, print a clear, descriptive error message to `sys.stderr` (e.g. `print(f"[LOGGING ERROR] ...", file=sys.stderr)`) so logging failures are visible but do not crash the whole program.

8. Keep the logger function’s public interface the same as before (same function name and parameters) so existing code in the main script can continue calling it without changes; optionally, add thin wrapper functions if you need to support multiple historical names/signatures.

9. Open the main script file (e.g. `main.py`) and ensure it imports the logger helper from the logger module and calls it multiple times during the simulated assessment run, passing the same log file path each time.

10. Run the main script to confirm that multiple calls append to a single log file, that the file is closed properly after execution, and that providing an invalid path results in a readable error on stderr instead of an unhandled exception.


# symphony-test-board

Tiny Python library used as a test bed for the Symphony orchestrator
(per-issue agent runner against GitHub Issues).

It deliberately has a small surface (`greet`, `shout`) so that any
Symphony-driven change is small enough to verify in a single turn:

- `greet.py`         — two trivial functions.
- `test_greet.py`    — pytest cases covering both functions.
- `pyproject.toml`   — `pip install -e .` + `pytest` work without extras.

The repository is configured to be safely runnable on a Raspberry Pi
(aarch64, Ubuntu 24.04, Python 3.12). No platform-specific code.

Symphony workflow contract:

- Issues in the `open` state are eligible for dispatch.
- The orchestrator polls every 30s (configurable).
- Per-issue workspaces live under `~/.cache/symphony/workspaces/`.
- Each workspace is bootstrapped with `git clone` of this repo.
- The agent (`opencode acp`) makes the change, runs `pytest`, and
  opens a pull request back to `main`.

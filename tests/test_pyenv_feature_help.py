from test_pyenv import TestPyenvBase
from test_pyenv_helpers import run_pyenv_test


class TestPyenvFeatureGlobal(TestPyenvBase):
    def test_help(self, setup):
        def commands(ctx):
            stdout, stderr = ctx.pyenv("help")
            stdout = "\r\n".join(stdout.splitlines()[:2])
            assert stdout.strip() == "Usage: pyenv <command> [<args>]"
            assert stderr == ""
        run_pyenv_test({}, commands)

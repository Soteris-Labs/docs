"""Regression checks for the docs validation workflow, using only the stdlib."""

from pathlib import Path
import re
import unittest


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/docs-validation.yml"


class DocsValidationTest(unittest.TestCase):
    def setUp(self):
        self.workflow = WORKFLOW.read_text()

    def test_main_triggers_without_path_filters(self):
        self.assertIn(
            "on:\n  pull_request:\n    branches: [main]\n"
            "  push:\n    branches: [main]\n",
            self.workflow,
        )
        self.assertNotRegex(self.workflow, r"(?m)^\s+(?:paths|paths-ignore|if):")

    def test_read_only_permissions_and_stable_job(self):
        self.assertIn("permissions:\n  contents: read\n", self.workflow)
        self.assertIn("jobs:\n  docs-validation:\n    name: docs-validation\n", self.workflow)
        self.assertNotIn("secrets.", self.workflow)
        self.assertNotIn("continue-on-error:", self.workflow)

    def test_actions_and_node_are_pinned(self):
        actions = re.findall(r"uses: (\S+)", self.workflow)
        self.assertEqual(actions, [
            "actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd",
            "actions/setup-node@v4.4.0",
        ])
        self.assertIn("node-version: '22.23.4'", self.workflow)

    def test_pinned_cli_runs_in_content_root(self):
        self.assertIn(
            "      - name: Check broken links\n"
            "        working-directory: site\n"
            "        run: npx --yes mint@4.2.676 broken-links\n",
            self.workflow,
        )


if __name__ == "__main__":
    unittest.main()

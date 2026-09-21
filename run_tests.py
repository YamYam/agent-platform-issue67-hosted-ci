import json
import os
import unittest
from pathlib import Path

result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.discover(str(Path(__file__).parent)))
counts = dict(head=os.environ.get('GITHUB_SHA', 'local'), tests=result.testsRun,
              skips=len(result.skipped), failures=len(result.failures) + len(result.errors))
print('::notice title=agent-tests::' + json.dumps(counts))
raise SystemExit(0 if result.wasSuccessful() and result.testsRun > 0 and not result.skipped else 1)

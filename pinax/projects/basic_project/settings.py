"""
This is the Pinax project settings file. Don't add settings here,
instead modify the appropriate file (or add new files) within the
conf/ directory.

"""
import os.path
from pinax.utils.conf import get_settings

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

locals().update(get_settings(PROJECT_ROOT))

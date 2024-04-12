import os
from pathlib import Path

from dotenv import load_dotenv
from fsspec import fuse

from dbfs_modified import DatabricksFileSystem

load_dotenv()

mount_path = Path("dbfs")
mount_path.mkdir(exist_ok=True)

fs = DatabricksFileSystem(
    instance=os.getenv("DATABRICKS_INSTANCE"), token=os.getenv("DATABRICKS_TOKEN")
)
fuse.run(
    fs, path="/", mount_point=str(mount_path.absolute()), threads=False, foreground=True
)

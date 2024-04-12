import os
from pathlib import Path

# import requests
from dotenv import load_dotenv
from fsspec import filesystem, fuse
from fsspec.implementations.dbfs import DatabricksFileSystem
from fsspec.implementations.local import LocalFileSystem

load_dotenv()

# # from fsspec.implementations.dbfs import DatabricksFileSystem



fs = filesystem("dbfs", instance=os.getenv("DATABRICKS_INSTANCE"), token=os.getenv("DATABRICKS_TOKEN"))


print(fs.ls("/databricks-datasets/"))


# fuse.run(fs, path="/", mount_point="/workspaces/db_fsspec/databricks-datasets/", threads=False, foreground=True)

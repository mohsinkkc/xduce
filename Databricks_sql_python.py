from databricks import sql
import os

with sql.connect(server_hostname = os.getenv("MOHASIN-DTS"),
                 http_path       = os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:


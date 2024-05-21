import os
from snowflake.snowpark import Session
from snowflake.ml.utils import connection_params

sp_session = Session.builder.configs(connection_params.SnowflakeLoginOptions()).create()

DEFAULT_SESSION_TIMEOUT_SEC = int(os.environ.get("SNOWFLAKE_SESSION_TIMEOUT_SEC", 120))
SNOWFLAKE_ROLE = sp_session.get_current_role()
SNOWFLAKE_WAREHOUSE = sp_session.get_current_warehouse()
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_HOST = sp_session.get_current_account()

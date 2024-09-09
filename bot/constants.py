from pydantic_settings import BaseSettings


class EnvConfig(
    BaseSettings,
    env_file=(".env.server", ".env"),
    env_file_encoding="utf-8",
    env_nested_delimiter="__",
    extra="ignore",
):
    """Configs"""


class _Bot(EnvConfig, env_prefix="bot_"):
    prefix: str = "!"
    token: str


Bot = _Bot()  # type: ignore


class _Project(EnvConfig, env_prefix="project_"):
    root_folder: str
    extension_folder: str


Project = _Project()  # type: ignore

class _Database(EnvConfig, env_prefix="database_"):
    url: str


Database = _Database()  # type: ignore
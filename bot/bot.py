"""Módulo principal"""
from discord.ext.commands import Bot

from importlib import import_module
from pkgutil import iter_modules, walk_packages
from pathlib import Path

from bot.constants import Project


class Pudimversify(Bot):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            *args,
            **kwargs,
        )

    async def _load_extensions(self) -> None:
        try:
            ext_module = next(
                (
                    import_module(name=name, package=Project.root_folder)
                    for _, name, is_pkg in walk_packages(
                        path=[str(Path(Project.root_folder).resolve())],
                        prefix=f"{Project.root_folder}.",
                    )
                    if name.endswith(Project.extension_folder) and is_pkg
                ),
            )
        except StopIteration:
            message = "Módulo de extensão em falta, verifique o pacote."
            raise ModuleNotFoundError(message)

        for _, extension, _ in iter_modules(
            path=[str(Path(ext_module.__path__[0]).resolve())],
            prefix=f"{ext_module.__name__}.",
        ):
            if not Path(f"{str(extension).replace(".", "/")}/entrypoint.py").is_file():
                continue

            try:
                await self.load_extension(f"{extension}.entrypoint")
            except Exception:
                continue

    async def setup_hook(self) -> None:
        await self._load_extensions()
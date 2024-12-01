from dependency_injector import containers, providers
from core.utils.db_api import Database, connect


class DBContainer(containers.DeclarativeContainer):
    """DI-контейнер для базы данных."""

    # pool connection provider
    db_pool = providers.Resource(connect)

    # Database instance provider
    db = providers.Factory(Database, pool=db_pool)

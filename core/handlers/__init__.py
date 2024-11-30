from aiogram import Router
from . import users


def get_routers() -> list[Router]:
    main_group_router = Router()
    main_group_router.include_routers(
        users.basic.router,
    )

    return [
        main_group_router,
    ]

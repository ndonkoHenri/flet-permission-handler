import asyncio
from typing import Optional

import flet as ft
from .types import PermissionStatus, PermissionType

__all__ = ["PermissionHandler"]


@ft.control("PermissionHandler")
class PermissionHandler(ft.Service):
    """
    A control that allows you check and request permission from your device.
    This control is non-visual and should be added to `page.overlay` list.

    -----

    Online docs: https://flet.dev/docs/controls/permissionhandler
    """

    async def check_permission_async(
        self, type: PermissionType
    ) -> Optional[PermissionStatus]:
        r = await self._invoke_method_async("check_permission", {"type": type})
        return PermissionStatus(r) if r is not None else None

    async def request_permission_async(
        self, type: PermissionType
    ) -> Optional[PermissionStatus]:
        r = await self._invoke_method_async("request_permission", {"type": type})
        return PermissionStatus(r) if r is not None else None

    def open_app_settings(self):
        asyncio.create_task(self.open_app_settings_async())

    async def open_app_settings_async(self):
        return await self._invoke_method_async("open_app_settings")

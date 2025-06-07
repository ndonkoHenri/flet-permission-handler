from typing import Optional

import flet as ft

from .types import Permission, PermissionStatus

__all__ = ["PermissionHandler"]


@ft.control("PermissionHandler")
class PermissionHandler(ft.Service):
    """
    A control that allows you check and request permission from your device.
    This control is non-visual and should be added to `page.overlay` list.

    -----

    Online docs: https://flet.dev/docs/controls/permissionhandler
    """

    async def get_status_async(
        self, permission: Permission
    ) -> Optional[PermissionStatus]:
        """
        Gets the current status of the given `permission`.

        Returns `PermissionStatus` if the status is known, otherwise `None`.
        """
        status = await self._invoke_method_async(
            "get_status",
            {"permission": permission}
        )
        return PermissionStatus(status) if status is not None else None

    async def request_async(
        self, permission: Permission
    ) -> Optional[PermissionStatus]:
        """
        Request the user for access to the `permission`.
        if access hasn't already been granted access before.

        Returns the new `PermissionStatus`.
        """
        r = await self._invoke_method_async(
            "request",
            {"permission": permission}
        )
        return PermissionStatus(r) if r is not None else None

    async def open_app_settings_async(self) -> bool:
        """
        Opens the app settings page.

        Returns `True` if the app settings page could be opened, otherwise `False`.
        """
        return await self._invoke_method_async("open_app_settings")

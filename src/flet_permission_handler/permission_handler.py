from typing import Optional

import flet as ft

from .types import Permission, PermissionStatus

__all__ = ["PermissionHandler"]


@ft.control("PermissionHandler")
class PermissionHandler(ft.Service):
    """
    A control that allows you check and request permission from your device.
    This control is non-visual and should be added to `page.services` list.

    Note: This control is currently only supported on Android, iOS, Windows, and Web platforms.
    """

    def before_update(self):
        super().before_update()
        self.__validate_platform()

    def __validate_platform(self):
        """Validates if the current platform supports the PermissionHandler."""
        if not (self.page.web or self.page.platform in [
            ft.PagePlatform.ANDROID,
            ft.PagePlatform.IOS,
            ft.PagePlatform.WINDOWS,
        ]):
            raise ft.FletUnimplementedPlatformEception(
                "PermissionHandler is currently only supported on Android, iOS, Windows, and Web platforms."
            )

    async def get_status_async(
        self, permission: Permission
    ) -> Optional[PermissionStatus]:
        """
        Gets the current status of the given `permission`.

        Returns `PermissionStatus` if the status is known, otherwise `None`.
        """
        self.__validate_platform()
        status = await self._invoke_method_async(
            "get_status",
            {"permission": permission}
        )
        return PermissionStatus(status) if status is not None else None

    async def request_async(
        self, permission: Permission, timeout: int = 60
    ) -> Optional[PermissionStatus]:
        """
        Request the user for access to the `permission`.
        if access hasn't already been granted access before.

        Returns the new `PermissionStatus`.
        """
        self.__validate_platform()
        r = await self._invoke_method_async(
            "request",
            {"permission": permission},
            timeout=timeout
        )
        return PermissionStatus(r) if r is not None else None

    async def open_app_settings_async(self) -> bool:
        """
        Opens the app settings page.

        Returns `True` if the app settings page could be opened, otherwise `False`.
        """
        self.__validate_platform()
        return await self._invoke_method_async("open_app_settings")

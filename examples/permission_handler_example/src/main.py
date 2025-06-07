import flet as ft

import flet_permission_handler as fph


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.appbar = ft.AppBar(title=ft.Text("PermissionHandler Tests"))

    async def check_permission(e):
        s = await ph.get_status_async(e.control.data)
        page.add(ft.Text(f"{e.control.data.name} status: {s}"))

    async def request_permission(e):
        s = await ph.request_async(e.control.data)
        page.add(ft.Text(f"Requested {e.control.data.name}: {s}"))

    async def open_app_settings(e):
        await ph.open_app_settings_async()

    ph = fph.PermissionHandler()
    page.services.append(ph)

    page.add(
        ft.OutlinedButton(
            "Get Microphone PermissionStatus",
            data=fph.Permission.MICROPHONE,
            on_click=check_permission,
        ),
        ft.OutlinedButton(
            "Request Microphone Permission",
            data=fph.Permission.MICROPHONE,
            on_click=request_permission,
        ),
        ft.OutlinedButton(
            "Open App Settings",
            on_click=open_app_settings,
        ),
    )


ft.app(main)

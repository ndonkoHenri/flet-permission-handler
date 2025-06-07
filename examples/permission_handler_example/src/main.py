import flet as ft

import flet_permission_handler as fph


def main(page: ft.Page):
    page.appbar = ft.AppBar(title="PermissionHandler Playground")

    def show_snackbar(message: str):
        page.show_dialog(ft.SnackBar(ft.Text(message)))

    async def get_permission_status(e: ft.ControlEvent):
        status = await p.get_status_async(fph.Permission.MICROPHONE)
        show_snackbar(f"Microphone permission status: {status.name}")

    async def request_permission(e: ft.ControlEvent):
        status = await p.request_async(fph.Permission.MICROPHONE)
        show_snackbar(f"Requested microphone permission: {status.name}")

    async def open_app_settings(e: ft.ControlEvent):
        show_snackbar("Opening app settings...")
        await p.open_app_settings_async()

    p = fph.PermissionHandler()
    page.services.append(p)  # (1)!

    page.add(
        ft.OutlinedButton("Open app settings", on_click=open_app_settings),
        ft.OutlinedButton("Request Microphone permission", on_click=request_permission),
        ft.OutlinedButton(
            "Get Microphone permission status", on_click=get_permission_status
        ),
    )


ft.run(main)

# flet-permission-handler

[![pypi](https://img.shields.io/pypi/v/flet-permission-handler.svg)](https://pypi.python.org/pypi/flet-permission-handler)
[![downloads](https://static.pepy.tech/badge/flet-permission-handler/month)](https://pepy.tech/project/flet-permission-handler)
[![license](https://img.shields.io/github/license/flet-dev/flet-permission-handler.svg)](https://github.com/flet-dev/flet-permission-handler/blob/main/LICENSE)

A Flet extension that simplifies working with permissions in your app.

It is based on the [permission_handler](https://pub.dev/packages/permission_handler) Flutter package
and brings similar functionality to Flet, including:

- Requesting permissions at runtime
- Checking the current permission status (e.g., granted, denied)
- Redirecting users to system settings to manually grant permissions

## Platform Support

This package supports the following platforms:

| Platform | Supported |
|----------|:---------:|
| Windows  |     ✅     |
| macOS    |     ❌     |
| Linux    |     ❌     |
| iOS      |     ✅     |
| Android  |     ✅     |
| Web      |     ✅     |

## Example

```python title="main.py"
--8<-- "examples/permission_handler_example/src/main.py"
``` 

1. The [`PermissionHandler`][flet_permission_handler.permission_handler.PermissionHandler] instance must be added to the
   page's [`services`](https://flet.dev/docs/controls/page#services) (not `controls`) list to work properly.
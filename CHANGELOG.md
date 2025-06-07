# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2025-mm-dd

## Added

- Deployed online documentation: https://flet-dev.github.io/flet-permission-handler/

### Changed

- **Breaking**: The following methods of `PermissionHandler` have been removed:
    * `open_app_settings()` → replaced by `open_app_settings_async()`.
    * `request_permission()` / `request_permission_async()` → replaced by `request_async()`.
    * `check_permission()` / `check_permission_async()` → replaced by `get_status_async()`.

- **Breaking**: The `PermissionType` enum has been renamed to `Permission`.
- **Breaking**: The `PermissionHandler` class can now only be used on the following platforms: Windows, iOS, Android,
  and Web. A `FletUnimplementedPlatformEception` will be raised if used on other (unsupported) platforms.

## [0.1.0] - 2025-01-15

Initial release.


[Unreleased]: https://github.com/flet-dev/flet-permission-handler/compare/0.1.0...HEAD

[0.1.0]: https://github.com/flet-dev/flet-permission-handler/releases/tag/0.1.0
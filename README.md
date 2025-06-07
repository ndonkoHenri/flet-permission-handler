# flet-permission-handler

<a href="https://pypi.org/project/flet-permission-handler" target="_blank">
    <img src="https://img.shields.io/pypi/v/flet-permission-handler?color=%2334D058" alt="Package version">
</a>

<a href="https://pypi.org/project/flet-permission-handler" target="_blank">
    <img src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fflet-dev%2Fflet-permission-handler%2Frefs%2Fheads%2Fmain%2Fpyproject.toml" alt="Supported Python versions">
</a>

<br>

<img src="https://img.shields.io/badge/Platform-Windows-blue?logo=windows" alt="Windows">
<img src="https://img.shields.io/badge/Platform-iOS-lightgrey?logo=apple" alt="iOS">
<img src="https://img.shields.io/badge/Platform-Android-green?logo=android" alt="Android">
<img src="https://img.shields.io/badge/Platform-Web-blue?logo=googlechrome" alt="Web">

`flet-permission-handler` is a Flet extension that simplifies working with permissions in your app.

It is based on the popular [permission_handler](https://pub.dev/packages/permission_handler) Flutter package
and brings similar functionality to Flet, including:

- Requesting permissions at runtime
- Checking the current permission status
- Redirecting users to system settings to manually grant permissions

## Platform Support

| Platform | Supported |
|----------|:---------:|
| Windows  |     ✅     |
| macOS    |     ❌     |
| Linux    |     ❌     |
| iOS      |     ✅     |
| Android  |     ✅     |
| Web      |     ✅     |

## Setup

- Add `flet-permission-handler` as dependency (`pyproject.toml` or `requirements.txt`) to your Flet project.

- Ensure that your app has the necessary [permissions declared](https://flet.dev/docs/publish#permissions).

## Examples

For examples, see [this](https://github.com/flet-dev/flet-permission-handler/tree/main/examples)
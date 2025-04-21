from enum import Enum

__all__ = [
    "PermissionStatus",
    "PermissionType",
]


class PermissionStatus(Enum):
    GRANTED = "granted"
    DENIED = "denied"
    PERMANENTLY_DENIED = "permanentlyDenied"
    LIMITED = "limited"
    PROVISIONAL = "provisional"
    RESTRICTED = "restricted"


class PermissionType(Enum):
    ACCESS_MEDIA_LOCATION = "accessMediaLocation"
    ACCESS_NOTIFICATION_POLICY = "accessNotificationPolicy"
    ACTIVITY_RECOGNITION = "activityRecognition"
    APP_TRACKING_TRANSPARENCY = "appTrackingTransparency"
    ASSISTANT = "assistant"
    AUDIO = "audio"
    BACKGROUND_REFRESH = "backgroundRefresh"
    BLUETOOTH = "bluetooth"
    BLUETOOTH_ADVERTISE = "bluetoothAdvertise"
    BLUETOOTH_CONNECT = "bluetoothConnect"
    BLUETOOTH_SCAN = "bluetoothScan"
    CALENDAR_FULL_ACCESS = "calendarFullAccess"
    CALENDAR_WRITE_ONLY = "calendarWriteOnly"
    CAMERA = "camera"
    CONTACTS = "contacts"
    CRITICAL_ALERTS = "criticalAlerts"
    IGNORE_BATTERY_OPTIMIZATIONS = "ignoreBatteryOptimizations"
    LOCATION = "location"
    LOCATION_ALWAYS = "locationAlways"
    LOCATION_WHEN_IN_USE = "locationWhenInUse"
    MANAGE_EXTERNAL_STORAGE = "manageExternalStorage"
    MEDIA_LIBRARY = "mediaLibrary"
    MICROPHONE = "microphone"
    NEARBY_WIFI_DEVICES = "nearbyWifiDevices"
    NOTIFICATION = "notification"
    PHONE = "phone"
    PHOTOS = "photos"
    PHOTOS_ADD_ONLY = "photosAddOnly"
    REMINDERS = "reminders"
    REQUEST_INSTALL_PACKAGES = "requestInstallPackages"
    SCHEDULE_EXACT_ALARM = "scheduleExactAlarm"
    SENSORS = "sensors"
    SENSORS_ALWAYS = "sensorsAlways"
    SMS = "sms"
    SPEECH = "speech"
    STORAGE = "storage"
    SYSTEM_ALERT_WINDOW = "systemAlertWindow"
    UNKNOWN = "unknown"
    VIDEOS = "videos"

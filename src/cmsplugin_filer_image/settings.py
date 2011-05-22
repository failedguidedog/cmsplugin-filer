from django.conf import settings

ENABLE_IMAGE_URL = getattr(settings, "CMSPLUGIN_FILER_IMAGE_ENABLE_IMAGE_URL", True)
ENABLE_ALT_TEXT = getattr(settings, "CMSPLUGIN_FILER_IMAGE_ENABLE_ALT_TEXT", True)
ENABLE_AUTOMATIC_SCALING = getattr(settings, "CMSPLUGIN_FILER_IMAGE_ENABLE_AUTOMATIC_SCALING", True)
ENABLE_INDIVIDUAL_THUMBNAIL_SETTINGS = getattr(settings, "CMSPLUGIN_FILER_IMAGE_ENABLE_INDIVIDUAL_THUMBNAIL_SETTINGS", True)
ENABLE_ZOOMABLE = getattr(settings, "CMSPLUGIN_FILER_IMAGE_ENABLE_ZOOM", True)

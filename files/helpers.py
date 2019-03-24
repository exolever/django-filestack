from .conf import settings


UPLOADED_FILE_VERSIONED_MIMETYPE = {
    settings.FILES_CH_RESOURCE_ITEM_TYPE_PDF: [
        settings.FILES_APPLICATION_PDF
    ],
    settings.FILES_CH_RESOURCE_ITEM_TYPE_SLIDES: [
        settings.FILES_APPLICATION_VND_PRESENTATION,
        settings.FILES_APPLICATION_VND_GOOGLE,
    ],
    settings.FILES_CH_RESOURCE_ITEM_TYPE_SPREEDSHET: [
        settings.FILES_APPLICATION_VND_XML_SHEET,
        settings.FILES_APPLICATION_VND_XML_SPREADSHEET,
    ],
    settings.FILES_CH_RESOURCE_ITEM_TYPE_IMG: [
        settings.FILES_IMG_JPEG,
        settings.FILES_IMG_PNG,
        settings.FILES_IMG_SVG,
    ],
    settings.FILES_CH_RESOURCE_ITEM_TYPE_LINKS: [
        settings.FILES_AUDIO_MPEG,
        settings.FILES_AUDIO_MP3,
        settings.FILES_APPLICATION_ZIP,
        settings.FILES_APPLICATION_X_ZIP,
        settings.FILES_APPLICATION_OCTET,
    ],
    settings.FILES_CH_RESOURCE_ITEM_TYPE_DOC: [
        settings.FILES_TEXT_HTML,
        settings.FILES_TEXT_PLAIN,
        settings.FILES_APPLICATION_RTF,
        settings.FILES_APPLICATION_VND_OASIS,
        settings.FILES_APPLICATION_VND_XML_DOC,
        settings.FILES_TEXT_CSV,
    ],
}

DEFAULT_MIMETYPE = settings.FILES_CH_RESOURCE_ITEM_TYPE_DOC

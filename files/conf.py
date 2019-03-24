# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# python imports
import logging

# 3rd. libraries imports
from appconf import AppConf

# django imports
from django.conf import settings  # noqa

logger = logging.getLogger(__name__)


class FileConfig(AppConf):
    CH_RESOURCE_ITEM_TYPE_PDF = 'P'
    CH_RESOURCE_ITEM_TYPE_DOC = 'D'
    CH_RESOURCE_ITEM_TYPE_SLIDES = 'S'
    CH_RESOURCE_ITEM_TYPE_FORM = 'F'
    CH_RESOURCE_ITEM_TYPE_SPREEDSHET = 'R'
    CH_RESOURCE_ITEM_TYPE_VIDEO = 'V'
    CH_RESOURCE_ITEM_TYPE_LINKS = 'L'
    CH_RESOURCE_ITEM_TYPE_IMG = 'I'
    CH_RESOURCE_ITEM_TYPE_UPLOADER = 'U'
    CH_RESOURCE_ITEM_TYPE_DEFAULT = CH_RESOURCE_ITEM_TYPE_PDF

    CH_RESOURCE_ITEM_TYPE = (
        (CH_RESOURCE_ITEM_TYPE_PDF, 'PDF'),
        (CH_RESOURCE_ITEM_TYPE_DOC, 'Document'),
        (CH_RESOURCE_ITEM_TYPE_SLIDES, 'Slides'),
        (CH_RESOURCE_ITEM_TYPE_FORM, 'Form'),
        (CH_RESOURCE_ITEM_TYPE_SPREEDSHET, 'Spreedshet'),
        (CH_RESOURCE_ITEM_TYPE_VIDEO, 'Video'),
        (CH_RESOURCE_ITEM_TYPE_LINKS, 'Link'),
        (CH_RESOURCE_ITEM_TYPE_UPLOADER, 'Uploader')
    )

    TEXT_HTML = 'text/html'
    TEXT_PLAIN = 'text/plain'
    APPLICATION_RTF = 'application/rtf'
    APPLICATION_VND_OASIS = 'application/vnd.oasis.opendocument.text'
    APPLICATION_PDF = 'application/pdf'
    APPLICATION_VND_XML_DOC = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    APPLICATION_VND_XML_SHEET = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    APPLICATION_VND_XML_SPREADSHEET = 'application/x-vnd.oasis.opendocument.spreadsheet'
    TEXT_CSV = 'text/csv'
    IMG_JPEG = 'image/jpeg'
    IMG_PNG = 'image/png'
    IMG_SVG = 'image/svg+xml'
    APPLICATION_VND_PRESENTATION = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    APPLICATION_VND_GOOGLE = 'application/vnd.google-apps.script+json'
    AUDIO_MPEG = 'audio/mpeg'
    AUDIO_MP3 = 'audio/mp3'
    APPLICATION_ZIP = 'application/zip'
    APPLICATION_X_ZIP = 'application/x-zip-compressed'
    APPLICATION_OCTET = 'application/octet-stream'

    UPLOADED_FILE_PERM_FULL = 'full_view'
    UPLOADED_FILE_PERM_VIEW = 'view'

    CDN_FILESTACK = 'cdn.filestackcontent.com'

    UPLOADED_FILE_STATUS_ACTIVE = 'Stored'
    UPLOADED_FILE_STATUS_INTRANSIT = 'InTransit'
    UPLOADED_FILE_STATUS_FAILED = 'Failed'
    UPLOADED_FILE_STATUS_DISABLED = 'Disabled'

    UPLOADED_FILE_STATUS_CH = (
        (UPLOADED_FILE_STATUS_ACTIVE, 'Active'),
        (UPLOADED_FILE_STATUS_INTRANSIT, 'InTransit'),
        (UPLOADED_FILE_STATUS_FAILED, 'Failed'),
        (UPLOADED_FILE_STATUS_DISABLED, 'Disabled'),
    )

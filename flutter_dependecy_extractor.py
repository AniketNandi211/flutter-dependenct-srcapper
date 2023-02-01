# import os
# import time
# import io

import uris
import scrapper
from scrapper import parseLink
import constants


def __extract_package_version(uri: str) -> str:
    soup = parseLink(uri)
    span = scrapper.findElement(soup, constants.FLUTTER_PACKAGE_TITLE_CLASS)
    return scrapper.findElement(span, constants.FLUTTER_PACKAGE_CONTENT_COPY_CLASS)[constants.FLUTTER_DEPENDENCY_TEXT_COPY_ATTRIBUTE].replace('^', '')


def extract_flutter_package_versions():
    uri_set = uris.flutter_dependency_uri_list
    dependency_version_set = []
    content = ''
    for uri in uri_set:
        dependency_version_set.append(__extract_package_version(uri))
    print('\n\n')
    for version in dependency_version_set:
        print(f'{version}')
    #  add a logic to arrange the text and make it copy
    #  to system clipboard

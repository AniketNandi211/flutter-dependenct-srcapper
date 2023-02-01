# General uses for testing features with scraper
google_uri = 'https://www.google.com'
amazon_uri = 'https://www.amazon.in/'

# flutter package uris core [exported as List of uris]
# core dependencies
__flutter_dio_uri = 'https://pub.dev/packages/dio'
__flutter_path_provider_uri = 'https://pub.dev/packages/path_provider'
__flutter_screenutil_uri = 'https://pub.dev/packages/flutter_screenutil'
__flutter_filepicker_uri = 'https://pub.dev/packages/file_picker'
__flutter_svg_asset_uri = 'https://pub.dev/packages/flutter_svg'
__flutter_openfile_uri = 'https://pub.dev/packages/open_file_safe'
__flutter_version_info_uri = 'https://pub.dev/packages/package_info_plus'

# state management solutions (anyone should be used)
__flutter_getx_uri = 'https://pub.dev/packages/get'
__flutter_riverpod_uri = 'https://pub.dev/packages/flutter_riverpod'
__flutter_provider_uri = 'https://pub.dev/packages/provider'

# optional
__flutter_permission_handler_uri = 'https://pub.dev/packages/permission_handler'
__flutter_hooks_uri = 'https://pub.dev/packages/flutter_hooks'
__flutter_animations_uri = 'https://pub.dev/packages/animations'
__flutter_connectivity_uri = 'https://pub.dev/packages/connectivity_plus'
__flutter_frezzed_uri = 'https://pub.dev/packages/freezed_annotation'

# required dependency list
flutter_dependency_uri_list = [
    # common
    __flutter_dio_uri,
    __flutter_path_provider_uri,
    __flutter_screenutil_uri,
    __flutter_filepicker_uri,
    __flutter_svg_asset_uri,
    __flutter_openfile_uri,
    __flutter_version_info_uri,
    # state management
    __flutter_riverpod_uri,
    # optional
    __flutter_permission_handler_uri,
    __flutter_connectivity_uri
]

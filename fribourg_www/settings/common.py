# Django settings for project project.

# ugettext_laty not supported to writre to db in PageAdmin

import os

DJANGO_BASE = os.path.dirname(os.path.dirname(__file__))
PROJECT_BASE = os.path.dirname(DJANGO_BASE)

gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (('Jonathan Stoppani', 'st.jonathan@gmail.com'),)

SEND_BROKEN_LINK_EMAILS = True

IGNORABLE_404_ENDS = ['favicon.ico','favicon.png','favicon.ico/']

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_BASE, 'data', 'database.db')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_BASE, 'htdocs')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.filesystem.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'cms.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
)

ROOT_URLCONF = 'urls'

SECRET_KEY = 'trtzz-r^8-0noo-=eq$lh73fzwm)xeal5-@%99*0f#vp7&w2yw'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_BASE, 'templates'),
)

INSTALLED_APPS = (
    #'coffin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.syndication',
 #   'south',
    'tinymce',
    'cms',
    'menus',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'mptt',
    'publisher',
    'schedule',
    #'articles',
    'calendars',
    'filebrowser',
)

LANGUAGES = (
    ('fr', gettext('French')),
    ('de', gettext('German')),
    #('en', gettext('English')),
)

CMS_HIDE_UNTRANSLATED = False
CMS_LANGUAGE_FALLBACK = True

CMS_TEMPLATES = (
    ('default.html', gettext('Default template')),
    ('index.html', gettext('Homepage template')),
    ('calendar.html', gettext('Calendar month')),
)

CMS_PERMISSION = True
CMS_SOFTROOT = True
CMS_MODERATOR = False
CMS_CONTENT_CACHE_DURATION = 1

# Django-schedule configuration
FIRST_DAY_OF_WEEK = 1 # Monday

TINYMCE_JS_URL = os.path.join(MEDIA_URL, 'scripts', 'tiny_mce', 'tiny_mce.js')
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, 'scripts', 'tiny_mce')

TINYMCE_DEFAULT_CONFIG = {
    'width': 600,
    'height': 400,
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_buttons3_add' : "tablecontrols",
}


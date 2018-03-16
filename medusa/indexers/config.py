# coding=utf-8

"""Indexer config module."""
from __future__ import unicode_literals

from medusa.app import BASE_PYMEDUSA_URL
from medusa.indexers.imdb.api import Imdb
from medusa.indexers.tmdb.api import Tmdb
from medusa.indexers.tvdbv2.api import TVDBv2
from medusa.indexers.tvmaze.api import TVmaze
from medusa.session.core import MedusaSafeSession, MedusaSession


initConfig = {
    'valid_languages': [
        "da", "fi", "nl", "de", "it", "es", "fr", "pl", "hu", "el", "tr",
        "ru", "he", "ja", "pt", "zh", "cs", "sl", "hr", "ko", "en", "sv", "no"
    ],
    'langabbv_to_id': {
        'el': 20, 'en': 7, 'zh': 27,
        'it': 15, 'cs': 28, 'es': 16, 'ru': 22, 'nl': 13, 'pt': 26, 'no': 9,
        'tr': 21, 'pl': 18, 'fr': 17, 'hr': 31, 'de': 14, 'da': 10, 'fi': 11,
        'hu': 19, 'ja': 25, 'he': 24, 'ko': 32, 'sv': 8, 'sl': 30
    }
}

INDEXER_TVDBV2 = 1
INDEXER_TVRAGE = 2  # Must keep
INDEXER_TVMAZE = 3
INDEXER_TMDB = 4
# FIXME: Change all references to EXTERNAL_IMDB to INDEXER_IMDB
INDEXER_IMDB = EXTERNAL_IMDB = 10
EXTERNAL_ANIDB = 11
EXTERNAL_TRAKT = 12

EXTERNAL_MAPPINGS = {
    EXTERNAL_ANIDB: 'anidb_id',
    INDEXER_TVRAGE: 'tvrage_id',
    EXTERNAL_TRAKT: 'trakt_id'
}

# trakt indexer name vs Medusa indexer
TRAKT_INDEXERS = {'tvdb': INDEXER_TVDBV2, 'tmdb': INDEXER_TMDB, 'imdb': INDEXER_IMDB, 'trakt': EXTERNAL_TRAKT}

STATUS_MAP = {
    'returning series': 'Continuing',
    'canceled/ended': 'Ended',
    'tbd/on the bubble': 'Continuing',
    'in development': 'Continuing',
    'new series': 'Continuing',
    'never aired': 'Ended',
    'final season': 'Continuing',
    'on hiatus': 'Continuing',
    'pilot ordered': 'Continuing',
    'pilot rejected': 'Ended',
    'canceled': 'Ended',
    'ended': 'Ended',
    'to be determined': 'Continuing',
    'running': 'Continuing',
    'planned': 'Continuing',
    'in production': 'Continuing',
    'pilot': 'Continuing',
    'cancelled': 'Ended',
    'continuing': 'Continuing'
}

indexerConfig = {
    INDEXER_TVDBV2: {
        'enabled': True,
        'id': INDEXER_TVDBV2,
        'name': 'TVDBv2',
        'module': TVDBv2,
        'api_params': {
            'language': 'en',
            'use_zip': True,
            'session': MedusaSession(cache_control={'cache_etags': False}),
        },
        'xem_origin': 'tvdb',
        'icon': 'thetvdb16.png',
        'scene_loc': '{base_url}/scene_exceptions/scene_exceptions_tvdb.json'.format(base_url=BASE_PYMEDUSA_URL),
        'base_url': 'https://api.thetvdb.com/',
        'show_url': 'http://thetvdb.com/?tab=series&id={0}',
        'mapped_to': 'tvdb_id',  # The attribute to which other indexers can map there thetvdb id to
        'identifier': 'tvdb',  # Also used as key for the custom scenename exceptions. (_get_custom_exceptions())
    },
    INDEXER_TVMAZE: {
        'enabled': True,
        'id': INDEXER_TVMAZE,
        'name': 'TVmaze',
        'module': TVmaze,
        'api_params': {
            'language': 'en',
            'use_zip': True,
            'session': MedusaSession(cache_control={'cache_etags': False}),
        },
        'xem_mapped_to': INDEXER_TVDBV2,
        'icon': 'tvmaze16.png',
        'scene_loc': '{base_url}/scene_exceptions/scene_exceptions_tvmaze.json'.format(base_url=BASE_PYMEDUSA_URL),
        'show_url': 'http://www.tvmaze.com/shows/{0}',
        'base_url': 'http://api.tvmaze.com/',
        'mapped_to': 'tvmaze_id',  # The attribute to which other indexers can map their tvmaze id to
        'identifier': 'tvmaze',  # Also used as key for the custom scenename exceptions. (_get_custom_exceptions())
    },
    INDEXER_TMDB: {
        'enabled': True,
        'id': INDEXER_TMDB,
        'name': 'TMDB',
        'module': Tmdb,
        'api_params': {
            'language': 'en',
            'use_zip': True,
            'session': MedusaSession(cache_control={'cache_etags': False}),
        },
        'icon': 'tmdb16.png',
        'scene_loc': '{base_url}/scene_exceptions/scene_exceptions_tmdb.json'.format(base_url=BASE_PYMEDUSA_URL),
        'base_url': 'https://www.themoviedb.org/',
        'show_url': 'https://www.themoviedb.org/tv/{0}',
        'mapped_to': 'tmdb_id',  # The attribute to which other indexers can map their tmdb id to
        'identifier': 'tmdb',  # Also used as key for the custom scenename exceptions. (_get_custom_exceptions())
    },
    INDEXER_IMDB: {
        'enabled': True,
        'id': INDEXER_IMDB,
        'name': 'IMDb',
        'module': Imdb,
        'api_params': {
            'language': 'en',
            'use_zip': True,
            'session': MedusaSession(cache_control={'cache_etags': False}),
        },
        'xem_mapped_to': INDEXER_TVDBV2,
        'icon': 'imdb16.png',
        'scene_loc': '{base_url}/scene_exceptions/scene_exceptions_imdb.json'.format(base_url=BASE_PYMEDUSA_URL),
        'show_url': 'http://www.imdb.com/title/tt{0:07d}',
        'base_url': 'https://v2.sg.media-imdb.com',
        'mapped_to': 'imdb_id',  # The attribute to which other indexers can map their imdb id to
        'identifier': 'imdb',  # Also used as key for the custom scenename exceptions. (_get_custom_exceptions())
    }
}
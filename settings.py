from split_settings.tools import optional, include

include(
    'components/base.py',
    'components/installed.py',
    'components/celery_conf.py',
    'components/confident.py'
)
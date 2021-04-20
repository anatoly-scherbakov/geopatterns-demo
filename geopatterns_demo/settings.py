import os

SENTRY_DSN = (
    'https://6ea056a17e994b2391e13234a91be7e6@o575501.ingest.sentry.io/5727804'
)

IS_IN_LAMBDA = os.environ.get('AWS_EXECUTION_ENV') is not None

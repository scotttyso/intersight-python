import argparse
import os
def cli_arguments_function():
    Parser = argparse.ArgumentParser(description='Intersight Converged Infrastructure Deployment Module')
    Parser.add_argument(
        '-a', '--api-key-id', default=os.getenv('INTERSIGHT_API_KEY_ID'),
        help='The Intersight API key id for HTTP signature scheme.'
    )
    Parser.add_argument(
        '-d', '--dir',
        default = 'Intersight',
        help = 'The Directory to use for the Creation of the Terraform Files.'
    )
    Parser.add_argument(
        '-e', '--endpoint', default='intersight.com',
        help='The Intersight hostname for the API endpoint. The default is intersight.com.'
    )
    Parser.add_argument(
        '-i', '--ignore-tls', action='store_false',
        help='Ignore TLS server-side certificate verification.  Default is False.'
    )
    Parser.add_argument(
        '-k', '--api-key-file', default=os.getenv('INTERSIGHT_API_PRIVATE_KEY'),
        help='Name of the file containing The Intersight secret key for the HTTP signature scheme.'
    )
    args = Parser.parse_args()
    return args
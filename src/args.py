"""
Utility for arguments
"""
import argparse

def parse_args() -> argparse.Namespace:
    """
    Parse the CLI arguments
    """
    parser = argparse.ArgumentParser(description='Helper for cmd line.')
    parser.add_argument('action', action = 'store',
                        help='an integer for the accumulator')

    return parser.parse_args()

import argparse

from vdt.version.shared import VersionError


def parse_version_extra_args(version_args):
    p = argparse.ArgumentParser(description="Package builder for puppet forge.")
    p.add_argument('--modulename', help="puppet forge module name")
    p.add_argument('--version', help="puppet forge required version")
    args, extra_args = p.parse_known_args(version_args)
    
    if args.modulename is None:
        raise VersionError("puppetforge requires --modulename to be specified.")
    
    return args, extra_args
    
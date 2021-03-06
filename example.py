#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse
import autoscrape


def parse_args():
    desc = 'Example of running various autoscrapers.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        'baseurl', type=str,
        help='The base URL to begin scraping.')
    parser.add_argument(
        '--scraper', type=str, default="test",
        help=('Which scraper to use. Default is the test DFS '
              'scraper "test". Options: test, test-manual-control'))
    parser.add_argument(
        '--maxdepth', type=int, default=10,
        help='Maximum depth to allow the scraper to traverse.')
    parser.add_argument(
        '--formdepth', type=int, default=0,
        help=('Maximum depth to allow the scraper iterate through forms '
              'using "next" buttons. Default: 0, meaning no limit (will .'
              'continue clicking "next" until no more are found). This '
              'only has an effect on form interacting scrapers (test-manual-'
              'control).'))
    parser.add_argument(
        '--loglevel', type=str, default="INFO",
        help='Log level. Default: INFO. Options: DEBUG, INFO, WARN, ERROR')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    kwargs = {
        "maxdepth": args.maxdepth,
        "loglevel": args.loglevel,
        "formdepth": args.formdepth,
    }

    if args.scraper == "test":
        autoscrape.TestScraper(args.baseurl, **kwargs).run()

    elif args.scraper == "test-manual-control":
        autoscrape.TestManualControlScraper(args.baseurl, **kwargs).run()

    else:
        print("No scraper found for %s" % args.scraper)


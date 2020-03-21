import argparse

def get_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--youtube', required=True,
                        help='Choose whether to download from youtube or not',
                        type=str, choices=['yes', 'no'])
    parser.add_argument('--fn',
                        help='Type text file name of youtube links (with the extension)',
                        type=str)
    parser.add_argument('--audio', required=True,
                        help='Choose whether to extract audio or not',
                        type=str, choices=['yes', 'no'])
    args = parser.parse_args()

    return args.youtube, args.fn, args.audio
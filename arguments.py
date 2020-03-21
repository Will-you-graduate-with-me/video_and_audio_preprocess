import argparse

def get_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--youtube', required=True,
                        help='Choose whether download from youtube or not\n yes or no',
                        type=str, choices=['yes', 'no'])
    args = parser.parse_args()

    return args.youtube
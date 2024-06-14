import argparse
from glob import glob


def modify_webm_file(filename: str, prefix: bytes, patch: bytes) -> None:
    # load a webm file
    with open(filename, 'rb') as f:
        data = f.read()

    # values to modify the video length as 0
    prefix = bytes.fromhex(prefix)
    patch = bytes.fromhex(patch)

    # find for the first occurrence of <prefix>
    idx = data.find(prefix)

    # apply <patch> to the data
    modified_data = data[:idx + len(prefix)] + patch + data[idx + len(prefix) + len(patch):]

    # save to a webm file
    with open(filename, 'wb') as f:
        f.write(modified_data)


def main():
    parser = argparse.ArgumentParser()

    # positional arguments
    parser.add_argument("input_dir", help="directory with webm files [e.g. ./path_to_videos]")

    # optional arguments
    parser.add_argument("-f", type=str, nargs='+', help="webm filenames [e.g. f1 f2 f3 ...]")
    parser.add_argument("-a", "--all", type=bool, default=False, help="wether to modify all webm files or a single one")

    # parse the command-line arguments
    args = parser.parse_args()

    # values to modify the videos
    prefix = '4489'
    patch = '843f8000'

    # Access the parsed arguments
    if args.all:
        webm_paths = glob(pathname=f"{args.input_dir}/*.webm")
        for webm in webm_paths:
            modify_webm_file(webm, prefix, patch)
    else:
        for file in args.f:
            modify_webm_file(f"{args.input_dir}/{file}.webm", prefix, patch)


if __name__ == "__main__":
    main()

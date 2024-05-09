#!/usr/bin/env python3
"""
@TODO: Describe the application here
@author: christopher.tubbs
"""
import sys
import typing
import asyncio
import pathlib
import traceback

from argparse import ArgumentParser


#DEFAULT_MODEL = "tts_models/en/ljspeech/tacotron2-DDC_ph"
DEFAULT_MODEL = "tts_models/en/vctk/vits"


class Arguments(object):
    def __init__(self, *args):
        self.__path: typing.Optional[pathlib.Path] = None
        self.__parse_command_line(*args)

    # Add a property for each argument
    @property
    def path(self) -> pathlib.Path:
        return self.__path

    def __parse_command_line(self, *args):
        parser = ArgumentParser("Convert a simple text document to an audio file")

        # Add Arguments
        parser.add_argument(
            "path",
            type=pathlib.Path,
            help="The path to the file to read aloud"
        )

        # Parse the list of args if one is passed instead of args passed to the script
        if args:
            parameters = parser.parse_args(args)
        else:
            parameters = parser.parse_args()

        # Assign parsed parameters to member variables
        self.__path = pathlib.Path(parameters.path)


def get_text(path: pathlib.Path) -> str:
    return path.read_text()


def output_sound(text: str, output_path: pathlib.Path):
    from TTS.api import TTS
    speech_model = TTS(DEFAULT_MODEL).to("cpu")
    speech_model.tts_to_file(text=text, speaker="p244", file_path=str(output_path))


async def main():
    """
    Define your main function here
    """
    arguments = Arguments()
    text = get_text(arguments.path)
    output_path = pathlib.Path(f"{arguments.path.stem}.wav").absolute()

    try:
        output_sound(text, output_path)
        print(f"There should now be a written audio file at {output_path}")
        exit_code = 0
    except BaseException as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        print(f"Could not write an audio file to {output_path}")
        exit_code = 1

    return exit_code


if __name__ == "__main__":
    code = asyncio.run(main())
    sys.exit(code)

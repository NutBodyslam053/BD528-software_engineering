import os
from box.exceptions import BoxValueError
import yaml
from src.mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): If True, display information about directory creation.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

# @ensure_annotations
def display_section_heading(title, content, symbol="=", title_case="title", color=None, alignment="center", bold=True):
    """Display a section heading with a specified title and content.

    Args:
        title:          The title of the section.
        content:        The content to be displayed below the title.
        symbol:         The symbol used for formatting the heading.
        title_case:     The case transformation for the title.
        color (str):    ANSI escape code for text color 
                        (e.g.,  '\033[91m' for red
                                '\033[92m' for green, 
                                '\033[94m' for blue, 
                                '\033[93m' for yellow).
        alignment:      Text alignment for the content ("left", "right", "center").
        bold:           Whether to make the heading bold.

    Raises:
        ValueError: If the symbol is not a single character.
                    If the title is longer than the terminal width.

    Returns:
        None
    """
    # Ensure the symbol is a single character
    if len(symbol) != 1:
        raise ValueError("The symbol should be a single character.")
    
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError as e:
        terminal_width = 100
        print(f"Error getting terminal size: {e}")

    # Calculate the available space for the title
    available_space = terminal_width - len(title) - 2

    # Ensure there is enough space for the title
    if available_space < 0:
        raise ValueError("Title is longer than the terminal width.")
    
    #################################### Heading Section ####################################
    num_symbols_on_each_side = available_space // 2

    bold_code = '\033[1m' if bold else ''
    unbold_code = '\033[22m' if bold else ''

    heading = (
        (color if color else '') +
        symbol * num_symbols_on_each_side
        + " " + bold_code + getattr(title, title_case)() + unbold_code + " " +
        symbol * num_symbols_on_each_side
    )
    
    
    #################################### Content Section ####################################
    content_width = len(content)

    # Customize content alignment
    if alignment == "left":
        spaces_on_each_side = 0
    elif alignment == "right":
        spaces_on_each_side = terminal_width - content_width
    else:  # Default to "center"
        spaces_on_each_side = (terminal_width - content_width) // 2

    content = (" " * spaces_on_each_side) + content + (" " * (terminal_width - content_width - spaces_on_each_side))

    #################################### Ending Section ####################################
    ending = (
        symbol * terminal_width
        + '\033[0m'  # Reset formatting after the ending
    )
    
    print(heading)
    print(content)
    print(ending)


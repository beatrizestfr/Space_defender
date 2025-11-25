
import os      # to work with paths and folders
import pygame  # to load images, sounds and fonts


# BASE_DIR points to the root folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# assets/ folder inside the project
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# subfolders for different asset types
SPRITES_DIR = os.path.join(ASSETS_DIR, "sprites")
SFX_DIR = os.path.join(ASSETS_DIR, "sfx")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

def load_image(filename: str, size: tuple[int, int] | None = None) -> pygame.Surface:
    """
    Load an image from assets/sprites.
    If the file is missing, return a colored placeholder surface instead.
    """
    # build the full path: assets/sprites/<filename>
    path = os.path.join(SPRITES_DIR, filename)

    try:
        # load the image as a Surface and keep alpha transparency
        image = pygame.image.load(path).convert_alpha()

        # if a size is given, scale the image
        if size is not None:
            image = pygame.transform.scale(image, size)

        return image
    except FileNotFoundError:
        # if the file is missing, create a simple magenta rectangle
        # so it's very obvious something's wrong
        surf = pygame.Surface(size or (40, 40))
        surf.fill((255, 0, 255))
        return surf


def load_sound(filename: str) -> pygame.mixer.Sound | None:
    """
    Load a sound from assets/sfx.
    If the file is missing, return None instead of crashing.
    """
    path = os.path.join(SFX_DIR, filename)

    try:
        return pygame.mixer.Sound(path)
    except FileNotFoundError:
        return None

def get_font(size: int) -> pygame.font.Font:
    """
    Return a font object. If a custom font file exists in assets/fonts/,
    use it; otherwise fall back to pygame's default font.
    """
    
    custom_font_path = os.path.join(FONTS_DIR, "x")

    if os.path.exists(custom_font_path):
        return pygame.font.Font(custom_font_path, size)

    # fallback: default pygame font
    return pygame.font.Font(None, size)

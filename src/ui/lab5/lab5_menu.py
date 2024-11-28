from src.bll.classes.lab5.RotatingRenderer import RotatingRenderer
from src.bll.classes.lab5.SettingsManager import SettingsManager
from src.bll.classes.lab5.StaticRenderer import StaticRenderer


def main():
    """Main entry point for the program."""
    settings_manager = SettingsManager('settings.json')
    settings_manager.load_settings()

    renderers = {
        '1': RotatingRenderer(settings_manager.settings),
        '2': StaticRenderer(settings_manager.settings),
    }

    while True:
        print('\nMenu:')
        print('1. Render rotating 3D shape')
        print('2. Render static 3D shape')
        print('3. Exit')

        choice = input('Choose an option: ')
        if choice in renderers:
            renderers[choice].render_frame()
        elif choice == '3':
            break
        else:
            print('Invalid choice, try again.')


if __name__ == "__main__":
    main()
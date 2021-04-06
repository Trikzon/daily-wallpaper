# Daily Wallpaper
A python script that grabs today's top r/wallpaper and sets it as your desktop wallpaper

## Usage

Run the `daily_wallpaper.py` script with python3.

Wallpapers will download into a `./wallpapers` directory next to the `daily_wallpaper.py` file.

### Autorun

For the best experience, run this every day (automatically) for good wallpapers each day.

#### Windows

1. Install [AutoHotkey](https://www.autohotkey.com/)
2. Edit `daily_wallpaper.ahk`
3. Place `daily_wallpaper.ahk` in `C:\Users\NAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

#### Linux

1. Run `$ crontab -e`.
2. Write `0 3 * * * /path/to/script.py` to have it run daily at 3:00 am.
3. Running at system startup is system dependent.

## Dependencies


### Windows

No further dependencies needed.

To install all python dependencies:
```
$ py -m pip install -r .\requirements.txt
```

### Linux

Install [feh](https://wiki.archlinux.org/index.php/Feh) with your distro's package manager.

To install all python dependencies:
```
$ pip install -r ./requirements.txt
```

#### Arch

```
# pacman -S xwallpaper
```

## Credits

I copied a lot of code from [nagracks's reddit_get_top_images](https://github.com/nagracks/reddit_get_top_images) 
which is [licensed under the MIT license.](https://github.com/nagracks/reddit_get_top_images/blob/master/LICENSE)


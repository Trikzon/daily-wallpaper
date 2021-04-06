#Persistent

; Run once on startup.
;   Location of python script
Run "C:\Users\USERNAME\Desktop\daily_wallpaper.py"

; Check every minute if it is a new day.
SetTimer, check, 60000
return

check:
    FormatTime, time, A_Now, HHmm

    ; Note: Set to a time you don't use your PC b/c it pops up a cmd prompt window.
    ; 3:00am -> 0300
    ; 3:30pm -> 1530
    if (time == 0300)
    {
        ;   Location of python script
        Run "C:\Users\USERNAME\Desktop\daily_wallpaper.py"
    }
return
### Running every minute the script from crontab and showing dialog box with results in zenity. 

On Linux: 
   - 1. in any terminal window type: `crontab -e` 
   - 2. copy the following snippet into the file:

```
#!/bin/bash
#*     *     *   *    *
#-     -     -   -    -
#|     |     |   |    |
#|     |     |   |    +----- day of week (0 - 6) (Sunday=0)
#|     |     |   +------- month (1 - 12)
#|     |     +--------- day of month (1 - 31)
#|     +----------- hour (0 - 23)
#+------------- min (0 - 59)


* * * * * DISPLAY=:0 python /home/user-name-here/complete-path-to-script-here/verify_gmail.py 
```
   - 3. ctrl-x and Enter to save.

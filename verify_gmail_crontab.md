## Running every minute the verify gmail script from crontab and showing dialog box with zenity.
# On -Linux: 
  # type: crontab -e 
  # enter the following in the file

#!/bin/bash
#*     *     *   *    *
#-     -     -   -    -
#|     |     |   |    |
#|     |     |   |    +----- day of week (0 - 6) (Sunday=0)
#|     |     |   +------- month (1 - 12)
#|     |     +--------- day of        month (1 - 31)
#|     +----------- hour (0 - 23)
#+------------- min (0 - 59)


# or you can run it every five minutes: changing ---> /5 * * * * 
* * * * * DISPLAY=:0 python /home/user/complete-path-to-script/verify_gmail.py 

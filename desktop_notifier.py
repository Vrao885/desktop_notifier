# import the nessasary module !
from plyer import notification

#specify the parameters
title = 'wishes'
message= 'Happy new year to all !!'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)

#notification with motivational text / messsage

# import win10toast 
from win10toast import ToastNotifier
  
# create an object to ToastNotifier class
n = ToastNotifier()
 
n.show_toast("CommitToProject", "'Motivational Text'", duration = 20,
  icon_path =r'C:/Users/user/Downloads/hack3.ico')
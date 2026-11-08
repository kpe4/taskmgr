import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))

from ui.Interface import TaskManagerApp

if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()
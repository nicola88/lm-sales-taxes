import os

from lib import App

if __name__ == '__main__':

    for (root, dirs, files) in os.walk('samples'):
        for f in files:
            print("\nSIMULATION > " + str(f) + os.linesep)
            App.run_simulation(os.path.join(root, f))

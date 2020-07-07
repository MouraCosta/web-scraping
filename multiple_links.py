# Open multiples links in a browser

import webbrowser
import sys

for url in sys.argv[1:]:
    webbrowser.open_new_tab(url)

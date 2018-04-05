import os
import site

lib = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
site.addsitedir(lib)


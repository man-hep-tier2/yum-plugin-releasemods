from yum.plugins import TYPE_CORE
from yum.constants import *
import os, re
from os.path import *

requires_api_version = '2.4'
plugin_type = (TYPE_CORE)

def clean_repos(conduit):
    if conduit.confString('main', 'release_packages'):
        for po in conduit.getRpmDB().searchNames(conduit.confString('main', 'release_packages').split(' ')):
            conduit.info(8, "found %s %s" % (po.name, po.version))
            for file in po.returnFileEntries():
                if re.search('^/etc/yum.repos.d/.*\.repo', file):
                    if isfile(file):
                        conduit.info(8, "removing file %s" % file)
                        os.remove(file)
            if conduit.confString(po.name, 'files'):
                for file in conduit.confString(po.name, 'files').split(' '):
                    if isfile(file):
                        conduit.info(8, "removing file %s" % file)
                        os.remove(file)
        

def posttrans_hook(conduit):
    conduit.info(3, "posttrans_hook: cleaning repository files")
    clean_repos(conduit)

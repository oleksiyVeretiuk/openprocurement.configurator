from zope.component import getGlobalSiteManager

from openprocurement.api.interfaces import IContentConfigurator
from openprocurement.api.configurator import Configurator

config = {
    'AUCTION_PREFIX': 'AU-PS'
}

def includeme(*args, **kwargs):
    getGlobalSiteManager().registerUtility(Configurator(config, {}), IContentConfigurator)
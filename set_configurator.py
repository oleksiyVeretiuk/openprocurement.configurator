from zope.component import getGlobalSiteManager

from openprocurement.api.interfaces import IContentConfigurator
from openprocurement.api.configurator import Configurator

config = {
    'AUCTION_ID': 'AU-PS'
}

def set_up():
    import pdb; pdb.set_trace()
    getGlobalSiteManager().registerUtility(Configurator(config, {}), IContentConfigurator)
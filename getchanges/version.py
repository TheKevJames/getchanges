import pkg_resources


try:
    __version__ = pkg_resources.get_distribution('getchanges').version
except pkg_resources.DistributionNotFound:
    __version__ = 'dev'

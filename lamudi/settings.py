BOT_NAME = "lamudi"

SPIDER_MODULES = ["lamudi.spiders"]
NEWSPIDER_MODULE = "lamudi.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32  # Increase concurrency to speed up the scraping

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1  # Reduce delay to make scraping faster but still avoid being too aggressive
RANDOMIZE_DOWNLOAD_DELAY = True  # Randomize the delay to avoid patterns

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 32
CONCURRENT_REQUESTS_PER_IP = 32

# Disable cookies (enabled by default)
COOKIES_ENABLED = False  # Disable cookies to reduce the chance of being tracked and blocked

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
}

# Enable or disable spider middlewares
#SPIDER_MIDDLEWARES = {
#    "lamudi.middlewares.LamudiSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 500,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# Enable or disable extensions
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
#ITEM_PIPELINES = {
#    "lamudi.pipelines.LamudiPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True  # Enable AutoThrottle to avoid hitting the server too hard
AUTOTHROTTLE_START_DELAY = 1  # Short delay to start with
AUTOTHROTTLE_MAX_DELAY = 5  # Maximum delay to avoid getting blocked
AUTOTHROTTLE_TARGET_CONCURRENCY = 5.0  # Aim for 5 concurrent requests per server
AUTOTHROTTLE_DEBUG = False  # Disable AutoThrottle debugging for cleaner logs

# Enable and configure HTTP caching (disabled by default)
HTTPCACHE_ENABLED = True  # Enable HTTP caching to reduce server load and speed up re-requests
HTTPCACHE_EXPIRATION_SECS = 86400  # Cache for 1 day
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = [500, 502, 503, 504, 408]  # Ignore caching on error pages
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

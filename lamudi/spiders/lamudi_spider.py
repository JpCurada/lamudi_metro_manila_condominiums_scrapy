import scrapy

class LamudiSpider(scrapy.Spider):
    name = 'lamudi_spider'
    allowed_domains = ['lamudi.com.ph']
    start_urls = [
        'https://www.lamudi.com.ph/buy/metro-manila/condo/'
    ]

    def parse(self, response):
        # Extract all relative href links within the specified div and convert to absolute URLs
        by_metro_city_links = [response.urljoin(link) for link in response.css('div.CrosslinkFilter-container a::attr(href)').extract()]

        # Follow each city link
        for city_link in by_metro_city_links:
            yield response.follow(city_link, self.parse_city)

    def parse_city(self, response):
        # Extract all district links (if applicable) or proceed with property links
        by_district_links = [response.urljoin(link) for link in response.css('div.CrosslinkFilter-container a::attr(href)').extract()]

        for district_link in by_district_links:
            yield response.follow(district_link, self.parse_district)

    def parse_district(self, response):
        # Extract property links from the district page
        property_links = [response.urljoin(link) for link in response.css('div.ListingCell-MainImage a::attr(href)').extract()]

        for link in property_links:
            yield response.follow(link, self.parse_property_details)

        # Pagination - find the next page link and follow it
        next_page = response.css('div.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse_district)

    def parse_property_details(self, response):
        # Function to safely extract and strip text, even if it is missing
        def safe_extract(selector):
            result = response.css(selector).get()
            return result.strip() if result else None

        # Extract details from each property page
        yield {
            'title': safe_extract('h1.Title-pdp-title span::text'),
            'number_of_bedrooms': safe_extract('div.ellipsis.listing-details-label[data-attr-name="bedrooms"] + div.last::text'),
            'floor_sqm': safe_extract('div.ellipsis.listing-details-label[data-attr-name="building_size"] + div.last::text'),
            'number_of_bathrooms': safe_extract('div.ellipsis.listing-details-label[data-attr-name="bathrooms"] + div.last::text'),
            'developer': safe_extract('div.AgentInfoV2-agent-name::text'),
            'condominium_name': safe_extract('div.ellipsis.listing-details-label[data-attr-name="condominiumname"] + div.last::text'),
            'floor': safe_extract('div.ellipsis.listing-details-label[data-attr-name="floor"] + div.last::text'),
            'car_space': safe_extract('div.ellipsis.listing-details-label[data-attr-name="car_spaces"] + div.last::text'),
            'classification': safe_extract('div.ellipsis.listing-details-label[data-attr-name="classification"] + div.last::text'),
            'price': safe_extract('div.Title-pdp-price span.FirstPrice::text'),
            'location_name': safe_extract('div.LandmarksPDP-Wrapper::attr(data-location)'),
            'latitude': safe_extract('div.LandmarksPDP-Wrapper::attr(data-lat)'),
            'longitude': safe_extract('div.LandmarksPDP-Wrapper::attr(data-lon)'),
        }

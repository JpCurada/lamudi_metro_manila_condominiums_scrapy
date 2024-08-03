
# Lamudi Listings for Condominiums within Metro Manila

This project uses Scrapy, a powerful web scraping framework, to collect data on condominium listings within Metro Manila from the Lamudi website. The collected data includes essential details like prices, locations, and property descriptions, which can be used for various analyses and insights.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running the Scraper](#running-the-scraper)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

### 1. Fork the Repository
To get started, you can fork this repository to your GitHub account:

1. Click the "Fork" button at the top-right corner of this page.
2. Clone your fork to your local machine:
    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/lamudi-listings-scraper.git
    cd lamudi-listings-scraper
    ```

### 2. Create a Virtual Environment
It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
Activate the virtual environment:

- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies
Install the necessary Python packages by running:

```bash
pip install -r requirements.txt
```

## Usage

### Configuration

1. **Set the User Agent**:
   - Open the `settings.py` file located within your Scrapy project's directory.
   - Find the line with `USER_AGENT = 'your-user-agent-string'`.
   - Replace `'your-user-agent-string'` with your actual user agent. You can find your user agent string by searching "what is my user agent" in your web browser.

   Example:
   ```python
   USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
   ```

2. **Modify Other Settings (Optional)**:
   - If needed, you can modify other settings like download delay, request headers, etc., in the `settings.py` file.

### Running the Scraper

1. **Run the Scrapy Project**:
   - Navigate to the project’s root directory and run the following command to start scraping:
   ```bash
   scrapy crawl lamudi
   ```

2. **Output Data**:
   - By default, the scraped data will be saved in a JSON file in the project's root directory. You can change the output format and location by modifying the command:
   ```bash
   scrapy crawl lamudi -o output/condominiums.json
   ```

## Output
The scraper will generate a JSON file containing the data from the Lamudi listings. The JSON file will include fields such as:

- Property Name
- Price
- Location
- Area (in sqm)
- Number of Bedrooms
- Number of Bathrooms
- Description
- Listing URL

You can use this data for further analysis or integrate it into other applications.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or create an Issue if you have any suggestions or improvements.

### Steps to Contribute

1. Fork the repository.
2. Create your feature branch:
    ```bash
    git checkout -b feature/YourFeatureName
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/YourFeatureName
    ```
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Scrapy Documentation](https://docs.scrapy.org/en/latest/) - The official documentation for Scrapy.
- [Lamudi](https://www.lamudi.com.ph/) - The source of the condominium listings.


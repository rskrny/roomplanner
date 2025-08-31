# Data Sources & Catalog

The initial product catalog will be assembled from publicly available sources and open data. During the MVP phase, RoomPlanner does not integrate with proprietary APIs; instead, it gathers data from:

## Global Retailers
- **IKEA** – Public product information scraped from the IKEA website or open product feeds.
- **Amazon** – Basic product data (title, price, dimensions) extracted from the Amazon Product Advertising API or scraped from publicly visible pages. Since API keys are not available, only limited public data will be used.
- **Wayfair** – Public listings for furniture items including dimensions and price.
- **Etsy** – Unique handmade items with publicly visible information (seller, price, materials).

## Local London Sources
- **London independent furniture stores** – Many independent shops have Shopify or WooCommerce storefronts with publicly accessible product pages. Examples: Heal’s, SCP London, Another Country, and MADE.com (depending on availability).
- **Marketplaces** – Platforms like Gumtree and Vinterior list pre-owned and vintage furniture in London. Listing information can be scraped to gather item names, dimensions and prices.
- **Open datasets** – Public datasets that catalogue furniture or consumer goods (e.g., open-government commodity data) may be used to seed additional sample items.

## Data Ingestion Strategy
For the MVP, the backend will include a `data/catalog_sample.csv` file with a curated list of 15–20 sample items from the sources above. Each entry will include fields such as:
- `id`, `title`, `category`, `width_cm`, `depth_cm`, `height_cm`, `price_gbp`, `currency`, `store_name`, `source_url`.

As the product scales, the ingestion service can be expanded to:
- Use headless browsers or scraping tools to periodically update the catalog.
- Allow store owners to upload their own product feeds (CSV or API).
- Integrate with official APIs once keys are obtained (e.g., Amazon PA API, Shopify, etc.).

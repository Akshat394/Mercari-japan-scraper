# Mercari Japan AI Shopper

## Overview
This project is a Python-based AI agent and web application for searching, scraping, and recommending products from Mercari Japan. It features a robust backend scraper, PostgreSQL integration, SEO tagging, and a modern Streamlit UI. The system is designed to:
- Understand user requests (LLM integration ready)
- Search Mercari Japan for products using diverse keywords
- Extract and store product data (name, price, image, etc.)
- Tag products with SEO metadata
- Present products in a user-friendly, filterable web UI

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Akshat394/Mercari-japan-scraper.git
   cd Mercari-japan-scraper
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. **Configure PostgreSQL:**
   - Edit `config.py` with your database credentials.
   - Ensure your PostgreSQL server is running.
4. **Run the scraper:**
   ```bash
   python scraper.py
   ```
5. **Tag products with SEO tags:**
   ```bash
   python -c "import seo_tagger; seo_tagger.tag_unprocessed_products()"
   ```
6. **Launch the Streamlit UI:**
   ```bash
   python -m streamlit run streamlit_app.py
   ```

## Usage Instructions
- Use the web UI to search, filter, and browse products.
- The search bar supports real-time keyword search.
- Filter by category, SEO tags, price, and more.

## Design Choices
- **Scraping:** Uses `mercapi` for robust, API-like scraping of Mercari Japan.
- **Database:** PostgreSQL with SQLAlchemy ORM for reliability and scalability.
- **SEO Tagging:** Rule-based tagger for product enrichment.
- **UI:** Streamlit for rapid, modern web app development.
- **Extensibility:** LLM integration (OpenAI/Claude) is ready for natural language understanding and recommendations.

## Potential Improvements
- Integrate OpenAI or Claude for natural language request parsing and product recommendations.
- Add user authentication and favorites/cart features.
- Schedule periodic scraping and auto-tagging.
- Add more advanced analytics and product insights.
- Expand SEO tagging with LLMs for richer metadata.

## License
MIT 
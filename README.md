<!DOCTYPE html>
<html lang="en">
<body>
	<h1>Amzon Search Result Scraper</h1>
<p>A scraper that scrapes products from the search results of Amazon. 🕵️‍♂️🛍️</p>

  <h2>Features of products that it scrapes:</h2>
  <ul>
  <li>Title: Product title 📦</li>
  <li>Product URL: Link to the product page 🔗</li>
  <li>Image URL: Link to the product image 🖼️</li>
  <li>Total Reviews: Total number of reviews for the product 🌟</li>
  <li>Rating: Product rating out of 5 ⭐</li>
  <li>Price: Product price 💰</li>
  </ul>

  <p>You can set how many pages you want to scrape and the output format (Excel or CSV). Note that you need to insert the link to the second page of the search results, not the first page.</p>

  <h2>How to use</h2>
  <ol>
  <li>Clone the repository to your local machine.</li>
  <li>Install the required libraries by running the following command:</li>
  <pre><code>pip install -r requirements.txt</code></pre>
  <li>Open the <code>main.py</code> file and insert the link of the second page of the search results.</li>
  <li>Set the number of pages you want to scrape and the output format (Excel or CSV).</li>
  <li>Run <code>main.py</code>. The scraped data will be saved in a file named <code>products.xlsx</code> or <code>products.csv</code> depending on the output format you chose.</li>
  </ol>

  <h2>Contributing</h2>
  <p>Contributions are welcome! Feel free to submit a pull request. 🤝👨‍💻👩‍💻</p>
  </body>
  </html>

# Web Scraper

This Python script allows you to scrape job positions from the Seek website, filter positions based on specified criteria, find specific keywords in job descriptions, create custom cover letters, and open or apply to job positions.

## Installation

1. Clone the repository:

'git clone https://github.com/your_username/web-scraper.git'

2. Install the required dependencies:

'pip install beautifulsoup4 docx2txt requests'

3. Update the configuration file:
Modify the desired parameters in config dictionary in '''web-scraping-try.py''' such as the website, job title, location, filter keywords, and other options.

## Usage

1. Run the script:

'web-scraping-try.py'

2. The script will perform the following actions based on the configuration:
- If `get_from_seek` is set to `True`, it will scrape job positions from the Seek website based on the specified job title and location. The positions will be stored in a JSON file. It will also remove job positions based on specific keywords.
- If `filter_positions` is set to `True`, it will filter the positions from the previous step based on the specified filter keywords. The filtered positions will be stored in a separate JSON file.
- If `find_keywords` is set to `True`, it will analyze the job descriptions of the positions and find specific keywords. The positions with their corresponding keywords will be stored in the original JSON file.
- If `create_cl` is set to `True`, it will generate custom cover letters based on a template file (`template_cl`) and the positions with their keywords. The cover letters will be saved in the `cover_letters` directory.
- If `open_links` is set to `True`, it will open the job links in Google Chrome. Each link will be opened in a new tab or window.
- If `apply` is set to `True`, it will open the "apply" links in Google Chrome. Each link will be opened in a new tab or window.

3. Customize the script:
- Modify the `template_cl.docx` file to create your own cover letter template. The placeholder texts (`the_date`, `the_role`, `the_company`, `the_link`, `the_key_1`, `the_key_2`, `the_key_3`, `the_key_4`) will be automatically replaced with the content corresponding to a particular job position. `the_key_1` - `the_key_4` are  keywords from the job description that match your skills (can be bullet points).
- Modify the job keywords JSON file (config['my_keywords_file']) to reflect your skills. The first four skills will replace the `the_key_1` - `the_key_4` in the cover letter if there are no other matches. One word keys will be accompanied by 'Experiense in' + key or Key + 'skills'. Two or more words keys will be capitalized.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).

from web_scraper import WebScraper

config = {
    'website': 'https://www.seek.co.nz',
    'job': 'audio engineer',
    'location': ['auckland',
    'wellington'],
    'remove': ['senior', 'lead', 'one year', 'contract', 'fixed term', 'leader'],
    'get_from_seek': True,
    'filter_positions': False,
    'find_keywords': False,
    'filter_keywords': ['grad', 'junior', 'internship', 'graduate'],
    'my_keywords_file': 'config/audio_engineer_keywords.json',
    'create_cl': False,
    'template_cl': 'template_cl.docx',
    'output_file_prefix': 'Full-Name',
    'cl_positions_file': 'filtered audio engineer positions.json',
    'open_links': False,
    'open_positions': 'audio engineer positions.json', 
    'apply': True,
    'apply_positions': 'audio engineer positions.json',
    'applied_folder': 'applied_jobs',
    'deleted_folder': 'deleted_jobs'
}

scrapper = WebScraper(config)

if scrapper.config['get_from_seek']:
    # Get the initial positions from seek
    positions = scrapper.get_seek_positions()
    scrapper.write_to_file(positions, scrapper.positions_file)

if scrapper.config['filter_positions']:
    # Find the positions that have the filter keywords
    positions = scrapper.filter_positions(scrapper.positions_file, scrapper.filter_keywords)
    scrapper.write_to_file(positions, scrapper.filtered_positions_file)

if scrapper.config['find_keywords']:
    # Find specific keywords for the positions and write to .json
    positions = scrapper.find_keywords(scrapper.filtered_positions_file, scrapper.my_keywords_file)
    scrapper.write_to_file(positions, scrapper.filtered_positions_file)

if scrapper.config['create_cl']:
    # Create a custom cover letter
    scrapper.create_cl(scrapper.template_cl, scrapper.output_file_prefix, scrapper.cl_positions_file, scrapper.my_keywords_file)

if scrapper.config['open_links']:
    # Open links in a new window
    scrapper.open_links(scrapper.open_positions)

if scrapper.config['apply']:
    # Open 'apply' links in a new window
    scrapper.apply(scrapper.apply_positions)

# Surf the Strait

This repository contains the source for the **surfthestrait.com** static site. The site aggregates tide tables, wind data and other coastal conditions for surfers on Vancouver Island's west coast.

## Contents

- `index.html` and `styles.css` – the main website files
- `current_data.csv` – current predictions for Race Rocks
- `renfrew_tides.csv` – Port Renfrew tide data
- `fetch_carmanah_latest.py` – helper script to retrieve the most recent Carmanah camera image

## Setup

The pages are completely static. Clone the repository and open `index.html` in a modern web browser. To fetch the latest camera image you may run:

```bash
python fetch_carmanah_latest.py
```

The script prints the direct image URL. It requires an active internet connection.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.


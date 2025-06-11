# Surf the Strait

This repository contains the source for the Surf the Strait website.

## Updating the Carmanah camera image

The script `fetch_carmanah_latest.py` downloads the newest image from the
[Carmanah camera](https://ccgsitecams.ca/sites/carmanah/camera_1/) and saves it
as `Pictures/carmanah_latest.jpg` by default.  Pass a different file path or
`--base-url` if you need a custom source.

The image file is ignored by git, so running the script won't change the
repository unless you add the file with `git add -f`.

Run the script manually:

```bash
python fetch_carmanah_latest.py
```

### Automated updates

To keep the image up to date you can run the script periodically. A cron entry
that updates the image every 10 minutes might look like:

```cron
*/10 * * * * cd /path/to/surfthestrait && python fetch_carmanah_latest.py
```

Alternatively, the provided GitHub Actions workflow in
`.github/workflows/update_carmanah_image.yml` performs the same task on a
10-minute schedule and commits the updated image back to the repository. Make
sure GitHub Actions is enabled on your fork if you want automatic updates.


# Wuguang

English · [中文说明](README.md)

> See what you own before deciding what to buy.

Wuguang is a photo-first, local-first personal inventory tool. It helps people gradually build an inventory of their belongings, record purchase value and usage, and create basic outfit combinations from clothes they already own.

**Live demo:** https://wuguang-inventory.streamlit.app/

## Why Wuguang

The problem is often not that we own too little, but that we cannot clearly see what we already have. Traditional inventory software can feel like an ERP system: too many fields, too much maintenance, and too much work before any value appears.

Wuguang aims to make the starting point lighter. Begin with one item you use today and one photo. You do not need to catalogue your entire home at once.

The current version still requires users to enter the name and category manually. It first validates the complete workflow. A future vision model can turn item entry from filling every field into reviewing, correcting, and confirming a structured suggestion.

## Current Features

- Take a photo or select multiple photos and confirm them one at a time;
- Record name, major category, subcategory, quantity, unit price, colour, and storage location;
- Filter by Clothing, Home, and Digital;
- Summarise item count and recorded purchase value;
- Record individual item usage;
- Navigate by four product areas: Inventory, How to Use, About It, and Data & Backup;
- Enter category-specific usage areas for clothing, home items, and digital devices while retaining the complete clothing workflow;
- Add an optional story to any item, review stories in one place, and export a privacy-controlled PNG story card;
- Build basic combinations from tops, bottoms, dresses, outerwear, shoes, bags, and accessories;
- Tag clothing for Everyday, Commute, Workout, and Social occasions; incompatible items are filtered out before outfit ranking;
- Record “I wore this outfit today” and view recent usage history;
- Chart item appearance rates and exact-combination appearance rates from recorded wears;
- Export and restore a complete JSON backup containing photos, stories, items, and usage history, with backward compatibility for earlier backups without stories;
- Use the in-app feedback entry for WeChat guidance or a structured GitHub Issue;
- Expose an optional read-only WebMCP tool named `read_inventory_summary` in compatible environments.

## Current Limitations

- AI image recognition is not connected yet;
- Outfit combinations are not professional styling advice;
- Data and photos are stored only in the current browser's IndexedDB;
- There is no automatic sync across devices or browsers;
- The Streamlit page hosts the interface inside an iframe, so storage and download behaviour should be tested on each target mobile browser;
- There are no user accounts, cloud database, or household collaboration features yet.

Read the [privacy and data notes](docs/PRIVACY.md) before use. Export a backup after entering a meaningful batch of items.

## Run Locally

Python 3.10 or later is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Deploy on Streamlit Community Cloud

1. Fork or copy this repository;
2. Create an app in Streamlit Community Cloud;
3. Select the repository and the `main` branch;
4. Set the main file path to `streamlit_app.py`;
5. Test the deployed app on mobile, inside WeChat, and in a private browser window.

This release does not require any secrets. When AI recognition is introduced, API keys must remain in server-side secrets and must never be placed in `inventory.html`.

## Data Boundary

The browser stores items, photos, and usage records. The Streamlit Python process only reads and embeds the bundled HTML file. In the current release, user-selected photos are not sent to the Python service or to a third-party AI provider.

The `wuguang-backup` JSON file contains photos, item details, and usage records. Treat it as a private file. Do not attach a real backup to a public issue or post it in a public chat.

## Product and Technical Documents

- [Product definition (Chinese)](docs/PRODUCT.md)
- [Product decision: from personal inventory to a personal belongings archive](docs/PRODUCT_DECISION_2026-09-30_EN.md) · [中文](docs/PRODUCT_DECISION_2026-09-30.md)
- [Outfit discovery algorithm (Chinese)](docs/OUTFIT_DISCOVERY.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Roadmap and time estimates](docs/ROADMAP.md)
- [Privacy and data notes](docs/PRIVACY.md)

The next priorities are:

1. Structured AI recognition from a single-item photo;
2. Weather- and occasion-aware outfits constrained to the real wardrobe;
3. Similar-item detection and duplicate-purchase reminders;
4. Accounts and cloud sync only after sustained usage is demonstrated.

## Feedback and Contributions

- Use the Bug report form for reproducible defects;
- Use the Feature request form to describe a real usage scenario and desired outcome;
- Follow [SECURITY.md](SECURITY.md) for security or personal-data concerns. Do not publish private photos or backups.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting code.

## License

Wuguang is released under the [MIT License](LICENSE).

## Acknowledgements

The product and technical research drew on public workflows from:

- [Hangar](https://github.com/Gurshaan-Deol/Hangar): AI clothing analysis, weather-aware outfits, and provider abstraction;
- [HomeBox](https://github.com/sysadminsmedia/homebox): household inventory and item lifecycle;
- [Libre Closet](https://github.com/Lazztech/Libre-Closet): digital wardrobe and outfit interaction;
- [Grocy](https://github.com/grocy/grocy): household consumables and inventory management.

No source code from these projects is included in the current repository. If third-party code is introduced later, its copyright and licence notices will be retained as required.

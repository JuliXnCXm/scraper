# delivery sites scraper

By: BI team - rappi.

Version: 0.1.0


## Prerequisites

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- npm & nodejs (https://nodejs.org/es/)
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate delivery_sites_scraper
```

or

```bash
mamba env create -f environment.yml
activate delivery_sites_scraper
```

## Setup

1. git clone or download ZIP project
2. install anaconda
3. create enviroment
4. move to backend_sraper and execute npm intall in terminal

## Init Process

1. move to backend_scraper and execute npm start
2. in browser http://localhost:3000/
3. close browser
3. execute "py pipeline.py ifood" in terminal

## Project organization

    delivery_sites_scraper
        |──backend_scraper
        |   |──src
        |        |── config/
        |        |── controllers/
        |        |── data/
        |        |── routers/
        |        |── index.js
        |
        ├── data
        │   ├── extract      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │   └── transform
        |
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---

    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---


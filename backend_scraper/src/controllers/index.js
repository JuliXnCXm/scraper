const axios = require('axios');
const {config } = require('../config/config');
const fs = require('fs');


class IndexController {

    getApi  = (req, res) => {
        var data = JSON.stringify({
            "supported-headers": [
                "OPERATION_HEADER"
            ],
            "supported-cards": [
                "MERCHANT_LIST",
                "CATALOG_ITEM_LIST",
                "CATALOG_ITEM_LIST_V2",
                "FEATURED_MERCHANT_LIST",
                "CATALOG_ITEM_CAROUSEL",
                "BIG_BANNER_CAROUSEL",
                "IMAGE_BANNER",
                "MERCHANT_LIST_WITH_ITEMS_CAROUSEL",
                "SMALL_BANNER_CAROUSEL",
                "NEXT_CONTENT",
                "MERCHANT_CAROUSEL",
                "MERCHANT_TILE_CAROUSEL",
                "SIMPLE_MERCHANT_CAROUSEL",
                "INFO_CARD",
                "MERCHANT_LIST_V2",
                "ROUND_IMAGE_CAROUSEL",
                "BANNER_GRID",
                "MEDIUM_IMAGE_BANNER"
            ],
            "supported-actions": [
                "catalog-item",
                "merchant",
                "page",
                "card-content",
                "last-restaurants",
                "webmiddleware"
            ],
            "feed-feature-name": "",
            "faster-overrides": ""
        });

        var settings = {
        method: 'post',
        url: config.apiUrl,
        headers: {
            'Content-Type': 'application/json'
        },
        data : data
        };

        axios(settings)
        .then(function (response) {
            let resp = JSON.stringify(response.data.sections[0].cards);
            res.send(resp);
            fs.writeFileSync('src/data/data.json', resp, 'utf8', function (err) {
                if (err) throw err;
                console.log('Saved!');
            });

        })
        .catch(function (error) {
        console.log(error);
        });
    }
}

module.exports = IndexController;
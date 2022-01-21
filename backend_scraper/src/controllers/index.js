const axios = require('axios');
const fs = require('fs');


class IndexController {

    getApi  = (lat, lon, idx) => {

        var data = JSON.stringify({
            "supported-headers": ["OPERATION_HEADER"],
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
            "MEDIUM_IMAGE_BANNER",
            ],
            "supported-actions": [
            "catalog-item",
            "merchant",
            "page",
            "card-content",
            "last-restaurants",
            "webmiddleware",
            ],
            "feed-feature-name": "",
            "faster-overrides": "",
        });
        var settings = {
            method: "post",
            url: `https://marketplace.ifood.com.br/v2/home?alias=SINGLE_TAB_CO_CMS&latitude=${lat}&longitude=${lon}&channel=COMEYA&size=200`,
            headers: {
            "Content-Type": "application/json",
            },
            data: data,
        };

        axios(settings)
            .then(function (response) {
                let resp = JSON.stringify(response.data.sections[0].cards);
                fs.writeFileSync(
                    `src/data/data${idx}.json`,
                    resp,
                    {
                        encoding: 'utf8',
                        flag: 'w+'
                    },
                    (err, data) => {
                        if (!err) {
                            console.log("file saved");
                        } else {
                            console.log(err);
                        }
                    }
                );
                console.log('saved')
            }).catch(function (error) {
                console.log(error);
            });

    }
}

module.exports = IndexController;
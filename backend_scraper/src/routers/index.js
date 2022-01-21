const { Router } = require("express");
const IndexController = require( "../controllers" );

class IndexRouter {

    constructor() {
        this.router = Router();
        this.#config();

    }
    #config() {
        const locations = [
            ["4.7404756", "-74.0987969"],
            ["4.6171831", "-74.1876103"],
            ["6.2736399", "-75.56157"],
            ["4.6502712", "-74.1687749"],
            ["4.6872524", "-74.1491889"],
            ["4.6112676", "-74.1592864"],
            ["4.708713", "-74.135755"],
            ["10.9172982", "-74.7870181"],
        ];
        let idx = 0
        for (let i = 0; i < locations.length; i++) {
            const objIndex = new IndexController()
                objIndex.getApi(locations[i][0], locations[i][1], idx);
            idx++;
        }

        setTimeout(() => {
            process.exit(0);
        },4000)
    }
}

module.exports = IndexRouter;

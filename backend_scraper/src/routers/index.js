const { Router } = require("express");
const IndexController = require( "../controllers" );

class IndexRouter {

    constructor() {
        this.router = Router();
        this.#config();
    }
    #config() {
        const objIndex = new IndexController()
        this.router.get("/", objIndex.getApi);
    }
}

module.exports = IndexRouter;

'use strict';

var utils = require('../utils/writer.js');
var COVID19INFECTION = require('../service/COVID19INFECTIONService');

module.exports.searchInventory = function searchInventory (req, res, next, searchString, skip, limit) {
  COVID19INFECTION.searchInventory(searchString, skip, limit)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

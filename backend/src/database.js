const Sequelize = require('sequelize');
const settings = require('./config');


database = new Sequelize(
  settings.DB_NAME,
  settings.DB_USER,
  settings.DB_PASSWORD,
  {
      host: settings.DB_HOST,
      dialect: settings.DB_DIALECT,
  }
);

module.exports = database;
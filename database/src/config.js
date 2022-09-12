require('dotenv').config()

const PORT = process.env.PORT
const DB_USER = process.env.DB_USER
const DB_PASSWORD = process.env.DB_PASSWORD
const DB_NAME = process.env.DB_NAME
const DB_HOST = process.env.DB_HOST
const DB_DIALECT = process.env.DB_DIALECT
const FORCE = process.env.FORCE

module.exports = {
    PORT:PORT,
    DB_USER:DB_USER,
    DB_PASSWORD:DB_PASSWORD,
    DB_NAME:DB_NAME,
    DB_HOST:DB_HOST,
    DB_DIALECT:DB_DIALECT,
    FORCE:FORCE
}
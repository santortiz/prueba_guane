const Sequelize = require('sequelize');
const sequelize = require('../../database');


const Enterprise = sequelize.define('enterprise', {
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
        unique: true,
        allowNull:false
    },

    name: {
        type: Sequelize.STRING,
        allowNull: false,
    },

    nit: {
        type: Sequelize.INTEGER,
        allowNull: false
    }
},{
    timestamps: true,
    createdAt: 'created_at',
    updatedAt: 'updated_at',
})

module.exports = Enterprise;
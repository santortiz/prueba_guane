const Sequelize = require('sequelize');
const sequelize = require('../../database');


const User = sequelize.define('user', {
    document: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        unique: true,
        allowNull:false
    },

    name: {
        type: Sequelize.STRING,
        allowNull: false,
    },

    email: {
        type: Sequelize.STRING,
        allowNull: false,
        validate: {
            isEmail: true
        }
    }
}, {
    timestamps: true,
    createdAt: 'created_at',
    updatedAt: 'updated_at',
})

module.exports = User;
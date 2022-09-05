const Sequelize = require('sequelize');
const sequelize = require('../../database');
const UserXEnterprise = require('./userXEnterprise');

const Transaction = sequelize.define('transaction', {
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
        unique: true
    },

    count: {
        type: Sequelize.INTEGER,
        allowNull:false
    },

    type: {
        type: Sequelize.ENUM,
        values: ['ingreso', 'salida'],
        allowNull: false
    },

    user_x_enterprise_id: {
        type: Sequelize.INTEGER,
        references: {
            model: UserXEnterprise,
            key: 'id'
        }
    },
}, {
    timestamps: true,
    createdAt: 'created_at',
    updatedAt: 'updated_at',
});

UserXEnterprise.hasMany(Transaction, {
    foreignKey: 'user_x_enterprise_id', as: 'transactions'
})

Transaction.belongsTo(UserXEnterprise, {
    foreignKey: 'user_x_enterprise_id', as: 'user_x_enterprises'
})

module.exports = Transaction;
const Sequelize = require('sequelize');
const sequelize = require('../../database');
const Enterprise = require('./enterprise');
const User = require('./user');

const UserXEnterprise = sequelize.define('userXEnterprise', {
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
        unique: true
    },

    user_document: {
        allowNull: true,
        type: Sequelize.INTEGER,
        references: {
            model: User,
            key: 'document',
        },
    },

    enterprise_id: {
        allowNull: false,
        type: Sequelize.INTEGER,
        references: {
            model: Enterprise,
            key: 'id',
        },
    },
}, {
    timestamps: true,
    createdAt: 'created_at',
    updatedAt: 'updated_at',
});

UserXEnterprise.belongsTo(User,{
    foreignKey: 'user_document', targetKey: 'document', as: 'users'
});

User.hasMany(UserXEnterprise, {
    foreignKey: 'user_document',
    as: 'user_x_enterprise_id'
});

UserXEnterprise.belongsTo(Enterprise,{
    foreignKey: 'enterprise_id', targetKey: 'id', as: 'enterprises'
});

Enterprise.hasMany(UserXEnterprise,{
    foreignKey: 'enterprise_id',
    as: 'user_x_enterprise_id'
})


module.exports= UserXEnterprise;
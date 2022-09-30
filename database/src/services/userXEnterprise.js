const Enterprise = require('./../infra/models/enterprise');
const User = require('./../infra/models/user');
const Transaction = require('./../infra/models/transaction');
const UserXEnterprise = require('./../infra/models/userXEnterprise');
const BaseService = require('./../infra/services/baseService');

const includeModels = [
    {
        model: User,
        as: 'user'
    },
    {
        model: Enterprise,
        as: 'enterprise'
    },
    {
        model: Transaction,
        as: 'transactions'
    }
];


class UserXEnterpriseService extends BaseService {}
const service = new UserXEnterpriseService(UserXEnterprise, includeModels);
module.exports = service;
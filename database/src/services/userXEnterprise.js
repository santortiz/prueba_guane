const Enterprise = require('./../infra/models/enterprise');
const User = require('./../infra/models/user');
const Transaction = require('./../infra/models/transaction');
const UserXEnterprise = require('./../infra/models/userXEnterprise');
const BaseService = require('./../infra/services/baseService');

const includeModels = [
    {
        model: User,
        as: 'users'
    },
    {
        model: Enterprise,
        as: 'enterprises'
    },
    {
        model: Transaction,
        as: 'transactions'
    }
];


class UserXEnterpriseService extends BaseService {

    get = async (req, res) => {
        try {
            const { enterprise_id, user_document } = req.query;
            await this.schema.findOne({
                include: this.include,
                where: {
                    enterprise_id,
                    user_document
                },
            })
                .then((data) => {
                    if (data) {
                        res.status(200).json(data);
                    } else {
                        const response = { success: false, detail: 'Object not found' };
                        res.status(404).json(response);
                    }
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error get');
            console.log(error);
            const response = { success: false, detail: 'Error get' };
            res.status(400).json(response);
        }
    };

    delete = async (req, res) => {
        try {
            const { id } = req.params;
            await this.schema.destroy({
                where: { id },
            })
                .then((data) => {
                    if (data) {
                        res.status(204).json();
                    } else {
                        const response = { success: false, detail: 'Object not found' };
                        res.status(404).json(response);
                    }
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error delete');
            console.log(error);
            const response = { success: false, detail: 'Error delete' };
            res.status(400).json(response);
        }
    };
}
const service = new UserXEnterpriseService(UserXEnterprise, includeModels);
module.exports = service;
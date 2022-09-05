const UserXEnterprise = require('../infra/models/userXEnterprise');
const Transaction = require('../infra/models/transaction');
const { checkError } = require('../infra/services/database');
const BaseService = require('../infra/services/baseService');


const includeModels = [
    {
        model: UserXEnterprise,
        as: 'user_x_enterprises'
    }
]

class TransactionService extends BaseService {

    delete = async (req, res) => {
        try {
            const { id } = req.params;
            await this.schema.destroy({
                where: { id },
            })
                .then((data) => {
                    if (data) {
                        res.status(201).json({
                            success: true,
                            detail: 'object deleted'
                        });
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

const service = new TransactionService(Transaction, includeModels);
module.exports = service;



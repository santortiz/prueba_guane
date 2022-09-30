const UserXEnterprise = require('../infra/models/userXEnterprise');
const User = require('../infra/models/user');
const Transaction = require('../infra/models/transaction');
const { checkError } = require('../infra/services/database');
const BaseService = require('../infra/services/baseService');


const includeModels = [
    {
        model: UserXEnterprise,
        as: 'user_x_enterprise',
        attributes: ['id'],
        include: [{
            model: User,
            as: 'user'
        }]
    }
]

class TransactionService extends BaseService {

    list = async (req, res) => {
        const payload = req.query;
        let skip = 0;
        let limit = 100;
        skip = parseInt(payload.skip, 10);
        delete payload.skip;
        limit = parseInt(payload.limit, 10);
        delete payload.limit;

        if (payload.user_document && payload.enterprise_id) {
            
            let user_x_enterprise= await UserXEnterprise.findOne({
                where: {
                    user_document: payload.user_document,
                    enterprise_id: payload.enterprise_id
                }
            })

            payload.user_x_enterprise_id = user_x_enterprise.id

            delete payload.user_document;
            delete payload.enterprise_id;
        }
        
        try {
            await this.schema.findAll({
                include: this.include,
                where: payload,
                offset: skip,
                limit,
                order: [
                    ['updated_at', 'DESC'],
                ],
            })
                .then((data) => {
                    res.status(200).json(data);
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error list');
            console.log(error);
            const response = { success: false, detail: 'Error list' };
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

    totalcount = async (req, res) => {
        const payload = req.query;
        let skip = 0;
        let limit = 100;
        skip = parseInt(payload.skip, 10);
        delete payload.skip;
        limit = parseInt(payload.limit, 10);
        delete payload.limit;
        
        try {
            
            let user_x_enterprise= await UserXEnterprise.findOne({
                where: {
                    user_document: payload.user_document,
                    enterprise_id: payload.enterprise_id
                }
            })
    
            payload.user_x_enterprise_id = user_x_enterprise.id
    
            delete payload.user_document;
            delete payload.enterprise_id;


            await this.schema.findAll({
                include: this.include,
                where: payload,
                offset: skip,
                limit,
                order: [
                    ['updated_at', 'DESC'],
                ],
            })
                .then((data) => {

                    let ingresos= [];
                    let salidas = [];

                    for (let transaction of data){
                        
                        if (transaction.type == 'ingreso') {
                            ingresos.push(transaction.count)
                        } else {
                            salidas.push(transaction.count)
                        }
                    }

                    let total = ingresos.reduce((a,b)=> a+b,0) - salidas.reduce((a,b)=> a+b,0) 

                    res.status(200).json({
                        totalCount: total
                    });
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error list');
            console.log(error);
            const response = { success: false, detail: 'Error list' };
            res.status(400).json(response);
        }
    }; 
}


const service = new TransactionService(Transaction, includeModels);

module.exports = service;



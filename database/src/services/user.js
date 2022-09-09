const User = require('../infra/models/user');
const UserXEnterprise = require('../infra/models/userXEnterprise');
const BaseService = require('../infra/services/baseService');
const { checkError } = require('../infra/services/database');


const includeModels= [
    {
        model: UserXEnterprise,
        as: 'user_x_enterprises',
        where: {}
    }
]

class UserService extends BaseService {

    list = async (payload) => {
        let response = {};
        const filter = payload;
        let skip= 0;
        let limit= 100;
        skip= parseInt(filter.skip, 10);
        delete filter.skip;
        limit = parseInt(filter.limit, 10);
        delete filter.limit;

        if (filter.enterprise_id) {
            this.include[0].where['enterprise_id'] = filter.enterprise_id
        } else {
            this.include[0].where = {}
        }
        
        delete filter.enterprise_id;


        try {
            await this.schema.findAll({
                include: this.include,
                where: filter,
                offset: skip,
                limit,
                order: [
                    ['updated_at', 'DESC']
                ],
            }).then((data) => {
                response= {
                    data,
                    status: 200,
                }
            })
            .catch((error) => {
                response = {
                    data: checkError(error),
                    status: 400,
                };
            });

        } catch (error) {
            console.log('Error list');
            console.log(error);
            response = {
                data: { success: false, detail: 'Error during listing' },
                status: 400,
            };
        }
        return response;
    };

    get = async (req, res) => {
        try {
            const { document } = req.params;
            await this.schema.findOne({
                include: this.include,
                where: { document },
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

    update = async (req, res) => {
        try {
            const { document } = req.params;
            const { body } = req;
            await this.schema.update(
                body,
                {
                    where: {
                        document,
                    },
                    returning: true,
                },
            )
                .then((data) => {
                    if (data[0] == 1) {
                        const response = data[1][0].dataValues;
                        res.status(201).json(response);
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
            console.log('Error update');
            console.log(error);
            const response = { success: false, detail: 'Error update' };
            res.status(400).json(response);
        }
    };

    delete = async (req, res) => {
        try {
            const { document } = req.params;
            await this.schema.destroy({
                where: { document },
            })
                .then((data) => {
                    if (data) {
                        const response = { success: true, detail: 'Object deleted' };
                        res.status(201).send(response);
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

const service = new UserService(User, includeModels);
module.exports = service;



